#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r
from modules.webidl.HTMLElement import HTMLElement

class HTMLButtonElement(HTMLElement):
    '''
    The HTMLButtonElement interface provides properties and methods for manipulating the layout and presentation of button elements.
    (beyond the <button> object interface it also has available to them by inheritance)
    '''
    # Properties
    # Inherits properties from its parent, HTMLElement.
    def p_autofocus(self):
        # 规定当页面加载时按钮应当自动地获得焦点
        return r.choice([r.bool(), "autofocus"])

    def p_disabled(self):
        # 规定应该禁用该按钮
        return r.bool()

    def p_form(self):
        pass

    def p_formAction(self):
        return r.URI()

    def p_formEncType(self):
        # application/x-www-form-urlencoded	在发送前对所有字符进行编码（默认）
        # multipart/form-data	不对字符编码。当使用有文件上传控件的表单时，该值是必需的
        # text/plain	将空格转换为 "+" 符号，但不编码特殊字符
        return r.choice(["application/x-www-form-urlencoded", "multipart/form-data", "text/plain", ""])

    def p_formMethod(self):
        # 覆盖 form 元素的 method 属性
        return r.choice(["get", "post"])

    def p_formNoValidate(self):
        return r.bool()

    def p_formTarget(self):
        target = ["_blank", "_self", "_parent", "_top", r.DOMString(r.zint(256))]
        return r.choice(target)

    def p_labels(self):
        pass

    def p_menu(self):
        return "document.createElement('menu')"

    def p_name(self):
        return r.DOMString(r.zint(256))

    def p_type(self):
        behavior = ["submit", "reset", "button", "menu"]
        return r.choice(behavior)

    def p_validationMessage(self):
        pass

    def p_validity(self):
        pass

    def p_value(self):
        return r.DOMString(r.zint(256))

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





