#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r
from modules.webidl.HTMLElement import HTMLElement

class HTMLCanvasElement(HTMLElement):
    '''
    The HTMLCanvasElement interface provides properties and methods for manipulating the layout and presentation of canvas elements.
    The HTMLCanvasElement interface also inherits the properties and methods of the HTMLElement interface.
    '''
    # properties
    # Inherits properties from its parent, HTMLElement.

    def p_height(self):
        # 设置 canvas 的高度
        return r.zint(2048)

    def p_mozOpaque(self):
        return r.bool()

    def p_width(self):
        # 设置 canvas 的宽度
        return r.zint(2048)

    # Methods
    # Inherits methods from its parent, HTMLElement.
    def m_captureStream(self):
        return r.choice([r.double(1), ""])

    def m_getContext(self):
        # 获取绘图环境
        contextID = ["2d", "webgl2", "webgl", "bitmaprenderer"]
        return "'%s'" % r.choice(contextID)

    def m_toDataURL(self):
        # 将canvas转换为基于Base64编码的图像
        type = r.choice(["image/png", "image/jpeg"])
        args = r.double(1)
        return r.choice(["'%s',%s" % (type, args), "'%s'" % type, ""])

    def m_toBlob(self):
        callback = r.Funcs()
        mimeType = r.MIMEType()
        qualityArgument = r.double(1)
        return "'%s','%s',%s" % (callback, mimeType, qualityArgument)

    def m_transferControlToOffscreen(self):
        pass

    def m_mozGetAsFile(self):
        name = r.DOMString(r.zint(256))
        type= r.MIMEType()
        return "'%s','%s'" % (name, type)