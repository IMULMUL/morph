#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r
from modules.webidl.HTMLElement import HTMLElement

class HTMLContentElement(HTMLElement):
    '''
    The HTMLContentElement interface represents a <content> HTML Element, which is used in Shadow DOM.
    '''
    # Properties
    # This interface inherits the properties of HTMLElement.
    def p_select(self):
        return "'%s'" % r.selector()

    # Methods
    # This interface inherits the methods of HTMLElement.
    def m_getDistributedNodes(self):
        pass