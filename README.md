# Morph
------

Morph is an open source browser fuzzing framework written by Walkerfuz of Taurus Security.It provides an automated way to fuzz a browser, like IE, Firefox, Chrome, etc.

You can write yourself fuzzer for morph, for example nduja, fileja, cross_fuzz, etc.

# Features

* 支持多种浏览器，例如IE、Chrome、Firefox等
* 支持自定义扩展插件，比如nduja、fileja、cross_fuz等

# Requirements

* Required
    * Python >= 3.4
    * IE9+, Firefox6+, Chrome14+, etc
    * Current only for Windows x86 or x64 system
* Optional
    * Windbg and !exploitable plug-in

# Usages

	Morph usage:
	  -b,--browser:    Select which browser,contains IE, FF, CM, etc.
	  -f,--fuzzer:     Select which fuzzer to use.
	  -d,--debugger:   Select which debugger monitor uses, contains WerFault, windbg, gdb, etc.
					   This parameter is optional.
	  -h,--help:       help message.
	For example:
	  morph --browser=IE --fuzzer=nduja.html
	  morph --browser=FF --fuzzer=simple --debugger=windbg

1.默认情况下，可以下载Morph直接运行：

> morph -b IE -f nduja.html

监控器进程根据config.py中设置的默认异常进程判断是否发生Crash。

2.如果Fuzzer插件包括html模板和其它文档，可以指定某个目录作为Fuzzer插件：

> morph --browser=FF --fuzzer=simple

程序会将simple目录下的simple.html作为Fuzzer插件模板，其余文件被拷贝至样本目录以供调用。

3.除使用默认的WerFault.exe作为异常进程外，也可以选择Windbg作为Debugger即时调试器：

> morph --browser=FF --fuzzer=nduja.html --debugger=windbg

这种情况下，需要在Fuzz之前将cdb.exe设置为系统默认即时调试器：

> cdb.exe -iaec "-logo c:/log.txt -c \"!load msec.dll;!exploitable -v;\""

设置默认即时调试器的作用时，当浏览器进程发生崩溃时，会调用cdb.exe并执行上面的命令。必须保证该命令中的c:/log.txt与config.py中MOR_DEBUGGERS对应的log参数一致。另外!load msec.dll;!exploitable -v命令用于判断漏洞样本的可利用性。

> 安装!exploitable：将MSEC.dll拷贝至windbg/winext目录，并在windbg中提前测试load msec.dll是否成功。
若出现Can't Load Library错误，则需要安装Visual C++ Redistributable 2008/2012运行时环境。

4.在Fuzz之前需要开启目标浏览器进程的页堆调试功能，比如IE浏览器：

> gflags.exe /i iexplore.exe +hpa

5.如果Fuzz目标是Firefox，则需要关闭安全模式。
> 在firefox进入about:config找到toolkit.startup.max_resumed_crashes（默认是3），将其设置为-1即可。

# Versions

* v0.2.4
	* 修复了因样本运行时间过长导致无法继续Fuzz的错误
* v0.2.3
	* 修复了Dict字典无序性导致默认Debugger取值混乱的错误
	* 修复了Fuzzer作为目录形式时Crash目录缺少Fuzzer相关文件的错误
	
[详细信息](https://github.com/walkerfuz/morph/blob/master/versions.md)

# Others

如果设置了cdb.exe作为系统默认的即时调试器，若后续想采用WerFault.exe监控方法，需要提前取消之前的即时设置。

取消cdb.exe默认即时调试器的方法：将注册表以下两个位置的Debugger 和Auto键值删除。

> x86：HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AeDebug

> x64： HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows NT\CurrentVersion\AeDebug

------

如果有什么bug或建议，请邮件联系walkerfuz#outlook.com。
