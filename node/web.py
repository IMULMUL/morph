#! /user/bin/python
# coding:UTF-8
import logging
import tornado.web
import tornado.ioloop

import config

class MainHandler(tornado.web.RequestHandler):
    def initialize(self, module):
        self.module = __import__("modules." + module, {}, {}, ["mod"])

    def get(self):
        temp = self.module.gen()
        config.MOR_RESULT = temp.replace("window.location.reload(true);", "")
        self.write(temp.encode('utf-8'))

class PocHandler(tornado.web.RequestHandler):
    def get(self):
       self.write(config.MOR_RESULT.encode('utf-8'))

class FileHandler():
    def set_extra_headers(self, path):
        self.set_header("Cache-control", "no-cache")


class WebServer():
    def __init__(self, port, module):
        self.port = port
        self.static = module
        handler = [
            (r"/sample", MainHandler, dict(module=module)),
            (r"/result", PocHandler),
            (r"/static/(.*)", tornado.web.StaticFileHandler, dict(path=self.static)),
        ]
        self.httpServer = tornado.web.Application(handlers=handler)

    def listen(self):
        # cancel log output in commandline
        logging.getLogger('tornado.access').disabled = True
        logging.getLogger('tornado.general').disabled = True

        self.httpServer.listen(self.port)
        tornado.ioloop.IOLoop.current().start()