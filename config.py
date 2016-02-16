#! /user/bin/python
# coding:UTF-8

import sys

if sys.version.find("AMD64") != -1:
    MOR_PATH = "Program Files (x86)"
else:
    MOR_PATH = "Program Files"

MOR_BROWSER = {
    "IE": {
        'path': "C:/%s/Internet Explorer/iexplore.exe" % MOR_PATH,
        'args': "",
    },
    "FF": {
        'path': "C:/%s/Mozilla Firefox/firefox.exe" % MOR_PATH,
        'args': "",
    },
    "CM": {
        'path': "C:/%s/Google/Chrome/Application/chrome.exe" % MOR_PATH,
        'args': "--no-sandbox",
    },
}

MOR_POSTFIX = ".html"

MOR_PORT = 7890
MOR_WEB = "http://127.0.0.1:%s" % MOR_PORT