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

