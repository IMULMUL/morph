#! /user/bin/python
# coding:UTF-8

import os
import shutil

def ReadFromFile(file):
    content = ''
    try:
        f = open(file, 'r')
    except:
        return ''
    try:
        content = f.read()
    except:
        return ''
    finally:
        f.close()
    return content

def WriteToFile(file, content):
    try:
        f = open(file, 'w')
    except:
        return False
    try:
        f.write(content)
    except:
        return False
    finally:
        f.close()
    return True

def SaveFileFromSrcToDst(src, dst):
    # 拷贝保存某个文件
    try:
        shutil.copy(src, dst)
    except:
        return False
    return True

def CopyDirFromSrcToDst(src, dst):
    # 拷贝目录
    try:
        shutil.copytree(src, dst)
    except:
        return False
    return True

def CreateFolder(folder):
    try:
        os.makedirs(folder)
    except:
        return False
    return True

def DeleteFolder(folder):
    try:
        shutil.rmtree(folder)
    except:
        return False
    return True