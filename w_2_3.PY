#coding=utf8

__author__ = 'WangHai zhen'

while True:
	N = input('Please input integer N:')
	for i in range(1, int(N)+1):
		for j in range(1, i+1):
			print('%dx%d=%d' % (i,j,i*j), end = '\t')
		print()
