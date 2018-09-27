import time
import importlib
import multiprocessing
import os
import sys
import urllib.request
import json
import shutil

class Fuzzer():

    def __init__(self, morpit):

        # TODO: Check all morpit arguments are valid or not
        self.proc_path = morpit["proc_path"]
        self.proc_name = morpit["proc_name"]
        self.proc_args = morpit["proc_args"]
        
        generator = importlib.import_module(morpit["generator"])
        #self.generator = generator.Generator(morpit["template"])
        self.generator = None 

        gflags = importlib.import_module(morpit["gflags"])
        self.gflags = gflags.GFlags(self.proc_name)
        self.gflags.enable(unaligned=False)

        debugger = importlib.import_module(morpit["debugger"])
        self.monitor = debugger.Debugger()
        self.confirm = debugger.Debugger()
        self.timeout = morpit["timeout"]

        self.result_dir = morpit["fuzz_results_dir"]

    def save_crash(self):
        crash_name = "{}_{}{}".format(self.proc_name, self.confirm.crash_name, os.path.splitext(self.generator.fuzz_path))
        try:
            with open(self.generator.save_path, "rb") as f:
                crash_data = f.read()
            if self.result_dir.startswith("http://"):
                post_data = {'file_name': crash_name, 'file_content': crash_data}
                post_data = urllib.parse.urlencode(post_data).encode("utf-8")
                req = urllib.request.Request(url=self.result_dir, data=post_data)
                urllib.request.urlopen(req)
            else:
                shutil.copy(self.generator.save_path, os.path.join(self.result_dir, crash_name))
        except Exception as e:
            print("[-] Error: {} when saving {} to {}.".format(repr(e), self.confirm.crash_name, self.generator.save_path))
            return
        print("[+] Status: Finded crash %s and saved successfully." % (self.confirm.crash_name))        

    def run(self):

        while 1:
            #fuzz_path = self.generator.run()
            fuzz_path = "D:\\test.tif"
            process = "{} {} {}".format(self.proc_path, self.proc_args, fuzz_path)
            # fuzz
            pf = multiprocessing.Process(target=self.monitor.run, args=(process,))
            pf.start()
            pf.join(self.timeout)
            if not self.monitor.crash_name or not self.monitor.crash_description:
                pf.terminate()
                continue
            
            # Confirm
            pc = multiprocessing.Process(target=self.confirm.run, args=(process,))
            pc.start()
            pc.join(self.timeout)
            if not self.confirm.crash_name or not self.confirm.crash_description:
                print("[-] Ops: Can not confirm twice of  crash {}.".format(self.monitor.crash_name))
                pc.terminate()
                continue
            #saving
            self.save_crash()