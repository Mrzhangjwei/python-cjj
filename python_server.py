#coding:gbk

import socket

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind(('127.0.0.1',9000))
soc.listen(5)
con,add = soc.accept()
#print con
print add,'is connected'

while True:
    sends = raw_input('>>>')
    if sends == 'exit':
        con.send(sends)
        break
    else:
        con.send(sends)
    recvs = con.recv(512)
    if recvs == 'exit':
        print recvs
    else:
        print recvs
soc.close()
