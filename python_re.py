#coding:gbk

import re


a = 'My name is xiao_zhang,\nI am 19 years old,\tmy job is IT_monkey!'

#����re�����ʽ����һ�ָ߼��ַ�������ʽ��ͨ��������ƥ�䡣
    #ƥ��ķ�ʽ
        #����ƥ��:ͨ��������Ҫƥ�����ݵ��ص����ƥ��
            #ƥ��Ĺ���
                #ƥ�����ݵĹ���
                    #ԭ��ƥ��
#print re.findall(r'name',a)
                    #. ƥ����˻��з�֮�����������
#print re.findall(r'.',a)
#print re.findall(r'...',a)
                    #\w ƥ�����е�������ĸ�»���
#print re.findall(r'\w',a)
                    #\W ƥ�����з�������ĸ�»��ߵ�����
#print re.findall(r'\W',a)
                    #\d ƥ�����е�����
#print re.findall(r'\d',a)
                    #\D ƥ�����з����ֵ�����
#print re.findall(r'\D',a)
                    #\s ƥ�����еĿհ׷�������\n \t��
#print re.findall(r'\s',a)
                    #\S ƥ�����зǿհ׷�������
#print re.findall(r'\S',a)
                    #\b ���ʱ߽磬ֻƥ��һ��λ��
#print re.findall(r'\w\b',a)
#print re.findall(r'\b\w',a)
                    #\B 
#print re.findall(r'\w\B',a)
#print re.findall(r'\w\d',a)
                    #\A ƥ���ַ����Ŀ�ͷ
#print re.findall(r'\A\w',a)
#print re.findall(r'\A',a)
                    #\Z ƥ���ַ�����ĩβ
#print re.findall(r'..\Z',a)
a = '''My name is xiao_zhang,
I am 19 years old,
my job is IT_monkey!'''

                    #^ �ӿ�ͷ
#print re.findall(r'^\w',a)
                    #$ ��ĩβ
#print re.findall(r'\W$',a)
#print re.findall(r'^My$',a)
                    # | ƥ��ܵ�������һ�ߵ�����
#print re.findall(r'\W|\d',a)

                    #[] ƥ�������ŵ�������һ�ֱ��ʽ
#print re.findall(r'[\W\d]',a)
#print re.findall(r'\W\d',a)
#b = '3242343451234313454545545454154324654765765'
                    #[^] ����������ı��ʽ
#print re.findall(r'[^\w]',a)
#print re.findall(r'\W',a)
                    #[a-z] [A-Z] ƥ��һ����Χ
                    #[a-zA-Z]
#print re.findall(r'[a-z]',a)
#print re.findall(r'[A-Z]',a)
#print re.findall(r'[a-z]|[A-Z]',a)
#print re.findall(r'[a-zA-Z]',a)
                    #() ��ƥ��,��������ƥ���ʱ��������ƥ�䷽ʽ��Ϊ��ƥ�����������ƥ�䣬
                        #������ƥ�� ƥ�䵽������
#print re.findall(r'\w\d',a)
#print re.findall(r'\w(\d)',a)
b = 'a3a c5d e6e f7f g2b'
                    #(?P<name>...)������
#print re.findall(r'(?P<laoli>\w)',b)
#print re.findall(r'\w',b)
                    #(?P=name) ����������ƥ�䵽������
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
                    #̰��ƥ��(.*)
#print re.findall(r'a(.*)b','abbbbbbbbbb')
a = '''
<html>
    <head>
        <title>
        `   hello
        </title>
    </head>
    <body>
        <p>
            nihao,python
        </p>
    </body>
</html>
'''
#print re.findall(r'<(.*?)>',a)
                    #��̰��ƥ
#print re.findall(r'(.*?)b','abbbbbbbbbb')
a = '''My name is xiao_zhang,
I am 19 years old,
my job is IT_monkey!'''
                    #ǰհ����ƥ��(?=...)
#print re.findall(r'\d(?=\w)',a)
#print re.findall(r'\d(\w)',a)
                    #��ǰհ����ƥ��(?!...)
#print re.findall(r'\d(?!\w)',a)

                    #��˶���ƥ��(?<=...)
#print re.findall(r'(?<=\w)\d',a)
                    #����˶���ƥ��(?<!...)
#print re.findall(r'(?<!\w)\d',a)
                #ƥ�������Ĺ���
                    # * 0�����
#print re.findall(r'\w*',a)
                    # ? 0��1��
#print re.findall(r'\w?',a)
                    # + 1�����
#print re.findall(r'\w+',a)                    
                    #{3} ƥ��ָ���Ĵ���
#print re.findall(r'\w{3}',a)
#print re.findall(r'\d{2}',a)
                    #{1,3} 
#print re.findall(r'\w{1,3}',a)

a = '''My name is xiao_zhang,
I am 19 years \nold,
my job \t is \n IT_monkey!'''
c = 'AASDFDSSDdsfdfsdfDADA'

                #�������
                    #re.M ����ģʽ
#print re.findall(r'^\w',a)
#print re.findall(r'^\w',a,re.M)
                    #re.I ���Դ�Сд
#print re.findall(r'f',c,re.I)
                    #re.S �޸�.��ƥ�䷽ʽ
#print re.findall(r'.',a,re.S)
            #ƥ��ķ���
                #findall ��ָ�����ַ����в�����������������ʽ���������ݣ������б���ʽ
                #match ��ָ�����ַ�����ͷ����ƥ�䣬���صõ���ƥ�����
                    #ƥ�����ķ���
                        #group()
                        #groups()
#print re.match(r'\w\w',a).group()
#print re.match(r'(\w\w)(\W)(\w+)',a).groups()
#print re.match(r'\d',a)
                #search ���ַ������н���ƥ�䣬���ص�һ��ƥ�䵽������
#print re.search(r'\d',a).group()
#print re.search(r'\d','abc')
                #compile�γ�����ģ��
'''
com = re.compile(r'\d')
print com.findall(a)
'''
                #sub �������ַ������е�replace
#print re.sub(r'\w','*',a)
#print re.sub(r'\w','*',a,3)
                #split �������ַ�����split
b = 'a3a c5d e6e f7f g2b'
#print re.split(r'\d',b)


c = '34817947394890583405939041901989082173898214398490384158797309898'

#print re.findall(r'13\d{9}|15\d{9}|18\d{9}|17\d{9}',c)
#print re.findall(r'1[3578]\d{9}',c)
        #�ṹƥ��
            #Beautifulsoup  xml
print re.findall(r'<div class = "content">(.*)</div>','''<div class = "content">���ٷ�����㷢���������˵��Ӿ�</div>''')
