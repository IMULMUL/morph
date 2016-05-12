#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as randoms

class HTMLHyperlinkElementUtils():
    '''
    The HTMLHyperlinkElementUtils mixin defines utility methods and properties to work with HTMLAnchorElement and HTMLAreaElement.
    These utilities allow to deal with common features like URLs.
    '''
    # properties
    def p_hash(self):
        # 设置或者返回锚部分
        return "#" + randoms.DOMString(randoms.zint(256))

    def p_host(self):
        rand = randoms.zint(1)
        if rand == 1:
            return randoms.DOMString(randoms.zint(256))
        else:
            return "%s:%s" % (randoms.DOMString(randoms.zint(256)), randoms.zint(65535))

    def p_hostname(self):
        return randoms.DOMString(randoms.zint(256))

    def p_href(self):
        return randoms.URI()

    def p_origin(self):
        pass

    def p_password(self):
        return randoms.DOMString(randoms.zint(256))

    def p_pathname(self):
        return randoms.DOMString(randoms.zint(256))

    def p_port(self):
        return randoms.zint(65535)

    def p_protocol(self):
        return randoms.choice(["http:", "https:",])

    def p_search(self):
        return randoms.DOMString(randoms.zint(256))

    def p_username(self):
        return randoms.DOMString(randoms.zint(256))

    # Methods:This interface doesn't inherit any method.
    def m_toString(self):
        pass
