#coding:gbk -->声明字符集
#!D:\Python27\python.exe -->声明解析器
'''
python 模块：
	1、三方模块
	2、自写模块
	3、内置模块

.py 脚本文件  .pyc 临时文件  .pyw  图形化文件
'''

#单行注释 ---> #
#多行注释 ---> 三单引或者三双引


#python 数字运算
    #整形数 int
    #浮点数 float
    #长整形

    #数字运算符
        # + - * / ** //(地板除，整除) ==(值相等) is(全等)
        #+= -= *= /= %(取余)
        
#a = 10 (=赋值)
#a += 10 ---> a = a + 10
        
#python 是一门弱变量语言，变量即用即生成，变量的类型由值的类型来决定。


#python 字符串(str):元素以引号包围的不可修改的序列
    #'' ""
    #''' '''  """ """

    #转义符
        # \
        # % -->% 用 %来转译
    #特殊字符
        #\n 换行符 \t水平制表符
        
#print '\\n'
#print '\t'
#print '\\t'
        
        #占位符(字符串的格式化)
            #%d %s %f  %.2f
#print 'my name is %s'%'ITmonkey'
#print 'my name is %+30s'%'ITmonkey'
#print 'my name is %-30s'%'ITmonkey'
#print '%-10d'%30
#print '%s'%30
            #format
'''
name = 'xiaoli'
age = 20
print 'name:{0},age:{1}'.format(name,age)
'''
#a = 'name:{0},age:{1}'
#print a.format('xiaozhang',20)
#print 'name:{0},age:{1}'.format('xiaowang',25)

    #字符串的方法
        #字符串的索引（字符串的分片）
s = 'hello world'
#print s[0:4] 包含下限，不包含上限
#print s[0:5]
#print s[6]
#print s[1:8]
#print s[1:8:3]
#print s[:]
#print s[:5]
#print s[::]
#print s[::2]
#print s[-2]
#print s[5:-1]
#print s[3::]
#print s[3::4]
        #字符串的查找
            #find 查找指定字符在指定字符串当中的索引位，如果存在返回第一次出现的位置
                #如果不存在，返回值为-1
#print s.find('o')
#print s.find('z')
#print s.find('o',5,6)
            #index 查找指定字符在指定字符串当中的索引位，如果存在返回第一次出现的位置
                #如果不存在，报错
#print s.index('l')
#print s.index('z')
            #count 查找指定字符在指定字符串当中出现的次数
#print s.count('l')
#print s.count('o',5,8)
#print s.count('z')

s = 'hello world'
        #字符串的填充
            #center 居中
#print s.center(30)
#print s.center(30,'*')
#print s.center(30,'a')
            #ljust 左对齐
#print s.ljust(30)
#print s.ljust(30,'0')
            #rjust 右对齐
#print s.rjust(20)
#print s.rjust(20,'0')
            #zfill
#print s.zfill(20)
            #expandtabs
#print 'a\tb'.expandtabs()
#print 'a\tb'.expandtabs(4)
#print 'a\tb'.expandtabs(10)

s = '   hello world,I am xiaoli.   '
a = 'ooooohello worldooooo'
        #字符串的删减
            #strip 默认删除字符串两端的空白符,亦可以删除两端指定的字符
            #lstrip默认删除字符串左端的空白符
            #rstrip默认删除字符串右端的空白符
#print s.strip()
#print a.strip('o')
#print a.lstrip('o')
#print s.rstrip()

s = 'ooohellowooo'
#print s.strip('hello')


#print '''sadadasdnkas
#sdadsasd
#dassad
#as'''

        #字符串的变形
            #upper 将字符串当中小写字母转换为大写
            #lower 将字符串当中大写字母转换为小写
            #title 单词首字母大写
            #capitalize 字符串首字母大写
            #swapcase 大小写互换

s = 'Hello World'

#print s.upper()
#print s.lower()

a = 'dfaDFfafdd hDFello woGBrld'
#print a.title()
#print a.capitalize()
#print a.swapcase()
        #字符串的拼接
            #join
            #+
            #* 重复
#print s.join('abc')
#print 'nihao' + 'python'
#print 'http://127.0.0.1:8000/' + 'appserv/conf' + '?page=3'
#print 'hello' * 3

        #字符串的切分
            #split 默认按空白符从左到右进行切分，也可以以指定字符切分
            #rspilt 默认按空白符从右到左进行切分，也可以以指定字符切分
#a = 'hello world,I am xiao wang. [123]'

#print a.split()
#print a.split('o')
#print a.split('o',1)
#print a.rsplit('a')
#print a.rsplit('a',1)


a = 'hello world,my name is xiao wang,I am 18 years old.'
b = 'abcdefg12345'
c = 'abcdefg 12345'
d = 'abcdefg'
e = '123456'
        #字符串的判断
            #isalnum 判断字符串是否完全由数字字母组成
#print a.isalnum()
#print b.isalnum()
#print c.isalnum()
#print d.isalnum()
            #isalpha 判断字符串是否完全由字母组成
#print b.isalpha()
#print d.isalpha()
            #isdigit 判断字符串是否完全由数字组成
#print b.isdigit()
#print d.isdigit()
#print e.isdigit()

            #isupper 判断字符串是否完全由大写字母组成
#print 'PYTHON'.isupper()
            #islower 判断字符串是否完全由小写字母组成
#print 'python'.islower()
            #isspace 判断字符串是否完全由空白符组成
#print 'hello world'.isspace()
#print '  '.isspace() 判断字符串是否符合title格式
            #istitle
#print 'Hello Python hi'.istitle()

            #startswith 
            #endswith

#print 'hello'.startswith('o')
#print 'hello'.startswith('hel')
#print 'hello world'.startswith(' ',5,8)
        #字符串的替换
            #replace
#print 'heollo pytohon'.replace('o','abc')
#print 'heollo pytohon'.replace('o','abc',3)
#print 'heollo pytohon'.replace('o','abc',2)
        #字符串的编码
            #encode 加码
            #decode 解码
#print 'abc'.encode('utf-8')


#python 列表（list）：元素以中括号包围的，元素之间以逗号隔开的，有序的，可修改的序列。
    #列表的定义
        #list(可迭代对象)
        #range()
        #[]

    #列表的索引
l = [123,456,'abc','hello',['1234','efg',[0]]]
#print l[0]
#a =  l[-1]
#b =  a[-1]
#print b[0]
#print l[-1][-1][0]
    #列表的方法
        #列表的查找
            #count 查找指定元素在指定列表当中的数量
            #index 查找指定元素在指定列表当中第一次出现的索引位
l = ['a','b','c','a',123,1,444,'a']
#print l
#print l.count(5)
#print l.index('a')
#print l.index('a',2,5)
#print l.index('z')
        #列表的添加
            #append 追加单个元素
            #extend 添加多个元素
            #insert 在指定的索引位之前插入指定的元素
        #列表的排序
            #sort 正序
            #reverse 按索引倒排序
l = [12,16,3,1,36,'a','e','q','F','R','Z','@','$']

#l.sort()
#print l

#l.reverse()
#print l

'''
l.sort()
l.reverse()
print l
'''
'''
l.sort(reverse = True)
print l
'''
l = [12,16,3,1,36,'a','e','q','F','R','Z','@','$']
        #列表的删除
            #pop 默认弹出最后一位索引位上的元素,亦可以弹出指定索引位对应的元素
            #remove 删除指定的元素
'''
print l.pop()
print l.pop()
print l.pop()
print l
'''
#print l.pop(6)
#print l
'''
l.remove('@')
print l
'''
        #del
#del l
#print l
'''
del l[4]
print l
'''
'''
l[5] = 'abc'
print l
'''

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
#python 元组（tuple）:元素以小括号包围的。元素之间以逗号隔开，有序的，不可修改的序列。










