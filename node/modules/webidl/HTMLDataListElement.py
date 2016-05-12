#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r
from modules.webidl.HTMLElement import HTMLElement

class HTMLDataListElement(HTMLElement):
    '''
    The HTMLDataListElement interface provides special properties to manipulate <datalist> elements and their content.
    (beyond the HTMLElement object interface it also has available to it by inheritance)
    '''
    # Properties
    # Inherits properties from its parent, HTMLElement.
    def p_options(self):
        pass

    # Methods
    # No specific method; inherits methods from its parent, HTMLElement.