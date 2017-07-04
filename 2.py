#coding=utf8

while True:
	s1 = input('Please input the first list:')
	s2 = input('Please input the first list:')
	L=[]
	[L.append(s1[a]+s2[b]) for a in len(s1) for b in len(s2)]
	print(L)
