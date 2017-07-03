#coding=utf8

__author__ = 'WangHaizhen'

from detectionIP import *

while True:
    flag = 0 
    s=input('Please enter string:')
    x = s.split('.')  
    L=[]
    if j(x[0]) and j(x[1]) and j(x[2]) and j(x[3]):
        for xx in x:
            L.append(my_bin(int(xx)))
        print('.'.join(L))
    else:
        flag = 1
        print('[Error]: cannot compose IP address')


		


