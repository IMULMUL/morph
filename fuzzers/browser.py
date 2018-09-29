import time
import importlib
import multiprocessing
import os
import sys
import urllib.request
import json

utils = importlib.import_module("core.utils")

class Fuzzer():

    def __init__(self, morpit):

        # TODO: Check all morpit arguments are valid or not
        self.proc_path = morpit["proc_path"]
        self.proc_name = morpit["proc_name"]
        self.proc_args = morpit["proc_args"]
        
        generator = importlib.import_module(morpit["generator"])
        self.generator = generator.Generator(morpit["template"])        

        gflags = importlib.import_module(morpit["gflags"])
        self.gflags = gflags.GFlags(self.proc_name)
        self.gflags.enable(unaligned=False)

        debugger = importlib.import_module(morpit["debugger"])
        self.monitor = debugger.Debugger()
        self.confirm = debugger.Debugger()

        self.fuzz_timeout = morpit["fuzz_timeout"]
        self.confirm_timeout = morpit["confirm_timeout"]
        self.result_dir = morpit["fuzz_results_dir"]

    def start_generator(self):
        p_s = multiprocessing.Process(target=self.generator.run)
        p_s.daemon = True  # daemon with main process
        p_s.start()
        while not self.generator.check():
            time.sleep(2)
            print("[-] Warning: Generator 127.0.0.1:{} is not opened, wait or check.".format(self.generator.port))
        print("[+] Status: Generator 127.0.0.1:{} is running.".format(self.generator.port))

    def save_crash(self):
        try:
            crash_name = "{}_{}".format(self.proc_name, self.confirm.crash_name.value.decode('utf-8'))
            crash_data = (urllib.request.urlopen(self.generator.confirm_path).read())
            crash_description = self.confirm.crash_description.value
            
            if self.result_dir.startswith("http://"):
                utils.post_file(self.result_dir, crash_name+".html", crash_data)
                utils.post_file(self.result_dir, crash_name+".log", crash_description)
            else:
                utils.save_file(os.path.join(self.result_dir, crash_name+".html"), crash_data)
                utils.save_file(os.path.join(self.result_dir, crash_name+".log"), crash_description)
            print("[+] Status: Finded crash %s and saved successfully." % (self.confirm.crash_name.value.decode("utf-8")))
        except:
            print("[-] Error: Wrong when saving {} to {}.".format(self.confirm.crash_name.value.decode("utf-8"), self.result_dir))

    def run(self):
        self.start_generator()
        while 1:         
            # fuzz
            process = "{} {} {}".format(self.proc_path, self.proc_args, self.generator.fuzz_path)
            pf = multiprocessing.Process(target=self.monitor.run, args=(process,))
            pf.start()
            pf.join(self.fuzz_timeout)
            if len(self.monitor.crash_name.value) <= 0:
                pf.terminate()
                continue
            print('[+]Status: Crash {} is confirming...'.format(self.monitor.crash_name.value.decode("utf-8")))
            # confirm
            process_confirm = "{} {} {}".format(self.proc_path, self.proc_args, self.generator.confirm_path)
            pc = multiprocessing.Process(target=self.confirm.run, args=(process_confirm,))
            pc.start()
            pc.join(self.confirm_timeout)
            if len(self.confirm.crash_name.value) <= 0:
                print("[-] Ops: Can not confirm twice of crash {}.".format(self.monitor.crash_name.value.decode("utf-8")))
                pc.terminate()
                continue
            # save crash
            self.save_crash()