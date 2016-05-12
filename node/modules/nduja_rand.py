#! /user/bin/python
# coding:UTF-8

import random

f= open("modules/nduja.html", "r")
try:
    G_TEMP = f.read()
except Exception as e:
    raise e
finally:
    f.close()

class JSTemplater():

    def __init__(self):
        self.template = G_TEMP

    def generate(self):
        # 1.generate random arrays
        intArray = []
        for x in range(100000):
            intArray.append(random.randint(0, 100000))
        # 2.replace vecotr template
        return self.template.replace("%MOR_ARRAY%", str(intArray), 1)

def gen():
    js = JSTemplater()
    return js.generate()