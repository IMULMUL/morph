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

MOR_PRE_VECTORS_NUM = 150
MOR_RANDOM_ARRAY_LENGTH = 10000
MOR_MAX_RANDOM_NUMBER = 1000
MOR_WEBSOCKET_SERVER = "127.0.0.1:8080"

MOR_BROWSERS = {
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
}

MOR_DEBUGGERS = {
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
}

# configs which Do not recommend changes
MOR_LAST_COMPLETE_VECOTR = -1
MOR_MONITOR_RUNNING = False

MOR_FUZZER_NICK = ""
MOR_BROWSER_NICK = ""
MOR_DEBUGGER_NICK = ""
MOR_FUZ_VECTOR_TEMPLET = ""
MOR_END_VECTOR_TEMPLET = ""

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

def TerminateProc( ):
    while psutil.exist_process(MOR_DEBUGGERS[MOR_DEBUGGER_NICK]['proc']):
        psutil.kill_process(MOR_DEBUGGERS[MOR_DEBUGGER_NICK]['proc'])
        time.sleep(1)
    while psutil.exist_process(MOR_BROWSERS[MOR_BROWSER_NICK]['fault']):
        psutil.kill_process(MOR_BROWSERS[MOR_BROWSER_NICK]['fault'])
        time.sleep(1)
    while psutil.exist_process(MOR_BROWSERS[MOR_BROWSER_NICK]['proc']):
        psutil.kill_process(MOR_BROWSERS[MOR_BROWSER_NICK]['proc'])
        time.sleep(1)

def LoadBrowserProc(vector):
    vector_path = os.path.join(os.path.abspath(""), MOR_VECTORS_FOLDER, str(vector) + MOR_FUZZER_SUFFIX)
    command = MOR_BROWSERS[MOR_BROWSER_NICK]['path'] + " " + MOR_BROWSERS[MOR_BROWSER_NICK]['args'] \
              + " " + "file:///" + vector_path
    return psutil.load(command)

def InitFuzzArgs():
    global MOR_FUZ_VECTOR_TEMPLET, MOR_END_VECTOR_TEMPLET
    # 检查Browser程序和Debugger是否存在
    b_if = os.path.exists(MOR_DEBUGGERS[MOR_DEBUGGER_NICK]['path'])
    d_if = os.path.exists(MOR_BROWSERS[MOR_BROWSER_NICK]['path'])
    if not b_if or not d_if:
        logging_exception('I', "Browser %s or Debugger %s module is not found, plz recheck."
                          % (MOR_DEBUGGERS[MOR_DEBUGGER_NICK]['path'], MOR_BROWSERS[MOR_BROWSER_NICK]['path']))
        sys.exit()
    # 检查Crashes和Vectors文件夹是否存在 不存在就创建
    if not os.path.exists(MOR_CRASHES_FOLDER):
        try:
            os.makedirs(MOR_CRASHES_FOLDER)
        except:
            logging_exception('I', "Could not create folder:%s." % MOR_CRASHES_FOLDER)
            sys.exit()
    if os.path.exists(MOR_VECTORS_FOLDER):
        try:
            shutil.rmtree(MOR_VECTORS_FOLDER)
        except:
            logging_exception('I', "Could not delete folder:%s." % MOR_VECTORS_FOLDER)
            sys.exit()
    # 检查Fuzzer插件和init.morph配置文件是否存在 并读取模板
    fuzzer = os.path.join(MOR_FUZZERS_FOLDER, MOR_FUZZER_NICK)
    if os.path.isdir(fuzzer) is True:
        if file.CopyDirFromSrcToDst(fuzzer, MOR_VECTORS_FOLDER) is False:
            logging_exception('I', "Could not copy folder:%s to %s." % (fuzzer, MOR_VECTORS_FOLDER))
            sys.exit()
        fuzzer_path = os.path.join(fuzzer, MOR_FUZZER_NICK + MOR_FUZZER_SUFFIX)
    elif os.path.isfile(fuzzer) is True:
        fuzzer_path = fuzzer
        try:
            os.makedirs(MOR_VECTORS_FOLDER)
        except:
            logging_exception('I', "Could not create folder:%s." % MOR_VECTORS_FOLDER)
            sys.exit()
    else:
        logging_exception('I', "Can not find %s in path %s." % (MOR_FUZZER_NICK, MOR_FUZZERS_FOLDER))
        sys.exit()
    MOR_FUZ_VECTOR_TEMPLET = file.ReadFromFile(fuzzer_path)
    MOR_END_VECTOR_TEMPLET = file.ReadFromFile(os.path.join(MOR_FUZZERS_FOLDER, 'init.morph'))
    if len(MOR_FUZ_VECTOR_TEMPLET) <= 0 or len(MOR_END_VECTOR_TEMPLET) <= 0:
        logging_exception('I', "Read fuzzer:%s or init.morph from %s is failed." % (MOR_FUZZER_NICK, MOR_FUZZERS_FOLDER))
        sys.exit()
    logging_info('I', "Loaded fuzzer:%s and inint.morph." % MOR_FUZZER_NICK)

def logging_info(module, info):
    print("[+%s+]: %s" % (module,info))
def logging_exception(module, err):
    print("[-%s-]: %s" % (module, err))