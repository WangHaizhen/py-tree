#coding=utf8

__author__ = 'WangHai zhen'

while True:
	print('Please input  a list:')
	s = input()
	List = list(s.split())
	list1 = []
	for i in List:
		if i not in list1:
			list1.append(i)
	print(list1)