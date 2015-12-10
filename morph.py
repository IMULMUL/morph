#! /user/bin/python
# coding:UTF-8

import os
import random
import threading
import time
import sys
import getopt

import server
import monitor
from core import file
import config

def generateVectors( ):
    # 生成第一个VECTOR样本
    vector_init = config.MOR_INIT_VECTOR_TEMPLET.replace("%MOR_WEBSOCKET_SERVER%", config.MOR_WEBSOCKET_SERVER, 1)
    vector_init = vector_init.replace("%MOR_CURRENT_HREF%", "0", 1)
    next = "%s%s" % ("1", config.MOR_FUZZER_SUFFIX)
    vector_init = vector_init.replace("%MOR_NEXT_HREF%", next, 1)
    init = "%s%s" % ("0", config.MOR_FUZZER_SUFFIX)
    ip = os.path.join(config.MOR_VECTORS_FOLDER, init)
    if file.WriteToFile(ip, vector_init) is False:
        return False

    for i in range(1, config.MOR_PRE_VECTORS_NUM):
        # 1.generate random arrays
        random_int_array = []
        for x in range(config.MOR_RANDOM_ARRAY_LENGTH):
            random_int_array.append(random.randint(0, config.MOR_MAX_RANDOM_NUMBER))
        # 2.replace vecotr template
        vector_content = config.MOR_FUZ_VECTOR_TEMPLET.replace("%MOR_RANDOM_INT_ARRAY%", str(random_int_array), 1)
        vector_content = vector_content.replace("%MOR_RANDOM_ARRAY_LENGTH%", str(config.MOR_RANDOM_ARRAY_LENGTH), 1)
        vector_content = vector_content.replace("%MOR_WEBSOCKET_SERVER%", config.MOR_WEBSOCKET_SERVER, 1)
        vector_content = vector_content.replace("%MOR_CURRENT_HREF%", str(i), 1)
        if i+1 >= config.MOR_PRE_VECTORS_NUM:
            next = "javascript:void(0)"
        else:
            next = "%d%s" % (i+1, config.MOR_FUZZER_SUFFIX)
        vector_content = vector_content.replace("%MOR_NEXT_HREF%", next, 1)
        # 3.save vector file
        current = "%d%s" % (i, config.MOR_FUZZER_SUFFIX)
        fp = os.path.join(config.MOR_VECTORS_FOLDER, current)
        if file.WriteToFile(fp, vector_content) is False:
            return False
    return True

def pre_fuzz():
    # 防止浏览器进程不结束导致Vectors生成失败
    config.TerminateProc()
    # 生成每次Fuzz使用的Vectors样本
    if generateVectors() is False:
        config.logging_exception('G', "Generate vectors is failed.")
        return
    # 遍历所有Vectors样本
    vector_i = 0
    config.MOR_LAST_COMPLETE_VECOTR = -1
    while vector_i < config.MOR_PRE_VECTORS_NUM:
        config.TerminateProc()
        # 浏览器打开样本Vectors
        if config.LoadBrowserProc(vector_i) is False:
            config.logging_exception('L', "Open Browser process is failed.")
            break
        # 开启Monitor监控线程
        t_m = threading.Thread(target=monitor.Watch)
        t_m.setDaemon(True)
        t_m.start()
        t_m.join(60 * 5)  # seconds
        while t_m.is_alive(): # 线程超时
            config.MOR_MONITOR_RUNNING = False
            time.sleep(1)
        # 跳到下一个需要执行的Vector序号
        vector_i = config.MOR_LAST_COMPLETE_VECOTR + 1

def morph():
    config.morph_signals()
    config.InitFuzzArgs()
    config.logging_info('S', "Morph fuzzer started at %s..." % time.strftime('%Y-%m-%d %X', time.localtime()))
    # 开启WebSocket服务器
    config.logging_info('S', "WebSocket server running on %s..." % config.MOR_WEBSOCKET_SERVER)
    ws_s = config.MOR_WEBSOCKET_SERVER.split(':')
    t_s = threading.Thread(target=server.Run, args=(ws_s[0], ws_s[1],))
    t_s.setDaemon(True) # 主线程结束时子线程也结束
    t_s.start()
    config.logging_info('L', "Morph Fuzzing loop is running...")
    while 1:
        pre_fuzz()

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hb:f:d:", ["help","browser=", "fuzzer=", "debugger="])
    except getopt.GetoptError:
        config.morph_usage()
        sys.exit()
    browser = ''
    fuzzer = ''
    debugger = ''
    # 1.获取运行参数
    for name, value in opts:
        if name in ('-b', '--browser'):
            browser = value
        elif name in ('-f', '--fuzzer'):
            fuzzer = value
        elif name in ('-d', '--debugger'):
            debugger = value
        else:
            config.morph_usage()
            sys.exit()
    # 2.若参数中没有Debugger则设置为默认的
    dbg_keys = list(config.MOR_DEBUGGERS[config.MOR_SYSTEM].keys())
    browser_keys = list(config.MOR_BROWSERS[config.MOR_SYSTEM].keys())
    if len(dbg_keys) <= 0 or len(browser_keys) <= 0:
        config.morph_signals()
        config.logging_exception('C', "MOR_BROWSER or MOR_DEBUGGER is not found in config.py.")
        sys.exit()
    if len(debugger) <= 0:
        debugger = dbg_keys[0]
    # 3.判断运行参数是否合理
    fuzzer_path = os.path.join(config.MOR_FUZZERS_FOLDER, fuzzer)
    fuzzer_exist = os.path.exists(fuzzer_path)
    if browser not in browser_keys or debugger not in dbg_keys or len(fuzzer) <= 0 or fuzzer_exist is False :
        config.morph_usage()
        sys.exit()
    # 4.运行Fuzz主进程
    config.MOR_BROWSER_NICK = browser
    config.MOR_FUZZER_NICK = fuzzer
    config.MOR_DEBUGGER_NICK = debugger
    morph()
