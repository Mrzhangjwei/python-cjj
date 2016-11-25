#coding:gbk

#进程：程序的一次运行，又称为重量级进程
#线程：进程下的分支，又称为轻量级进程

#异步并发
    #时间片

#全局解释器锁（锁机制）

from time import ctime,sleep

'''
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
    loop0()
    loop1()
    print 'all done at:',ctime()

if __name__ == '__main__':
    main()
'''
import thread,threading

'''
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

'''
loops = [4,2] #不但确定了线程和锁的个数，还确定了线程挂起的时间

def loop(nloop,nsec,lock):
    print 'start loop',nloop,'at:',ctime()
    sleep(nsec)
    print 'loop',nloop,'done at:',ctime()
    lock.release()

def main():
    print 'starting at:',ctime()
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop,(i,loops[i],locks[i]))
    sleep(4)
    print 'all done at:',ctime()

if __name__ == '__main__':
    main()
                                
'''

'''
loops = [4,2]
def loop(nloop,nsec):
    print 'start loop',nloop,'at:',ctime()
    sleep(nsec)
    print 'loop',nloop,'done at:',ctime()

def main():
    print 'starting at:',ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target = loop,args = (i,loops[i]))
        threads.append(t)        
    for i in nloops:
        threads[i].start()
        #threads[i].setName('xiaowang')
        #print threads[i].getName()
        #print threads[i].isAlive()
    for i in nloops:
        threads[i].join()
    for i in nloops:
        #print threads[i].isAlive()
    print 'all done at:',ctime()

if __name__ == '__main__':
    main()
'''
'''
class Mythread(threading.Thread):
    def __init__(self,nloop,nsec):
        threading.Thread.__init__(self)
        self.nloop = nloop
        self.nsec = nsec
        
    def run(self):
        print 'start loop',self.nloop,'at:',ctime()
        sleep(self.nsec)
        print 'loop',self.nloop,'done at:',ctime()

if __name__ == '__main__':
    loops = [4,2]
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = Mythread(i,loops[i])
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
'''
'''

import re
import time
import threading

start_time = time.time()

f = open('C:\Users\guozheng\Desktop\data.txt','r')
allchars = f.read()
re_object = re.compile("\d{11}")
print len(allchars) / 10

def find_phone_number(start,stop,re_object):
    print "function find count :%s"%len(re.findall(re_object,allchars[start:stop+1]))

threads = []
for x in range(10):
    step = len(allchars) / 10
    start = step * x 
    stop = start + step
    t = threading.Thread(target = find_phone_number,args=(start,stop,re_object ))
    threads.append(t)
    prinmain():
    print 'startt step,start,stop

for i in range(10):
    threads[i].start()
for i in range(10):
    threads[i].join()
    
f.close()
stop_time = time.time()
total_time = stop_time - start_time

print "total_time:%s"%total_time  
'''

#hpython 队列

import Queue

#队列模式
    #先进先出 Queue.Queue(maxsize),如果maxsize < 1,代表队列无限长
    #先进后出 Queue.LifoQueue
    #优先级别低的先出 Queue.PriorityQueue
'''
q = Queue.Queue()
for i in range(10):
    q.put(i)

print q.get()
print q.get()
print q.get()

'''
'''
q = Queue.LifoQueue()
for i in range(10):
    q.put(i)

print q.get()
print q.get()
print q.get()
'''
'''
q = Queue.Queue(5)
for i in range(10):
    print q.empty()
    print 'q.qsize:',q.qsize()
    q.put(i)
    print q.qsize()
    print q.full()
'''
'''
q = Queue.Queue(0)
for i in range(10):
    print 'q.qsize:',q.qsize()
    q.put(i)
    print q.qsize()
'''
'''
import random

q = Queue.Queue(0)
workers_num = 3

class Mythread(threading.Thread):
    def __init__(self,input,worktype):
        threading.Thread.__init__(self)
        self.jobq = input
        self.worktype = worktype

    def run(self):
        while True:
            if self.jobq.qsize() > 0:
                job = self.jobq.get()
                worktype = self.worktype
                self.process_job(job,worktype)
            else:
                break
    def process_job(self,job,worktype):
        self.dojob(job)
    def dojob(self,job):
        sleep(random.random()*3)
        print 'doing...',job

if __name__ == '__main__':
    print 'begin...'
    for i in range(workers_num * 2):
        q.put(i)
    print "jobq'size",q.qsize()
    for j in range(workers_num):
        Mythread(q,j).start()
    
'''
