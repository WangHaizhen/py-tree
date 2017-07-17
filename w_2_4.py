#coding=utf8

__author__ = 'WangHai zhen'

import random

while True:
	x = int(input('Enetr the number of competition :'))
	List1 = input('Enter your own player (1<= x <=9) :').split()
	m = 0 ;n = 0
	print('The enemy is coming !\nWar outcome:')
	print(' ',end=' ')
	for i in List1:
		print(i,end=' ')
	print()
	for ii in [random.randint(1,9) for i in List1 ]:
		print(ii,end =' ')
		for k in List1:
			if ii < int(k):
				print('o',end=' ')
				m = m+1
			else:
				print('x',end=' ')
				n = n+1
		print()
	print('Congratulations! You won!') if m > n else print('I’m sorry you lost , try again~')
		
		
	