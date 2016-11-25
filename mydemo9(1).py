#coding:gbk

import re


a = 'My name is xiao_zhang,\nI am 19 years old,\tmy job is IT_monkey!'

#正则（re）表达式：是一种高级字符串处理方式，通常用来做匹配。
    #匹配的方式
        #内容匹配:通过描述所要匹配内容的特点进行匹配
            #匹配的规则
                #匹配内容的规则
                    #原样匹配
#print re.findall(r'name',a)
                    #. 匹配除了换行符之外的所有内容
#print re.findall(r'.',a)
#print re.findall(r'...',a)
                    #\w 匹配所有的数字字母下划线
#print re.findall(r'\w',a)
                    #\W 匹配所有非数字字母下划线的内容
#print re.findall(r'\W',a)
                    #\d 匹配所有的数字
#print re.findall(r'\d',a)
                    #\D 匹配所有非数字的内容
#print re.findall(r'\D',a)
                    #\s 匹配所有的空白符（包含\n \t）
#print re.findall(r'\s',a)
                    #\S 匹配所有非空白符的内容
#print re.findall(r'\S',a)
                    #\b 单词边界，只匹配一个位置
#print re.findall(r'\w\b',a)
#print re.findall(r'\b\w',a)
                    #\B 
#print re.findall(r'\w\B',a)
#print re.findall(r'\w\d',a)
                    #\A 匹配字符串的开头
#print re.findall(r'\A\w',a)
#print re.findall(r'\A',a)
                    #\Z 匹配字符串的末尾
#print re.findall(r'..\Z',a)
a = '''My name is xiao_zhang,
I am 19 years old,
my job is IT_monkey!'''

                    #^ 从开头
#print re.findall(r'^\w',a)
                    #$ 从末尾
#print re.findall(r'\W$',a)
#print re.findall(r'^My$',a)
                    # | 匹配管道符任意一边的内容
#print re.findall(r'\W|\d',a)

                    #[] 匹配中括号当中任意一种表达式
#print re.findall(r'[\W\d]',a)
#print re.findall(r'\W\d',a)
#b = '3242343451234313454545545454154324654765765'
                    #[^] 非中括号里的表达式
#print re.findall(r'[^\w]',a)
#print re.findall(r'\W',a)
                    #[a-z] [A-Z] 匹配一个范围
                    #[a-zA-Z]
#print re.findall(r'[a-z]',a)
#print re.findall(r'[A-Z]',a)
#print re.findall(r'[a-z]|[A-Z]',a)
#print re.findall(r'[a-zA-Z]',a)
                    #() 组匹配,当出现组匹配的时候，其他的匹配方式作为组匹配的条件进行匹配，
                        #返回组匹配 匹配到的内容
#print re.findall(r'\w\d',a)
#print re.findall(r'\w(\d)',a)
b = 'a3a c5d e6e f7f g2b'
                    #(?P<name>...)命名组
#print re.findall(r'(?P<laoli>\w)',b)
#print re.findall(r'\w',b)
                    #(?P=name) 调用命名组匹配到的内容
#print re.findall(r'(?P<laoli>\w)\d',b)
#print re.findall(r'(\w)\d',b)
#print re.findall(r'(?P<laoli>\w)\d(?P=laoli)',b)
'''
a3a
c5c
e6e
f7f
g2g
'''

                #匹配数量的规则
                    # * 0到多次
#print re.findall(r'\w*',a)
                    # ? 0到1次
#print re.findall(r'\w?',a)
                    # + 1到多次
#print re.findall(r'\w+',a)                    
                    #{3} 匹配指定的次数
#print re.findall(r'\w{3}',a)
#print re.findall(r'\d{2}',a)
                    #{1,3} 
#print re.findall(r'\w{1,3}',a)

a = '''My name is xiao_zhang,
I am 19 years \nold,
my job \t is \n IT_monkey!'''
c = 'AASDFDSSDdsfdfsdfDADA'

                #特殊规则
                    #re.M 多行模式
#print re.findall(r'^\w',a)
#print re.findall(r'^\w',a,re.M)
                    #re.I 忽略大小写
print re.findall(r'f',c,re.I)
                    #re.S 修改.的匹配方式
#print re.findall(r'.',a,re.S)
            #匹配的方法
                #findall 在指定的字符串中查找所有满足正则表达式描述的内容，返回列表形式
                
#匹配手机号
#匹配邮箱 
#匹配身份证号 15位|18位（X）
#匹配Ip 255.255.255.255
