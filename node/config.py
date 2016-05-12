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
        'mode': "S", # Single Process
    },
    "FF": {
        'path': "C:/%s/Mozilla Firefox/firefox.exe" % MOR_PATH,
        'args': "",
        'mode': "S", # Single Process
    },
    "CM": {
        'path': "C:/%s/Google/Chrome/Application/chrome.exe" % MOR_PATH,
        'args': "--no-sandbox",
        'mode': "M", # Multi Process
    },
    "OP": {
        'path': "C:/%s/Opera/launcher.exe" % MOR_PATH,
        'args': "--no-sandbox",
        'mode': "M", # Multi Process
    },
}

WEB_PORT = 7890
MOR_SERVER = "127.0.0.1:8080"

MOR_RESULT = "Morph - Version 0.3.0 By Walkerfuz of Taurus Security."