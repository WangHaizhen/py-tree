#coding=utf8

__author__ = 'WangHai zhen'


while True:
	print('please input a list:')
	s = input()
	List = list(set(s.split(' ')))
	print(List)