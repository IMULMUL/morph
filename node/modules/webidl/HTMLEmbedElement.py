#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r
from modules.webidl.HTMLElement import HTMLElement

class HTMLEmbedElement(HTMLElement):
    '''
    The HTMLEmbedElement interface, which provides special properties for manipulating <embed> elements.
    (beyond the regular HTMLElement interface it also has available to it by inheritance)
    '''
    # Properties
    # Inherits properties from its parent, HTMLElement.
    def p_align(self):
        return r.choice(["left", "right", "justify", "center", ""])

    def p_height(self):
        return "%spx" % r.zint(2048)

    def p_name(self):
        return r.DOMString(r.zint(256))

    def p_src(self):
        return r.URI()

    def p_type(self):
        return r.MIMEType()

    def p_width(self):
        return "%spx" % r.zint(2048)

    # Methods
    # No specific method; inherits methods from its parent, HTMLElement.