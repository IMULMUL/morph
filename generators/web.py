from http.server import BaseHTTPRequestHandler, HTTPServer
from functools import partial
import random
import socket
import importlib

fuzz_data_backup = None

class MyHttpRequestHandler(BaseHTTPRequestHandler):

    def __init__(self, template, *args, **kwargs):
        self.template = template
        # Resolved ConnectionResetError: [WinError 10054] 
        try:
            super().__init__(*args, **kwargs)
        except ConnectionResetError:
            pass

    # override log_message
    def log_message(self, format, *args):
        pass
    
    def fuzz_handler(self):
        global fuzz_data_backup
        fuzz_data = self.template.generate()
        fuzz_data_backup = fuzz_data.replace("window.location.reload(true);", "")
        return fuzz_data
    
    def save_handler(self):
        global fuzz_data_backup
        return fuzz_data_backup

    # GET
    def do_GET(self):
        try:
            if self.path == "/fuzz":
                response = self.fuzz_handler()
            elif self.path == "/save":
                response = self.save_handler()
            else:
                return

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(response.encode("utf-8"))
        except:
            pass

class Generator():
    def __init__(self, template):
        self.host = "127.0.0.1"
        self.port = random.randint(10000, 60000)
        self.fuzz_path = "http://127.0.0.1:{}/fuzz".format(self.port)
        self.save_path = "http://127.0.0.1:{}/save".format(self.port)

        template = importlib.import_module(template)
        self.template = template.Template()

    def check(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        ret = False
        try:
            sock.connect(("127.0.0.1", self.port))
            ret = True
        except:
            ret = False
        finally:
            sock.close()
        return ret

    def run(self): 
        handler = partial(MyHttpRequestHandler, self.template)
        self.httpd = HTTPServer((self.host, self.port), handler)
        self.httpd.serve_forever()