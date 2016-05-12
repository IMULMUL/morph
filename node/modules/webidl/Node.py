#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r
from modules.webidl.EventTarget import EventTarget

class Node(EventTarget):
    '''
    Node是一个接口,有很多种类型的DOM元素继承于它。
    下面这些类型的元素继承了该接口的所有属性和方法：
    Document, Element, Attr, CharacterData (Text, Comment,CDATASection继承该类型), ProcessingInstruction,
    DocumentFragment, DocumentType, Notation, Entity, EntityReference
    '''
    # properties
    # Inherits properties from its parents EventTarget
    def p_baseURI(self):
        # 返回节点的绝对基准 URI
        pass

    def p_childNodes(self):
        # 返回节点到子节点的节点列表
        pass

    def p_firstChild(self):
        # 返回节点的首个子节点
        pass

    def p_lastChild(self):
        # 返回节点的最后一个子节点
        pass

    def p_localName(self):
        # 返回节点的本地名称
        pass

    def p_namespaceURI(self):
        # 返回节点的命名空间 URI
        pass

    def p_nextSibling(self):
        # 返回节点之后紧跟的同级节点
        pass

    def p_nodeName(self):
        # 返回节点的名称，根据其类型
        pass

    def p_nodePrincipal(self):
        # 返回节点的principal
        pass

    def p_nodeType(self):
        # 返回节点的类型
        pass

    def p_nodeValue(self):
        # 设置或返回节点的值，根据其类型
        return r.DOMString(r.zint(256))

    def p_ownerDocument(self):
        # 返回节点的根元素（document 对象）
        pass

    def p_parentNode(self):
        # 返回节点的父节点
        pass

    def p_parentElement(self):
        # 返回节点父节点元素
        pass

    def p_prefix(self):
        # 返回节点的命名空间前缀
        pass

    def p_previousSibling(self):
        # 返回节点之前紧跟的同级节点
        pass

    def p_textContent(self):
        # 设置或返回节点及其后代的文本内容
        return r.DOMString(r.zint(256))

    def p_text(self):
        # 返回节点及其后代的文本（IE 独有的属性）
        pass

    def p_xml(self):
        # 返回节点及其后代的 XML（IE 独有的属性）
        pass

    # Methods
    # Inherits methods from its parents EventTarget
    def m_appendChild(self):
        # 向节点的子节点列表的结尾添加新的子节点
        newElem = "document.createElement('%s')" % r.HTMLTags()
        curElem = r.Element()
        return r.choice([newElem, curElem])

    def m_cloneNode(self):
        # 复制节点
        return r.choice([r.bool(), ""])

    def m_compareDocumentPosition(self):
        # 对比两个节点的文档位置
        newElem = "document.createElement('%s')" % r.HTMLTags()
        curElem = r.Element()
        return r.choice([newElem, curElem])

    def m_contains(self):
        otherNode = r.Element()
        return otherNode

    #def m_getFeature(self):
    #    # 返回一个 DOM 对象，此对象可执行带有指定特性和版本的专门的 API
    #    pass

    def m_getUserData(self):
        # 返回与此节点上的某个键相关联的对象
        # 此对象必须首先通过使用相同的键来调用 setUserData 被设置到此节点
        userKey = r.choice([r.randrange(40, 92), r.randrange(93, 127)])
        return "'%s'" % userKey

    def m_hasAttributes(self):
        # 判断当前节点是否拥有属性
        pass

    def m_hasChildNodes(self):
        # 判断当前节点是否拥有子节点
        pass

    def m_insertBefore(self):
        # 在指定的子节点前插入新的子节点
        newNode = r.choice(["document.createElement('%s')" % r.HTMLTags(), r.Element()])
        existingnode = r.choice(["document.createElement('%s')" % r.HTMLTags(), r.Element()])
        return r.choice(["%s,%s" % (newNode, existingnode), newNode])

    def m_isDefaultNamespace(self):
        # 返回指定的命名空间 URI 是否为默认
        namespaceURI = r.URI()
        return "'%s'" % namespaceURI

    def m_isEqualNode(self):
        # 检查两个节点是否相等
        otherNode = r.Element()
        return otherNode

    def m_isSameNode(self):
        # 检查两个节点是否是相同的节点
        otherNode = r.Element()
        return otherNode

    def m_isSupported(self):
        # 返回当前节点是否支持某个特性
        feature = r.DOMString(r.zint(256))
        version = r.choice(["1.0", "2.0", "3.0", "4.0", "5.0"])
        return "'%s','%s'" % (feature, version)

    def m_lookupNamespaceURI(self):
        # 返回匹配指定前缀的命名空间 URI
        return "'%s'" % r.DOMString(r.zint(256))

    def m_lookupPrefix(self):
        # 返回匹配指定命名空间 URI 的前缀
        return "'%s'" % r.choice([r.URI(), ""])

    def m_normalize(self):
        # 合并相邻的Text节点并删除空的Text节点
        pass

    def m_removeChild(self):
        # 删除（并返回）当前节点的指定子节点
        return r.choice(["document.createElement('%s')" % r.HTMLTags(), r.Element()])

    def m_replaceChild(self):
        # 用新节点替换一个子节点
        newNode = r.choice(["document.createElement('%s')" % r.HTMLTags(), r.Element()])
        oldnode = r.choice(["document.createElement('%s')" % r.HTMLTags(), r.Element()])
        return "%s,%s" % (newNode, oldnode)

    def m_setUserData(self):
        # 把对象关联到节点上的一个键上
        userKey = r.choice([r.randrange(40, 92), r.randrange(93, 127), r.DOMString(r.zint(256))])
        userData = r.DOMString(r.zint(256))
        handler = r.Funcs()
        return "'%s','%s',%s" % (userKey, userData, handler)

    # TODO:IE独有属性 需重新修改
    #def m_selectNodes(self):
    #    # 用一个 XPath 表达式查询选择节点
    #    pass

    #def m_selectSingleNode(self):
    #    # 查找和 XPath 查询匹配的一个节点
    #    pass

    #def m_transformNode(self):
    #    # 使用 XSLT 把一个节点转换为一个字符串
    #    pass

    #def m_transformNodeToObject(self):
    #    # 使用 XSLT 把一个节点转换为一个文档
    #    pass