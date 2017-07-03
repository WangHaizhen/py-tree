#coding=utf8

__author__ = 'WangHai zhen'

def j(x):
	return True if 0<= int(x) <=255 else False;
def IP():
	s = input('Please enter string:')
	x = s.split('.')
	if j(x[0]) and j(x[1]) and j(x[2]) and j(x[3]):
		print('.'.join(x))
	else:
		print('[Error]: cannot compose IP address')


def my_bin(num):
    L = []
    if num == 0:
    	return('0')
    else:
    	while(num != 0):
        	L.append(str(num%2))
        	num=num//2
    #m = L.reverse()
    	return(''.join(L[::-1]))

if __name__ == '__main__':
	print (type(my_bin(6)))
	print(my_bin(6))
	IP()
