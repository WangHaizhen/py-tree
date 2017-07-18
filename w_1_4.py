
#coding=utf8

__author__ = 'WangHai zhen'

import base64
s1='XDRjXDY5XDY2XDY1XDIwXDY5XDczXDIwXDczXDY4XDZmXDcyXDc0XDJjXDIwXDQ5XDIwXDc1XDczXDY1XDIwXDcwXDc5XDc0XDY4XDZmXDZlXDJlXGFcNGNcNjlcNjZcNjVcMjBcNjlcNzNcMjBcNjJcNjVcNjFcNzVcNzRcNjlcNjZcNzVcNmNcMmNcMjBcNDlcMjBcNmNcNmZcNzZcNjVcMjBcNjJcNjFcNmZcNjJcNjFcNmZcMmU='
L=map(lambda x: chr(x),[int(i,16)  for i in base64.b64decode(s1).decode('utf-8').split('\\')  if i != ''])
print(''.join(L))
	