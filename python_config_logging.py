#coding:gbk

#conf .ini .txt .xml

import ConfigParser

con = ConfigParser.ConfigParser()

con.read('conf.ini')
#print con.sections() #��ȡ�����ļ�����½���
#print con.options('CONF') #��ȡ�����ļ�ָ���½��µ�ѡ����
#print con.items('CONF')
#print con.get('INFORMATION','name')#��ȡָ���½���ָ��ѡ��������Ӧ��ֵ

con.remove_section('INFORMATION')
#print con.sections()
con.remove_option('CONF','name')
#print con.options('CONF')
#con.add_section('E_MAIL')
#print con.sections()
#con.add_option('E_MAIL','address')
#print con.options('E_MAIL')
con.set('E_MAIL','address','admin@qq.com')
#print con.items('E_MAIL')
con.set('CONF','maskcolor','skyblue')
#print con.get('CONF','maskcolor')

#con.write(open('conf.ini','w'))



#python��־

import logging

#��־�ȼ�
    #NOTSET 0
    #DEBUG  10
    #INFO   20
    #WARNING 30
    #ERROR  40
    #CRITICAL 50

'''
logging.basicConfig(
    level = 10,
    filename = 'mylog.log',
    format = "%(levelname)-10s %(asctime)s %(message)s"
    )

logging.warning('I am a pretty boy')
logging.debug('you must be a football player')
logging.error('you may be error')

try:
    123 + [123]
    print 'hello'
except Exception,e:
    logging.error(e)
'''    
