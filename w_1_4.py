
#coding=utf8

__author__ = 'WangHai zhen'

import base64
s1='XDRjXDY5XDY2XDY1XDIwXDY5XDczXDIwXDczXDY4XDZmXDcyXDc0XDJjXDIwXDQ5XDIwXDc1XDczXDY1XDIwXDcwXDc5XDc0XDY4XDZmXDZlXDJlXGFcNGNcNjlcNjZcNjVcMjBcNjlcNzNcMjBcNjJcNjVcNjFcNzVcNzRcNjlcNjZcNzVcNmNcMmNcMjBcNDlcMjBcNmNcNmZcNzZcNjVcMjBcNjJcNjFcNmZcNjJcNjFcNmZcMmU='
s2 = base64.b64decode(s1).decode('utf-8').split('\\')
List = [int(i,16)  for i in s2  if i != '']
for i in List:
	print(chr(i),end='')