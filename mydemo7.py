#coding:gbk

#������������LEGB��:ʹ�ñ������ߺ����ķ�Χ

    #L ���������򣨾ֲ��� --> local
    #E Ƕ�������� --> est
    #G ȫ�������� --> global
    #B �ڽ������� --> bulid-in

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
#global ����ȫ�ֱ���
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
#Ƕ��

#�հ�

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

#�ݹ飺���������������
    #������
        #������һ�����ڣ���С�����ԣ�
        #�����������

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
#os,sysģ��
#��Ԫ����


#�������
    #��������Զ���һ�д��ڵĶ��Ƕ���
    #�ࣺ������Ļ���
    #ʵ��������������ľ���
        #�����������ʵ���ı���
            #�������������ı���
            #ʵ������������ʵ���ı���
        #���������������ʵ���ĺ���
        #���ԣ���ͷ�����ͳ��

#��Ķ���
'''
class ����(�̳ж���): -->�շ�Ƿ�
    block
'''
'''
class Dongwu_Persorn_Huang():
    pass
'''

'''
class Bird():
    hungry = True
    
#��ĵ���(ʵ����)
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
#��python����������У�ÿ�������������б���һ������self�Ĳ�����������ʵ����֮��ʵ��=��()��
#���ǵ��÷�����ʵ��.����()����ϵͳ���Զ�ת��Ϊ����.����(ʵ��)��ִ�У�Ҳ����˵self����ʵ������


#����������������
    #�̳�
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

    #�����ࣺ���̳�object����
    #��ʽ�ࣺ�̳�object����
'''
class A():
    pass
print type(A)

class B(object):
    pass
print type(B)
'''
#������ļ̳У���˳��̳�
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
#��ʽ��ļ̳У������޸����ȼ�
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

    #��װ
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
#print a.__hp��ʾû�и����ԣ���Ϊ__hp����Ϊ��˽������
#a.__jn()
a.jn1()
'''
    #��̬
'''
'zbcd' + 'ABCD'
[123] + ['A','B','C']
'''

#��������ħ������
    #__init__���캯��,ʵ����֮���Զ�ִ��
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

    #__del__ ��������,ɾ��ʵ��֮���Զ�����
'''
class Demo():
    def __del__(self):
        print 'Bye-Bye'
d = Demo()
del d
'''
    #__doc__˵���ĵ��ַ���
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


    #__module__������__name__

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
    #print random.random()#�������0-1֮��ĸ�����
    #print random.uniform(10,20)#�������ָ����Χ֮��ĸ�����
    #print random.randint(10,20)#�������ָ����Χ֮�������������������
         print random.randrange(10,20)#�������ָ����Χ֮�������,�������ޣ�����������
         print random.randrange(10,20,2)
'''
l = range(20)
for i in l:
'''
    #print random.choice(l)#��ָ�������е��У������ȡһ��Ԫ��
    #random.shuffle(l)#��ָ���������������˳��
    #print l
    #print random.sample(l,3)#��ָ�������е��У������ȡָ��������Ԫ�أ������б���ʽ


