#coding=utf-8
 
__author__ = 'WangHai zhen'

import os
import re

def clear(fp):
    if re.search('\[',fp) and fp.find(']') != -1:
        return re.sub('\[.*?\]', '', fp)  #re.sub()将fp中匹配'\[.*?\]'的字符串替换为''
    elif re.search(u'【',fp) and fp.find(u'】') != -1:
        return re.sub('\【.*?\】', '', fp)#re.sub()将fp中匹配'\【.*?\】'的字符串替换为''
    elif re.search('\-',fp):
        return fp.replace(u"-","")
    else:
        return fp
     

path = r'E:\Workspace\markdown.md\py-tree\x_x\example_input'
for i in os.listdir(os.getcwd()):
    if i == "x_x.py":
        continue
    #print(clear(i))
 
    t = (clear(i)).split('.')
    while '' in t:
        t.remove('')
    newname = '.'.join(t)
    os.rename(os.path.join(path,i),os.path.join(path,newname)) #对文件进行重命名     #对原来的文件名i进行重命名
    #print(i)       #输出当前目录下重命名后的文件名
