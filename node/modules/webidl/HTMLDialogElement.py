#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r
from modules.webidl.HTMLElement import HTMLElement

class HTMLDialogElement(HTMLElement):
    '''
    The HTMLDialogElement interface provides methods to manipulate <dialog> elements.
    It inherits properties and methods from the HTMLElement interface.
    '''
    # Properties
    # Inherits properties from its parent, HTMLElement.
    def p_open(self):
        r.bool()

    def p_returnValue(self):
        return r.DOMString(r.zint(256))

    # Methods
    # Inherits methods from its parent, HTMLElement.

    def m_close(self):
        return r.choice(["", "'%s'" % r.DOMString(r.zint(256))])

    def m_show(self):
        return r.choice(["", r.Element(), r.EvtObj()])


    def m_showModal(self):
        return r.choice(["", r.Element(), r.EvtObj()])