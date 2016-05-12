#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r

class ChildNode():
    '''
    The ChildNode interface contains methods that are particular to Node objects that can have a parent.
    ChildNode is a raw interface and no object of this type can be created; it is implemented by
    Element, DocumentType, and CharacterData objects.
    '''
    # properties
    # There are neither inherited, nor specific properties.
    # Methods
    # There are no inherited methods.
    def m_remove(self):
        pass

    def m_before(self):
        node = r.Element()
        text = r.DOMString(r.zint(256))
        return r.choice(["'%s'" % text, node])

    def m_after(self):
        node = r.Element()
        text = r.DOMString(r.zint(256))
        return r.choice(["'%s'" % text , node])

    def m_replaceWith(self):
        node = r.Element()
        text = r.DOMString(r.zint(256))
        return r.choice(["'%s'" % text , node])
