#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r
from modules.webidl.HTMLElement import HTMLElement

class HTMLBRElement(HTMLElement):
    '''
    The HTMLBRElement interface represents a HTML line break element (<br>).
    It inherits from HTMLElement.
    '''
    # properties
    # Inherits properties from its parent, HTMLElement.

    def p_clear(self):
        # 设置一个元素的侧面是否允许其他的浮动元素
        # left	在左侧不允许浮动元素
        # right	在右侧不允许浮动元素
        # both	在左右两侧均不允许浮动元素
        # none	默认。允许浮动元素出现在两侧
        return r.choice(["left", "right", "both", "none"])

    # Methods
    # No specific method; inherits methods from its parent, HTMLElement.
    pass