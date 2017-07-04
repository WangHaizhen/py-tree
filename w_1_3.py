#coding=utf8

__author__ = 'WangHaizhen'

from detectionIP import *

def my_bin(num):
    L = []
    if num == 0:
        return('0')
    else:
        while(num != 0):
            L.append(str(num%2))
            num=num//2
        return(''.join(L[::-1]))


while True:
    s=input('Please enter string:')
    re = IP(s)
    if re == True:
        x=s.split('.')
        L = []
        for xx in x:
            L.append(my_bin(int(xx)))
        print('.'.join(L))
    else:
        print('[Error]: cannot compose IP address')
    


		


