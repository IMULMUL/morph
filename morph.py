#! /user/bin/python
# coding:UTF-8

import os
import sys
import getopt
import urllib.request
import multiprocessing
from PyDbgEng3 import Debugger

import config
import web

def signals():
    print('''
            __________              ____  __    __
           /  __  __  \____  ____  / __ \/ /   / /
          /  / / / /  / __ \/  __\/ /_/ / /___/ /
         /  / / / /  / /_/ /  /  /  ___/  ___  /
         \_/  \/  \_/\____/\_/   \_/   \_/  /_/

  By Walkerfuz of Taurus Security(github.com/walkerfuz)
                                  Morph - Version 0.2.5
    ''')


def usage():
    print('Morph usage:')
    print('  -b,--browser:    Select which browser,contains IE, FF, CM, etc.')
    print('  -f,--fuzzer:     Select which fuzzer to use.')
    print('  -h,--help:       help message.')
    print('For example:')
    print('  morph -b IE -f nduja.html')


def pre_fuzz(browser_args, poc_args):
    crashInfo = Debugger.Run(browser_args.encode())
    try:
        #print "Exception: Writing to file"
        # 指定encoding=utf-8 解决了下列问题
        # UnicodeEncodeError: 'gbk' codec can't encode character: illegal multibyte sequence
        fd = open("crash/" + crashInfo['bucket'] + '.crash', "w", encoding='utf-8')
        fd.write(crashInfo['description'])
        fd.close()
        vectorInfo = (urllib.request.urlopen(poc_args).read()).decode('utf-8')
        # 下述为POST方法
        #req = urllib.request.Request(poc_args, b"@#$%")
        #vectorInfo = (urllib.request.urlopen(req).read()).decode('utf-8')
        fd = open("crash/" + crashInfo['bucket'] + '.html', "w", encoding='utf-8')
        fd.write(vectorInfo)
        fd.close()
        print("[+S+]:Poc %s is saved." % crashInfo['bucket'])
    except Exception as e:
        pass

if __name__ == "__main__":
    # 1.获取运行参数
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hb:f:", ["help", "browser=", "fuzzer="])
    except getopt.GetoptError:
        usage()
        sys.exit()
    browser = None
    fuzzer = None
    for name, value in opts:
        if name in ('-b', '--browser'):
            browser = value
        elif name in ('-f', '--fuzzer'):
            fuzzer = value
        else:
            usage()
            sys.exit()

    # 判断参数是否合法
    if browser not in config.MOR_BROWSER.keys() or os.path.exists(os.path.join('fuzzer', fuzzer)) is False:
        usage()
        sys.exit()

    signals()
    # 2.开启Web服务器
    p_s = multiprocessing.Process(target=web.listen, args=(config.MOR_PORT, fuzzer, config.MOR_POSTFIX ))
    p_s.daemon = True  # 随主进程一起结束
    p_s.start()
    print("[+R+]:Web server is running...")

    # 3.浏览器打开网页样本
    browser_args = "%s %s %s " % (config.MOR_BROWSER[browser]['path'], config.MOR_BROWSER[browser]['args'], config.MOR_WEB+"/vector")
    poc_args = config.MOR_WEB+"/poc"
    while 1:
        p_b = multiprocessing.Process(target=pre_fuzz, args=(browser_args, poc_args, ))
        p_b.daemon = True
        p_b.start()
        p_b.join(300)
        p_b.terminate()