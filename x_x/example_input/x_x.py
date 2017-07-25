#coding=utf-8
 
__author__ = 'WangHai zhen'

import os
import re

def clear(fp):
    if re.search('\[',fp):
        if fp.find(']') != -1:
            fp = fp.replace("[","l").replace("]","l")
            pattern = re.compile(r'(l)(.+)(l)')
            return pattern.sub(r'',fp)
        else:
            return fp
    elif re.search(u'【',fp):
        if fp.find(u'】') != -1:
            fp = fp.replace(u"【","l").replace(u"】","l")
            pattern = re.compile(r'(l)(.+)(l)')
            return pattern.sub(r'',fp)
        else:
            return fp
    elif re.search('\-',fp):
        return fp.replace(u"-","")
    else:
        return fp


path = 'E:\\Workspace\\markdown.md\\py-tree\\x_x\\example_input'
for i in os.listdir(os.getcwd()):
    if i == "x_x.py":
        continue
    t = (clear(i)).split('.')
    while '' in t:
        t.remove('')
    newname = '.'.join(t)
    os.rename(os.path.join(path,i),os.path.join(path,newname)) #对文件进行重命名     #对原来的文件名i进行重命名
    #print(i)       #输出当前目录下重命名后的文件名
