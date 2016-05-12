#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as randoms

class NonDocumentTypeChildNode():
    '''
    The NonDocumentTypeChildNode interface contains methods that are particular to Node objects that can have a parent,
    but not suitable for DocumentType.
    NonDocumentTypeChildNode is a raw interface and no object of this type can be created;
    it is implemented by Element, and CharacterData objects.
    '''
    # properties
    # There is no inherited property.
    def p_previousElementSibling(self):
        pass

    def p_nextElementSibling(self):
        pass

    # Methods
    # There is neither inherited, nor specific method.