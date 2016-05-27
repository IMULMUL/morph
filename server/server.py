#! /user/bin/python
# coding:UTF-8

import os
import sys
import getopt
import tornado.ioloop
import tornado.web

class UploadFileHandler(tornado.web.RequestHandler):
    def get(self):
        upload_path = os.path.join(os.path.dirname(__file__),'upload')
        file_list = os.listdir(upload_path)
        self.render('list.html', file_list=file_list)

    def post(self):
        #提取数据
        file_name = self.get_argument('file_name')
        file_content = self.get_argument('file_content')
        filepath = os.path.join(os.path.dirname(__file__), 'upload', file_name)
        # 指定encoding=utf-8 解决了下列问题
        # UnicodeEncodeError: 'gbk' codec can't encode character: illegal multibyte sequence
        file = open(filepath, 'w', encoding='utf-8')
        try:
            file.write(file_content)
        except:
            pass
        finally:
            file.close()
        self.write('true')

def usage():
    print('Upload Server usage:')
    print('  -p,--port:       Select port to listen on, 8080 default.')
    print('  -h,--help:       help message.')
    print('For example:')
    print('  server -p 8080')

if __name__ == '__main__':

    # 1.获取运行参数并检查合法性
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hp:", ["help", "port="])
    except getopt.GetoptError:
        usage()
        sys.exit()
    port = None
    for name, value in opts:
        if name in ('-p', '--port'):
            port = value
        else:
            usage()
            sys.exit()

    if port is None:
        port = 8080

    upload_path = os.path.join(os.path.dirname(__file__),'upload')

    handler = [
        (r"/upload", UploadFileHandler),
        (r"/upload/(.*)", tornado.web.StaticFileHandler, dict(path=upload_path)),
    ]
    template_path = os.path.join(os.path.dirname(__file__), "templates")
    static_path = os.path.join(os.path.dirname(__file__), "static")
    http_Server = tornado.web.Application(handlers=handler, template_path=template_path, static_path=static_path, )
    http_Server.listen(port)
    print("[+R+]: Http upload server is listening on %s..." % port)
    print("[+R+]: Url is http://127.0.0.1:%s/upload..." % port)
    tornado.ioloop.IOLoop.current().start( )