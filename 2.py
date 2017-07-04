#coding=utf8

while True:
	A = input('Please input the first list:')
	B = input('Please input the first list:')
	print( [int(a)+int(b) for a in A.split() for b in B.split()] )
