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
    #������
    #������
    #������

    #���������
        # + - * / ** //(�ذ��������) ==(ֵ���) is(ȫ��)
        #+= -= *= /= %(ȡ��)
        
#a = 10 (=��ֵ)
#a += 10 ---> a = a + 10
        
#python ��һ�����������ԣ��������ü����ɣ�������������ֵ��������������


#python �ַ���(str):Ԫ�������Ű�Χ������
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
        #�ַ������������ַ�������Ƭ��
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

#s = '   hello world,I am xiaoli.   '
#a = 'ooooohello worldooooo'
        #�ַ�����ɾ��
            #strip Ĭ��ɾ���ַ������˵Ŀհ׷�,�����ɾ������ָ�����ַ�
            #lstripĬ��ɾ���ַ�����˵Ŀհ׷�
           #rstripĬ��ɾ���ַ����Ҷ˵Ŀհ׷�
s='   jjjabcdjajjbjjj    '
#print s.lstrip()
print s.strip('j')
#print a.strip('o') 
#print a.lstrip('o')
#print s.rstrip()


