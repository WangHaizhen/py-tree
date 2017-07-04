#coding=utf8

__author__ = 'WangHaizhen'

from w_1_1 import *

def my_bin(num):
    num = int(num)
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
    if IP(' '.join(s.split('.'))):
        L = map(my_bin, s.split('.'))
        print('.'.join(L))
    else:
        print('[Error]: Not an IP address.')
    


		


