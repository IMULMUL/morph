# About

Morph is an open source browser fuzzing framework based python.It provides an automated way to fuzz a browser.You can write yourself fuzzer for morph, for example nduja, fileja, cross_fuzz, etc.

# Features

* 支持多种浏览器，例如IE、Chrome、Firefox等
* 支持自定义扩展插件，比如nduja、fileja、cross_fuz等

# Requirements

* Required
    * Python >= 3.0
	* Tornado
	* Comtypes
	* PyDbgEng3
    * IE3+, Firefox1+, Chrome1+, etc
    * Currently only for Windows platform
	
# Usages

	Morph usage:
	  -b,--browser:    Select which browser,contains IE, FF, CM, etc.
	  -f,--fuzzer:     Select which fuzzer to use.
	  -h,--help:       help message.
	For example:
	  morph -b IE -f nduja.html

1.安装必需模块：

Download Tornado from https://pypi.python.org/pypi/tornado/ and setup.

Download Comtypes from https://github.com/enthought/comtypes and setup.

Download PyDbgEng3 from https://github.com/walkerfuz/PyDbgEng3 and setup.

Download Morph from https://github.com/walkerfuz/Morph and unrar.
	  
2.默认情况下，可以下载Morph直接运行：

> morph -b IE -f nduja.html

得到的POC样本存储在Crash目录。

3.如果Fuzzer插件除html模板外的图片或视频，可以指定某个目录作为Fuzzer插件：

> morph -b FF -f simple

# Precautions

1.如果Fuzz目标是IE，则需将IE设置为单进程模式：
> 将HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\Main下面的TabProcGrowth键值设置为0

2.如果Fuzz目标是Firefox，则需关闭安全模式：
> 在firefox进入about:config找到toolkit.startup.max_resumed_crashes（默认是3），将其设置为-1

# Versions
	
[详细信息](https://github.com/walkerfuz/morph/blob/master/versions.md)

------

如果有什么bug或建议，请邮件联系walkerfuz#outlook.com。
