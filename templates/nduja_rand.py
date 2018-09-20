import random
import os

class Template():

    def __init__(self):
        nduja_path = os.path.join(os.path.dirname(__file__), "nduja.html")
        with open(nduja_path, "r") as f:
            self.template = f.read()
    
    def generate(self):
        # 1.generate random arrays
        intArray = []
        for x in range(100000):
            intArray.append(random.randint(0, 100000))
        # 2.replace vecotr template
        return self.template.replace("%MOR_ARRAY%", str(intArray), 1)