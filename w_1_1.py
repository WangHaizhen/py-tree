#coding=utf8

__author__ = 'WangHai zhen'

def j(x):
	return True if 0<= int(x) <=255 else False;
def IP():
	while True:
		s = input('Please enter string:')
		x = s.split()
		if j(x[0]) and j(x[1]) and j(x[2]) and j(x[3]):
			print('.'.join(x))
		else:
			print('[Error]: cannot compose IP address')

if __name__=='__main__':
	IP()

