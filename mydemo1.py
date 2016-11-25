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
    #整形数
    #浮点数
    #长整形

    #数字运算符
        # + - * / ** //(地板除，整除) ==(值相等) is(全等)
        #+= -= *= /= %(取余)
        
#a = 10 (=赋值)
#a += 10 ---> a = a + 10
        
#python 是一门弱变量语言，变量即用即生成，变量的类型由值的类型来决定。


#python 字符串(str):元素以引号包围的序列
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
        #字符串的索引（字符串的切片）
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

#s = '   hello world,I am xiaoli.   '
#a = 'ooooohello worldooooo'
        #字符串的删减
            #strip 默认删除字符串两端的空白符,亦可以删除两端指定的字符
            #lstrip默认删除字符串左端的空白符
           #rstrip默认删除字符串右端的空白符
s='   jjjabcdjajjbjjj    '
#print s.lstrip()
print s.strip('j')
#print a.strip('o') 
#print a.lstrip('o')
#print s.rstrip()


