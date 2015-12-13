#! /user/bin/python
# coding:UTF-8

import os
import stat
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

# 改进的shutil.copytree 可以拷贝至目标已存在的目录中
def copytree(src, dst, symlinks = False, ignore = None):
  if not os.path.exists(dst):
    os.makedirs(dst)
    shutil.copystat(src, dst)
  lst = os.listdir(src)
  if ignore:
    excl = ignore(src, lst)
    lst = [x for x in lst if x not in excl]
  for item in lst:
    s = os.path.join(src, item)
    d = os.path.join(dst, item)
    if symlinks and os.path.islink(s):
      if os.path.lexists(d):
        os.remove(d)
      os.symlink(os.readlink(s), d)
      try:
        st = os.lstat(s)
        mode = stat.S_IMODE(st.st_mode)
        os.lchmod(d, mode)
      except:
        pass
    elif os.path.isdir(s):
      copytree(s, d, symlinks, ignore)
    else:
      shutil.copy2(s, d)

def CopyDirFromSrcToDst(src, dst):
    # 拷贝目录
    try:
        copytree(src, dst)
    except:
        return False
    return True