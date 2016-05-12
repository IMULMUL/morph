#! /user/bin/python
# coding:UTF-8

import modules.webidl.randoms as randoms
from modules.webidl.HTMLAnchorElement import HTMLAnchorElement
from modules.webidl.HTMLAreaElement import HTMLAreaElement
from modules.webidl.HTMLAudioElement import HTMLAudioElement
from modules.webidl.HTMLBodyElement import HTMLBodyElement
from modules.webidl.HTMLButtonElement import HTMLButtonElement
from modules.webidl.HTMLBaseElement import HTMLBaseElement
from modules.webidl.HTMLBaseFontElement import HTMLBaseFontElement
from modules.webidl.HTMLBRElement import HTMLBRElement
from modules.webidl.HTMLCanvasElement import HTMLCanvasElement
from modules.webidl.HTMLContentElement import HTMLContentElement

from modules.webidl.HTMLDataElement import HTMLDataElement
from modules.webidl.HTMLDataListElement import HTMLDataListElement
from modules.webidl.HTMLDialogElement import HTMLDialogElement
from modules.webidl.HTMLDivElement import HTMLDivElement
from modules.webidl.HTMLDListElement import HTMLDListElement
from modules.webidl.HTMLEmbedElement import HTMLEmbedElement


class WebAPIFuzz():

    def __init__(self):

        self.relation = {
            "a": [HTMLAnchorElement, ],
            "area": [HTMLAreaElement, ],
            "audio": [HTMLAudioElement, ],
            "base": [HTMLBaseElement, ],
            "basefont": [HTMLBaseFontElement, ] ,
            "body": [HTMLBodyElement, ],
            "br": [HTMLBRElement,],
            "button": [HTMLButtonElement, ],
            "canvas": [HTMLCanvasElement,],
            "content": [HTMLContentElement, ],
            "data": [HTMLDataElement],
            "datalist": [HTMLDataListElement],
            "dialog": [HTMLDialogElement],
            "div": [HTMLDivElement],
            "dlist": [HTMLDListElement],
            "embed": [HTMLEmbedElement],
        }
        self.elements = []
        self.codes = []
        self.MAX_ELEMS = 5
        self.ret = ""

    def new_elem(self):
        return "Element%s" % len(self.elements)

    def create_element(self, tag):
        codes = []
        name = self.new_elem()
        codes.append("%s=document.createElement('%s');" % (name, tag))
        codes.append("%s.id='%s';" % (name, name))
        codes.append("%s.appendChild(%s);" % ("document.body", name))
        self.elements.append([name, tag])
        return codes

    def try_catch(self, codes):
        ret_codes = ""
        for code in codes:
            ret_codes += ("try{%s}catch(e){}\n" % code)
        return ret_codes

    def fuzz(self):

        codes = []
        for i in range(randoms.MAX_ELEMENTS_NUM):
            tag_list = list(self.relation.keys())
            tag = randoms.choice(tag_list)
            name = self.new_elem()
            codes += self.create_element(tag)

        elem = randoms.choice(self.elements)
        name = elem[0]
        tag = elem[1]

        cls = randoms.choice(self.relation[tag])
        property_methods = dir(cls)

        properties = [func for func in property_methods if "p_" == func[0:2]]
        cur_props = randoms.sample(properties, 10)
        for prop in properties:
            prop_name = prop[2:]
            func = getattr(cls(), prop)
            ret = func()
            code = ""
            if isinstance(ret, int) is True:
                code = "%s.%s=%s;" % (name, prop_name, ret)
            if isinstance(ret, str) is True:
                code = "%s.%s=\"%s\";" % (name, prop_name, ret)
            if ret is None:
                code = "document.write(%s.%s);" % (name, prop_name)
            codes.append(code)

        methods = [func for func in property_methods if "m_" == func[0:2]]
        cur_mtds = randoms.sample(methods, 10)
        for method in methods:
            method_name = method[2:]
            func = getattr(cls(), method)
            ret = func()
            if ret is None:
                code = "%s.%s();" % (name, method_name)
            else:
                code = "%s.%s(%s);" % (name, method_name, ret)
            codes.append(code)

        cccccccccc = self.try_catch(codes)

        funcs = ""
        for j in range(randoms.MAX_FUNS_NUM):
            funcs += "function %s(){\r\n%s\r\n}\r\n" % ("Func%s"%j, cccccccccc)

        codes.append("window.location.reload(true);")


        return funcs + self.try_catch(codes)

    def gen_tags(self, tag, content=""):
        return "<" + tag + ">\n" + content +"</" + tag + ">\n"

    def generate(self):
        script = self.fuzz()
        script = self.gen_tags("script", script)
        title = "<title>WebAPIs Fuzzer</title>\n"
        head = self.gen_tags("head", title)
        body = self.gen_tags("body", script)
        ret = self.gen_tags("html", head+body)
        return ret

def gen():
    page = WebAPIFuzz()
    return page.generate()