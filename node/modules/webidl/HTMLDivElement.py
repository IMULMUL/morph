#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r
from modules.webidl.HTMLElement import HTMLElement

class HTMLDivElement(HTMLElement):
    '''
    The HTMLDivElement interface provides special properties for manipulating div elements.
    (beyond the regular HTMLElement interface it also has available to it by inheritance)
    '''
    # Properties
    # Inherits properties from its parent, HTMLElement.
    def p_align(self):
        r.choice(["left", "right", "justify", "center", ""])

    # Methods
    # No specific method; inherits methods from its parent, HTMLElement.