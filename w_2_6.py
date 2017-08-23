#coding=utf8

__author__ = 'WangHai zhen'


while True:
	print('please input a list:')
	s = input()
	t = s.split(' ')
	List = list(set(t))
	List.sort(key = t.index )
	print(List)