import importlib

class Template():

    def __init__(self):
        self.domato = importlib.import_module("templates.google_domato.generator")
        pass
    
    def generate(self):
        return self.domato.generate_samples()