#coding:gbk

#�������ǶԳ����߼����нṹ������̻���һ�ֱ�̷���

#�����Ķ���
    #def funcname(args):
        #block
    #lambda arg1,arg2:�������ʽ һ�к���
#�����ĵ���
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

#�б��Ƶ�ʽ
'''
for i in range(10):
    for j in range(5):
        print i+j
'''
'''
a = [i+j for i in range(10) for j in range(5)]
print a
'''

#�����Ĳ���
    #�βΣ������Ƕ��庯����ʱ�򣬶���Ĳ���
    #ʵ�Σ������ǵ��ú�����ʱ�򣬴��ݵĲ���

    #λ�ò���:�����ǵ��ú�����ʱ�򣬴��ݲ������ն����βε�˳����С�
'''
def func(a,b,c):
    print a
    print '%s'%b
    print '%s'%c
func(10,3,0 )
'''

    #�ؼ��ֲ���:�����ǵ��ú�����ʱ�򣬴��ݲ��������β� = ʵ�εķ�ʽ���У��Ӷ����Դ��ε�˳��
'''
def func(a,b,c):
    print a,b,c 
func(a=10,c=20,b=30)
'''

    #Ĭ�ϲ���:�����Ƕ��庯����ʱ�򣬰��� �β� = Ĭ��ֵ�����У������ǵ��ú�����ʱ�� ��
            #����ֵ���βο��Ժ��Դ���ʵ�Σ��������ʵ�Σ���ôʵ�λḲ��Ĭ��ֵ��
'''
def func(a,c,b = 25):
    print a
    print b
     print c
func(10,30)
func(10,20,30)
'''
    #������
        #�����Ƕ��庯����ʱ�򣬲���ǰ���һ��*,��ô�����ǵ��ú�������ʱ�����γ�һ��Ԫ���Ͳ���
          #�����Ƕ��庯����ʱ�򣬲���ǰ�������*����ô�����ǵ��ú�������ʱ�����γ�һ���ֵ��Ͳ���

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
#return ����һ�����
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


#callable �жϸ��������Ƿ���Ե�������������
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

#1���ú���ʵ��zip����
#2��쳲���������

