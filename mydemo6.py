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

