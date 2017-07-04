#coding=utf8

while True:
	A = input('Please input the first list:')
	B = input('Please input the first list:')
	L=[]
	[L.append(s1[a]+s2[b]) for a in A for b in B]
	print(L)
