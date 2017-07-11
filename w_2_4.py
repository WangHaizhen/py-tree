#coding=utf8

__author__ = 'WangHai zhen'

import random

while True:
	x = input('Enetr the number of competition :')
	List1 = input('Enter your own player (1<= x <=9) :').split()
	m = 0 ;n = 0
	print('The enemy is coming !\nWar outcome:')
	print(' ',end=' ')
	for i in List1:
		print(i,end=' ')
	print()
	for ii in random.sample(range(1, 9), int(x)):
		print(ii,end =' ')
		for j in List1:
			if int(ii) < int(j):
				print('o',end=' ')
				m = m+1
			else:
				print('x',end=' ')
				n = n+1
		print()
	if m > n:
		print('Congratulations! You won!')
	else:
		print('I’m sorry you lost , try again~')
	