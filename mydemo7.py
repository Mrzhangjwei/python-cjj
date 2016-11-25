#coding:gbk

#函数的作用域（LEGB）:使用变量或者函数的范围

    #L 本地作用域（局部） --> local
    #E 嵌套作用域 --> est
    #G 全局作用域 --> global
    #B 内建作用域 --> bulid-in

'''
a = 100
def func():
    print 'a is:',a
    
def demo():
    print a
func()
demo()
'''
'''
def func():
    a = 10
    print a

def demo():
    print a

demo()
'''
#global 声明全局变量
'''
a = 100
def func(a):
    print 'a is:',a
    a = 10
    print 'a change is:',a
func(a)
print 'a still is',a
'''
'''
a = 100
def func():
    print 'a is:',a
    global a
    a = 10
    print 'a change is:',a
func()
print 'a still is',a
'''
#嵌套

#闭包

'''
def outer(a):
    print a+1
    def inner():
        print a
    return inner()
outer(10)
'''
'''
def outer(a):
    print a+1
    def inner():
        print a
    return inner
outer(10)()
'''
'''
def outer(a):
    print a+1
    def inner(b):
        print a+b
    return inner
outer(10)(20)
'''
'''
def outer(a):
    print a+1
    def inner(b):
        print a+b
    return inner
outer(10)(20)

def demo():
    print a
'''

#递归：函数自身调用自身
    #条件：
        #必须有一个出口（最小可能性）
        #自身调用自身

'''
def func():
    print 'hello'
    return func() 

func()
'''
'''
def jc(num):
    a = 1
    for i in range(1,num+1):
        a *= i
    print a

jc(10)
'''
'''
def dgjc(num):
    if num == 0:
        return 1
    else:
        return num * dgjc(num-1)
print dgjc(10)
'''
'''
10*dgjc(9)
9*dgjc(8)
...
1*dgjc(0)
1
'''
'''
def qm(d,z):
    a = d
    if z == 0:
        return 1
    else:
        for i in range(z-1):
            a *= d
        return a
print qm(2,5)
    
#a = d*d*d*d
'''
'''
def dgqm(d,z):
    if z == 0:
        return 1
    else:
        return d * dgqm(d,z-1)

print dgqm(5,5)
'''

#5*dgqm(5,4) 5*dgqm(5,3) 5*dgqm(5,2) 5*dgqm(5,1) 5*dgqm(5,0) 1
#5*5*5*5*5*1

'''
def demo(num):
    if num/2.0 < 1:
        return 1

    else:
        return num + num/2.0 + demo(num/2.0)

print demo(100)
'''
#os,sys模块
#二元查找


#面向对象
    #对象：万物皆对象，一切存在的都是对象
    #类：对事物的划分
    #实例：具体的事物，类的具象化
        #域：属于类或者实例的变量
            #类变量：属于类的变量
            #实例变量：属于实例的变量
        #方法：属于类或者实例的函数
        #属性：域和方法的统称

#类的定义
'''
class 类名(继承对象): -->驼峰记法
    block
'''
'''
class Dongwu_Persorn_Huang():
    pass
'''

'''
class Bird():
    hungry = True
    
#类的调用(实例化)
    #Bird()
    #print Bird.hungry
jiaque = Bird()
print jiaque.hungry
'''
'''
class Hero():
    hp = 100
    mp = 100
Hero.hp = 50
houzi = Hero()
houzi.mp = 80
print 'Hero.hp:',Hero.hp
print 'houzi.hp:',houzi.hp
print 'houzi.mp:',houzi.mp
print 'Hero.mp:',Hero.mp
mangseng = Hero()
print 'mangseng.hp:',mangseng.hp
print 'mangseng.mp:',mangseng.mp
'''
'''
class Hero():
    hp = 100
    mp = 100
    def jn(self):
        Hero.mp -= 10
        print Hero.mp
houzi = Hero()
houzi.jn()
'''
'''
class Hero():
    hp = 100
    mp = 100
    def jn1(self):
        if Hero.jn2:
            Hero.mp -= 10
            Hero.hp += 10
        print Hero.mp,Hero.hp
    def jn2(self):
        return 1
houzi = Hero()
houzi.jn1()
'''
'''
class Bird():
    hungry = False
    def eating(self):
        if self.hungry == False:
            print 'gudu...gudu...gudu...'
            print self
bailing = Bird()
bailing.eating()
print bailing

jiaque = Bird()
jiaque.eating()
print jiaque
'''
'''
class Hero():
    hp = 100
    mp = 100
    def jn1(self):
        if self.jn2:
            self.mp -= 10
            self.hp += 10
        print self.mp,self.hp   
    def jn2(self):
        return 1
houzi = Hero()
houzi.jn1()
'''
#在python的面向对象当中，每个方法函数都有必须一个叫做self的参数，当我们实例化之后（实例=类()）
#我们调用方法（实例.方法()），系统会自动转换为：类.方法(实例)来执行，也就是说self就是实例本身。


#面向对象的三大特征
    #继承
'''
class Parent():
    first_name = 'laoqiang'
    last_name = 'li'

class Child(Parent):
    first_name = 'xiaoqiang'

son = Child()
print son.first_name
print son.last_name
'''

    #经典类：不继承object对象
    #新式类：继承object对象
'''
class A():
    pass
print type(A)

class B(object):
    pass
print type(B)
'''
#经典类的继承：按顺序继承
'''
class A():
    def demo(self):
        print 'this is A'

class B(A):
    pass
class C(A):
    def demo(self):
        print 'this is C'

class D(B,C):
    pass
d = D()
d.demo()
'''
#新式类的继承：按照修改优先级
'''
class A(object):
    def demo(self):
        print 'this is A'
class B(A):
    pass
class C(A):
    def demo(self):
        print 'this is C'
class D(B,C):
    pass

d = D()
d.demo()
'''
'''
class Demo(object):
    pass
'''

    #封装
'''
class Hero():
    __hp = 100
    mp = 100
    def __jn(self):
        self.mp -= 10
        print self.mp
    def jn1(self):
        return self.__jn()

a = Hero()
print a.mp
#print a.__hp显示没有该属性，因为__hp被认为是私有属性
#a.__jn()
a.jn1()
'''
    #多态
'''
'zbcd' + 'ABCD'
[123] + ['A','B','C']
'''

#面向对象的魔术方法
    #__init__构造函数,实例化之后自动执行
'''
class Demo():
    def __init__(self):
        print 'hello python'

d = Demo()
'''
'''
class Demo():
    def func(self,a,b):
        print a + b
d = Demo()
d.func(10,20)

'''
'''
class Demo():
    def __init__(self,a,b):
        print a + b
        
d = Demo(20,30)
'''

    #__del__ 析构函数,删除实例之后自动运行
'''
class Demo():
    def __del__(self):
        print 'Bye-Bye'
d = Demo()
del d
'''
    #__doc__说明文档字符串
#class Demo():
    #'''hello world,my name is laoli,I am 20 years old,
    #my job is ITmonkey!!!'''

#print Demo.__doc__

    #__dict__
'''
class Hero():
    hp = 100
    mp = 100
    def jn(self):
        self.hp += 10
        print self.hp
#print Hero.__dict__

    #dir
#print dir(Hero)
    #__name__
#h = Hero()
#print Hero.__name__

#if __name__ == __main__:
 #   block


    #__module__类似于__name__

print Hero.__module__
    #issubclass
'''
'''
class A():
    pass
class B(A):
    pass
'''
#print issubclass(B,A)

    #isinstance
#b = B()
#print isinstance(b,B)
'''
class Hero():
    hp = 100
    mp = 100
    def jn(self):
        self.hp += 10
        print self.hp
'''
    #hasattr()
#print hasattr(Hero,'hp')
#print hasattr(Hero,'jn')
    #getattr()
#print getattr(Hero,'jn')
#print getattr(Hero,'wp',20)
    #setattr()
'''
setattr(Hero,'qw',50)
print hasattr(Hero,'qw')
print getattr(Hero,'qw')
'''
'''
def jn2(self):
    print 'hello'
setattr(Hero,'nihao',jn2)
print hasattr(Hero,'nihao')
print getattr(Hero,'nihao')
'''
    #delattr()
'''
delattr(Hero,'mp')
print dir(Hero)
'''
'''
import random

class Doudizhu():
    h = ['hei','hong','mei','fang']
    s = list('AJQK') + range(2,11)
    puke = []
    def hs(self):
        for i in self.h:
            for j in self.s:
                self.puke.append('%s of %s'%(i,j))
    def king(self):
        for i in ['boss','BOSS']:
            self.puke.append(i)
if __name__ == '__main__':
    d = Doudizhu()
    d.hs()
    d.king()
    random.shuffle(d.puke)
    #print d.puke
    a = d.puke[0::3]
    b = d.puke[1::3]
    c = d.puke[2::3]
    print ','.join(a)
    print ','.join(b)
    print ','.join(c)
'''

import random

for i in range(50):
    #print random.random()#随机生成0-1之间的浮点数
    #print random.uniform(10,20)#随机生成指定范围之间的浮点数
    #print random.randint(10,20)#随机生成指定范围之间的整数，包含上下限
         print random.randrange(10,20)#随机生成指定范围之间的整数,包含下限，不包含上限
         print random.randrange(10,20,2)
'''
l = range(20)
for i in l:
'''
    #print random.choice(l)#在指定的序列当中，随机抽取一个元素
    #random.shuffle(l)#将指定的序列随机打乱顺序
    #print l
    #print random.sample(l,3)#在指定的序列当中，随机抽取指定个数的元素，返回列表形式


