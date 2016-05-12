#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r
from modules.webidl.Node import Node
from modules.webidl.ParentNode import ParentNode
from modules.webidl.ChildNode import ChildNode
from modules.webidl.NonDocumentTypeChildNode import NonDocumentTypeChildNode

class Element(Node, ParentNode, ChildNode, NonDocumentTypeChildNode):
    '''
    Element（元素）接口是 Document的一个对象. 这个接口描述了所有相同种类的元素所普遍具有的方法和属性。
    这些继承自Element并且增加了一些额外功能的接口描述了具体的行为.
    例如,  HTMLElement 接口是所有HTML元素的基础接口， 而 SVGElement 接口是所有SVG元素的基本接口.
    '''
    # properties
    # Inherits properties from its parents Node, and its own parent, EventTarget,
    # and implements those of ParentNode, ChildNode, NonDocumentTypeChildNode, and Animatable.

    def p_accessKey(self):
        # 设置或返回访问一个链接的键盘按键
        index = [r.DOMString(2), r.DOMString(1), ""]
        return r.choice(index)

    def p_attributes(self):
        pass

    def p_childElementCount(self):
        pass

    def p_children(self):
        pass

    def p_classList(self):
        pass

    def p_className(self):
        return r.DOMString(r.zint(256))

    def p_clientHeight(self):
        pass

    def p_clientLeft(self):
        pass

    def p_clientTop(self):
        pass

    def p_clientWidth(self):
        pass

    def p_firstElementChild(self):
        pass

    def p_id(self):
        return r.DOMString(r.zint(256))

    def p_innerHTML(self):
        return r.DOMString(r.zint(256))

    def p_lastElementChild(self):
        pass

    def p_localName(self):
        pass

    def p_namespaceURI(self):
        pass

    def p_outerHTML(self):
        return r.DOMString(r.zint(256))

    def p_prefix(self):
        pass

    def p_scrollHeight(self):
        pass
    def p_scrollLeft(self):
        return r.zint(65535)

    def p_scrollLeftMax(self):
        pass

    def p_scrollTop(self):
        return r.zint(65535)

    def p_scrollTopMax(self):
        pass

    def p_scrollWidth(self):
        pass

    def p_shadowRoot(self):
        pass

    def p_tabStop(self):
        return r.bool()

    def p_tagName(self):
        pass
    def p_undoManager(self):
        pass

    def p_undoScope(self):
        return r.bool()

    # Event handlers
    def p_ongotpointercapture(self):
        return r.Funcs()

    def p_onlostpointercapture(self):
        return r.Funcs()

    def p_onwheel(self):
        return r.Funcs()

    # Methods
    # Inherits methods from its parents Node, and its own parent, EventTarget,
    # and implements those of ParentNode, ChildNode, NonDocumentTypeChildNode, and Animatable.

    def m_attachShadow(self):
        shadowRootInit = r.choice(["open", "closed"])
        return shadowRootInit

    def m_animate(self):
        keyframes = r.choice([
            "{opacity:[ %s,%s],color:[ '#%s','#%s']}" % (r.zint(2048), r.zint(2048), r.shex(3), r.shex(3)),
            "[{opacity:%s,color: '#%s'}, {opacity:%s,color: '#%s'}]" % (r.zint(2048), r.shex(3), r.zint(2048), r.shex(3)),
            "{opacity:[ %s,%s],color:[ '#%s','#%s']}" % (r.zint(2048), r.zint(2048), r.shex(6), r.shex(6)),
            "[{opacity:%s,color: '#%s'}, {opacity:%s,color: '#%s'}]" % (r.zint(2048), r.shex(6), r.zint(2048), r.shex(6)),
        ])
        keyframeOptions = r.zint(65535)
        return "%s,%s" % (keyframes, keyframeOptions)

    def m_closest(self):
        return "'%s'" % r.selector()

    def m_createShadowRoot(self):
        # Creates a shadow DOM on on the element
        pass

    # TODO:下面三个方法没有找到详细资料 需要补全
    #def m_find(self):
    #    pass

    #def m_findAll(self):
    #    pass

    #def m_getAnimations(self):
    #    pass

    def m_getAttribute(self):
        return "'%s'" % r.Attributes()

    def m_getAttributeNames(self):
        pass

    def m_getAttributeNS(self):
        namespace = r.URI()
        name = r.Attributes()
        return "'%s','%s'" % (namespace, name)

    def m_getAttributeNode(self):
        return "'%s'" % r.Attributes()

    def m_getAttributeNodeNS(self):
        namespace = r.URI()
        name = r.Attributes()
        return "'%s','%s'" % (namespace, name)

    def m_getBoundingClientRect(self):
        pass

    def m_getClientRects(self):
        # returns a collection of rectangles that indicate the bounding rectangles for each box in a client.
        pass

    #def m_getDestinationInsertionPoints(self):
    #    pass

    def m_getElementsByClassName(self):
        name = r.DOMString(r.zint(256))
        return "'%s'" % name

    def m_getElementsByTagName(self):
        tagName = r.HTMLTags()
        return "'%s'" % tagName

    def m_getElementsByTagNameNS(self):
        namespaceURI = r.URI()
        localName = ("%s.localName") % r.Element()
        return "'%s', %s" % (namespaceURI, localName)

    def m_hasAttribute(self):
        return "'%s'" % r.Attributes()

    def m_hasAttributeNS(self):
        namespaceURI = r.URI()
        localName = ("%s.localName") % r.Element()
        return "'%s', %s" % (namespaceURI, localName)

    def m_hasAttributes(self):
        pass

    def m_insertAdjacentHTML(self):
        # 插入邻近的HTML
        position = r.choice(['beforebegin', 'afterbegin', 'beforeend', 'afterend'])
        tag = r.HTMLTags()
        # TODO:这里不支持script标签，查明原因 有可能是浏览器的问题
        while tag == "script":
            tag = r.HTMLTags()
        text = "<%s>%s</%s>" % (tag, r.DOMString(r.zint(256)), tag)
        return "'%s',\"%s\"" % (position, text)

    def m_matches(self):
        return "'%s'" % r.selector()

    def m_querySelector(self):
        return "'%s'" % r.selector()

    def m_querySelectorAll(self):
        return "'%s'" % r.selector()

    def m_releasePointerCapture(self):
        return "%s.pointerId" % r.Element()

    def m_removeAttribute(self):
        return "'%s'" % r.Attributes()

    def m_removeAttributeNS(self):
        namespace = r.URI()
        name = r.Attributes()
        return "'%s','%s'" % (namespace, name)

    def m_removeAttributeNode(self):
        return "'%s'" % r.Attributes()

    def m_requestFullscreen(self):
        pass

    def m_requestPointerLock(self):
        pass

    def m_scrollIntoView(self):
        alignToTop = r.bool()
        behavior = r.choice(["auto", "instant", "smooth"])
        block = r.choice(["start", "end"])
        scrollIntoViewOptions = "{behavior:'%s',block:'%s',}" % (behavior, block)
        return r.choice(["", alignToTop, scrollIntoViewOptions])

    def m_setAttribute(self):
        name = r.Attributes()
        value = r.NiceValue()
        return "'%s',%s" % (name, value)

    def m_setAttributeNS(self):
        namespace = r.URI()
        name = r.Attributes()
        value = r.NiceValue()
        return "'%s','%s',%s" % (namespace, name, value)

    def m_setAttributeNode(self):
        return "'%s'" % r.Attributes()

    def m_setAttributeNodeNS(self):
        return "'%s'" % r.Attributes()

    def m_setCapture(self):
        return r.bool()

    def m_setPointerCapture(self):
        return "%s.pointerId" % r.Element()