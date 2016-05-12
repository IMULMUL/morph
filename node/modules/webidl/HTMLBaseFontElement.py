#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r
from modules.webidl.HTMLElement import HTMLElement

class HTMLBaseFontElement(HTMLElement):
    '''
    The HTMLBaseFontElement interface provides special properties for manipulating <basefont> elements.
    (beyond the regular HTMLElement interface it also has available to it by inheritance)
    The <basefont> element has been deprecated in HTML4 and removed in HTML5.
    This latest specification requires that this element implements HTMLUnknownElement rather than HTMLBaseFontElement.
    '''
    # properties
    # Inherits properties from its parent, HTMLElement.
    def p_color(self):
        return r.color()

    def p_face(self):
        return r.fonts()

    def p_size(self):
        size = r.randrange(1, 8)
        return r.choice([size, "+%s" % size, "-%s" % size])

    # Methods
    # No specific method; inherits methods from its parent, HTMLElement.