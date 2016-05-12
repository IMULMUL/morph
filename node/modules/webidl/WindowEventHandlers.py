#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as r


class WindowEventHandlers():
    '''
    WindowEventHandlers mixin describes the event handlers common to several interfaces
    like Window, or HTMLBodyElement and  HTMLFrameSetElement.
    Each of these interfaces can implement additional specific event handlers.
    WindowEventHandlers is a not an interface and no object of this type can be created.
    '''
    # Properties
    # The events properties, of the form onXYZ, are defined on the WindowEventHandlers,
    # and implemented by Window, and WorkerGlobalScope for Web Workers.

    def p_onafterprint(self):
        return r.Funcs()

    def p_onbeforeprint(self):
        return r.Funcs()

    def p_onbeforeunload(self):
        return r.Funcs()

    def p_onhashchange(self):
        return r.Funcs()

    def p_onlanguagechange(self):
        return r.Funcs()

    def p_onmessage(self):
        return r.Funcs()

    def p_onoffline(self):
        return r.Funcs()

    def p_ononline(self):
        return r.Funcs()

    def p_onpagehide(self):
        return r.Funcs()

    def p_onpageshow(self):
        return r.Funcs()

    def p_onpopstate(self):
        return r.Funcs()

    def p_onstorage(self):
        return r.Funcs()

    def p_onunhandledrejection(self):
        return r.Funcs()

    def p_onunload(self):
        return r.Funcs()

    # Methods
    # This interface defines no method.