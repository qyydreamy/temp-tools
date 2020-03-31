#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import xml.sax
 
from xml.dom.minidom import parse
import xml.dom.minidom
def parse_path(path):
   # 使用minidom解析器打开 XML 文档
   DOMTree = xml.dom.minidom.parse(path)
   root = DOMTree.documentElement
    
   files = root.getElementsByTagName("camitem")

   cnt = 0;
   file_list = list()
   for file in files:
      if file.hasAttribute("script"):
         file_list.append(file.getAttribute("script"))
         cnt+=1
   print(cnt)
   return file_list

def appendAttribute(path):
   import re  
   f=open(path,'r', errors='ignore')  
   lines=f.readlines()  
   f.close()  
   f=open(path,'w+', errors='ignore')  
   for eachline in lines:  
       a=re.sub('<Animation','<Animation UIChange=\"true\"', eachline)  
       f.writelines(a)  
   f.close()  


if  __name__ == "__main__":
   file_list = parse_path("D:\\Work_Log\\NewUI\\temp\\file_list.xml")
   prefix = "E:\\version4.3.7\\exe\\resources\\"
   #print(file_list)
   cnt=0
   for file in file_list:
      cnt += 1
      appendAttribute(prefix+file)
   print(cnt)

 
 
