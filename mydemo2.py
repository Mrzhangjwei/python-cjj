#coding:gbk -->�����ַ���
#!D:\Python27\python.exe -->����������
'''
python ģ�飺
	1������ģ��
	2����дģ��
	3������ģ��

.py �ű��ļ�  .pyc ��ʱ�ļ�  .pyw  ͼ�λ��ļ�
'''

#����ע�� ---> #
#����ע�� ---> ������������˫��


#python ��������
    #������ int
    #������ float
    #������

    #���������
        # + - * / ** //(�ذ��������) ==(ֵ���) is(ȫ��)
        #+= -= *= /= %(ȡ��)
        
#a = 10 (=��ֵ)
#a += 10 ---> a = a + 10
        
#python ��һ�����������ԣ��������ü����ɣ�������������ֵ��������������


#python �ַ���(str):Ԫ�������Ű�Χ�Ĳ����޸ĵ�����
    #'' ""
    #''' '''  """ """

    #ת���
        # \
        # % -->% �� %��ת��
    #�����ַ�
        #\n ���з� \tˮƽ�Ʊ��
        
#print '\\n'
#print '\t'
#print '\\t'
        
        #ռλ��(�ַ����ĸ�ʽ��)
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

    #�ַ����ķ���
        #�ַ������������ַ����ķ�Ƭ��
s = 'hello world'
#print s[0:4] �������ޣ�����������
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
        #�ַ����Ĳ���
            #find ����ָ���ַ���ָ���ַ������е�����λ��������ڷ��ص�һ�γ��ֵ�λ��
                #��������ڣ�����ֵΪ-1
#print s.find('o')
#print s.find('z')
#print s.find('o',5,6)
            #index ����ָ���ַ���ָ���ַ������е�����λ��������ڷ��ص�һ�γ��ֵ�λ��
                #��������ڣ�����
#print s.index('l')
#print s.index('z')
            #count ����ָ���ַ���ָ���ַ������г��ֵĴ���
#print s.count('l')
#print s.count('o',5,8)
#print s.count('z')

s = 'hello world'
        #�ַ��������
            #center ����
#print s.center(30)
#print s.center(30,'*')
#print s.center(30,'a')
            #ljust �����
#print s.ljust(30)
#print s.ljust(30,'0')
            #rjust �Ҷ���
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
        #�ַ�����ɾ��
            #strip Ĭ��ɾ���ַ������˵Ŀհ׷�,�����ɾ������ָ�����ַ�
            #lstripĬ��ɾ���ַ�����˵Ŀհ׷�
            #rstripĬ��ɾ���ַ����Ҷ˵Ŀհ׷�
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

        #�ַ����ı���
            #upper ���ַ�������Сд��ĸת��Ϊ��д
            #lower ���ַ������д�д��ĸת��ΪСд
            #title ��������ĸ��д
            #capitalize �ַ�������ĸ��д
            #swapcase ��Сд����

s = 'Hello World'

#print s.upper()
#print s.lower()

a = 'dfaDFfafdd hDFello woGBrld'
#print a.title()
#print a.capitalize()
#print a.swapcase()
        #�ַ�����ƴ��
            #join
            #+
            #* �ظ�
#print s.join('abc')
#print 'nihao' + 'python'
#print 'http://127.0.0.1:8000/' + 'appserv/conf' + '?page=3'
#print 'hello' * 3

        #�ַ������з�
            #split Ĭ�ϰ��հ׷������ҽ����з֣�Ҳ������ָ���ַ��з�
            #rspilt Ĭ�ϰ��հ׷����ҵ�������з֣�Ҳ������ָ���ַ��з�
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
        #�ַ������ж�
            #isalnum �ж��ַ����Ƿ���ȫ��������ĸ���
#print a.isalnum()
#print b.isalnum()
#print c.isalnum()
#print d.isalnum()
            #isalpha �ж��ַ����Ƿ���ȫ����ĸ���
#print b.isalpha()
#print d.isalpha()
            #isdigit �ж��ַ����Ƿ���ȫ���������
#print b.isdigit()
#print d.isdigit()
#print e.isdigit()

            #isupper �ж��ַ����Ƿ���ȫ�ɴ�д��ĸ���
#print 'PYTHON'.isupper()
            #islower �ж��ַ����Ƿ���ȫ��Сд��ĸ���
#print 'python'.islower()
            #isspace �ж��ַ����Ƿ���ȫ�ɿհ׷����
#print 'hello world'.isspace()
#print '  '.isspace() �ж��ַ����Ƿ����title��ʽ
            #istitle
#print 'Hello Python hi'.istitle()

            #startswith 
            #endswith

#print 'hello'.startswith('o')
#print 'hello'.startswith('hel')
#print 'hello world'.startswith(' ',5,8)
        #�ַ������滻
            #replace
#print 'heollo pytohon'.replace('o','abc')
#print 'heollo pytohon'.replace('o','abc',3)
#print 'heollo pytohon'.replace('o','abc',2)
        #�ַ����ı���
            #encode ����
            #decode ����
#print 'abc'.encode('utf-8')


#python �б�list����Ԫ���������Ű�Χ�ģ�Ԫ��֮���Զ��Ÿ����ģ�����ģ����޸ĵ����С�
    #�б�Ķ���
        #list(�ɵ�������)
        #range()
        #[]

    #�б������
l = [123,456,'abc','hello',['1234','efg',[0]]]
#print l[0]
#a =  l[-1]
#b =  a[-1]
#print b[0]
#print l[-1][-1][0]
    #�б�ķ���
        #�б�Ĳ���
            #count ����ָ��Ԫ����ָ���б��е�����
            #index ����ָ��Ԫ����ָ���б��е�һ�γ��ֵ�����λ
l = ['a','b','c','a',123,1,444,'a']
#print l
#print l.count(5)
#print l.index('a')
#print l.index('a',2,5)
#print l.index('z')
        #�б�����
            #append ׷�ӵ���Ԫ��
            #extend ��Ӷ��Ԫ��
            #insert ��ָ��������λ֮ǰ����ָ����Ԫ��
        #�б������
            #sort ����
            #reverse ������������
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
        #�б��ɾ��
            #pop Ĭ�ϵ������һλ����λ�ϵ�Ԫ��,����Ե���ָ������λ��Ӧ��Ԫ��
            #remove ɾ��ָ����Ԫ��
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
#python Ԫ�飨tuple��:Ԫ����С���Ű�Χ�ġ�Ԫ��֮���Զ��Ÿ���������ģ������޸ĵ����С�










