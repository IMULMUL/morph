#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r
from modules.webidl.HTMLElement import HTMLElement

class HTMLFieldSetElement(HTMLElement):
    '''
    he HTMLFieldSetElement interface has special properties and methods for manipulating the layout and presentation of field-set elements.
    (beyond the regular HTMLelement interface it also has available to it by inheritance)
    '''
    # Properties
    # Inherits properties from its parent, HTMLElement.
    def p_disabled(self):
        return r.bool()

    def p_elements(self):
        pass

    def p_form(self):
        pass

    def p_name(self):
        return r.DOMString(r.zint(256))

    def p_type(self):
        pass

    def p_validationMessage(self):
        pass

    def p_validity(self):
        pass

    def p_willValidate(self):
        return r.bool()

    # Methods
    # Inherits methods from its parent, HTMLElement.
    def m_checkValidity(self):
        # 检测表单验证的有效性
        pass

    def m_setCustomValidity(self):
        tip = r.DOMString(r.zint(256))
        return "'%s'" % tip