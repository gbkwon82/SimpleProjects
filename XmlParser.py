# -*- coding: utf-8 -*-

import re
import xml.etree.ElementTree as element

class XmlParser:
    def __init__(self, _xml_src_file, _xml_work_file):
        self.xml_src_file = _xml_src_file
        self.xml_work_file = _xml_work_file
        self.workXmlElement = None
        
    # XML 파일내 주석을 삭제함
    def removeComments(self):
        comment_obj1 = re.compile("<!--.*-->", re.DOTALL)
        comment_obj2 = re.compile("<[?].*[?]>", re.DOTALL)
        
        xmlFileObj = open(self.xml_src_file, 'r')
        newFileObj = open(self.xml_work_file, 'w')
        
        xmlText = xmlFileObj.read()
        
        newText = comment_obj1.sub("", xmlText)
        newText = comment_obj2.sub("", newText)
        
        newFileObj.write(newText)
         
        xmlFileObj.close()
        newFileObj.close()
    
    # XML Indent를 맞춰줌
    def xmlIndent(self, root, level=0):
        i = "\n" + level*"  "
        if len(root):
            if not root.text or not root.text.strip():
                root.text = i + "  "
            if not root.tail or not root.tail.strip():
                root.tail = i
            for root in root:
                self.xmlIndent(root, level+1)
            if not root.tail or not root.tail.strip():
                root.tail = i
        else:
            if level and (not root.tail or not root.tail.strip()):
                root.tail = i
        
    # XML 파일을 정규화 하여 새로운 파일을 생성함
    def makeNormalizeXmlFile(self):
        self.removeComments()
        
        elementTreeObj = element.parse(self.xml_work_file)
        
        etRoot = elementTreeObj.getroot()
        self.xmlIndent(etRoot, 0)
        
        elementTreeObj.write(self.xml_work_file)
    
    # Parses an XML section into an element tree and root element for this tree.
    def xmlParsing(self):
        self.workXmlElement = element.parse(self.xml_work_file)
        self.workXmlRoot = self.workXmlElement.getroot()
    
    # Returns the element attributes as a sequence of (name, value) pairs.
    def getItems(self, etObj):
        return etObj.items()
    
    # Returns the elements attribute names as a list.
    def getKeys(self, etObj):
        return etObj.keys()

    def test(self):
        for rxVl in self.workXmlRoot.findall('RxVL'):
            print rxVl.attrib
            
    
if __name__ == "__main__" :
    obj = XmlParser('afdxConfig1.xml', "NewAFDXConfig1.xml")
    obj.makeNormalizeXmlFile()
    obj.xmlParsing()
    obj.test()
# 
#     tree = parser.parse('afdxConfig1.xml')
#     root = tree.getroot()
#     print root.tag
#     print root.attrib
#     
#     for child in root:
#         print child.tag, child.attrib
        

