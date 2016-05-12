#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as randoms

class ParentNode():
    '''
    The ParentNode interface contains methods that are particular to Node objects that can have children.
    ParentNode is a raw interface and no object of this type can be created; it is implemented by
    Element, Document, and DocumentFragment objects.
    '''
    # properties
    def p_children(self):
        pass

    def p_firstElementChild(self):
        pass

    def p_lastElementChild(self):
        pass

    def p_childElementCount(self):
        pass

    # Methods

    def m_append(self):
        # 将指定元素插入匹配元素
        node = randoms.Element()
        text = randoms.DOMString(randoms.zint(256))
        return "'%s'" % randoms.choice([node, text])

    def m_prepend(self):
        # 将指定元素插入匹配元素内部的开头
        node = randoms.Element()
        text = randoms.DOMString(randoms.zint(256))
        return "'%s'" % randoms.choice([node, text])

    def m_query(self):
        n = randoms.choice([randoms.HTMLTags(), randoms.Element(), "'*'"])
        return "'%s'" % n

    def m_queryAll(self):
        n = randoms.choice([randoms.HTMLTags(), randoms.Element(), "'*'"])
        return "'%s'" % n

    def m_querySelector(self):
        # 找到一个后就返回节点对象
        selectors = randoms.choice([randoms.HTMLTags(), randoms.Element(), "*"])
        return "'%s'" % selectors

    def m_querySelectorAll(self):
        # 找出所有匹配的节点并返回数组
        selectors = randoms.choice([randoms.HTMLTags(), randoms.Element(), "*"])
        return "'%s'" % selectors
