#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r
from modules.webidl.Element import Element

class HTMLElement(Element):
    '''
    HTMLElement 接口表示所有的 HTML 元素。一些HTML元素直接实现了HTMLElement接口，其它的间接实现HTMLElement接口
    '''
    # properties:继承自父接口Element的属性
    # 实现了GlobalEventHandlers和TouchEventHandlers的属性

    def p_accessKeyLabel(self):
        # A string that represents the element's assigned access key
        return r.DOMString(r.zint(256))

    def p_contentEditable(self):
        # 获取/设置元素的可编辑状态
        return r.bool()

    def p_isContentEditable(self):
        # 指示元素的内容是否可被编辑
        pass

    def p_dataset(self):
        # 允许读写元素的自定义data特性
        pass

    def p_dir(self):
        # 规定元素内容的文本方向
        value = ["ltr", "rtl", "auto", ""]
        return r.choice(value)

    def p_draggable(self):
        # 规定元素是否可拖动
        value = ["true", "false", "auto"]
        return r.choice(value)

    def p_dropzone(self):
        # 规定在元素上拖动数据时，是否拷贝、移动或链接被拖动数据
        value = ["copy", "move", "link"]
        return r.choice(value)

    def p_hidden(self):
        # 是否应该隐藏元素的内容
        return r.bool()

    def p_itemScope(self):
        return r.bool()

    def p_itemType(self):
        pass

    def p_itemId(self):
        return r.DOMString(r.zint(256))

    def p_itemRef(self):
        pass

    def p_itemProp(self):
        pass

    def p_itemValue(self):
        return r.DOMString(r.zint(256))

    def p_lang(self):
        # 规定元素内容的语言
        return r.language()

    def p_offsetHeight(self):
        pass

    def p_offsetLeft(self):
        pass

    def p_offsetParent(self):
        pass

    def p_offsetTop(self):
        pass

    def p_offsetWidth(self):
        pass

    def p_properties(self):
        pass

    def p_spellcheck(self):
        # 规定是否对元素进行拼写和语法检查
        return r.bool()

    def p_style(self):
        # TODO
        return ""

    def p_tabIndex(self):
        # 设置或返回tab 键控制次序
        return r.randrange(-1, 2048)

    def p_title(self):
        return r.DOMString(r.zint(256))

    def p_translate(self):
        # 规定是否应该翻译元素内容
        value = ["yes", "no"]
        return r.choice(value)

    # Event handlers:Most events properties, of the form onXYZ, are defined on the GlobalEventHandlers
    #   or TouchEventHandlers, implemented by HTMLElement. A few more are specific to HTMLElement.
    def p_oncopy(self):
        return r.Funcs()

    def p_oncut(self):
        return r.Funcs()

    def p_onpaste(self):
        return r.Funcs()

    def p_ontouchstart(self):
        return r.Funcs()

    def p_ontouchend(self):
        return r.Funcs()

    def p_ontouchmove(self):
        return r.Funcs()

    def p_ontouchenter(self):
        return r.Funcs()

    def p_ontouchleave(self):
        return r.Funcs()

    def p_ontouchcancel(self):
        return r.Funcs()

    # Methods:从父元素Element继承的方法
    def m_blur(self):
        # 从当前已经获得焦点的元素上移除键盘焦点
        pass

    #def m_click(self):
    #    # 模拟鼠标左键单击一个元素
    #    pass

    def m_focus(self):
        # 让当前元素获取焦点
        pass

    def m_forceSpellCheck(self):
        # 强制对元素内容进行拼写检查
        pass
