import os
import sys

class GFlags():

    def __init__(self, process, frame=None):
        if frame is None:
            if sys.version.find("AMD64") != -1:
                self.frame = "x64"
            else:
                self.frame = "x86"
        self.process = process
        self.gflags = os.path.join(os.path.dirname(__file__), "utils", self.frame, "gflags.exe")

    def enable(self, unaligned=True):
        if unaligned:
            unaligned = "/unaligned"
        else:
            unaligned = ""
        p = os.popen("{} /p /enable {} /full {}".format(self.gflags, self.process, unaligned))
        print(p.read())
    
    def disable(self):
        p = os.popen("{} /p /disable {}".format(self.gflags, self.process))
        print(p.read())
