#coding:gbk

#python �ֵ䣨dict����Ԫ���Դ����Ű�Χ�ģ�Ԫ�سʼ�ֵ����ʾ���Զ��Ÿ����ģ�����ģ����޸ĵ�����
    #�ֵ�Ķ���
        #dict(([��x��, 1], [��y��, 2]))
        #{}
        #dict(zip(range(10),'abcdefg'))
            #zip()��ָ�����ж�Ӧ����λ�ϵ�Ԫ�غϲ�Ϊһ��Ԫ�飬������һ���б��Զ̵�Ϊ����
            #map()��ָ�����ж�Ӧ����λ�ϵ�Ԫ�غϲ�Ϊһ��Ԫ�飬������һ���б��Գ���Ϊ��,����ĵط���None���䡣
    #�ֵ�ķ���

d = {'name':'xiaoli','age':20,'address':'beijing','abc':{'name':'xiaozhang'}}
#print d['abc']['name']
#d['name'] = 'laoli'
#print d
'''
del d['abc']
print d
'''
    #�ֵ�ķ���
        #keys
        #values
#print d.keys()
#print d.values()
#print d['aaa']
        #get ��ָ�����ֵ䵱�л�ȡָ���ļ�����Ӧ��ֵ����������ڣ����ض�Ӧ��ֵ
             #����������ڣ�Ĭ�Ϸ���None(���߷����趨ֵ)
#print d.get('name')
#print d.get('aaa')
#print d.get('name','xiaoqiang')
#print d.get('aaa','123')
        #pop ����ָ��������Ӧ��ֵ����������Ϊ��
#print d.pop('name')
#print d.pop()
#print d

        #setdefault
d = {'name':'xiaoli','age':20,'address':'beijing'}

#print d.setdefault('name')
#print d.setdefault('ass','21')
#print d.setdefault('name','laozhang')
#print d
        #update  ����
'''
d.update(name = 'laozhang')
print d
#d['name'] = 'laoli'
#print d
'''
        #items ���ֵ�ļ���ֵ����һ��Ԫ���У�ÿһ������ֵ��Ϊһ��Ԫ�飬�����б��д洢����
'''
a = d.items()
print a
'''
        #����ģʽ
            #iteritems
            #iterkeys
            #itervalues
d = {'name':'xiaoli','age':20,'address':'beijing'}
'''
a = d.iteritems() 
print a.next()
print next(a)
print a.next()
'''
'''
b = d.iterkeys()
print b.next()
print next(b)
'''
c = d.itervalues()
#print c
        #��ͼģʽ
            #viewitems
            #viewkeys
            #viewvalues
'''
print d.viewitems()
print d.viewkeys()
print d.viewvalues()
'''

        #�ֵ��ɾ��
            #pop ����ָ��������Ӧ��ֵ
            #popitem  ������ֵ��
            #clear ����ֵ䣬��ɾ���ֵ�
            #del
d = {'name':'xiaoli','age':20,'address':'beijing'}
#print d.pop('age')
#print d
#print d
#print d.popitem()
'''
d.clear()
print d
'''
#del d['name']
#print d
        #has_key �ж�ָ�����Ƿ������ָ�����ֵ䵱��
        #in
#print d.has_key('age')
#print d.has_key('ddd')
#print 'age' in d

        #copy(Ƕ��)

            #ģ��copy
                #copy.copy() ǳ�㿽��
                #copy.deepcopy()��㿽��
'''
d = {'name':'xiaoli','age':20,'address':'beijing'}
a = d.copy()
d['gender'] = 'nv'
print d
print a
'''
'''
zgyh = {'name':'','money':{'dollar':0,'RMB':0}}

lz = zgyh.copy()
zs = zgyh.copy()

lz['name'] = 'laozhang'
zs['name'] = 'zhangsao'

lz['money']['RMB'] = 30
zs['money']['RMB'] = 10
zgyh['money']['dollar'] = 2
print zgyh
print lz
print zs
'''

#python Ԫ�飨tuple��:Ԫ����С���Ű�Χ��,Ԫ��֮���Զ��Ÿ���������ģ������޸ĵ����С�
        #��ΪԪ��Ĳ����޸��ԣ�һ����Ԫ����д�����ļ�
        #��Ԫ��Ԫ�飬ĩβ����Ӷ���(123,)
    #count
    #index


#python �Ƚ������
    # > < == >= <= != <>


#python ����ֵ�Ƚ�
    #True  �ǿ��ַ������ǿ��б��ǿ��ֵ䡢�ǿ�Ԫ�桢��0����
    #False ���ַ��������б����ֵ䡢��Ԫ�桢0

#python �߼������
    #���ȼ�  not > and > or
    #and ����Ϊ�棬ȡ���ߣ��м�Ϊ��
    #or ����Ϊ�棬ȡǰ�ߣ�����Ϊ��
    #not
#print True and False or False
#print True or False and False
#print not True and False
#print not True or True 

#cmp(x,y)
    #��x = y ʱ������0
    #��x > y ʱ������1
    #��x < y ʱ������-1
#print cmp(10,10)
#print cmp(10,20)
#print cmp(10,5)

#repr �ѱ�ʶ��ͬʱת��Ϊ�ַ���

#type �鿴ָ�����������

#dir �鿴ָ�����������

#help �鿴ָ���������÷�

#isinstance �ж�ָ�������Ƿ�ָ�����ʵ��

'''
class Hero():
    hp = 100

huangzi = Hero()
#print huangzi.hp
print isinstance(huangzi,Hero)
'''

#ģ��ĵ���
    #import time  -->ģ����.����
    #import ConfigParser as hello
    #from ģ���� import ����,����
    #from ģ���� import ���� as ����

'''
print 'hello',
print 'world',
print 'I am'
'''
#print 'hello','world'

#import pachong

#���û�������
    #�ҵĵ��� --> �һ� --> ���� --> �߼�ϵͳ���� --> �����������û�������PYTHONPATH(������)
    #import sys  --> sys.path(�鿴) --> sys.path.append()(���)

'''
from time import ctime,sleep
import thread
    
def loop0():
    print 'start loop0 at:',ctime()
    sleep(4)
    print 'loop0 done at:',ctime()

def loop1():
    print 'start loop1 at:',ctime()
    sleep(2)
    print 'loop1 done at:',ctime()

def main():
    print 'starting at:',ctime()
    thread.start_new_thread(loop0,())
    thread.start_new_thread(loop1,())
    sleep(4)
    print 'all done at:',ctime()
    
if __name__ == '__main__':
    main()
'''

#python ��ֵ
    #ֱ�Ӹ�ֵ
    #��ʽ��ֵ
    #���н����ֵ

#a = 10
#a = b = c = 'abc'
#a,b = 10,20
'''
a = 10
b = 20
a,b = b,a
'''
#python �ؼ����ж�

import keyword

#print keyword.kwlist
#print keyword.iskeyword('continue')
#print keyword.iskeyword('aaa')


#exec ִ���ַ�����python����
    #exec('import time')
    #exec("print 'hello world'")
    #exec('print(10*3)')

#eval ִ���ַ������python�������ʽ
    #eval('100+100/25')
    #eval('10*3')
