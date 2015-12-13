# About

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

* v0.2.3
	* 修复了Dict字典无序性导致默认Debugger取值混乱的错误
	* 修复了Fuzzer作为目录形式时Crash目录缺少Fuzzer相关文件的错误

* v0.2.2
	* 优化了Fuzzer插件读取策略，能够支持Fuzzer目录作为插件
	* 优化监控器逻辑，使得不安装Windbg也可以进行Fuzz
	* 更改了Browser和Debugger相关参数的跨平台特性

* v0.2.1
	* 优化了Fuzzer插件的编写格式，将其分为morph_random、morph_fuzz和morph_notify_href三部分
	* 解决了连续两个样本存在Crash时Morph序号读取死循环的错误
    * 优化了样本重现时的对WebSockets有依赖的逻辑
	* 增加了关闭Firefox安全模式的方法

* v0.2.0
	* 全面改写为静态Fuzz框架 采用file:///本地打开网页进行Fuzz

* v0.1.5
	* 解决了MSECExtentions v1.6.0插件在Windbg中出现Can't load Library的错误
	
* v0.1.3
	* 增加了t_m.isAlive判断监控进程是否真正结束的标志
	
* v0.1.2
	* 解决了Process32First和Process32Next返回值不等同于Python False对象类型引起的bug

* v0.1.1
	* 解决了threading.join超时后监控CrashProc的Monitor子线程没有结束的bug

* v0.1.0
	* 解决了浏览器标签页无响应阻塞Fuzz循环继续进行的bug

# Others

如果设置了cdb.exe作为系统默认的即时调试器，若后续想采用WerFault.exe的监控方法，需要提前取消之前的即时设置。

取消cdb.exe默认即时调试器的方法：将注册表以下两个位置的Debugger 和Auto键值删除。

> x86：HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AeDebug

> x64： HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows NT\CurrentVersion\AeDebug

------

如果有什么bug或建议，请邮件联系walkerfuz@outlook.com。
