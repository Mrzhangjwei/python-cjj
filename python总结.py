#coding:gbk
#!D:\Python27\python.exe
#!usr/var/bin/python

#python 模块
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
时间戳时间 time.time()
struct_time时间
asctime time.ctime()
time.mktime()
time.strftime()
'''

    #random

    #thread
'''
thread.start_new_thread(func,())
GIL 锁机制
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
    def run(self) 功能函数
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
        #配置阿帕奇服务器

        #cgi.FieldStorage()
            #getvalue
            #setvalue

    
    #sys sys.path   sys.path.append()  sys.stdout  sys.stdin  sys.stderr
    #os  os.path   os.path.join()
    #keyword
    #codecs  codecs.open(filename,mode,gbk)
#python 文件操作
    #open(filename,mode) 

#python 捕获异常
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
#python 数据类型
    #int
    #float
    #str
    #list  index count append extend insert pop remove del sort reverse
    #dict  
    #tuple count index


#python 安装三方模块
    #.exe
    #解压，切到解压目录，找到setup.py  执行python setup.py install
    #切到python安装目录下的scripts，执行pip install Scrapy


#python 语句

'''
if 判断
name = 'xiaoli'
if name:
    print ''
else:
    print ''

if:
elif:
elif:
else:

循环
for i in  :
    block
while name:
    break
print
eval('10*10')
exec('print()')

import
from time from 方法
'''

#python 函数 --->面向过程

#def func(参数):
    #block

    #位置参数
    #默认参数
    #关键字参数
    #参数组 *arg   **arg

    #LEGB
    #递归：最小可能性，自身调用自身
    #装饰器  生成器  迭代器

#面向对象
'''
class Mydemo(继承对象):
    name = '12'
    def func(self):
        block
'''
    #三大特征
        #继承
            #新式类：object
            #经典类
        #封装 私有化
        #多态
#python对象的特征
    #魔术方法
        #__init__
        #__del__
        #__doc__
        #__dict__
        #__name__
        #__module__
        #dir
        #hasattr setattr getattr delattr

#and or not


