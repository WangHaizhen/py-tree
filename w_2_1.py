#coding=utf8

__author__ = 'WangHai zhen'

while True:
	A = input('Please input the first list:')
	B = input('Please input the first list:')
	for i,a in enumerate(A.split()):
		for j,b in enumerate(B.split()):
			print("列表 A 的第 %d 个元素和列表 B 的第 %d 个元素相加得 %d " 
			 % (i+1, j+1, int(a)+int(b)) )

