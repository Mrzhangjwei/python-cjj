#coding:gbk

import time

'''
class Myreader():
    def __init__(self,path):
        self.files = open(path,'r')
        self.files.seek(0,2)
        self.all = self.files.tell()
        self.files.seek(0,0)

    def f_page(self):
        for i in range(10):
            print self.files.readline(),
        #print '%s%%'%((self.files.tell() / float(self.all)) * 100)

    def page_num(self):
        return '%s%%'%((self.files.tell() / float(self.all)) * 100)

    def __del__(self):
        self.files.close()
        print 'Bye-Bye'

#a = Myreader('1.txt')
#while True:
    #print a.f_page()
    #time.sleep(3)

if __name__ == '__main__':
    a = Myreader('1.txt')
    while True:
        b = raw_input('%s'%a.page_num() + '>>>')
        if b == 'S':
            a.f_page()
            #a.page_num()
        elif b == 'Z':
            while True:
                a.f_page()
                print a.page_num()
                time.sleep(3)
        elif b == 'exit':
            break
    del a

'''

import time

def myday(y,m,d):
    today = time.time()
    tm = time.struct_time((y,m,d,0,0,0,0,0,0))
    the_time = time.mktime(tm)
    return int((today - the_time)/3600/24)

if __name__ == '__main__':
    a = raw_input('请输入指定时间：')
    b = a.split(',')
    #y = b[0]
    #m = b[1]
    #d = b[2]
    y,m,d = [int(i) for i in b]
    print myday(y,m,d)
  
        
       
