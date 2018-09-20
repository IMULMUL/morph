#! /user/bin/python
# coding:UTF-8
import logging
import tornado.web
import tornado.ioloop
import socket
import importlib
import random

template_backup = None

class FuzzHandler(tornado.web.RequestHandler):
    def initialize(self, template):
        self.template = importlib.import_module("templates.{}".format(template))
        self.template = self.template.Template()

    def get(self):
        global template_backup
        fuzz_data = self.template.generate()
        template_backup = fuzz_data.replace("window.location.reload(true);", "")
        self.write(fuzz_data.encode('utf-8'))

class SaveHandler(tornado.web.RequestHandler):
    def get(self):
        global template_backup
        self.write(template_backup.encode('utf-8'))

class Generator():
    def __init__(self, template):
        self.port = random.randint(50000, 60000)
        handler = [
            (r"/fuzz", FuzzHandler, dict(template=template)),
            (r"/save", SaveHandler),
        ]
        self.fuzz_path = "http://127.0.0.1:{}/fuzz".format(self.port)
        self.save_path = "http://127.0.0.1:{}/save".format(self.port)

        self.httpServer = tornado.web.Application(handlers=handler)
    
    def save(self):
        pass

    def check(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        try:
            sock.connect(("127.0.0.1", self.port))
            return True
        except:
            return False

    def run(self):
        # cancel log output in commandline
        logging.getLogger('tornado.access').disabled = True
        logging.getLogger('tornado.general').disabled = True
        self.httpServer.listen(self.port)
        tornado.ioloop.IOLoop.current().start()