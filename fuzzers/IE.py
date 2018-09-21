import time
import importlib
import multiprocessing
import sys
import urllib

class Fuzzer():

    def __init__(self, generator, template):
        self.generator = importlib.import_module("generators.{}".format(generator))
        self.generator = self.generator.Generator(template)

        if sys.version.find("AMD64") != -1:
            self.proc = "C:/Program Files (x86)/Internet Explorer/iexplore.exe"
        else:
            self.proc = "C:/Program Files/Internet Explorer/iexplore.exe"

        debugger = importlib.import_module("monitors.windbg.UserDebugger")
        self.monitor = debugger.Debugger()
        self.confirm = debugger.Debugger()

    def start_generator(self):
        p_s = multiprocessing.Process(target=self.generator.run)
        p_s.daemon = True  # daemon with main process
        p_s.start()

        while not self.generator.check():
            print("Warning: Generator 127.0.0.1:{} is not opened, wait or check.".format(self.generator.port))
            time.sleep(2)
        print("Status: Generator 127.0.0.1:{} is not opened, wait or check.".format(self.generator.port))
    
    def recheck(self):
        # confirm
        self.confirm.run("{} {}".format(self.proc, self.generator.save_path))
        if not self.confirm.crash_name or self.confirm.crash_description:
            return
        print("[+R+]:Crash is confirmed, saving...")
        # save to file
        try:
            crash_data = (urllib.request.urlopen(self.generator.save_path).read()).decode('utf-8')
        except:
            print("[-E-]:Get Crash data %s from %s is failed." % (self.confirm.crash_name, self.generator.save_path))
            return
        
        with open("{}.html".format(self.confirm.crash_name), "wb") as fw:
            fw.write(crash_data)
        print("[+R+]:Finded crash %s and saved successfully." % (self.confirm.crash_name))


    def fuzz(self):
        self.monitor.run("{} {}".format(self.proc, self.generator.fuzz_path))
        if not self.monitor.crash_name or self.monitor.crash_description:
            return

        p_c = multiprocessing.Process(target=self.recheck)
        p_c.daemon = True
        p_c.start()
        p_c.join(30)
        p_c.terminate()       

    def run(self):
        self.start_generator()
        while True:
            p_b = multiprocessing.Process(target=self.fuzz)
            p_b.start()
            p_b.join(300)
            p_b.terminate()