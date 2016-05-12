#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r
from modules.webidl.HTMLElement import HTMLElement

class HTMLBaseElement(HTMLElement):
    '''
    The HTMLBaseElement interface contains the base URI for a document.
    This object inherits all of the properties and methods as described in the HTMLElement interface.
    '''
    # Properties
    # Inherits properties from its parent, HTMLElement.

    def p_href(self):
        return r.URI()

    def p_target(self):
        target = ["_blank", "_self", "_parent", "_top", "", r.DOMString(r.zint(256))]
        return r.choice(target)

    # Methods
    # No specific method; inherits attributes from its parent, HTMLElement.