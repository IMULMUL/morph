#! /user/bin/python
# coding:UTF-8

import random as r
import modules.variable as g

class JSTemplater():

    def __init__(self):
        self.elements = []
        self.funcs = []
        self.initTags = 3
        self.event_list = []

    # adjust
    def trys(self, case):
        return "try{%s}catch(e){}\n" % case

    def gen_tags(self, tag, content=""):
        return "<" + tag + ">\n" + content +"</" + tag + ">\n"

    # Random
    def randb(self):
        return r.choice(["true", "false"])

    def randElem(self):
        return r.choice(self.elements)

    def randFunc(self):
        return r.choice(self.funcs)

    def randDoc(self):
        i = r.randint(0, len(self.elements)+self.initTags)
        # 针对document.all.length取余数可以保证取值的合法性
        return "document.all[%s]" % str(i)
        #return "document.all[%s%%document.all.length]" % str(i)

    def newElem(self):
        return "Element%s" % len(self.elements)

    def lastElem(self):
        return "Element%s" % (len(self.elements) - 1)

    def randTag(self):
        return r.choice(g.HTMLTags)

    def randEvent(self):
        return r.choice(g.EVENTS)

    def randAttrs(self):
        return r.choice(g.HTMLAttributes)

    def randInteresting(self):
        return r.choice(g.NICE_VALUES)

    def randStyle(self):
        return r.choice(g.STYLES)

    def randElemById(self):
        return "document.getElementById('%s')" % self.randElem()

    # cases
    def window_reload(self):
        return self.trys("window.location.reload(true);")

    def create_element_append_child(self):
        ret = ""
        ret += self.trys("%s = document.createElement('%s');" % (self.newElem(), self.randTag()))
        ret += self.trys("%s.id = '%s';" % (self.newElem(), self.newElem()))
        ret += self.trys("%s.appendChild(%s);" % (self.randDoc(),  self.newElem()))
        self.elements.append(self.newElem())
        return ret

    def add_event_listener(self, element, func=None):
        event = self.randEvent()
        if func is None:
            func = self.randFunc()
        self.event_list.append([func, event, ])
        return self.trys("%s.addEventListener('%s', %s, %s);" % (element, event, func, self.randb()))

    def remove_event_listener(self, element, func):
        ret = ""
        for ig in self.event_list:
            if ig[0] == func:
                ret += self.trys("%s.removeEventListener('%s', %s, %s);" % (element, ig[1], func, self.randb()))
        return ret

    def create_element_range(self, name):
        ret = ""
        ret += self.trys("%s = document.createRange();" % name)
        ret += self.trys("%s.setStart(%s,0);" % (name, self.randDoc()))
        ret += self.trys("%s.setEnd(%s,0);" %(name,  self.randDoc()))
        return ret

    def delete_element_range(self, name):
        ret = ""
        ret += self.trys("%s.deleteContents();" % name)
        return ret

    def alter_element_range(self):
        ret = ""
        cmd = r.randint(0, 26)
        if cmd == 0:
            ret += self.trys("range.cloneContents();")
        if cmd == 1:
            ret += self.trys("range.cloneRange();")
        if cmd == 2:
            ret += self.trys("range.collapse(%s);" % self.randb())
        if cmd == 3:
            how = r.choice(["Range.END_TO_END", "Range.END_TO_START", "Range.START_TO_END", "Range.START_TO_START",])
            sourceRange = "document.createRange()"
            ret += self.trys("range.compareBoundaryPoints(%s,%s);" % (how, sourceRange))
        if cmd == 4:
            ret += self.trys("range.compareNode(%s);" % self.randDoc())
        if cmd == 5:
            ret += self.trys("range.comparePoint(%s, 1);" % self.randDoc())
        if cmd == 6:
            tagString = "<div>I am a div node</div>"
            ret += self.trys("range.createContextualFragment('%s');" % tagString)
        if cmd == 7:
            ret += self.trys("range.deleteContents();")
        if cmd == 8:
            ret += self.trys("range.detach();")
        if cmd == 9:
            ret += self.trys("range.extractContents();")
        if cmd == 10:
            ret += self.trys("range.getBoundingClientRect();")
        if cmd == 11:
            ret += self.trys("range.getClientRects();")
        if cmd == 12:
            ret += self.trys("newNode = document.createElement('%s');" % r.choice(g.HTMLTags))
            ret += self.trys("newNode.appendChild(document.createTextNode('New Node Inserted Here'));")
            ret += self.trys("range.insertNode();")
        if cmd == 13:
            ret += self.trys("var bool = range.intersectsNode(%s);" % self.randDoc())
        if cmd == 14:
            ret += self.trys("bool = range.isPointInRange(%s, 1);" % self.randDoc())
        if cmd == 15:
            ret += self.trys("range.selectNode(%s);" % self.randDoc())
        if cmd == 16:
            ret += self.trys("range.selectNodeContents(%s);" % self.randDoc())
        if cmd == 17:
            ret += self.trys("range.setEnd(%s,0);" % self.randDoc())
        if cmd == 18:
            return self.trys("range.setEndAfter(%s);" % self.randDoc())
        if cmd == 19:
            ret += self.trys("range.setEndBefore(%s);" % self.randDoc())
        if cmd == 20:
            ret += self.trys("range.setStart(%s,0);" % self.randDoc())
        if cmd == 21:
            ret += self.trys("range.setStartAfter(%s);" % self.randDoc())
        if cmd == 22:
            ret += self.trys("range.setStartBefore(%s);" % self.randDoc())
        if cmd == 23:
            ret += self.trys("range.surroundContents(%s );" % self.randDoc())
        if cmd == 24:
            ret += self.trys("range.setEndAfter(%s);" % self.randDoc())
        if cmd == 25:
            ret += self.trys("range.setEndAfter(%s);" % self.randDoc())
        if cmd == 26:
            ret += self.trys("range.toString();")
        return ret

    def create_text_range(self):
        ret = ""
        ret += self.trys("range2 = document.createTextRange();")
        ret += self.trys("range2.moveToElementText(%s);" % self.randDoc())
        cls = r.choice(["character", "Unit"])
        ret += self.trys("range2.moveEnd(%s,%s)" % (cls, r.randint(0,20)))
        return ret

    def alter_text_range(self):
        ret = ""
        ret += self.trys("range2.select();")
        ret += self.trys("range2.execCommand('%s',true,null);" % r.choice(g.Commands))
        return ret

    def move_iterator(self):
        ret = ""
        rmoves = r.randint(0,4)
        for i in range(rmoves):
            rm = r.randint(0,1)
            if rm == 0:
                ret += self.trys("ni.nextNode();")
            if rm == 1:
                ret += self.trys("ni.previousNode();")

        ret += self.fuzz_attributes("it")
        return ret

    def move_tree_walker(self):
        ret = ""
        rMoves = r.randint(0,4)
        for i in range(rMoves):
            rm = r.randint(0, 6)
            if rm == 0:
                ret += self.trys("tw.nextNode();")
            if rm == 1:
                ret += self.trys("tw.previousNode();")
            if rm == 2:
                ret += self.trys("tw.previousSibling();")
            if rm == 3:
                ret += self.trys("tw.nextSibling();")
            if rm == 4:
                ret += self.trys("tw.firstChild();")
            if rm == 5:
                ret += self.trys("tw.lastChild();")
            if rm == 6:
                ret += self.trys("tw.parentNode();")

        ret += self.fuzz_attributes("tw")
        return ret

    def insert_sub_tree(self):
        ret = ""
        for i in range(g.MAX_ELEM):
            ret += self.create_element_append_child()
        return ret

    def tree_crawler(self):
        ret = ""
        for elem in self.elements:
            ret += self.trys("%s.normalize();" % elem)
            ret += self.fuzz_attributes("tree")
        return ret

    def tag_crawler(self):
        ret = ""
        tc = r.randint(0, 5)
        for i in range(tc):
            ret += self.fuzz_attributes("tree")
        return ret

    def spray(self):
        ret = ""
        ret += self.trys("for(S='\\u4141',k=[],y=0;y++<65;)y<20?S+=S:k[y]=[S.substr(22)+'\\u4141\\u4141'].join('')")
        return ret

    def modify_dom_func(self, funcName):

        ret = ""
        ret += "switch(event.eventPhase){\n"
        ret += "case Event.CAPTURING_PHASE:\n"
        ret += self.remove_event_listener("event.currentTarget", funcName)
        ry = r.randint(0, 3)
        if ry == 0:
            ret += self.create_element_range("range")
            ret += self.alter_element_range()
        if ry == 1:
            ret += self.create_text_range()
            ret += self.alter_text_range()
        if ry == 2:
            ret += self.create_element_range("range")
            ret += self.alter_element_range()
            ret += self.move_iterator()
        if ry == 3:
            ret += self.create_text_range()
            ret += self.alter_text_range()
            ret += self.move_tree_walker()
        ry == r.randint(0, 3)
        if ry == 0:
            ret += self.move_iterator()
        if ry == 1:
            ret += self.insert_sub_tree()
        if ry == 2:
            ret += self.tree_crawler()
        if ry == 3:
            ret += self.move_tree_walker()
        self.spray()
        ret += "break;\n"
        ret += "case Event.CAPTURING_PHASE:\n"
        ret += self.add_event_listener("event.target")
        ret += "break;\n"
        ret += "case Event.CAPTURING_PHASE:\n"
        ret += self.remove_event_listener("event.currentTarget", funcName)
        ry = r.randint(0,3)
        if ry == 0:
            ret += self.create_element_range("range")
            ret += self.alter_element_range()
        if ry == 1:
            ret += self.create_text_range()
            ret += self.alter_text_range()
        if ry == 2:
            ret += self.create_element_range("range")
            ret += self.alter_element_range()
            ret += self.create_text_range()
            ret += self.alter_text_range()
        if ry == 3:
            ret += self.create_text_range()
            ret += self.alter_text_range()
            ret += self.create_element_range("range")
            ret += self.alter_element_range()
        ry = r.randint(0,3)
        if ry == 0:
            ret += self.move_iterator()
        if ry == 1:
            ret += self.insert_sub_tree()
        if ry == 2:
            ret += self.tree_crawler()
        if ry == 3:
            ret += self.move_tree_walker()
        ret += self.add_event_listener("event.target")
        ret += "break;\n"
        ret += "}"
        ret = "function %s(%s){\n%s\n}\n" % (funcName, "event", ret)
        return ret

    def tweak_attributes(self, element):
        ret = ""
        for attribute in g.HTMLAttributes:
            ret += self.trys("%s.setAttribute('%s',%s);" % (element, attribute, self.randInteresting()))
        return ret

    def create_node_iterator(self):
        ret = ""
        nf = [
            "NodeFilter.SHOW_ALL", "NodeFilter.SHOW_ELEMENT", "SHOW_ATTRIBUTE", "NodeFilter.SHOW_TEXT", "NodeFilter.SHOW_CDATA_SECTION",
            "NodeFilter.SHOW_ENTITY_REFERENCE","NodeFilter.SHOW_ENTITY", "NodeFilter.SHOW_PROCESSING_INSTRUCTION",
            "NodeFilter.SHOW_COMMENT", "NodeFilter.SHOW_DOCUMENT", "NodeFilter.SHOW_DOCUMENT_TYPE", "NodeFilter.SHOW_DOCUMENT_FRAGMENT",
            "NodeFilter.SHOW_NOTATION",
        ]
        ret += self.create_element_range("range1")
        ret += self.delete_element_range("range1")
        nf2 = [
            "NodeFilter.FILTER_ACCEPT", "NodeFilter.FILTER_SKIP",
        ]
        ret += self.trys("ni = document.createNodeIterator(%s,%s,%s,%s);" % (self.randDoc(), r.choice(nf), r.choice(nf2), self.randb()))
        return ret

    def create_tree_walker(self):
        ret = ""
        nf = [
            "NodeFilter.SHOW_ALL", "NodeFilter.SHOW_ELEMENT", "SHOW_ATTRIBUTE", "NodeFilter.SHOW_TEXT", "NodeFilter.SHOW_CDATA_SECTION",
            "NodeFilter.SHOW_ENTITY_REFERENCE","NodeFilter.SHOW_ENTITY", "NodeFilter.SHOW_PROCESSING_INSTRUCTION",
            "NodeFilter.SHOW_COMMENT", "NodeFilter.SHOW_DOCUMENT", "NodeFilter.SHOW_DOCUMENT_TYPE", "NodeFilter.SHOW_DOCUMENT_FRAGMENT",
            "NodeFilter.SHOW_NOTATION",
        ]
        ret += self.create_element_range("range1")
        ret += self.delete_element_range("range1")
        nf2 = [
            "NodeFilter.FILTER_ACCEPT", "NodeFilter.FILTER_SKIP",
        ]
        ret += self.trys("ni = document.createTreeWalker(%s,%s,%s,%s);" % (self.randDoc(), r.choice(nf), r.choice(nf2), self.randb()))
        return ret

    def create_tag_aggregation(self):
        ret = ""
        ret += self.trys("tagAggregation = document.getElementsByTagName(%s.tagName);" % self.randElem())
        return ret

    def fuzz_attributes(self, orig):
        ret = ""
        for objBlack in g.OBJ_BLACKLIST:

            c = r.randint(0,5)
            if c == 0:
                if orig == "tree":
                    ret += self.trys("%s.%s=null;" % (self.randElem(), objBlack))
                if orig == "tag":
                    rx = r.randint(0, 1000)
                    ret += self.trys("tagAggregation[%s%%tagAggregation.length].%s=null;" % (rx, objBlack))
                if orig == "it":
                    ret += self.trys("currentNode.%s=null;" % objBlack)
                if orig == "tw":
                    ret += self.trys("currentLeaf.%s=null;" % objBlack)
            if c == 1:
                if orig == "tree":
                    ret += self.trys("%s.%s();" % (self.randElem(), objBlack))
                if orig == "tag":
                    rx = r.randint(0, 1000)
                    ret += self.trys("tagAggregation[%s%%tagAggregation.length].%s();" % (rx, objBlack))
                if orig == "it":
                    ret += self.trys("currentNode.%s();" % objBlack)
                if orig == "tw":
                    ret += self.trys("currentLeaf.%s();" % objBlack)
            if c == 2:
                if orig == "tree":
                    ret += self.trys("%s.%s(%s.parentNode);" % (self.randElem(), objBlack, self.randElem() ))
                if orig == "tag":
                    rx = r.randint(0, 1000)
                    ret += self.trys("tagAggregation[%s%%tagAggregation.length].%s(tagAggregation[%s%%tagAggregation.length].parentNode);" % (rx, objBlack, rx))
                if orig == "it":
                    ret += self.trys("currentNode.%s(currentNode.parentNode);" % objBlack)
                if orig == "tw":
                    ret += self.trys("currentLeaf.%s(currentLeaf.parentNode);" % objBlack)
            if c == 3:
                if orig == "tree":
                    ret += self.trys("%s.%s=%s.parentNode.%s;" % (self.randElem(), objBlack, self.randElem(), objBlack ))
                if orig == "tag":
                    rx = r.randint(0, 1000)
                    ret += self.trys("tagAggregation[%s%%tagAggregation.length].%s=tagAggregation[%s%%tagAggregation.length].parentNode.%s;" % (rx, objBlack, rx, objBlack))
                if orig == "it":
                    ret += self.trys("currentNode.%s=currentNode.parentNode.%s;" % (objBlack, objBlack))
                if orig == "tw":
                    ret += self.trys("currentLeaf.%s=currentLeaf.parentNode.%s;" % (objBlack, objBlack))
            if c == 4:
                if orig == "tree":
                    ret += self.trys("%s.%s=%s;" % (self.randElem(), objBlack, self.randInteresting()))
                if orig == "tag":
                    rx = r.randint(0, 1000)
                    ret += self.trys("tagAggregation[%s%%tagAggregation.length].%s=%s;" % (rx, objBlack, self.randInteresting()))
                if orig == "it":
                    ret += self.trys("currentNode.%s=%s;" % (objBlack, self.randInteresting()))
                if orig == "tw":
                    ret += self.trys("currentLeaf.%s=%s;" % (objBlack, self.randInteresting()))
            if c == 5:
                if orig == "tree":
                    ret += self.trys("%s.%s(%s);" % (self.randElem(), objBlack, self.randInteresting()))
                if orig == "tag":
                    rx = r.randint(0, 1000)
                    ret += self.trys("tagAggregation[%s%%tagAggregation.length].%s(%s);" % (rx, objBlack, self.randInteresting()))
                if orig == "it":
                    ret += self.trys("currentNode.%s(%s);" % (objBlack, self.randInteresting()))
                if orig == "tw":
                    ret += self.trys("currentLeaf.%s(%s);" % (objBlack, self.randInteresting()))

        return ret

    def fuzz_nduja(self):
        ret = ""

        # 1. build element treee for nduja
        # create element and append child
        for i in range(g.MAX_ELEM):
            ret += self.create_element_append_child()
            # add event listener
            for i in range(g.MAX_LISTENERS):
                func_name = "func%s" % len(self.funcs)
                self.funcs.append(func_name)
                ret += self.add_event_listener(self.lastElem(), func_name)
            # tweak attributes
            ret += self.tweak_attributes(self.lastElem())

        # boom
        ret += self.create_node_iterator()
        ret += self.create_tree_walker()
        ret += self.create_tag_aggregation()
        ret += self.create_element_range("range")
        ret += self.create_text_range()
        ret += self.alter_element_range()
        ret += self.spray()
        ret += self.move_iterator()
        ret += self.move_tree_walker()
        ret += self.tag_crawler()

        # generate functions
        s2 = ""
        for func_i in self.funcs:
            s2 += self.modify_dom_func(func_i)


        ret = s2 + ret
        return ret

    def generate(self):
        script = self.fuzz_nduja()
        script += self.window_reload()
        script = self.gen_tags("script", script)
        head = "<title>nduja_fuzzer</title>\n"
        body = self.gen_tags("body", script)
        return head + body

def gen():
    js = JSTemplater()
    return js.generate()