#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r
from modules.webidl.HTMLElement import HTMLElement
from modules.webidl.HTMLHyperlinkElementUtils import HTMLHyperlinkElementUtils

class HTMLAnchorElement(HTMLElement, HTMLHyperlinkElementUtils):
    '''
    HTMLAnchorElement 接口表示超链接元素，并提供一些特别的属性和方法以用于操作这些元素的布局和显示
    父类：HTMLElement
    抽象基类接口：HTMLHyperlinkElementUtils
    '''
    # properties
    # 继承其父类 HTMLElement 的属性，并实现 URLUtils 中（定义）的（属性）
    def p_charset(self):
        # 设置或返回字符编码
        charset = ["ASCII", "Windows-1252", "ISO-8859-1", "UTF-8", ""]
        return r.choice(charset)

    def p_coords(self):
        # 设置或者返回坐标值
        rand = r.zint(2)
        if rand == 0: # rect
            num = 2
        elif rand == 1: # circ
            num = 3
        else: # poly
            num = r.zint(2048)
        return r.choice([r.coords(num), ""])

    def p_download(self):
        # 规定被下载的超链接目标名称
        return r.DOMString(r.zint(256))

    def p_hreflang(self):
        return r.language()

    def p_media(self):
        md = ["screen", "tty", "tv", "projection", "handheld", "print", "braille", "aural", "all"]
        return r.sample2(md, ",")

    def p_name(self):
        return r.DOMString(r.zint(256))

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

    def p_rev(self):
        # 指定当前文档与被链接文档的关系
        return self.p_rel()

    def p_shape(self):
        shape = ["default", "rect", "circ", "poly", ]
        return r.choice(shape)

    def p_target(self):
        target = ["_blank", "_self", "_parent", "_top", "", r.DOMString(r.zint(256))]
        return r.choice(target)

    def p_text(self):
        return r.DOMString(r.zint(256))

    def p_type(self):
        return r.MIMEType()

    # Methods
    # 继承其父类 HTMLElement 的方法，并实现 HTMLHyperlinkElementUtils 中（定义）的（方法）