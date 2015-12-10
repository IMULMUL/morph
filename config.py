#! /user/bin/python
# coding:UTF-8

import platform
import os
import time
import sys
import shutil

from core import psutil, file

# configs which Can be modified
MOR_FUZZERS_FOLDER = "fuzzer"
MOR_CRASHES_FOLDER = "crash"
MOR_VECTORS_FOLDER = "vector"
MOR_FUZZER_SUFFIX = ".html"
MOR_DBGLOG_SUFFIX = ".log"

MOR_PRE_VECTORS_NUM = 100
MOR_RANDOM_ARRAY_LENGTH = 10000
MOR_MAX_RANDOM_NUMBER = 1000
MOR_WEBSOCKET_SERVER = "127.0.0.1:8080"

MOR_BROWSERS = {
    "Windows": {
        "IE": {
            'proc': 'iexplore.exe',
            'args': "",
            'fault': "WerFault.exe",
            'path': "C:/Program Files/Internet Explorer/iexplore.exe",
        },
        "FF": {
            'proc': 'firefox.exe',
            'args': "",
            'fault': "WerFault.exe",
            'path': "C:/Program Files (x86)/Mozilla Firefox/firefox.exe",
        },
        "CM": {
            'proc': 'chrome.exe',
            'args': "--no-sandbox",
            'fault': "WerFault.exe",
            'path': "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
        },
    },
    "Linux": {
        "FF": {
            'proc': 'firefox',
            'args': "",
            'fault': "",
            'path': "",
        },
    },
}

# 必须保证至少有一个Debugger
MOR_DEBUGGERS = {
    "Windows": {
        "WerFault": {
            'proc': "WerFault.exe",
            'path': "C:/Windows/System32/WerFault.exe",
            'log': "",
        },
        "windbg": {
            'proc': "cdb.exe",
            'path': "C:/Program Files (x86)/Debugging Tools for Windows (x86)/cdb.exe",
            'log': "C:/log.txt",
        },
    },
    "Linux": {
        "gdb": {
            'proc': "gdb",
            'path': "/usr/bin/gdb",
            'log': "",
        },
    },
}

# configs which Do not recommend changes
MOR_LAST_COMPLETE_VECOTR = -1
MOR_MONITOR_RUNNING = False

MOR_FUZZER_NICK = ""
MOR_BROWSER_NICK = ""
MOR_DEBUGGER_NICK = ""
MOR_FUZ_VECTOR_TEMPLET = ""
MOR_INIT_VECTOR_TEMPLET = ""
MOR_SYSTEM = platform.system()

# Some global functions to call
def morph_signals():
    print('''
            __________              ____  __    __
           /  __  __  \____  ____  / __ \/ /   / /
          /  / / / /  / __ \/  __\/ /_/ / /___/ /
         /  / / / /  / /_/ /  /  /  ___/  ___  /
         \_/  \/  \_/\____/\_/   \_/   \_/  /_/

  By Walkerfuz of Taurus Security(github.com/walkerfuz)
                                  Morph - Version 0.2.2
    ''')

def morph_usage():
    morph_signals()
    print('Morph usage:')
    print('  -b,--browser:    Select which browser,contains IE, FF, CM, etc.')
    print('  -f,--fuzzer:     Select which fuzzer to use.')
    print('  -d,--debugger:   Select which debugger monitor uses, contains WerFault, windbg, gdb, etc.')
    print('                   This parameter is optional, default is WerFault.')
    print('  -h,--help:       help message.')
    print('For example:')
    print('  morph --browser=IE --fuzzer=nduja.html')
    print('  morph --browser=IE --fuzzer=simple --debugger=windbg')

def TerminateProc( ):
    d_proc = MOR_DEBUGGERS[MOR_SYSTEM][MOR_DEBUGGER_NICK]['proc']
    b_fault_proc = MOR_BROWSERS[MOR_SYSTEM][MOR_BROWSER_NICK]['fault']
    b_proc = MOR_BROWSERS[MOR_SYSTEM][MOR_BROWSER_NICK]['proc']
    while psutil.exist_process(d_proc):
        psutil.kill_process(d_proc)
        time.sleep(1)
    while psutil.exist_process(b_fault_proc):
        psutil.kill_process(b_fault_proc)
        time.sleep(1)
    while psutil.exist_process(b_proc):
        psutil.kill_process(b_proc)
        time.sleep(1)

def LoadBrowserProc(vector):
    vector_path = os.path.join(os.path.abspath(""), MOR_VECTORS_FOLDER, str(vector) + MOR_FUZZER_SUFFIX)
    command = MOR_BROWSERS[MOR_SYSTEM][MOR_BROWSER_NICK]['path'] + " " + MOR_BROWSERS[MOR_SYSTEM][MOR_BROWSER_NICK]['args'] \
              + " " + "file:///" + vector_path
    return psutil.load(command)

def InitFuzzArgs():
    global MOR_FUZ_VECTOR_TEMPLET, MOR_INIT_VECTOR_TEMPLET
    # 检查Browser程序和Debugger是否存在
    b_path = MOR_BROWSERS[MOR_SYSTEM][MOR_BROWSER_NICK]['path']
    d_path = MOR_DEBUGGERS[MOR_SYSTEM][MOR_DEBUGGER_NICK]['path']
    if not os.path.exists(b_path) or not os.path.exists(d_path):
        logging_exception('I', "Browser %s or Debugger %s module is not found." % (b_path, d_path))
        sys.exit()
    # 检查Crashes目录是否存在，不存在就创建
    if not os.path.exists(MOR_CRASHES_FOLDER) and file.CreateFolder(MOR_CRASHES_FOLDER) is False:
        logging_exception('I', "Could not create folder:%s." % MOR_CRASHES_FOLDER)
        sys.exit()
    # 检查Vectors目录是否存在，存在就清空
    if os.path.exists(MOR_VECTORS_FOLDER) and file.DeleteFolder(MOR_VECTORS_FOLDER) is False:
        logging_exception('I', "Could not delete folder:%s." % MOR_VECTORS_FOLDER)
        sys.exit()
    # 检查Fuzzer插件和init.morph配置文件是否存在 并读取模板
    f_path = os.path.join(MOR_FUZZERS_FOLDER, MOR_FUZZER_NICK)
    if os.path.isdir(f_path) is True:
        if file.CopyDirFromSrcToDst(f_path, MOR_VECTORS_FOLDER) is False:
            logging_exception('I', "Could not copy folder:%s to %s." % (f_path, MOR_VECTORS_FOLDER))
            sys.exit()
        f_path = os.path.join(f_path, MOR_FUZZER_NICK + MOR_FUZZER_SUFFIX)
    elif os.path.isfile(f_path) is True:
        if file.CreateFolder(MOR_VECTORS_FOLDER) is False:
            logging_exception('I', "Could not create folder:%s." % MOR_VECTORS_FOLDER)
            sys.exit()
    else:
        logging_exception('I', "Can not find %s in path %s." % (MOR_FUZZER_NICK, MOR_FUZZERS_FOLDER))
        sys.exit()
    MOR_FUZ_VECTOR_TEMPLET = file.ReadFromFile(f_path)
    MOR_INIT_VECTOR_TEMPLET = file.ReadFromFile(os.path.join(MOR_FUZZERS_FOLDER, 'init.morph'))
    if len(MOR_FUZ_VECTOR_TEMPLET) <= 0 or len(MOR_INIT_VECTOR_TEMPLET) <= 0:
        logging_exception('I', "Read fuzzer:%s or init.morph from %s is failed." % (MOR_FUZZER_NICK, MOR_FUZZERS_FOLDER))
        sys.exit()
    logging_info('I', "Loaded fuzzer:%s and inint.morph." % MOR_FUZZER_NICK)

def logging_info(module, info):
    print("[+%s+]: %s" % (module,info))
def logging_exception(module, err):
    print("[-%s-]: %s" % (module, err))