#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r
from modules.webidl.HTMLElement import HTMLElement

class HTMLDListElement(HTMLElement):
    '''
    The HTMLDListElement interface provides special properties for manipulating definition list elements.
    (beyond those of the regular HTMLElement interface it also has available to it by inheritance)
    '''
    # Properties
    # Inherits properties from its parent, HTMLElement.
    def p_compact(self):
        return r.bool()

    # Methods
    # No specific method; inherits methods from its parent, HTMLElement.