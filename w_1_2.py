#coding=utf8

__author__ = 'WangHaizhen'

from w_1_1 import *

while True:
  str = input('Please enter string:')
  x = str.split()
  if IP( ' '.join(x[1:5]) ):
    print('%s://%s:%s/%s'%(x[0], '.'.join(x[1:5]), x[5], x[6]))
  else:
    print('[Error]: cannot compose IP address')

    