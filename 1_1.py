#coding=utf8
while True:
	flag = 0 
	s=input('Please enter string:')
	x = s.split()  
	for j in range(4):
		if int(x[j]) < 0 or int(x[j]) > 255:
			print('[Error]: cannot compose IP address')
			flag = 1
			break
	if flag == 0:
		print('.'.join(x))