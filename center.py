import os
import sys
import getopt
import tornado.ioloop
import tornado.web
import argparse

class UploadFileHandler(tornado.web.RequestHandler):

    def post(self):
        # save post file
        file_name = os.path.join(os.path.dirname(__file__), "results", self.get_argument('file_name'))
        file_content = self.get_argument('file_content')
        with open(file_name, "wb") as fw:
            fw.write(file_content.encode("utf-8"))

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int, help="Listening port.")
    args = parser.parse_args()

    if not os.path.exists("results"):
        os.mkdir("results")

    handler = [
        (r"/upload", UploadFileHandler),
    ]
    http_Server = tornado.web.Application(handlers=handler)
    http_Server.listen(args.port)
    print("[+] Status: Http server is listening on {}...".format(args.port))
    print("[+] Status: Upload URL is http://0.0.0.0:{}/upload...".format(args.port))
    tornado.ioloop.IOLoop.current().start( )