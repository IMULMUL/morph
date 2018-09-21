# Morph

```
            __________              ____  __    __
           /  __  __  \____  ____  / __ \/ /   / /
          /  / / / /  / __ \/  __\/ /_/ / /___/ /
         /  / / / /  / /_/ /  /  /  ___/  ___  /
         \_/  \/  \_/\____/\_/   \_/   \_/  /_/

  By Walkerfuz of Taurus Security(https://github.com/walkerfuz)
                                          Morph - Version 0.4.0
```

Morph is an open source fuzzing framework based python. 

It provides an automated way to fuzz brower, windows photo viewer, smb protocol, dll, etc. You can create any templates like domato, tiff, avi format for everything you want to fuzz.

# Features

* Support multiple browsers, such as IE, Chrome, Firefox, etc. Edge is considering.
* Support custom extension templates such as domato, peach pits etc.
* Currently only support windows, linux is under development.

## Install

1. pip install comtypes.

2. Download visual c++ redistributable 2012 and setup.
3. Download morph and run.

# Usages

Fuzzing IE with domato template:

```bash
python morph.py -f IE -g web -t domato
```

# Precautions

When fuzzing Firefox, set below arguments in `about:config` firstly：

| toolkit.startup.max_resumed_crashes    | -1    |
| :------------------------------------- | ----- |
| browser.safebrowsing.debug             | false |
| browser.sessionstore.resume_from_crash | false |



# Attentions

[1] - In Win10x64:

```
AttributeError: module 'comtypes.gen.DbgEng' has no attribute 'DEBUG_ANY_ID'
```

fix:

This is permission error in comtypes. You have to run the script as Administrator. 

# Versions

- v0.4.0 
  - Redesigned the framework.

# Todo

- [ ] develop TIFF target and template
- [ ] support edge
- [ ] support linux gdb.

# Thanks

Morph is reformed from Peach, Cisso-kitty.

- Peach - https://github.com/MozillaSecurity/peach
- Kitty Fuzzer - https://github.com/cisco-sas/kitty

------

如果有什么bug或建议，请邮件联系walkerfuz#outlook.com。
