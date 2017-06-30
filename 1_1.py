#coding=utf8
while True:
	flag = 0 
	s=input('Please enter string:')
	x = s.split()  
	for xx in x:
		if int(xx) < 0 or int(xx) > 255:
			print('[Error]: cannot compose IP address')
			flag = 1
			break
	if flag == 0:
		print('.'.join(x))