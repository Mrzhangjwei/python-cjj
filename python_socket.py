#coding:gbk

#����������ʽ������
    #���� ֻ��һ���ŵ���ͨ��˫�������� BP��
    #��˫�� ֻ��һ���ŵ���ͨ��˫������ �Խ���
    #ȫ˫�� �ж����ŵ���ͨ��˫������

#TCP���������ӵ�Э�� ��۱Ƚϸߣ��Ƚ�׼ȷ
#UDP�������ӵ�Э��

import socket

#�������������
    #1�������׽��ֶ���
        #socket_family
            #AF_INET 
            #AF_UNIX
            #AF_INET6
        #socket_type
            #SOCK_STREAM -->TCP
            #SOCK_DGRAM -->UDP
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #2����IP�Ͷ˿ں�,��Ҫһ��˫Ԫ��Ԫ��
        #bind
        #0-65535,0-1024
soc.bind(('127.0.0.1',8000))
#soc.bind(('',8000))
    #3����������
soc.listen(3)
    #4�����ܺͷ�������
        #accept
con,add = soc.accept()
print con
print add,'is connected'

con.send('I am your server')
print con.recv(512)
    #5���ر��׽��ֶ���
soc.close()


#�����ͻ�������
    #1�������׽��ֶ���
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #2������,��Ҫһ��˫Ԫ��Ԫ��
        #connect
sock.connect(('127.0.0.1',8000))
    #3�����պͷ�������
print sock.recv(512)
sock.send('I am you user')
    #4���ر��׽��ֶ���
sock.close()


#TCP���պͷ�������
    #recv
    #send

#UDP���ܺͷ�������
    #recvfrom
    #sendto
