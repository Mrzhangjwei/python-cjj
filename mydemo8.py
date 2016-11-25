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

#1970.01.01.0.0.0 计算机的纪元时间
#时间戳时间 
#夏令时
#UTC 0时区
#瞬秒

#print time.localtime() 返回time.struct_time格式时间
a = time.localtime(time.time())
#print time.localtime(1000)
#print time.time() 返回当前时间的时间戳时间
#print a[-2]
#print a.tm_yday

#print time.mktime((1997,07,01,0,0,0,0,0,0))将struct_time格式时间转化为时间戳时间
#print time.mktime(time.localtime())

'''
print 'Please waiting for me 3 seconds'
time.sleep(3) 休眠，程序挂起时间
print 'thank you'
'''

#print time.gmtime() 返回零时区的struct_time格式时间
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

#print time.asctime() 把struct_time格式时间转化为asctime格式时间
#print time.asctime(time.localtime())
#print time.asctime((1997,07,01,0,0,0,0,0,0))

#print time.ctime() 把时间戳时间转化为asctime格式时间
#print time.ctime(time.time())
#print time.ctime(10000)

#print time.strftime('%Y-%m-%d %H:%M:%S')
#print time.strftime('%y-%m-%d %I:%M %p')
#print time.strftime('%c')
#print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
#print time.strftime('%Y-%m-%d %H:%M:%S',(2008,07,07,0,0,0,0,0,0))


#python_file 文件操作

#1、open(path,mode,buffering)打开文件
    #path 文件路径 字符串形式
    #mode 权限
        #w 覆盖写
        #a 追加写
        #r 只读
        #rb 二进制的读
        #wb 二进制的写
        #rU 通用换行符的读
        #wU 通用换行符的写
        #r+ w+ 读写双模式
    #buffering 缓存

#open('1.txt','r')

#2、文件处理
    #读
        #read 读全文
        #readline 读一行
        #readlines 以行读全文
    #写
        #write 写字符串
        #writelines 写序列   
    #指针seek
        #第一个参数代表指针移动的相对距离
        #第二个参数
            #0从开头
            #1从当前
            #2从末尾
#f = open('1.txt','r')
#f.seek(100,2)
    #tell返回指针的位置
#3、关闭文件

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

#python处理异常

    #几种常见的异常
        #NameError 
        #TypeError
        #KeyError
        #SyntaxError
        #AttributeError

#捕获异常

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
#诱发异常
    #raise
'''
for i in range(10):
    print i
    raise TypeError('nihao')
'''
