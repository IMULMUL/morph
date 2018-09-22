import os
import importlib

from .google_domato import generator
from .google_domato.grammar import Grammar


class Template():

    def __init__(self):
        #self.domato = importlib.import_module("templates.google_domato.generator")

        grammar_dir = os.path.join(os.path.dirname(__file__), "google_domato")
        f = open(os.path.join(grammar_dir, 'template.html'))
        self.template = f.read()
        f.close()

        self.htmlgrammar = Grammar()
        err = self.htmlgrammar.parse_from_file(os.path.join(grammar_dir, 'html.txt'))
        # CheckGrammar(self.htmlgrammar)
        if err > 0:
            print('There were errors parsing grammar')
            return

        self.cssgrammar = Grammar()
        err = self.cssgrammar.parse_from_file(os.path.join(grammar_dir, 'css.txt'))
        # CheckGrammar(self.cssgrammar)
        if err > 0:
            print('There were errors parsing grammar')
            return

        self.jsgrammar = Grammar()
        err = self.jsgrammar.parse_from_file(os.path.join(grammar_dir, 'js.txt'))
        # CheckGrammar(self.jsgrammar)
        if err > 0:
            print('There were errors parsing grammar')
            return

        # JS and HTML grammar need access to CSS grammar.
        # Add it as import
        self.htmlgrammar.add_import('cssgrammar', self.cssgrammar)
        self.jsgrammar.add_import('cssgrammar', self.cssgrammar)     
        pass
    
    def generate(self):
        return generator.generate_new_sample(self.template, self.htmlgrammar, self.cssgrammar, self.jsgrammar)