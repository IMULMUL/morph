# Morph

Morph is an open source fuzzing framework based python. 

![](./morph.png)

It provides an automated way to fuzz brower, windows photo viewer, smb protocol, dll, etc. You can create any templates like domato, tiff, avi format for everything you want to fuzz.

# Features

* Support multiple browsers, such as IE, Chrome, Firefox, etc. Edge is considering.
* Support custom extension templates such as domato, peach pits etc.
* Currently only support windows, linux is under development.

## Install

1. pip install comtypes.
2. [Optional when using center.py] pip install tornado
3. **Download [Visual C++ Redistributable for Visual Studio 2012 Update 4](https://www.microsoft.com/en-us/download/details.aspx?id=30679) and setup.**
4. Download morph and run.

# Usages

### 0x01. fuzzing only at local machine:

Fuzzing IE with domato template:

1. Setting samples/ie.json:

```
{
    "fuzzer": "fuzzers.browser",
    "argument":{
        "proc_path": "C:/Program Files/Internet Explorer/iexplore.exe",
        "proc_name": "iexplore.exe",
        "proc_args": "",
        
        "generator": "generators.web",
        "template": "templates.domato",
        "gflags": "monitors.windbg.gflags",
        "debugger": "monitors.windbg.UserDebugger",

        "fuzz_results_dir": "results"
    }
}
```

2. Then run the script as Administrator:

```bash
python morph.py samples/ie.json
```

### 0x02. fuzzing and saving results to Remote Server:

1. setting samples/ie.json:

```
{
    "fuzzer": "fuzzers.browser",
    "argument":{
        "proc_path": "C:/Program Files/Internet Explorer/iexplore.exe",
        "proc_name": "iexplore.exe",
        "proc_args": "",
        
        "generator": "generators.web",
        "template": "templates.domato",
        "gflags": "monitors.windbg.gflags",
        "debugger": "monitors.windbg.UserDebugger",

        "fuzz_results_dir": "http://192.168.1.200:8080/upload"
    }
}
```

2. Then run center.py in Remote server 192.168.1.200:

```
python center.py 8080
```

3. And run morph script as Administrator in client machine:

```bash
python morph.py samples/ie.json
```

All results saved to `results` directory.

# Precautions

1. When fuzzing IE, Internet Options --> Advanced, cancel below：

- 启用自动崩溃恢复
- 通过页面预测启用快速翻页
- 在后台加载站点和内容以优化性能

2. When fuzzing Firefox, set below arguments in `about:config` firstly：

| toolkit.startup.max_resumed_crashes    | -1    |
| :------------------------------------- | ----- |
| browser.safebrowsing.debug             | false |
| browser.sessionstore.resume_from_crash | false |

# Versions

- v0.4.2
  - Add center.py to save results remotely.
- v0.4.1
  - Fix `ConnectionResetError: [WinError 10054]` bug
  -  Redesigned the framework with json config

# Todo

- [ ] [v0.5.0] optimize domato template and support file format  2018/10/10
- [ ] [v0.6.0] support Microsoft Edge 2018/10/30
- [ ] [...] support peach pits and linux debugger.

# Thanks

Morph is reformed from Peach, Cisso-kitty.

- Peach - https://github.com/MozillaSecurity/peach
- Kitty Fuzzer - https://github.com/cisco-sas/kitty

------

If there is any bug or suggestion, please contact to walkerfuz#outlook.com。
