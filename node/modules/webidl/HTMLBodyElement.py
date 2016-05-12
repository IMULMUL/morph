#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r
from modules.webidl.HTMLElement import HTMLElement
from modules.webidl.WindowEventHandlers import WindowEventHandlers

class HTMLBodyElement(HTMLElement, WindowEventHandlers):
    '''
    The HTMLBodyElement interface provides special properties for manipulating body elements.
    (beyond those of the regular HTMLElement interface they also inherit)
    '''
    # Properties
    # nherits properties from its parent, HTMLElement and from WindowEventHandlers.
    def p_aLink(self):
        return r.color()

    def p_background(self):
        # 规定文档的背景图像
        # TODO:完善具体的图像
        return r.URI()

    def p_bgColor(self):
        # 规定文档的背景颜色
        return r.color()

    def p_link(self):
        # 规定文档中未访问链接的默认颜色
        return r.color()

    def p_text(self):
        # 规定文档中所有文本的颜色
        return r.color()

    def p_vLink(self):
        # 规定文档中已被访问链接的颜色
        return r.color()

    # Event handlers
    # No specific event handlers; inherits event handlers from its parent, HTMLElement and from WindowEventHandlers.

    # Methods
    # No specific methods; inherits methods from its parent, HTMLElement and from WindowEventHandlers.
    pass