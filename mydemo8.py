#coding:gbk

'''
import random
code = []
for i in range(6):
    if i == random.randint(0,2):
        code.append(str(random.randint(0,9)))
    elif i == random.randint(2,4):
        code.append(chr(random.randint(65,90)))
    else:
        code.append(chr(random.randint(97,122)))
print ''.join(code)
'''

#python_time
import time

#1970.01.01.0.0.0 ������ļ�Ԫʱ��
#ʱ���ʱ�� 
#����ʱ
#UTC 0ʱ��
#˲��

#print time.localtime() ����time.struct_time��ʽʱ��
a = time.localtime(time.time())
#print time.localtime(1000)
#print time.time() ���ص�ǰʱ���ʱ���ʱ��
#print a[-2]
#print a.tm_yday

#print time.mktime((1997,07,01,0,0,0,0,0,0))��struct_time��ʽʱ��ת��Ϊʱ���ʱ��
#print time.mktime(time.localtime())

'''
print 'Please waiting for me 3 seconds'
time.sleep(3) ���ߣ��������ʱ��
print 'thank you'
'''

#print time.gmtime() ������ʱ����struct_time��ʽʱ��
#print time.localtime()
#print time.gmtime(10000)

'''
if __name__ == '__main__':
    time.sleep(1)
    print 'clock1:%s'%time.clock()
    time.sleep(2)
    print 'clock2:%s'%time.clock()
    time.sleep(3)
    print 'clock3:%s'%time.clock()
'''

#print time.asctime() ��struct_time��ʽʱ��ת��Ϊasctime��ʽʱ��
#print time.asctime(time.localtime())
#print time.asctime((1997,07,01,0,0,0,0,0,0))

#print time.ctime() ��ʱ���ʱ��ת��Ϊasctime��ʽʱ��
#print time.ctime(time.time())
#print time.ctime(10000)

#print time.strftime('%Y-%m-%d %H:%M:%S')
#print time.strftime('%y-%m-%d %I:%M %p')
#print time.strftime('%c')
#print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
#print time.strftime('%Y-%m-%d %H:%M:%S',(2008,07,07,0,0,0,0,0,0))


#python_file �ļ�����

#1��open(path,mode,buffering)���ļ�
    #path �ļ�·�� �ַ�����ʽ
    #mode Ȩ��
        #w ����д
        #a ׷��д
        #r ֻ��
        #rb �����ƵĶ�
        #wb �����Ƶ�д
        #rU ͨ�û��з��Ķ�
        #wU ͨ�û��з���д
        #r+ w+ ��д˫ģʽ
    #buffering ����

#open('1.txt','r')

#2���ļ�����
    #��
        #read ��ȫ��
        #readline ��һ��
        #readlines ���ж�ȫ��
    #д
        #write д�ַ���
        #writelines д����   
    #ָ��seek
        #��һ����������ָ���ƶ�����Ծ���
        #�ڶ�������
            #0�ӿ�ͷ
            #1�ӵ�ǰ
            #2��ĩβ
#f = open('1.txt','r')
#f.seek(100,2)
    #tell����ָ���λ��
#3���ر��ļ�

   #close
'''
f = open('2.txt','r')
#print f.read()
print f.read(10)
f.close()
'''
'''
f = open('2.txt','r')
#print f.readline()
print f.readline(10)
f.close()
'''
'''
f = open('2.txt','r')
print f.readlines()
f.close()
'''
'''
f = open('2.txt','w')
f.write('hello world')
f.close()
'''
'''
f = open('2.txt','a')
f.write('nihao')
f.close()
'''
'''
f = open('3.txt','a')
#f.write('abcdefghijklmn')
#f.write("['A','B','C']")
#f.writelines('[123,456]')
#f.writelines("'123'")
f.close()
'''
'''
f = open('3.txt','r')
#f.seek(10)
#f.seek(10,1)
f.seek(20,2)
print f.read(20)
print f.tell()
f.close()
'''
'''
f = open('1.txt','r')
f.seek(0,2)
print f.tell()
f.close()
'''
'''
f = open('1.xls','w')
for i in range(1,10):
    for j in range(1,i + 1):
        f.write('%s*%s = %-3s'%(j,i,j*i))
    f.write('\n')
f.close()
'''

#python�����쳣

    #���ֳ������쳣
        #NameError 
        #TypeError
        #KeyError
        #SyntaxError
        #AttributeError

#�����쳣

'''
try:
    input('>>>') + 'abc'
    print 'nihao'
except:
    print 'hello'
'''
'''
try:
    input('>>>') + 'abc'
except Exception,e:
    #print Exception
    print e
'''
'''
try:
    input('>>>') + 'abc'
except NameError:
    print 'hello'
except TypeError:
    print 'nihao'
'''
'''
try:
    input('>>>') + 'abc'
except NameError:
    print 'nihao'   
except TypeError:
    print 'hello python'
finally:
    print 'Bye-Bye'
'''
'''
try:
    input('>>>') + 'abc'
except TypeError:
    print 'nihao'   
else:
    print 'hello python'
finally:
    print 'Bye-Bye'
'''
#�շ��쳣
    #raise
'''
for i in range(10):
    print i
    raise TypeError('nihao')
'''
