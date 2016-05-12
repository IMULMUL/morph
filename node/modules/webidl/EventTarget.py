#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as randoms

class EventTarget():
    '''
    EventTarget is an interface implemented by objects that can receive events and may have listeners for them.
    Element, document, and window are the most common event targets, but other objects can be event targets too,
    for example XMLHttpRequest, AudioNode, AudioContext, and others.
    Many event targets (including elements, documents, and windows) also support setting event handlers via on... properties and attributes.
    '''
    # methods
    def m_addEventListener(self):
        # 在这个EventTarget上添加指定事件类型的事件监听器 调用之前必须创建一个函数
        event = randoms.Events()
        function = randoms.Funcs()
        useCapture = randoms.bool()
        return "'%s',%s,%s" % (event, function, useCapture)

    def m_removeEventListener(self):
        # 从这个EventTarget移除事件监听器
        event = randoms.Events()
        function = randoms.Funcs()
        useCapture = randoms.bool()
        return "'%s',%s,%s" % (event, function, useCapture)

    def m_dispatchEvent(self):
        # 为这个EventTarget派发事件 调用之前必须创建一个Event对象
        return randoms.EvtObj()