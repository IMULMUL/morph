# Versions

* v0.2.5
	* 采用基于dbghelp.dll的PyDbgEng3来监控目标程序
	* 精简了Morph插件编写格式 只需要%MOR_ARRAY%
	* 采用window.reload代替了WebSocket逻辑
	* WEB Server采用Tornado实现	
	* 采用Multiprocessing代替Multithread	

* v0.2.4
	* 修复了因样本运行时间过长导致无法继续Fuzz的错误
	* 优化了Crash存储路径	

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
