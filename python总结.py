#coding:gbk
#!D:\Python27\python.exe
#!usr/var/bin/python

#python ģ��
    #wx
        #GetValue
        #SetValue
        #write
'''
app = wx.App()
frame = wx.Frame(None,id,title,pos,size,style,name)
panel = wx.Panel(frame)

textctrl = wx.TextCtrl(panel,value)
button = wx.Button(panel,label)
button.Bind(wx.EVT_BUTTON,func)

s_box = wx.BoxSizer()
s_box.Add(button,proportion,flag,border)

frame.Show()
app.MainLoop()
'''
    #re
'''
re.findall(r'',str)
re.match().group()
re.search().groups()
re.compile()
re.sub()
re.split()   * + ? {2} {2,5}

re.I  re.M  re.S
'''
    #time
'''
ʱ���ʱ�� time.time()
struct_timeʱ��
asctime time.ctime()
time.mktime()
time.strftime()
'''

    #random

    #thread
'''
thread.start_new_thread(func,())
GIL ������
'''
    #Queue
'''
Queue.Queue(mxsize)
Queue.LifoQueue()
put get qsize 
'''
    #threading
'''
t = threading.Thread(target = func,args = ())
t.start()
t.join()

class Thread(threading.Thread):
    def __init__(self,arg,args):
    def run(self) ���ܺ���
'''
    #socket
'''
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind(())
soc.listen()
con,add = soc.accept()
con.send()  con.sendto()
con.recv(256)  con.recvfrom()
soc.close()

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.connect(())
soc.recv(256)
soc.send()
soc.close()
'''

    #MySQLdb

'''
conn = MySQLdb(
    host = ,
    user = ,
    passwd = ,
    db = ,
    port = ,
    charset = 
    )

cur = conn.cursor()
cur.execute('%s',arg)
cur.fetchall()
cur.fetchmany()
cur.fetchone()

cur.close()
conn.commit()
conn.close()
'''
    #logging
'''
notset --> 0
debug  --> 10
info   --> 20
warning --> 30
error  --> 40
critical --> 50

logging.basicConfig(
    level = ,
    filename = ,
    format = "%(level)-10s %(asctime)s %(message)s"
    )
logging.error('')
try:
    input('>>>') + '123'
except Exception,e:
    logging.error(e)
'''
    #ConfigParser
'''
c = ConfigParser.ConfigParser()
c.read('')
c.sections()
c.options()
c.set()
c.add_section()
c.remove()
c.write(open('','w'))
'''
    #cgi
        #cmd  python -m CGIHTTPServer
        #���ð����������

        #cgi.FieldStorage()
            #getvalue
            #setvalue

    
    #sys sys.path   sys.path.append()  sys.stdout  sys.stdin  sys.stderr
    #os  os.path   os.path.join()
    #keyword
    #codecs  codecs.open(filename,mode,gbk)
#python �ļ�����
    #open(filename,mode) 

#python �����쳣
'''
    try:
    except:

    try:
    except:
    else:

    try:
    except:
    finally:

    try:
    except:
    else:
    finally:
'''
#python ��������
    #int
    #float
    #str
    #list  index count append extend insert pop remove del sort reverse
    #dict  
    #tuple count index


#python ��װ����ģ��
    #.exe
    #��ѹ���е���ѹĿ¼���ҵ�setup.py  ִ��python setup.py install
    #�е�python��װĿ¼�µ�scripts��ִ��pip install Scrapy


#python ���

'''
if �ж�
name = 'xiaoli'
if name:
    print ''
else:
    print ''

if:
elif:
elif:
else:

ѭ��
for i in  :
    block
while name:
    break
print
eval('10*10')
exec('print()')

import
from time from ����
'''

#python ���� --->�������

#def func(����):
    #block

    #λ�ò���
    #Ĭ�ϲ���
    #�ؼ��ֲ���
    #������ *arg   **arg

    #LEGB
    #�ݹ飺��С�����ԣ������������
    #װ����  ������  ������

#�������
'''
class Mydemo(�̳ж���):
    name = '12'
    def func(self):
        block
'''
    #��������
        #�̳�
            #��ʽ�ࣺobject
            #������
        #��װ ˽�л�
        #��̬
#python���������
    #ħ������
        #__init__
        #__del__
        #__doc__
        #__dict__
        #__name__
        #__module__
        #dir
        #hasattr setattr getattr delattr

#and or not


