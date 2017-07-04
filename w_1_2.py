#coding=utf8

__author__ = 'WangHaizhen'

from w_1_1 import *

while True:
  str = input('Please enter string:')
  x = str.split()
  st = x[1:5]
  s=' '.join(st)
  re = IP(s)
  if re == True:
    y = '.'.join(st)
    print(x[0] + '://' + y  + ':' + x[5] + '/' + x[6])
  else:
    print('[Error]: cannot compose IP address')

    