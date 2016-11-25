#coding:gbk
'''
unicode
cp936
utf-8
GB2312
'''

#迭代器
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

#生成器:是一种特殊的迭代器，也拥有next方法
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

#装饰器@ 给已经存在的对象增加新的功能

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
#python连接数据库


import MySQLdb

#mysql -uroot -p121
#增
    #create database dbname
    #create table tname(id int not null,name varchar(30))
    #insert into tname values()

#删
    #drop database dbname
    #drop table tname
    #delete table tname where id=1
    #truncate table tname

#改
    #alter table tname change colname colname
    #alter table tname add

#查
    #desc tname
    #select * from tname

#1、创建连接
'''
con = MySQLdb.connect(
    host = 'localhost',
    user = 'root',
    passwd = '121',
    db = 'hello'
    )
'''
#2、实例化游标（游标缓冲区）:发送python对数据库进行的操作命令和接收数据库返回给python数据的一片空间
#cur = con.cursor()
#3、进行数据库操作
#cur.execute('create table student(id int)')
#cur.execute('insert into student values(1)')
#cur.execute('insert into student values(%s)'%2)
#cur.execute('insert into student values(%s)',3)
#cur.executemany('insert into student values(%s)',range(10))
#cur.execute('select * from student')
#print cur.fetchall() #查看所有数据
'''
print cur.fetchone()  #查看一条数据
print cur.fetchone()
print cur.fetchone()
print cur.fetchone()
'''
#print cur.fetchmany(5) #查看多条数据

#关闭连接
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
#图形化阅读器
