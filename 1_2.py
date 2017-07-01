#coding=utf8
__author__ = 'WangHaizhen'
#import 1_1
while True:
	flag = 0 
	s=input('Please enter string:')
	x = s.split()  
	Ip=x[1:5]
	for xx in Ip:
		if int(xx) < 0 or int(xx) > 255:
			print('[Error]: cannot compose IP address')
			flag = 1
			break
	y='.'.join(Ip)
	if flag == 0:
		print(x[0] + '://' + y  + ':' + x[5] + '/' + x[6])

