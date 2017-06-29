#coding = utf8
i = 0
while( i < 4 ):
	flag = 0 
	s=input('Please enter string:')
	x = s.split(' ')  
	for j in range(4):
		if int(x[j]) < 0 or int(x[j]) > 255:
			print('[Error]: cannot compose IP address')
			flag = 1
			break
			j = j + 1
	y = '.'.join(x)  
	#print(x)
	if flag == 0:
		print(y)
	i = i + 1
