import time
import importlib
import multiprocessing
import os
import sys
import urllib.request
import json

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
        crash_name = "{}_{}.html".format(self.proc_name, self.confirm.crash_name)
        try:
            crash_data = (urllib.request.urlopen(self.generator.save_path).read()).decode('utf-8')
            if self.result_dir.startswith("http://"):
                post_data = {'file_name': crash_name, 'file_content': crash_data}
                post_data = urllib.parse.urlencode(post_data).encode("utf-8")
                req = urllib.request.Request(url=self.result_dir, data=post_data)
                urllib.request.urlopen(req)
            else:
                with open(os.path.join(self.result_dir, crash_name), "wb") as fw:
                    fw.write(crash_data.encode("utf-8"))
        except Exception as e:
            print("[-] Error: {} when saving {} to {}.".format(repr(e), self.confirm.crash_name, self.generator.save_path))
            return

        print("[+] Status: Finded crash %s and saved successfully." % (self.confirm.crash_name))  

    def fuzz(self):

        self.monitor.run("{} {} {}".format(self.proc_path, self.proc_args, self.generator.fuzz_path))
        if not self.monitor.crash_name or not self.monitor.crash_description:
            return
        print("[+] Status: Confirming crash {}...".format(self.monitor.crash_name))
        
        # Confirm twice
        self.confirm.run("{} {} {}".format(self.proc_path, self.proc_args, self.generator.save_path))
        if not self.confirm.crash_name or not self.confirm.crash_description:
            print("[-] Ops: Can not confirm twice of  crash {}.".format(self.monitor.crash_name))
            return
        print("[+] Status: Crash is confirmed, saving...")
        
        # save to file
        self.save_crash()
         

    def run(self):
        self.start_generator()
        while 1:
            p_b = multiprocessing.Process(target=self.fuzz)
            p_b.start()
            p_b.join(120)
            p_b.terminate()