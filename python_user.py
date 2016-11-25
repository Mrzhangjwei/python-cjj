#coding:gbk

import socket

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.connect(('127.0.0.1',9000))
print soc.recv(512)
soc.send('I am your user')
soc.close()
