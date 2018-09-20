#! /user/bin/python
# coding:UTF-8

import random

HTMLTags = [
    "CANVAS",  "ARTICLE",  "ASISE",  "B",  "BDI",  "BDO",  "BLOCKQUOTE",  "BR",  "BUTTON",  "CANVAS",  "CAPTION",  "CITE",  "COL",  "CODE",
    "COMMAND",  "DATALIST",  "DD",  "DEL",  "DETAILS",  "DFN",  "DL",  "DT",  "EM",  "STYLE",  "FIELDSET",  "FIGCAPTION",  "SCRIPT",  "EMBED",
    "FIGURE",  "FOOTER",  "HEADER",  "HGROUP",  "HR",  "I",  "INPUT",  "INS",  "KEYGEN",  "KBD",  "LEGEND",  "MARK",  "MENU",  "METER",  "NAV",
    "NOSCRIPT",  "OPTGROUP",  "OUTPUT",  "P",  "PARAM",  "PRE",  "PROGRESS",  "Q",  "RP",  "RT",  "RUBY",  "S",  "SAMP",  "SECTION",  "SELECT",
    "SMALL",  "SOURCE",  "SPAN",  "SUP",  "TH",  "THEAD",  "TIME",  "OBJECT",  "IFRAME",  "TEXTAREA",  "TRACK",  "U",  "VAR",  "WBR",  "FORM",
    "A",  "BODY",  "HTML",  "DIV",  "TABLE",  "AREA",  "TD",  "TR",  "LINK",  "BASE",  "FONT",  "HEAD",  "IMG",  "MAP",  "META",  "OL",  "LI",
    "TBODY",  "TITLE",  "H1",  "BLINK", "AREA",  "COL",  "SPAN",  "FRAMESET",  "FRAME",  "UL",  "OPTION",  "NOFRAMES",  "TFOOT",  "XMP",
    "ISINDEX",  "CENTER",  "HR",  "LABEL",  "OPTGROUP",  "AUDIO",  "VIDEO",  "SVG",
]

Events = [
    'DOMActivate','DOMCharacterDataModified','DOMNodeInserted','DOMNodeInsertedIntoDocument','DOMNodeRemoved','DOMNodeRemovedFromDocument',
    'DOMSubtreeModified','change','CheckboxStateChange','copy','cut','focus','input','load','paste',
    'select','selectionchange','textInput','unload',
]

HTMLAttributes = [
    "abbr","accept_charset","accept","accesskey","action","align","alink","allowfullscreen","alt","archive",
    "async","autocomplete","autofocus","autoplay","autosave","axis",
    "background","behavior","bgcolor","bgproperties","border","bordercolor",
    "capture","cellpadding","cellspacing","char","challenge","charoff","charset","checked","cellborder","cite",
    "class","classid","clear","code","codebase","codetype","color","cols","colspan","compact","composite",
    "content","contenteditable","controls","coords","crossorigin",
    "data","datetime","declare","default","defer","dir","direction","dirname","disabled","disposition","download",
    "draggable","webkitdropzone","enctype","end","event","expanded",
    "face","focused","for","form","formaction","formenctype","formmethod","formnovalidate","formtarget","frame","frameborder",
    "headers","height","hidden","high","href","hreflang","hspace","http_equiv",
    "id","incremental","indeterminate","is","ismap","itemid","itemprop","itemref","itemscope","itemtype","keytype","kind",
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
    "onwaiting","open","optimum", "pattern","placeholder","pluginspage","pluginurl","ping","poster","precision","preload","primary",
    "profile","progress","prompt","pseudo","readonly","rel","required","results","rev","reversed",
    "role","rows","rowspan","rules","sandbox","scheme","scope","scoped","scrollamount","scrolldelay",
    "scrolling","select","selected","shape","size","sizes","slot","sortable","sortdirection","span",
    "x-webkit-speech","x-webkit-grammar","spellcheck","src","srcset","srcdoc","srclang","standby",
    "start","step","style","subtitle","summary","tabindex","tableborder","target","text","title",
    "top","topmargin","translate","truespeed","type","uiactions","usemap","valign","value","valuetype",
    "version","vlink","vspace","webkitallowfullscreen","webkitattachmentpath","width","wrap","","autocorrect","autocapitalize",
]

NICE_VALUES = [
    "0","1","5e6","-7e6","8e-6","2e100","7500000000","4400000000","-4400000000","-7500000000","0x80000000","0xFFFFFFFF", "NaN",
    "false", "true", "null","'pink'","'ltr'","'rtl'","'auto'","'copy'","'move'","'link'","'ab'","'bg'","'en'","'no'","'open'","'controls'",
    "'\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141\\u4141'",
]

Commands=[
    'delete','insertButton','insertFieldset','insertHorizontalRule','insertIFrame','insertInputButton',
    'insertInputCheckbox','insertInputFileUpload','insertInputHidden','insertInputImage',
    'insertInputPassword','insertInputRadio','insertInputReset','insertInputSubmit','insertInputText',
    'insertMarquee','insertOrderedList','insertSelectDropdown','insertSelectListbox','insertTextArea',
    'insertUnorderedList'
]

OBJ_BLACKLIST = [
  'nodeName', 'nodeValue', 'nodeType', 'childNodes', 'location', 'name',  'opener', 'URL', 'onbeforeunload',
    'onunload','innerHTML', 'outerHTML', 'innerText', 'textContent', 'Components', 'controllers', 'lastChild',
    'previousSibling', 'previousElementSibling', 'parentNode', 'parentTextEdit', 'parentElement', 'ownerDocument',
    'document', 'cloneNode', 'open', 'close', 'print',
]

class Template():

    def __init__(self):
        self.MAX_ELEMS = 5
        self.MAX_LISTENERS = 3
        self.MAX_FUNC_NUMS = 2

        self.initTags = 3
        self.elements = []
        self.event_list = []

    def randb(self):
        return random.choice(["true", "false"])

    def new_elem(self):
        return "Element%s" % len(self.elements)

    def last_elem(self):
        return self.elements[-1]

    def rand_doc(self):
        i = random.randint(0, len(self.elements)+self.initTags)
        # 针对document.all.length取余数可以保证取值的合法性
        return "document.all[%s]" % str(i)

    def rand_func(self):
        return "Func%s" % random.randint(0, self.MAX_FUNC_NUMS-1)

    def try_catch(self, codes):
        ret_codes = ""
        for code in codes:
            ret_codes += ("try{%s}catch(e){}\n" % code)
        return ret_codes

    def create_element(self, tag):
        codes = []
        name = self.new_elem()
        fname = self.rand_doc()
        codes.append("%s=document.createElement('%s');" % (name, tag))
        codes.append("%s.id='%s';" % (name, name))
        codes.append("%s.appendChild(%s);" % (fname, name))
        self.elements.append(name)
        return codes

    def add_event_listener(self, element, func=None):
        codes = []
        event = random.choice(Events)
        if func is None:
            func = self.rand_func()
        self.event_list.append([func, event, ])
        codes.append("%s.addEventListener('%s', %s, %s);" % (element, event, func, self.randb()))
        return codes

    def remove_event_listener(self, element, func):
        codes = []
        for ig in self.event_list:
            if ig[0] == func:
                codes.append("%s.removeEventListener('%s', %s, %s);" % (element, ig[1], func, self.randb()))
        return codes

    def tweak_attributes(self, element):
        codes = []
        attr_list = random.sample(HTMLAttributes, 20)
        for attr in attr_list:
            codes.append("%s.setAttribute('%s',%s);" % (element, attr, random.choice(NICE_VALUES)))
        return codes

    def create_element_range(self, name):
        codes = []
        codes.append("%s = document.createRange();" % name)
        codes.append("%s.setStart(%s,0);" % (name, self.rand_doc()))
        codes.append("%s.setEnd(%s,0);" %(name,  self.rand_doc()))
        return codes

    def delete_element_range(self, name):
        codes = []
        codes.append("%s.deleteContents();" % name)
        return codes

    def create_node_iterator(self):
        codes = []
        nf = [
            "NodeFilter.SHOW_ALL", "NodeFilter.SHOW_ELEMENT", "SHOW_ATTRIBUTE", "NodeFilter.SHOW_TEXT", "NodeFilter.SHOW_CDATA_SECTION",
            "NodeFilter.SHOW_ENTITY_REFERENCE","NodeFilter.SHOW_ENTITY", "NodeFilter.SHOW_PROCESSING_INSTRUCTION",
            "NodeFilter.SHOW_COMMENT", "NodeFilter.SHOW_DOCUMENT", "NodeFilter.SHOW_DOCUMENT_TYPE", "NodeFilter.SHOW_DOCUMENT_FRAGMENT",
            "NodeFilter.SHOW_NOTATION",
        ]
        codes += self.create_element_range("range1")
        codes += self.delete_element_range("range1")
        nf2 = [
            "NodeFilter.FILTER_ACCEPT", "NodeFilter.FILTER_SKIP",
        ]
        root = self.rand_doc()
        whatToShow = random.choice(nf)
        filter = random.choice(nf2)
        codes.append("ni = document.createNodeIterator(%s,%s,%s,%s);" % (root, whatToShow, filter, self.randb()))
        return codes

    def create_tree_walker(self):
        codes = []
        nf = [
            "NodeFilter.SHOW_ALL", "NodeFilter.SHOW_ELEMENT", "SHOW_ATTRIBUTE", "NodeFilter.SHOW_TEXT", "NodeFilter.SHOW_CDATA_SECTION",
            "NodeFilter.SHOW_ENTITY_REFERENCE","NodeFilter.SHOW_ENTITY", "NodeFilter.SHOW_PROCESSING_INSTRUCTION",
            "NodeFilter.SHOW_COMMENT", "NodeFilter.SHOW_DOCUMENT", "NodeFilter.SHOW_DOCUMENT_TYPE", "NodeFilter.SHOW_DOCUMENT_FRAGMENT",
            "NodeFilter.SHOW_NOTATION",
        ]
        codes += self.create_element_range("range1")
        codes += self.delete_element_range("range1")
        nf2 = [
            "NodeFilter.FILTER_ACCEPT", "NodeFilter.FILTER_SKIP",
        ]
        root = self.rand_doc()
        whatToShow = random.choice(nf)
        filter = random.choice(nf2)
        codes.append("tw = document.createTreeWalker(%s,%s,%s,%s);" % (root, whatToShow, filter, self.randb()))
        return codes

    def create_tag_aggregation(self):
        codes = []
        elem = random.choice(self.elements)
        codes.append("tagAggregation = document.getElementsByTagName(%s.tagName);" % elem)
        return codes

    def create_text_range(self, name):
        codes = []
        codes.append("%s = document.createTextRange();" % name)
        codes.append("%s.moveToElementText(%s);" % (name, self.rand_doc()))
        cls = random.choice(["character", "Unit"])
        shift = random.randint(0,20)
        codes.append("%s.moveEnd(%s,%s)" % (name, cls, shift ))
        return codes

    def alter_text_range(self, name):
        codes = []
        codes.append("%s.select();" % name)
        codes.append("%s.execCommand('%s',true,null);" % (name, random.choice(Commands)))
        return codes

    def alter_range(self, name):
        codes = []
        cmd = random.randint(0, 26)
        if cmd == 0:
            codes.append("%s.cloneContents();" % name)
        elif cmd == 1:
            codes.append("%s.cloneRange();" % name)
        elif cmd == 2:
            codes.append("%s.collapse(%s);" % (name, self.randb()))
        elif cmd == 3:
            how = random.choice(["Range.END_TO_END", "Range.END_TO_START", "Range.START_TO_END", "Range.START_TO_START",])
            sourceRange = "document.createRange()"
            codes.append("%s.compareBoundaryPoints(%s,%s);" % (name, how, sourceRange))
        elif cmd == 4:
            codes.append("%s.compareNode(%s);" % (name, self.rand_doc()))
        elif cmd == 5:
            codes.append("%s.comparePoint(%s, 1);" % (name, self.rand_doc()))
        elif cmd == 6:
            tagString = "<div>I am a div node</div>"
            codes.append("%s.createContextualFragment('%s');" % (name, tagString))
        elif cmd == 7:
            codes.append("range.deleteContents();")
        elif cmd == 8:
            codes.append("range.detach();")
        elif cmd == 9:
            codes.append("range.extractContents();")
        elif cmd == 10:
            codes.append("range.getBoundingClientRect();")
        elif cmd == 11:
            codes.append("range.getClientRects();")
        elif cmd == 12:
            codes.append("newNode = document.createElement('%s');" % random.choice(HTMLTags))
            codes.append("newNode.appendChild(document.createTextNode('New Node Inserted Here'));")
            codes.append("range.insertNode();")
        elif cmd == 13:
            codes.append("var bool = range.intersectsNode(%s);" % self.rand_doc())
        elif cmd == 14:
            codes.append("bool = range.isPointInRange(%s, 1);" % self.rand_doc())
        elif cmd == 15:
            codes.append("range.selectNode(%s);" % self.rand_doc())
        elif cmd == 16:
            codes.append("range.selectNodeContents(%s);" % self.rand_doc())
        elif cmd == 17:
            codes.append("range.setEnd(%s,0);" % self.rand_doc())
        elif cmd == 18:
            codes.append("range.setEndAfter(%s);" % self.rand_doc())
        elif cmd == 19:
            codes.append("range.setEndBefore(%s);" % self.rand_doc())
        elif cmd == 20:
            codes.append("range.setStart(%s,0);" % self.rand_doc())
        elif cmd == 21:
            codes.append("range.setStartAfter(%s);" % self.rand_doc())
        elif cmd == 22:
            codes.append("range.setStartBefore(%s);" % self.rand_doc())
        elif cmd == 23:
            codes.append("range.surroundContents(%s );" % self.rand_doc())
        elif cmd == 24:
            codes.append("range.setEndAfter(%s);" % self.rand_doc())
        elif cmd == 25:
            codes.append("range.setEndAfter(%s);" % self.rand_doc())
        else: #  cmd == 26
            codes.append("%s.toString();" % name)
        return codes

    def spray(self):
        codes = []
        codes.append("for(S='\\u4141',k=[],y=0;y++<65;)y<20?S+=S:k[y]=[S.substr(22)+'\\u4141\\u4141'].join('')")
        return codes

    def move_iterator(self):
        codes = []
        rmoves = random.randint(0,4)
        for i in range(rmoves):
            rm = random.randint(0,1)
            if rm == 0:
                codes.append("ni.nextNode();")
            if rm == 1:
                codes.append("ni.previousNode();")

        codes += self.fuzz_attributes(-1, "it")
        return codes

    def move_tree_walker(self):
        codes = []
        rMoves = random.randint(0, 4)
        for i in range(rMoves):
            rm = random.randint(0, 6)
            if rm == 0:
                codes.append("tw.nextNode();")
            if rm == 1:
                codes.append("tw.previousNode();")
            if rm == 2:
                codes.append("tw.previousSibling();")
            if rm == 3:
                codes.append("tw.nextSibling();")
            if rm == 4:
                codes.append("tw.firstChild();")
            if rm == 5:
                codes.append("tw.lastChild();")
            if rm == 6:
                codes.append("tw.parentNode();")

        codes += self.fuzz_attributes(-1, "tw")
        return codes

    def tag_crawler(self):
        codes = []
        # TODO:此处tc应该等于tagAggregation.length
        tc = random.randint(0, 10)
        for i in range(tc):
            codes += self.fuzz_attributes(i, "tag")
        return codes

    def tree_crawler(self):
        codes = []
        for index, elem in enumerate(self.elements):
            codes.append("%s.normalize();" % elem)
            codes += self.fuzz_attributes(index, "tree")
        return codes

    def insert_sub_tree(self):
        codes = []
        for i in range(self.MAX_ELEMS):
            tag = random.choice(HTMLTags)
            codes += self.create_element(tag)
        return codes

    def event_capturing_phase(self, func):
        codes = []
        codes += self.remove_event_listener("event.currentTarget", func)
        ry = random.randint(0, 3)
        if ry == 0:
            codes += self.create_element_range("range")
            codes += self.alter_range("range")
        if ry == 1:
            codes += self.create_text_range("range2")
            codes += self.alter_text_range("range2")
        if ry == 2:
            codes += self.create_element_range("range")
            codes += self.alter_range("range")
            codes += self.move_iterator()
        if ry == 3:
            codes += self.create_text_range("range2")
            codes += self.alter_text_range("range2")
            codes += self.move_tree_walker()
        ry == random.randint(0, 3)
        if ry == 0:
            codes += self.move_iterator()
        if ry == 1:
            codes += self.insert_sub_tree()
        if ry == 2:
            codes += self.tree_crawler()
        if ry == 3:
            codes += self.move_tree_walker()
        codes += self.spray()
        return codes

    def event_at_target(self):
        codes = []
        for j in range(self.MAX_LISTENERS):
            codes += self.add_event_listener("event.target")
        return codes

    def event_bubbling_phase(self, func):
        codes = []
        codes += self.remove_event_listener("event.currentTarget", func)
        ry = random.randint(0, 3)
        if ry == 0:
            codes += self.create_element_range("range")
            codes += self.alter_range("range")
        if ry == 1:
            codes += self.create_text_range("range2")
            codes += self.alter_text_range("range2")
        if ry == 2:
            codes += self.create_element_range("range")
            codes += self.alter_range("range")
            codes += self.create_text_range("range2")
            codes += self.alter_text_range("range2")
        if ry == 3:
            codes += self.create_text_range("range2")
            codes += self.alter_text_range("range2")
            codes += self.create_element_range("range")
            codes += self.alter_range("range")
        ry == random.randint(0, 3)
        if ry == 0:
            codes += self.move_iterator()
        if ry == 1:
            codes += self.insert_sub_tree()
        if ry == 2:
            codes += self.tree_crawler()
        if ry == 3:
            codes += self.move_tree_walker()

        for j in range(self.MAX_LISTENERS):
            codes += self.add_event_listener("event.target")
        return codes

    def modify_dom(self, func):
        ret = ""
        ret += "switch(event.eventPhase){\n"
        ret += "case Event.CAPTURING_PHASE:\n"
        ret += self.try_catch(self.event_capturing_phase(func))
        ret += "break;\n"
        ret += "case Event.AT_TARGET:\n"
        ret += self.try_catch(self.event_at_target())
        ret += "break;\n"
        ret += "case Event.BUBBLING_PHASE:\n"
        ret += self.try_catch(self.event_bubbling_phase(func))
        ret += "break;\n"
        ret += "}"
        return ret

    def fuzz_attributes(self, index, orig):
        codes = []
        for prop in OBJ_BLACKLIST:

            c = random.randint(0,5)
            if c == 0:
                if orig == "tree":
                    elem = self.elements[index]
                    codes.append("%s.%s=null;" % (elem, prop))
                    codes.append("document.%s.%s=null;" % (elem, prop))
                if orig == "tag":
                    codes.append("tagAggregation[%s].%s=null;" % (str(index), prop))
                if orig == "it":
                    # TODO:CurrentNode和CurrentLeaf在nduja逻辑中还没体现，可以改进
                    codes.append("currentNode.%s=null;" % prop)
                if orig == "tw":
                    codes.append("currentLeaf.%s=null;" % prop)
            if c == 1:
                if orig == "tree":
                    elem = self.elements[index]
                    codes.append("%s.%s();" % (elem, prop))
                    codes.append("document.%s.%s();" % (elem, prop))
                if orig == "tag":
                    codes.append("tagAggregation[%s].%s();" % (str(index), prop))
                if orig == "it":
                    codes.append("currentNode.%s();" % prop)
                if orig == "tw":
                    codes.append("currentLeaf.%s();" % prop)
            if c == 2:
                if orig == "tree":
                    elem = self.elements[index]
                    codes.append("%s.%s(%s.parentNode);" % (elem, prop, elem))
                    codes.append("document.%s.%s(document.%s.parentNode);" % (elem, prop, elem ))
                if orig == "tag":
                    codes.append("tagAggregation[%s].%s(tagAggregation[%s].parentNode);" % (str(index), prop, str(index)))
                if orig == "it":
                    codes.append("currentNode.%s(currentNode.parentNode);" % prop)
                if orig == "tw":
                    codes.append("currentLeaf.%s(currentLeaf.parentNode);" % prop)
            if c == 3:
                if orig == "tree":
                    elem = self.elements[index]
                    codes.append("%s.%s=%s.parentNode.%s;" % (elem, prop, elem, prop))
                    codes.append("document.%s.%s=document.%s.parentNode.%s;" % (elem, prop, elem, prop ))
                if orig == "tag":
                    codes.append("tagAggregation[%s].%s=tagAggregation[%s].parentNode.%s;" % (str(index), prop, str(index), prop))
                if orig == "it":
                    codes.append("currentNode.%s=currentNode.parentNode.%s;" % (prop, prop))
                if orig == "tw":
                    codes.append("currentLeaf.%s=currentLeaf.parentNode.%s;" % (prop, prop))
            if c == 4:
                rv = random.choice(NICE_VALUES)
                if orig == "tree":
                    elem = self.elements[index]
                    codes.append("%s.%s=%s;" % (elem, prop, rv))
                    codes.append("document.%s.%s=%s;" % (elem, prop, rv ))
                if orig == "tag":
                    codes.append("tagAggregation[%s].%s=%s;" % (str(index), prop, rv))
                if orig == "it":
                    codes.append("currentNode.%s=%s;" % (prop, rv))
                if orig == "tw":
                    codes.append("currentLeaf.%s=%s;" % (prop, rv))
            if c == 5:
                rv = random.choice(NICE_VALUES)
                if orig == "tree":
                    elem = self.elements[index]
                    codes.append("%s.%s(%s);" % (elem, prop, rv))
                    codes.append("document.%s.%s(%s);" % (elem, prop, rv))
                if orig == "tag":
                    codes.append("tagAggregation[%s].%s(%s);" % (str(index), prop, rv))
                if orig == "it":
                    codes.append("currentNode.%s(%s);" % (prop, rv))
                if orig == "tw":
                    codes.append("currentLeaf.%s(%s);" % (prop, rv))
        return codes

    def fuzz_nduja(self):

        codes = []

        # 1. build element treee for nduja
        for i in range(self.MAX_ELEMS):
            # create element and append child
            tag = random.choice(HTMLTags)
            codes += self.create_element(tag)
            # add event listener
            for j in range(self.MAX_LISTENERS):
                codes += self.add_event_listener(self.elements[-1])
            # tweak attributes
            codes += self.tweak_attributes(self.elements[-1])

        # 2. Boom
        codes += self.create_node_iterator()
        codes += self.create_tree_walker()
        codes += self.create_tag_aggregation()
        codes += self.create_element_range("range")
        codes += self.create_text_range("range2")
        codes += self.alter_range("range")
        codes += self.spray()
        codes += self.move_iterator()
        codes += self.move_tree_walker()
        codes += self.tag_crawler()

        codes.append("window.location.reload(true);")

        sentences_str = self.try_catch(codes)

        # generate functions
        funcs_str = ""
        for fi in range(self.MAX_FUNC_NUMS):
            temp = self.modify_dom(fi)
            funcs_str += "function %s(){\r\n%s\r\n}\r\n" % ("Func%s"%fi, temp)

        return funcs_str + sentences_str

    def gen_tags(self, tag, content=""):
        return "<" + tag + ">\n" + content +"</" + tag + ">\n"

    def generate(self):
        script = self.fuzz_nduja()
        script = self.gen_tags("script", script)
        title = "<title>Nduja Fuzzer</title>\n"
        head = self.gen_tags("head", title)
        body = self.gen_tags("body", script)
        html = self.gen_tags("html", head+body)
        return html