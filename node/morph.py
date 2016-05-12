#! /user/bin/python
# coding:UTF-8

import os
import sys
import time
import getopt
import socket
import urllib.request
import multiprocessing
import urllib.parse
import urllib.request
from PyDbgEng3 import Debugger

import config
from web import WebServer

def signals():
    print('''
            __________              ____  __    __
           /  __  __  \____  ____  / __ \/ /   / /
          /  / / / /  / __ \/  __\/ /_/ / /___/ /
         /  / / / /  / /_/ /  /  /  ___/  ___  /
         \_/  \/  \_/\____/\_/   \_/   \_/  /_/

  By Walkerfuz of Taurus Security(https://github.com/walkerfuz)
                                          Morph - Version 0.3.0
    ''')

def usage():
    print('Morph usage:')
    print('  -b,--browser:    Select which browser,contains IE, FF, CM, OP, EG, etc.')
    print('  -p,--port:       Select port to get sample and results, 7890 default.')
    print('  -m,--module:     Select which module to use.')
    print('  -s,--server:     Select which Server to save results, localhost default.')
    print('  -h,--help:       help message.')
    print('For example:')
    print('  morph -b IE -m WebAPIs')
    print('  morph -b IE -m nduja_rand -p 7890 -s 192.168.1.10:8080')

def push(url_args, file_name, file_content):
    post_data = {'file_name': file_name, 'file_content': file_content}
    post_data = urllib.parse.urlencode(post_data).encode("utf-8")
    req = urllib.request.Request(url=url_args, data=post_data)
    return urllib.request.urlopen(req).read().decode("utf-8")

def pre_fuzz(browser, proc, mode, result_url, server):
    crashInfo = Debugger.Run(proc.encode(), False, mode)
    # 目标进程被关闭
    # v0.3.1 修复判断crashInfo是否为空的正确方式
    #if crashInfo is None:
    #   return
    # 将if crashInfo is None 修改为 if not crashInfo
    if not crashInfo:
        return

    # 1. 获取漏洞样本
    try:
        vectorInfo = (urllib.request.urlopen(result_url).read()).decode('utf-8')
    except:
        print("[-E-]:Get poc file %s from %s is failed." % (crashInfo['bucket'], result_url))
        return
    # 2. 上传结果
    v_name = browser + "_" + crashInfo['bucket'] + ".html"
    c_name = browser + "_" + crashInfo['bucket'] + '.crash'
    upload_path = "http://%s/upload" % server
    if push(upload_path, c_name , crashInfo['description']) is False or push(upload_path, v_name, vectorInfo) is False:
        print("[-E-]:Push crash %s to %s is failed." % (crashInfo['bucket'], server))
        return
    print("[+R+]:Find crash %s and push to %s is succeed." % (crashInfo['bucket'], server))

def check_ser_listen(ip, port, timeout=3):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    ret = False
    try:
      sock.connect((ip, port))
      ret = True
    except:
      ret = False
    finally:
        sock.close()
    return ret

def check_args(b, m, s):
    # 判断参数是否合法
    if b not in config.MOR_BROWSER.keys():
        print("[-E-]:Brower must be in %s." % config.MOR_BROWSER.keys())
        sys.exit()

    try:
        __import__("modules." + m)
    except Exception as e:
        print("[-E-]:Importing module %s is failed because %s." % (m, e))
        sys.exit()

    server = s.split(":")
    if len(server) != 2:
        print("[-E-]:Server format %s is wrong, should like *.*.*.*:*." % s)
        sys.exit()

if __name__ == "__main__":
    # 1.获取运行参数并检查合法性
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:p:b:m:", ["help", "server=", "port=", "browser=", "module=", ])
    except getopt.GetoptError:
        usage()
        sys.exit()
    browser = None
    port = None
    module = None
    server = None
    for name, value in opts:
        if name in ('-b', '--browser'):
            browser = value
        elif name in ('-p', '--port'):
            port = value
        elif name in ('-m', '--module'):
            module = value
        elif name in ('-s', '--server'):
            server = value
        else:
            usage()
            sys.exit()
    signals()

    if port is None:
        port = config.WEB_PORT
    if server is None:
        server = config.MOR_SERVER

    check_args(browser, module, server)

    s_host = server.split(":")[0]
    s_port = int(server.split(":")[1])
    while check_ser_listen(s_host, s_port) is False:
        print("[-W-]:Can not connect to %s, should check alive or not." % server)
        time.sleep(2)

    # 2.加载WEB服务器
    web = WebServer(port, module)
    p_s = multiprocessing.Process(target=web.listen)
    p_s.daemon = True  # 随主进程一起结束
    p_s.start()
    while check_ser_listen("127.0.0.1", int(port)) is False:
        print("[+R+]: Waiting web server power on...")
        time.sleep(2)

    # 3.浏览器打开网页样本
    web = "http://127.0.0.1:%s" % port
    sample_url = web + "/sample"
    result_url = web + "/result"
    path = config.MOR_BROWSER[browser]['path']
    args = config.MOR_BROWSER[browser]['args']
    proc = "%s %s %s " % (path, args, sample_url)
    mode = config.MOR_BROWSER[browser]['mode']
    while 1:
        p_b = multiprocessing.Process(target=pre_fuzz, args=(browser, proc, mode, result_url, server, ))
        p_b.daemon = True
        p_b.start()
        p_b.join(300)
        p_b.terminate()
