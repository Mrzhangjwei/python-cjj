#coding:gbk
'''
unicode
cp936
utf-8
GB2312
'''

#������
a = range(10)
b = iter(a)
#print b
'''
for i in b:
    print i
'''
#print b.next()
#print next(b)
'''
try:
    for i in range(11):
        print b.next()

except StopIteration:
    print 'there is no element'
'''

#������:��һ������ĵ�������Ҳӵ��next����
'''
def func():
    yield 1
    yield 2
    for i in range(10):
        yield i

#print func()
generator = func()
for i in range(10):
    print generator.next()
'''
'''
def febo():
    a = b = 1
    yield a
    yield b
    while True:
        a,b = b,a+b
        yield b

fb = []
#print febo()
for i in febo():
    if i > 100:
        break
    fb.append(i)
print fb
'''
#[1,1,2,3,5,8,13,21,44,....]

#װ����@ ���Ѿ����ڵĶ��������µĹ���

'''
def func():
    print 'hello'

a = func
a()
'''
'''
def outer():
    def inner():
        print 'hello'
    return inner

outer()()
'''
'''
def outer(a):
    a()

def func():
    print 'hello'

outer(func)
'''
'''
def func(demo):
    print 'before myfunc...'
    demo()
    print 'after myfunc...'

@func  #--> func(myfunc)

def myfunc():
    print 'myfunc now'

#func(myfunc)
'''
#python�������ݿ�


import MySQLdb

#mysql -uroot -p121
#��
    #create database dbname
    #create table tname(id int not null,name varchar(30))
    #insert into tname values()

#ɾ
    #drop database dbname
    #drop table tname
    #delete table tname where id=1
    #truncate table tname

#��
    #alter table tname change colname colname
    #alter table tname add

#��
    #desc tname
    #select * from tname

#1����������
'''
con = MySQLdb.connect(
    host = 'localhost',
    user = 'root',
    passwd = '121',
    db = 'hello'
    )
'''
#2��ʵ�����α꣨�α껺������:����python�����ݿ���еĲ�������ͽ������ݿⷵ�ظ�python���ݵ�һƬ�ռ�
#cur = con.cursor()
#3���������ݿ����
#cur.execute('create table student(id int)')
#cur.execute('insert into student values(1)')
#cur.execute('insert into student values(%s)'%2)
#cur.execute('insert into student values(%s)',3)
#cur.executemany('insert into student values(%s)',range(10))
#cur.execute('select * from student')
#print cur.fetchall() #�鿴��������
'''
print cur.fetchone()  #�鿴һ������
print cur.fetchone()
print cur.fetchone()
print cur.fetchone()
'''
#print cur.fetchmany(5) #�鿴��������

#�ر�����
#con.commit()
'''
con.rollback()
cur.close()
con.close()
'''
'''
a = range(10)
for i in a:
    print a.pop(i)
'''
#ͼ�λ��Ķ���
