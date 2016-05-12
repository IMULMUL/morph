#! /user/bin/python
# coding:UTF-8

import random

def zint(max):
    return int(random.randint(0, max))

def choice(list):
    return random.choice(list)

def bool():
    return zint(2)

def randrange(left, right):
    return random.randrange(left, right)

def shex(num):
    chars = "0123456789ABCDEF"
    ret = ""
    for i in range(num):
        ret += random.choice(chars)
    return ret

def DOMString(num): # UTF-16
    chars = "0123456789ABCDEF"
    ret = ""
    for i in range(num):
        char = "\\u%s" % shex(4)
        ret += char
    return ret

def coords(max):
    num = zint(max)
    ret = zint(max)
    for i in range(num):
        ret = "%s,%s" % (ret, zint(max))
    return ret

def URI():
    ns = [
        'http://www.w3.org/2001/XMLSchema#','http://www.w3.org/2000/01/rdf-schema#',
        'http://www.w3.org/ns/prov#','http://www.w3.org/TR/html4/','http://www.w3.org/TR/html5/',
        'http://www.w3.org/1999/XSL/Transfor','http://www.w3.org/1999/xhtml',
        'http://www.w3.org/2000/svg','http://www.elsherei.com',
        'http://www.google.com',
        "",
    ]
    return random.choice(ns)

def language():
    lang = [
        "ab","aa","af","sq","am","ar","an","hy","as","ay","az","ba","eu","bn","dz","bh","bi","br","bg","my","be","km",
        "ca","zh","zh-Hans","zh-Hant","co","hr","cs","da","nl","en","eo","et","fo","fa","fj","fi","fr","fy","gl","gd",
        "gv","ka","de","el","kl","gn","gu","ht","ha","he"," iw","hi","hu","is","io","id","in","ia","ie","iu","ik","ga",
        "it","ja","jv","kn","ks","kk","rw","ky","rn","ko","ku","lo","la","lv","li","ln","lt","mk","mg","ms","ml","mt",
        "mi","mr","mo","mn","na","ne","no","oc","or","om","ps","pl","pt","pa","qu","rm","ro","ru","sm","sg","sa","sr",
        "sh","st","tn","sn","ii","sd","si","ss","sk","sl","so","es","su","sw","sv","tl","tg","ta","tt","te","th","bo",
        "ti","to","ts","tr","tk","tw","ug","uk","ur","uz","vi","vo","wa","cy","wo","xh","yi","ji","yo","zu","",
    ]
    return random.choice(lang)

def sample(list, num):
    # 随机取出不重复的元素
    return random.sample(list, num)

def sample2(list, split):
    # 随机取出不重复的元素 random.sample增强版
    num = zint(len(list))
    ret_list = random.sample(list, num)
    if len(ret_list) == 0:
        return ""
    ret = ret_list[0]
    for i in range(len(ret_list)-1):
        ret = "%s%s%s" % (ret, split, ret_list[i+1])
    return ret

def double(max):
    return random.random() * max

def MIMEType():
    MimeType = [
        "application/envoy", "application/fractals", "application/futuresplash", "application/hta", "application/internet-property-stream",
        "application/mac-binhex40", "application/msword", "application/octet-stream", "application/oda", "application/olescript",
        "application/pdf", "application/pics-rules", "application/pkcs10", "application/pkix-crl", "application/postscript",
        "application/rtf", "application/set-payment-initiation", "application/set-registration-initiation", "application/vnd.ms-excel",
        "application/vnd.ms-outlook", "application/vnd.ms-pkicertstore", "application/vnd.ms-pkiseccat", "application/vnd.ms-pkistl",
        "application/vnd.ms-powerpoint", "application/vnd.ms-project", "application/vnd.ms-works", "application/winhlp",
        "application/x-bcpio", "application/x-cdf", "application/x-compress", "application/x-compressed", "application/x-cpio",
        "application/x-csh", "application/x-director", "application/x-dvi", "application/x-gtar", "application/x-gzip", "application/x-hdf",
        "application/x-internet-signup", "application/x-iphone", "application/x-javascript", "application/x-latex", "application/x-msaccess",
        "application/x-mscardfile", "application/x-msclip", "application/x-msdownload", "application/x-msmediaview", "application/x-msmetafile",
        "application/x-msmoney", "application/x-mspublisher", "application/x-msschedule", "application/x-msterminal", "application/x-mswrite",
        "application/x-netcdf", "application/x-netcdf", "application/x-perfmon", "application/x-pkcs12", "application/x-pkcs7-certificates",
        "application/x-pkcs7-certreqresp", "application/x-pkcs7-mime", "application/x-pkcs7-signature", "application/x-sh", "application/x-shar",
        "application/x-shockwave-flash", "application/x-stuffit", "application/x-sv4cpio", "application/x-sv4crc", "application/x-tar",
        "application/x-tcl", "application/x-tex", "application/x-texinfo", "application/x-troff", "application/x-troff-man",
        "application/x-troff-me", "application/x-troff-ms", "application/x-ustar", "application/x-wais-source", "application/x-x509-ca-cert",
        "application/ynd.ms-pkipko", "application/zip", "audio/basic", "audio/basic", "audio/mid", "audio/mid", "audio/mpeg",
        "audio/x-aiff", "audio/x-mpegurl", "audio/x-pn-realaudio", "audio/x-wav	wav", "image/bmp", "image/cis-cod", "image/gif",
        "image/ief", "image/jpeg", "image/pipeg", "image/svg+xml", "image/tiff", "image/tiff", "image/x-cmu-raster", "image/x-cmx",
        "image/x-icon", "image/x-portable-anymap", "image/x-portable-bitmap", "image/x-portable-graymap", "image/x-portable-pixmap",
        "image/x-rgb", "image/x-xbitmap", "image/x-xpixmap", "image/x-xwindowdump", "message/rfc822", "text/css", "text/h323",
        "text/html", "text/iuls", "text/plain", "text/richtext", "text/scriptlet", "text/tab-separated-values", "text/webviewhtml",
        "text/x-component", "text/x-setext", "text/x-vcard", "video/mpeg", "video/quicktime", "video/x-la-asf", "video/x-ms-asf",
        "video/x-msvideo", "video/x-sgi-movie", "x-world/x-vrml", "",
    ]
    return random.choice(MimeType)

def HTMLTags():
    tags = [
        # https://developer.mozilla.org/en-US/docs/Web/HTML/Element
        "a","abbr","acronym","address","applet","area","article","aside","attachment","audio",
        "b","base","basefont","bdi","bdo","bgsound","big", "blink", "blockquote","body","br","button",
        "canvas","caption","center","cite","code","col","colgroup","command","content",
        "data","datalist","dd","del","details","dfn","dialog","dir","div","dl","dt",
        "element","em","embed",
        "fieldset","figcaption","figure","font","footer","form","frame","frameset",
        "h1","h2","h3","h4","h5","h6","head","header","hgroup","hr","html",
        "i","iframe","image","img","input","ins","isindex","kbd","keygen",
        "label","layer","legend","li","link","listing",
        "main","map","mark","marquee","menu","menuitem","meta","meter","multicol",
        "nav","nobr","noembed","noframes","nolayer","noscript",
        "object","ol","optgroup","option","output",
        "p","param","picture","plaintext","pre","progress",
        "q","rb","rp","rt","rtc","ruby",
        "s","samp","script","section","select","shadow","slot","small","source","spacer","span","strike","strong","style","sub","summary","sup", "svg",
        "table","tbody","td","template","textarea","tfoot","th","thead","time","title","tr","track","tt",
        "u","ul","var","video","wbr","xmp",
    ]
    return random.choice(tags)

def Attributes():
    Attributes = [
        "abbr","accept_charset","accept","accesskey","action","align","alink","allowfullscreen","alt","archive",
        "aria-activedescendant","aria-atomic","aria-busy","aria-checked","aria-colcount","aria-colindex","aria-colspan",
        "aria-controls","aria-current","aria-describedby","aria-disabled","aria-dropeffect","aria-expanded","aria-flowto",
        "aria-grabbed","aria-haspopup","aria-help","aria-hidden","aria-invalid","aria-label","aria-labeledby","aria-labelledby",
        "aria-level","aria-live","aria-modal","aria-multiline","aria-multiselectable","aria-orientation","aria-owns",
        "aria-placeholder","aria-posinset","aria-pressed","aria-readonly","aria-relevant","aria-required","aria-roledescription",
        "aria-rowcount","aria-rowindex","aria-rowspan","aria-selected","aria-setsize","aria-sort","aria-valuemax",
        "aria-valuemin","aria-valuenow","aria-valuetext","async","autocomplete","autofocus","autoplay","autosave","axis",
        "background","behavior","bgcolor","bgproperties","border","bordercolor",
        "capture","cellpadding","cellspacing","char","challenge","charoff","charset","checked","cellborder","cite",
        "class","classid","clear","code","codebase","codetype","color","cols","colspan","compact","composite",
        "content","contenteditable","controls","coords","crossorigin",
        "data","datetime","declare","default","defer","dir","direction","dirname","disabled","disposition","download",
        "draggable","webkitdropzone","enctype","end","event","expanded",
        "face","focused","for","form","formaction","formenctype","formmethod","formnovalidate","formtarget","frame","frameborder",
        "headers","height","hidden","high","href","hreflang","hspace","http_equiv",
        "id","incremental","indeterminate","is","ismap","itemid","itemprop","itemref","itemscope","itemtype",
        "keytype","kind",
        "label","lang","language","leftmargin","link","list","longdesc","loop","low","playcount","loopend","loopstart","lowsrc",
        "manifest","marginheight","marginwidth","max","maxlength","mayscript","media","mediagroup","method","min","multiple","muted",
        "name","nohref","nonce","noresize","noshade","novalidate","nowrap",
        "object","onabort","onanimationstart","onanimationiteration","onanimationend","onautocomplete","onautocompleteerror",
        "onbeforecopy","onbeforecut","onbeforeload","onbeforepaste","onbeforeunload","onblur","oncanplay","oncanplaythrough",
        "onchange","onclick","oncontextmenu","oncopy","oncut","ondblclick","ondrag","ondragend","ondragenter","ondragleave",
        "ondragover","ondragstart","ondrop","ondurationchange","onemptied","onended","onerror","onfocus","onfocusin",
        "onfocusout","onhashchange","oninput","oninvalid","onkeydown","onkeypress","onkeyup","ongesturestart",
        "ongesturechange","ongestureend","onload","onloadeddata","onloadedmetadata","onloadstart","onmessage",
        "onmousedown","onmouseenter","onmouseleave","onmousemove","onmouseout","onmouseover","onmouseup",
        "onmousewheel","ononline","onoffline","onorientationchange","onpagehide","onpageshow","onpaste",
        "onpause","onplay","onplaying","onpopstate","onprogress","onratechange","onreset","onresize",
        "onscroll","onsearch","onseeked","onseeking","onselect","onselectstart","onselectionchange",
        "onwebkitspeechchange","onwheel","onstalled","onstorage","onsuspend","onsubmit","ontimeupdate",
        "ontouchstart","ontouchmove","ontouchend","ontouchcancel","ontransitionend","onunload","onvolumechange",
        "onwaiting","onwebkitanimationstart","onwebkitanimationiteration","onwebkitanimationend","onwebkitbeginfullscreen",
        "onwebkitendfullscreen","onwebkitfullscreenchange","onwebkitfullscreenerror","onwebkitkeyadded",
        "onwebkitkeyerror","onwebkitkeymessage","onwebkitmouseforcechanged","onwebkitmouseforcedown",
        "onwebkitmouseforceup","onwebkitmouseforcewillbegin","onwebkitneedkey","onwebkitsourceclose",
        "onwebkitsourceended","onwebkitsourceopen","onwebkittransitionend","onwebkitwillrevealbottom",
        "onwebkitwillrevealleft","onwebkitwillrevealright","onwebkitwillrevealtop","open","optimum",
        "pattern","placeholder","pluginspage","pluginurl","ping","poster","precision","preload","primary",
        "profile","progress","prompt","pseudo","readonly","rel","required","results","rev","reversed",
        "role","rows","rowspan","rules","sandbox","scheme","scope","scoped","scrollamount","scrolldelay",
        "scrolling","select","selected","shape","size","sizes","slot","sortable","sortdirection","span",
        "x-webkit-speech","x-webkit-grammar","spellcheck","src","srcset","srcdoc","srclang","standby",
        "start","step","style","subtitle","summary","tabindex","tableborder","target","text","title",
        "top","topmargin","translate","truespeed","type","uiactions","usemap","valign","value","valuetype",
        "version","vlink","vspace","webkitallowfullscreen","webkitattachmentpath","width","wrap","","autocorrect",
        "autocapitalize","onwebkitcurrentplaybacktargetiswirelesschanged","onwebkitplaybacktargetavailabilitychanged",
        "onwebkitpresentationmodechanged","x-webkit-imagemenu","webkit-playsinline","x-webkit-airplay",
        "x-webkit-wirelessvideoplaybackdisabled","x-itunes-inherit-uri-query-component",
    ]
    return random.choice(Attributes)

def Events():
    events = [
        'DOMAttrModified', 'DOMCharacterDataModified', 'DOMContentLoaded', 'DOMNodeInserted', 'DOMNodeInsertedIntoDocument', 'DOMNodeRemoved',
        'DOMNodeRemovedFromDocument', 'DOMSubtreeModified',
        'SVGAbort', 'SVGError', 'SVGLoad', 'SVGResize', 'SVGScroll', 'SVGUnload', 'SVGZoom',
        'abort', 'activate', 'active', 'addsourcebuffer', 'addstream', 'addtrack', 'afterprint', 'afterscriptexecute', 'animationend',
        'animationiteration', 'animationstart', 'antennaavailablechange', 'audioend', 'audioprocess', 'audiostart',
        'autocomplete', 'autocompleteerror',
        'beforecopy', 'beforecut', 'beforeinput', 'beforepaste', 'beforeprint', 'beforescriptexecute', 'beforeunload',
        'beginEvent', 'blocked', 'blur', 'boundary',
        'cached', 'cancel', 'canplay', 'canplaythrough', 'cardstatechange', 'change', 'chargingchange', 'chargingtimechange',
        'checking', 'click', 'close', 'compassneedscalibration', 'complete', 'compositionend', 'compositionstart',
        'compositionupdate', 'connect', 'connectioninfoupdate', 'contactchange', 'contextmenu', 'controllerchange',
        'copy', 'cuechange', 'currentchannelchanged', 'currentsourcechanged', 'cut',
        'data', 'dataavailable', 'datachannel', 'dblclick', 'deliveryerror', 'deliverysuccess',
        'devicechange', 'devicelight', 'devicemotion', 'deviceorientation', 'deviceproximity', 'disabled',
        'dischargingtimechange', 'downloading', 'drag', 'dragend', 'dragenter', 'dragexit', 'dragleave', 'dragover',
        'dragstart', 'drain', 'drop', 'durationchange',
        'eitbroadcasted', 'emptied', 'enabled', 'encrypted', 'end', 'endEvent', 'ended', 'enter', 'error', 'exit',
        'failed', 'fetch', 'finish', 'focus', 'focusin', 'focusout', 'frequencychange', 'fullscreenchange', 'fullscreenerror',
        'gamepadconnected', 'gamepaddisconnected', 'gotpointercapture', 'hashchange', 'headphoneschange',
        'icccardlockerror', 'icecandidate', 'iceconnectionstatechange', 'icegatheringstatechange', 'identiyresult', 'idpassertionerror',
        'idpvalidationerror', 'inactive', 'incoming', 'input', 'install', 'invalid', 'isolationchange',
        'keydown', 'keystatuschange', 'keyup',
        'languagechange', 'levelchange', 'load', 'loaded', 'loadeddata', 'loadedmetadata', 'loadend', 'loading', 'loadingdone',
        'loadingerror', 'loadstart', 'lostpointercapture',
        'mark', 'message', 'midimessage', 'mousedown', 'mouseenter', 'mouseleave', 'mousemove', 'mouseout', 'mouseover', 'mouseup',
        'mozbrowseractivitydone', 'mozbrowserasyncscroll', 'mozbrowseraudioplaybackchange', 'mozbrowsercaretstatechanged',
        'mozbrowserclose', 'mozbrowsercontextmenu', 'mozbrowserdocumentfirstpaint', 'mozbrowsererror',
        'mozbrowserfindchange', 'mozbrowserfirstpaint', 'mozbrowsericonchange', 'mozbrowserloadend', 'mozbrowserloadstart',
        'mozbrowserlocationchange', 'mozbrowsermanifestchange', 'mozbrowsermetachange', 'mozbrowseropensearch',
        'mozbrowseropentab', 'mozbrowseropenwindow', 'mozbrowserresize', 'mozbrowserscroll', 'mozbrowserscrollareachanged',
        'mozbrowserscrollviewchange', 'mozbrowsersecuritychange', 'mozbrowserselectionstatechanged', 'mozbrowsershowmodalprompt',
        'mozbrowsertitlechange', 'mozbrowserusernameandpasswordrequired', 'mozbrowservisibilitychange', 'mozinterruptbegin',
        'mozinterruptend', 'moztimechange', 'mute', 'muted',
        'negotiationneeded', 'nodecreate', 'nomatch', 'noupdate', 'obsolete', 'offline', 'online', 'open', 'overconstrained',
        'pagehide', 'pageshow', 'paste', 'pause', 'peeridentity', 'peerinfoupdate', 'play', 'playing', 'pointercancel',
        'pointerdown', 'pointerenter', 'pointerleave', 'pointerlockchange', 'pointerlockerror', 'pointermove', 'pointerout',
        'pointerover', 'pointerup', 'popstate', 'progress', 'push', 'pushsubscriptionchange',
        'ratechange', 'readystatechange', 'received', 'removesourcebuffer', 'removestream', 'removetrack', 'repeatEvent',
        'reset', 'resize', 'result', 'resume', 'retrieving',
        'scanningstatechanged', 'scroll', 'seeked', 'seeking', 'select', 'selectionchange', 'selectstart',
        'sending', 'sent', 'sessionavailable', 'sessionconnect', 'settingchange', 'show',
        'signalingstatechange', 'sort', 'soundend', 'soundstart', 'sourceclose', 'sourceended',
        'sourceopen', 'speakerforcedchange', 'speechend', 'speechstart', 'stalled', 'start', 'started',
        'statechange', 'statuschange', 'stop', 'storage', 'submit', 'success', 'suspend',
        'timeout', 'timeupdate', 'toggle', 'tonechange', 'touchcancel', 'touchend', 'touchmove', 'touchstart', 'transitionend',
        'unload', 'unmute', 'unmuted', 'update', 'updateend', 'updatefound', 'updateready', 'updatestart', 'upgradeneeded', 'userproximity',
        'versionchange', 'visibilitychange', 'volumechange',
        'waiting', 'waitingforkey', 'webglcontextcreationerror', 'webglcontextlost', 'webglcontextrestored', 'wheel',
    ]
    return random.choice(events)

def NiceValue():
    nice_value = [
        "'%s'" % DOMString(zint(256)), "0","1","5e6","-7e6","8e-6","2e100","7500000000","4400000000","-4400000000","-7500000000","0x80000000","0xFFFFFFFF", "NaN",
        "false", "true", "null","'pink'","'ltr'","'rtl'","'auto'","'copy'","'move'","'link'","'ab'","'bg'","'en'","'no'","'open'","'controls'",
        "'\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141'",
    ]
    return random.choice(nice_value)

# TODO:必须提前创建Element、Funs和EvtObj

# 包括TextNode
# pElement = document.createElement("p")
# textNode = document.createTextNode(text)
MAX_ELEMENTS_NUM = 10
def Element():
    types = random.choice([
        '.firstChild','.firstChild.nextSibling','.lastChild','.lastChild.previousSibling',
        '.firstChild.parentNode','.lastChild.parentNode',''
    ])
    elements = random.choice(["Element%s" % zint(MAX_ELEMENTS_NUM), "document.all[%s%%docuemnt.all.length]" % zint(100)])
    return "%s%s" % (elements, types)

MAX_FUNS_NUM = 5
def Funcs():
    return "Func%s" % zint(MAX_FUNS_NUM)

# var evt = new MouseEvent
MAX_EvtObj_NUM = 5
def EvtObj():
    return "Event%s" % zint(MAX_EvtObj_NUM)


def fonts():
    fonts = [
        'Andale Mono', 'AndaleMono', 'AppleGothic', 'Arial', 'Arial Black', 'Arial Bold', 'Arial Narrow', 'Arial Rounded MT Bold',
        'Avant Garde', 'Avantgarde', 'Baskerville', 'Baskerville Old Face', 'Big Caslon', 'Bitstream Charter',
        'Bitstream Vera Sans Bold', 'Bitstream Vera Sans Mono', 'Bodoni MT', 'Book Antiqua', 'Book Antiqua', 'Book Antiqua',
        'Bookman', 'Bookman Old Style', 'Brush Script MT', 'Calibri', 'Calisto MT', 'Cambria', 'Candara', 'Century Gothic',
        'CenturyGothic', 'Charcoal', 'Consolas', 'Copperplate', 'Copperplate Gothic Light', 'Courier', 'Courier Bold',
        'Dejavu Sans', 'Didot', 'Didot LT STD', 'Didot LT STD', 'Franklin Gothic', 'Franklin Gothic Bold', 'Franklin Gothic Medium',
        'Frutiger', 'Frutiger Linotype', 'Futura', 'Gadget', 'Garamond', 'Geneva', 'Georgia', 'Gill Sans', 'Gill Sans MT',
        'Goudy Old Style', 'Haettenschweiler', 'Helvetica', 'Helvetica Inserat', 'Helvetica Neue', 'Helvetica Neue',
        'Helvetica Rounded', 'Hoefler Text', 'Hoefler Text', 'Hoefler Text', 'Hoefler Text', 'ITC Franklin Gothic',
        'Impact', 'Lucida Bright', 'Lucida Console', 'Lucida Grande', 'Lucida Sans', 'Lucida Sans Typewriter',
        'Lucida Sans Unicode', 'Lucida Typewriter', 'Monaco', 'Optima', 'Palatino', 'Palatino', 'Palatino LT STD',
        'Palatino LT STD', 'Palatino Linotype', 'Palatino Linotype', 'Palatino Linotype', 'Papyrus', 'Perpetua',
        'Rockwell', 'Rockwell Bold', 'Rockwell Extra Bold', 'Segoe', 'Segoe UI', 'Tahoma', 'Times', 'Times New Roman',
        'TimesNewRoman', 'Trebuchet MS', 'Trebuchet MS', 'Verdana', 'monaco'
    ]
    return sample2(fonts, ",")

def color():
    # TODO:完善取值范围
    # color_name	规定颜色值为颜色名称的文本颜色（比如 "red"）。
    # hex_number	规定颜色值为十六进制值的文本颜色（比如 "#ff0000"）。
    # rgb_number	规定颜色值为 rgb 代码的文本颜色（比如 "rgb(255,0,0)"）
    hex_number = "#" + shex(6)
    rgb_number = "rgb(%s,%s,%s)" % (zint(255), zint(255), zint(255))
    return random.choice([hex_number, rgb_number])

def selector():
    return random.choice([HTMLTags(), Element(), ".%s" % Attributes(), "*"])

