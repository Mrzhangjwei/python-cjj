#coding:gbk

#python 字典（dict）：元素以大括号包围的，元素呈键值对显示并以逗号隔开的，无序的，可修改的序列
    #字典的定义
        #dict(([’x’, 1], [’y’, 2]))
        #{}
        #dict(zip(range(10),'abcdefg'))
            #zip()将指定序列对应索引位上的元素合并为一个元组，并返回一个列表，以短的为主。
            #map()将指定序列对应索引位上的元素合并为一个元组，并返回一个列表，以长的为主,不足的地方以None补充。
    #字典的访问

d = {'name':'xiaoli','age':20,'address':'beijing','abc':{'name':'xiaozhang'}}
#print d['abc']['name']
#d['name'] = 'laoli'
#print d
'''
del d['abc']
print d
'''
    #字典的方法
        #keys
        #values
#print d.keys()
#print d.values()
#print d['aaa']
        #get 在指定的字典当中获取指定的键所对应的值，如果键存在，返回对应的值
             #如果键不存在，默认返回None(或者返回设定值)
#print d.get('name')
#print d.get('aaa')
#print d.get('name','xiaoqiang')
#print d.get('aaa','123')
        #pop 弹出指定键所对应的值，参数不可为空
#print d.pop('name')
#print d.pop()
#print d

        #setdefault
d = {'name':'xiaoli','age':20,'address':'beijing'}

#print d.setdefault('name')
#print d.setdefault('ass','21')
#print d.setdefault('name','laozhang')
#print d
        #update  更新
'''
d.update(name = 'laozhang')
print d
#d['name'] = 'laoli'
#print d
'''
        #items 将字典的键和值放在一个元组中，每一个键和值作为一个元组，放在列表中存储返回
'''
a = d.items()
print a
'''
        #迭代模式
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
        #视图模式
            #viewitems
            #viewkeys
            #viewvalues
'''
print d.viewitems()
print d.viewkeys()
print d.viewvalues()
'''

        #字典的删除
            #pop 弹出指定键所对应的值
            #popitem  弹出键值对
            #clear 请空字典，不删除字典
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
        #has_key 判断指定键是否存在于指定的字典当中
        #in
#print d.has_key('age')
#print d.has_key('ddd')
#print 'age' in d

        #copy(嵌套)

            #模块copy
                #copy.copy() 浅层拷贝
                #copy.deepcopy()深层拷贝
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

#python 元组（tuple）:元素以小括号包围的,元素之间以逗号隔开，有序的，不可修改的序列。
        #因为元组的不可修改性，一般用元组来写配置文件
        #单元素元组，末尾必须加逗号(123,)
    #count
    #index


#python 比较运算符
    # > < == >= <= != <>


#python 布尔值比较
    #True  非空字符串、非空列表、非空字典、非空元祖、非0数字
    #False 空字符串、空列表、空字典、空元祖、0

#python 逻辑运算符
    #优先级  not > and > or
    #and 两边为真，取后者，有假为假
    #or 两边为真，取前者，有真为真
    #not
#print True and False or False
#print True or False and False
#print not True and False
#print not True or True 

#cmp(x,y)
    #当x = y 时，返回0
    #当x > y 时，返回1
    #当x < y 时，返回-1
#print cmp(10,10)
#print cmp(10,20)
#print cmp(10,5)

#repr 把标识符同时转化为字符串

#type 查看指定对象的类型

#dir 查看指定对象的属性

#help 查看指定方法的用法

#isinstance 判断指定对象是否指定类的实例

'''
class Hero():
    hp = 100

huangzi = Hero()
#print huangzi.hp
print isinstance(huangzi,Hero)
'''

#模块的导入
    #import time  -->模块名.方法
    #import ConfigParser as hello
    #from 模块名 import 方法,方法
    #from 模块名 import 方法 as 别名

'''
print 'hello',
print 'world',
print 'I am'
'''
#print 'hello','world'

#import pachong

#设置环境变量
    #我的电脑 --> 右击 --> 属性 --> 高级系统设置 --> 环境变量（用户变量）PYTHONPATH(变量名)
    #import sys  --> sys.path(查看) --> sys.path.append()(添加)

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

#python 赋值
    #直接赋值
    #链式赋值
    #序列解包赋值

#a = 10
#a = b = c = 'abc'
#a,b = 10,20
'''
a = 10
b = 20
a,b = b,a
'''
#python 关键字判断

import keyword

#print keyword.kwlist
#print keyword.iskeyword('continue')
#print keyword.iskeyword('aaa')


#exec 执行字符串里python代码
    #exec('import time')
    #exec("print 'hello world'")
    #exec('print(10*3)')

#eval 执行字符串里的python算术表达式
    #eval('100+100/25')
    #eval('10*3')
