# Morph

```
            __________              ____  __    __
           /  __  __  \____  ____  / __ \/ /   / /
          /  / / / /  / __ \/  __\/ /_/ / /___/ /
         /  / / / /  / /_/ /  /  /  ___/  ___  /
         \_/  \/  \_/\____/\_/   \_/   \_/  /_/

  By Walkerfuz of Taurus Security(https://github.com/walkerfuz)
                                          Morph - Version 0.4.1
```

Morph is an open source fuzzing framework based python. 

It provides an automated way to fuzz brower, windows photo viewer, smb protocol, dll, etc. You can create any templates like domato, tiff, avi format for everything you want to fuzz.

# Features

* Support multiple browsers, such as IE, Chrome, Firefox, etc. Edge is considering.
* Support custom extension templates such as domato, peach pits etc.
* Currently only support windows, linux is under development.

## Install

1. pip install comtypes.

2. **Download [Visual C++ Redistributable for Visual Studio 2012 Update 4](https://www.microsoft.com/en-us/download/details.aspx?id=30679) and setup.**
3. Download morph and run.

# Usages

Fuzzing IE with domato template:

```bash
python morph.py samples/chrome.json
```

Attention:

You have to run the script as Administrator. 

# Precautions

When fuzzing Firefox, set below arguments in `about:config` firstly：

| toolkit.startup.max_resumed_crashes    | -1    |
| :------------------------------------- | ----- |
| browser.safebrowsing.debug             | false |
| browser.sessionstore.resume_from_crash | false |

# Versions

- v0.4.1
  - Fix `ConnectionResetError: [WinError 10054]` bug
  -  Redesigned the framework with json config

# Todo

- [ ] [v0.5.0] develop file format
- [ ] [v0.6.0] support edge
- [ ] [...] support peach pits and linux gdb.

# Thanks

Morph is reformed from Peach, Cisso-kitty.

- Peach - https://github.com/MozillaSecurity/peach
- Kitty Fuzzer - https://github.com/cisco-sas/kitty

------

If there is any bug or suggestion, please contact to walkerfuz#outlook.com。
