#coding:gbk

#被动的阻塞式的连接
    #单工 只有一条信道，通信双方不可逆 BP机
    #半双工 只有一条信道，通信双方可逆 对讲机
    #全双工 有多条信道，通信双方可逆

#TCP：面向连接的协议 早价比较高，比较准确
#UDP：无连接的协议

import socket

#创建服务端连接
    #1、创建套接字对象
        #socket_family
            #AF_INET 
            #AF_UNIX
            #AF_INET6
        #socket_type
            #SOCK_STREAM -->TCP
            #SOCK_DGRAM -->UDP
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #2、绑定IP和端口号,需要一个双元素元组
        #bind
        #0-65535,0-1024
soc.bind(('127.0.0.1',8000))
#soc.bind(('',8000))
    #3、监听个数
soc.listen(3)
    #4、接受和发送数据
        #accept
con,add = soc.accept()
print con
print add,'is connected'

con.send('I am your server')
print con.recv(512)
    #5、关闭套接字对象
soc.close()


#创建客户端连接
    #1、创建套接字对象
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #2、连接,需要一个双元素元组
        #connect
sock.connect(('127.0.0.1',8000))
    #3、接收和发送数据
print sock.recv(512)
sock.send('I am you user')
    #4、关闭套接字对象
sock.close()


#TCP接收和发送数据
    #recv
    #send

#UDP接受和发送数据
    #recvfrom
    #sendto
