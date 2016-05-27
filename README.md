![logic](https://github.com/walkerfuz/morph/blob/master/logic.png "logic")

# About

Morph is an open source browser fuzzing framework based python.It provides an automated way to fuzz a browser.You can write yourself fuzzer for morph, for example nduja, fileja, cross_fuzz, etc.

# Features

* 支持多种浏览器，例如IE、Chrome、Firefox等，正在考虑支持Edge
* 支持自定义扩展模块，比如nduja、fileja、cross_fuz等

# Requirements

* Required
    * Python >= 3.0
	* Tornado
	* PyDbgEng3
		* psutil
		* comtypes
		* Visual C++ Redistributable 2012
    * IE3-11, Firefox1+, Chrome1+, etc
    * Currently only for Windows platform
	
# Usages

    Morph usage:
      -b,--browser:    Select which browser,contains IE, FF, CM, OP, EG, etc.
      -p,--port:       Select port to get sample and results, 7890 default.
      -m,--module:     Select which module to use.
      -s,--server:     Select which Server to save results, localhost default.
      -h,--help:       help message.
	For example:
	  server -p 888
	  morph -b IE -m nduja_rand -p 7890 -s 192.168.1.10:8080

1.安装必需模块：

Download Tornado from https://pypi.python.org/pypi/tornado/ and setup.

Download psutil from https://pypi.python.org/pypi/psutil and setup.

Download comtypes from https://github.com/enthought/comtypes and setup.

Download Visual C++ Redistributable 2012 from https://www.microsoft.com/en-us/download/details.aspx?id=30679 and setup.

Download PyDbgEng3 from https://github.com/walkerfuz/PyDbgEng3 adn setup.

Download Morph from https://github.com/walkerfuz/Morph and unzip.

2.运行：

假设存储漏洞结果的服务器为192.168.1.10，运行Morph漏洞挖掘任务的客户端为192.168.1.20。

首先将Server目录拷贝至192.168.1.10服务器上，启动：

> server -p 8080

浏览器访问http://192.168.1.10:8080/upload展示收集的漏洞样本结果列表：

![server](https://github.com/walkerfuz/morph/blob/master/server.png "server")

然后将node目录拷贝至192.168.1.20客户端，运行Morph：

> morph -b IE/FF/CM -m nduja_rand -p 7890 -s 192.168.1.10:8080

![morph](https://github.com/walkerfuz/morph/blob/master/morph.png "morph")

当然客户端和服务端也可以同为一台机器，得到的结果存储在server下的upload目录。


# Modules

目前可用的modules包括nduja_rand、nduja_try、WebAPIs等。自定义Fuzzing逻辑只需编写对外提供可以生成静态样本的gen函数接口的Python脚本即可。格式如下：

```Python
#! /user/bin/python
# coding:UTF-8
class JSTemplater():
    def generate(self):
        script = self.fuzz_nduja()
        script += self.window_reload()
        script = self.gen_tags("script", script)
        head = "<title>nduja_fuzzer</title>\n"
        body = self.gen_tags("body", script)
        return head + body

def gen():
    js = JSTemplater()
    return js.generate()
```

# Precautions

1.如果Fuzz目标是IE，则需将IE设置为单进程模式：

> 将HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\Main下面的TabProcGrowth键值设置为0

2.如果Fuzz目标是Firefox，则需关闭安全模式：

> 在firefox进入about:config找到toolkit.startup.max_resumed_crashes（默认是3），将其设置为-1

关闭Firefox命令行调试提示信息：

> 将browser.safebrowsing.debug设置为false

# Versions

* v0.3.1
	* 增加了Crash二次确认逻辑，丢弃不可重现的Crash样本

* v0.3.0
	* 采用新的模块开发格式，支持Web API Fuzzing
	* 修复了浏览器单进程时Fuzz进程被错误终止的bug
	* 采用Web API module发现的漏洞样本为类似于Grinder生成的精简样本
	
[详细信息](https://github.com/walkerfuz/morph/blob/master/versions.md)

------

如果有什么bug或建议，请邮件联系walkerfuz#outlook.com。
