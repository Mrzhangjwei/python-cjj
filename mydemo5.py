#coding:gbk

#函数：是对程序逻辑进行结构化或过程化的一种编程方法

#函数的定义
    #def funcname(args):
        #block
    #lambda arg1,arg2:参数表达式 一行函数
#函数的调用
    #funcname(args)

'''
def demo():
    print 'hello,nihao'
demo()
'''

'''
def func():
    def demo():
        print 'hello'
    demo()
func()
'''

'''
a = lambda x,y,z,r,s:x+y-z
print a(10,20,30,1,1)
'''

'''
for i in range(10):
    a = lambda j:j+i
    print a(3),
'''

'''
def func(j):
    for i in range(10):
        print i+j
func(3)
'''

#列表推导式
'''
for i in range(10):
    for j in range(5):
        print i+j
'''
'''
a = [i+j for i in range(10) for j in range(5)]
print a
'''

#函数的参数
    #形参：当我们定义函数的时候，定义的参数
    #实参：当我们调用函数的时候，传递的参数

    #位置参数:当我们调用函数的时候，传递参数按照定义形参的顺序进行。
'''
def func(a,b,c):
    print a
    print '%s'%b
    print '%s'%c
func(10,3,0 )
'''

    #关键字参数:当我们调用函数的时候，传递参数按照形参 = 实参的方式进行，从而忽略传参的顺序
'''
def func(a,b,c):
    print a,b,c 
func(a=10,c=20,b=30)
'''

    #默认参数:当我们定义函数的时候，按照 形参 = 默认值来进行，当我们调用函数的时候 ，
            #给定值的形参可以忽略传递实参，如果传递实参，那么实参会覆盖默认值。
'''
def func(a,c,b = 25):
    print a
    print b
     print c
func(10,30)
func(10,20,30)
'''
    #参数组
        #当我们定义函数的时候，参数前面加一个*,那么当我们调用函数传参时，会形成一个元组型参数
          #当我们定义函数的时候，参数前面加两个*，那么当我们调用函数传参时，会形成一个字典型参数

'''       
def func(*a):
    print a
func()
func(10)
func(10,20,30,{'age':50})
'''

'''
def func(**a):
    print a
func()
func(name = {'name' : 'sas'})
func(name = 'laoli',age = 20)
'''
'''
def func(*args,**kwargs):
    print args
    print kwargs
#func()
#func(10,20,30)
#func(name = 'xiaoqiang')
func((10,20),30,'abc',[12,3],age = 50)
'''
#return 返回一个结果
'''
def outer(x,y):
    def inner():
        print x
        print y
        z = x + y
        return z 
        print z
    return inner()
outer(5,10)
'''

'''
def demo(x,y):
    z = x + y
    return z
demo(10,20)
'''

'''
def demo():
    print 'hello python'
demo()
'''
#func = demo()
#func

#func = demo
#demo()


#callable 判断给定对象是否可以当做函数被调用
'''
a = 10
def demo():
    pass
print callable(demo)
'''

for i in xrange(10):
	print i,

'''
>>> a = xrange(10)
>>> b = range(10)
>>> type(a)
<type 'xrange'>
>>> type(b)
<type 'list'>
>>> b
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a
xrange(10)
>>> 
'''

#map(lambda x,y:x+y,range(10),range(20,30))

#1、用函数实现zip功能
#2、斐波那契数列

