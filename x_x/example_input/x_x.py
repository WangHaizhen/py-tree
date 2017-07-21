#coding=utf8
 
__author__ = 'WangHai zhen'

import os
import re
import base64 

def clear(content):
    #先将[,],....替换成，普通字符l
    content = content.replace("[","l").replace("【","l").replace("]","l").replace("】","l").replace("-","l")
    pattern = re.compile(r'(l)(.+)(l)')
    return pattern.sub(r'',content)


def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):       #检验给出的路径是否是一个文件
        fileList.append(dir)
    elif os.path.isdir(dir):      #检测给出的路径是否是一个目录
        for s in os.listdir(dir): #返回指定目录下所有文件和目录名
            #如果需要忽略某些文件夹，使用以下代码
            if s == "1.py":
                continue
            newDir=os.path.join(s) #os.path.join()函数的作用是将多个路径组合后返回
            GetFileList(newDir, fileList)  
    return fileList



path = 'E:\\Workspace\\markdown.md\\py-tree\\x_x\\example_input'
for i in GetFileList(path, []):
    t = (clear(i)).split('.')
    while '' in t:
        t.remove('')
    newname = '.'.join(t)
    os.rename(os.path.join(path,i),os.path.join(path,newname)) #对文件进行重命名     #对原来的文件名i进行重命名
    #print(i)       #输出当前目录下重命名后的文件名

    