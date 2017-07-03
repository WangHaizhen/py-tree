#coding=utf8

__author__ = 'WangHaizhen'

from w_1_1 import j

while True:
  flag = 0 
  s=input('Please enter string:')
  x = s.split()  
  if j(x[1]) and j(x[2]) and j(x[3]) and j(x[4]):
    y='.'.join(x[1:5])
  else:
    flag = 1
    print('[Error]: cannot compose IP address')
  if flag == 0:
    print(x[0] + '://' + y  + ':' + x[5] + '/' + x[6])

    