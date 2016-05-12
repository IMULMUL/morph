#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as randoms


class GlobalEventHandlers():
    '''
    The GlobalEventHandlers mixin describes the event handlers common to several interfaces like HTMLElement, Document, or Window.
    Each of these interfaces can implement more event handlers.
    GlobalEventHandlers is a mixin and not an interface and no object of this type can be created.
    '''
    # Properties
    # The events properties, of the form onXYZ, are defined on the GlobalEventHandlers, and implemented by HTMLElement,
    # Document, Window, and WorkerGlobalScope for Web Workers.
    pass