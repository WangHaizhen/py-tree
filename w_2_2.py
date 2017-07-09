#coding=utf8

__author__ = 'WangHai zhen'

for i in range(1, 10):
	for j in range(1, i+1):
		print('%dx%d=%-2d' % (i,j,i*j), end = '\t')
	print()

