#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r
from modules.webidl.HTMLElement import HTMLElement
from modules.webidl.HTMLHyperlinkElementUtils import HTMLHyperlinkElementUtils

class HTMLAreaElement(HTMLElement, HTMLHyperlinkElementUtils):
    '''
    The HTMLAreaElement interface provides special properties and methods
    (beyond those of the regular object HTMLElement interface it also has available to it by inheritance)
    for manipulating the layout and presentation of area elements.
    '''
    # properties:Inherits properties from its parent, HTMLElement,
    # and implements those from HTMLHyperlinkElementUtils.
    def p_alt(self):
        # 规定在图像无法显示时的替代文本
        return r.DOMString(r.zint(256))

    def p_coords(self):
        # 设置或者返回坐标值
        rand = r.zint(2)
        if rand == 0: # rect
            num = 2
        elif rand == 1: # circ
            num = 3
        else: # poly
            num = r.zint(2048)

        ret = r.zint(2048)
        for i in range(num):
            ret = "%s,%s" % (ret, r.zint(2048))
        return ret

    def p_download(self):
        # 规定被下载的超链接目标名称
        return r.DOMString(r.zint(256))

    def p_hreflang(self):
        return r.language()

    def p_media(self):
        md = ["screen", "tty", "tv", "projection", "handheld", "print", "braille", "aural", "all",]
        return r.sample2(md, ",")

    def p_noHref(self):
        # indicating if the area is inactive (true) or active (false).
        return r.bool()

    def p_referrerPolicy(self):
        rp = ["no-referrer", "no-referrer-when-downgrade", "origin", "origin-when-crossorigin", "unsafe-url", "never", "default", "always", ]
        return r.sample2(rp, "|")

    def p_rel(self):
        # 指定当前文档和被连接文档之间的关系
        relation = [
            "appendix", "chapter", "contents", "copyright", "glossary", "index", "section", "start", "subsection", # 已删除的值
            "alternate", "stylesheet", "start", "next", "prev", "contents", "index", "glossary", "copyright", "chapter", "section", "subsection", "appendix", "help",
            "bookmark", "bookmark", "licence", "tag", "friend",
            "archives", "author", "bookmark", "external", "first", "index", "last", "license", "nofollow", "noreferrer", "search", "sidebar", "tag","up",# html5
            "",
        ]
        return r.choice(relation)

    def p_relList(self):
        pass

    def p_shape(self):
        shape = ["default", "rect", "circ", "poly", ]
        return r.choice(shape)

    def p_target(self):
        target = ["_blank", "_self", "_parent", "_top", "", r.DOMString(r.zint(256))]
        return r.choice(target)

    def p_type(self):
        return r.MIMEType()

    # Methods:Inherits methods from its parent, HTMLElement and  implement those from HTMLHyperlinkElementUtils.