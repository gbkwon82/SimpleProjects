# -*- coding: utf-8 -*-

# import python module
import re
import xml.etree.ElementTree as element

# import user module
import DateUtility

class XmlParser:
    def __init__(self):
        self.workXmlElement = None
        self.xml_src_path = None
        self.xml_work_path = None
        
    # XML 파일내 주석을 삭제함
    def removeComments(self, srcPath, workPath):
        srcFp = open(srcPath, 'r')
        workFp = open(workPath, 'w')
        
        comment_obj1 = re.compile("<!--.*-->", re.DOTALL)
        comment_obj2 = re.compile("<[?].*[?]>", re.DOTALL)
        
        xmlText = srcFp.read()
        
        newText = comment_obj1.sub("", xmlText)
        newText = comment_obj2.sub("", newText)
        
        workFp.write(newText)
        
        srcFp.close()
        workFp.close()
        
        
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
    def makeNormalizeXmlFile(self, _xml_src_path, _xml_work_path=None):
        self.xml_src_path = _xml_src_path
        self.xml_work_path = _xml_work_path
        if self.xml_work_path == None:
            self.xml_work_path = "_".join([self.xml_src_path, DateUtility.getTodayStr("%y%m%d_%H%M%S")])
           
        self.removeComments(self.xml_src_path, self.xml_work_path)
        
        elementTreeObj = element.parse(self.xml_work_path)    
        etRoot = elementTreeObj.getroot()
        self.xmlIndent(etRoot, 0)
        elementTreeObj.write(self.xml_work_path)
    
    # Parses an XML section into an element tree and root element for this tree.
    def xmlParsing(self):
        self.workXmlElement = element.parse(self.xml_work_path)
        self.workXmlRoot = self.workXmlElement.getroot()
    
    # Returns the element attributes as a sequence of (name, value) pairs. 
    # The attributes are returned in an arbitrary order.
    def getItems(self, _element=None):
        if _element == None:
            _element = self.workXmlRoot
        return _element.items()
    
    # Returns the elements attribute names as a list. 
    # The names are returned in an arbitrary order.
    def getKeys(self, _element):
        if _element == None:
            _element = self.workXmlRoot
        return _element.keys()
    
    # Gets the element attribute named key.
    # Returns the attribute value, or default if the attribute was not found.
    def get(self,key,_element):
        if _element == None:
            _element = self.workXmlRoot
        return _element.get(key) 
           
    # Finds the first subelement matching match. 
    # Match may be a tag name or path. Returns an element instance or None.
    def find(self, match, _element=None):
        if _element == None:
            _element = self.workXmlRoot
            
        return _element.find(match)
    
    # Finds all matching subelements, by tag name or path. 
    # Returns a list containing all matching elements in document order.
    def findAll(self, match, _element=None):
        if _element == None:
            _element = self.workXmlRoot
        
        return _element.findall(match)
    
    def makeXmlTreeDict(self):
        for childTree in self.workXmlRoot:
            print childTree.tag, childTree.attrib
    
    def test(self):
        for rxVl in self.workXmlRoot.findall('RxVL'):
            print rxVl.attrib
            
    
if __name__ == "__main__" :
    obj = XmlParser()
    #obj.makeNormalizeXmlFile('afdxConfig1.xml', "NewAFDXConfig1.xml")
    obj.makeNormalizeXmlFile('xml_doc/afdxConfig1.xml')
    obj.xmlParsing()
    obj.makeXmlTreeDict()
    print obj.find("MyES")
    print obj.find("PARTITION_MASK")
    print obj.findAll("RxVL")
    print obj.findAll("ETH_SRC_MAC_REF")
# 
#     tree = parser.parse('afdxConfig1.xml')
#     root = tree.getroot()
#     print root.tag
#     print root.attrib
#     
#     for child in root:
#         print child.tag, child.attrib
        

