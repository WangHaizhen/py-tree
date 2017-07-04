#coding=utf8

__author__ = 'WangHai zhen'

def j(x):
	return True if 0<= int(x) <=255 else False;

def IP(s):
	x = s.split('.')
	if j(x[0]) and j(x[1]) and j(x[2]) and j(x[3]):
		return True
	else:
		return False






