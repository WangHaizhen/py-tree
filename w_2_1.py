#coding=utf8

__author__ = 'WangHai zhen'

while True:
	A = input('Please input the first list:')
	B = input('Please input the first list:')
	for a in A.split():
		for b in B.split():
			print("列表 A 的第 %d 个元素和列表 B 的第 %d 个元素相加得 %d " 
			 % ((A.split()).index(a) + 1, (B.split()).index(b) + 1, int(a)+int(b)) )

