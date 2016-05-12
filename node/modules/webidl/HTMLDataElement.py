#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r
from modules.webidl.HTMLElement import HTMLElement

class HTMLDataElement(HTMLElement):
    '''
    The HTMLDataElement interface provides special properties for manipulating <data> elements.
    (beyond the regular HTMLElement interface it also has available to it by inheritance)
    '''
    # Properties
    # Inherits properties from its parent, HTMLElement.
    def p_value(self):
        return r.DOMString(r.zint(256))

    # Methods
    # No specific method; inherits methods from its parent, HTMLElement.