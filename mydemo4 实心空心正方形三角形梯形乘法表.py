#coding:gbk


#python ���

    #˳��ִ�����
    #����ִ�����
    #ѭ��ִ�����


    #if�ж�

'''
a = 10
if a < 10:
    print 'hello python'
else:
    print 'hello world'
 '''
'''
a = 10

if a < 10:
    print 'hello python'
elif a == 10:
    print 'nihao python'
else:
    print 'hi'
'''

'''
a = 3
if a < 5:
    if a < 3:
        print 'I am not A'
    else:
        print 'ni cuo le'
elif a > 5 and a <= 10:
    print 'hello world'
    '''

'''
if
elif
elif
elif
else
'''

    #for ѭ��(��ѭ������������)

#for ������ in �ɵ�������

'''
for i in range(10):
    print i,
'''
'''
for i in 'abc':
    print i
'''
"""
for i,j in dict(zip('abcdefg',range(10))).items():
    print i,j
for o,k in {'name':'laozhang','age':30}.items():
    print o,k
"""
'''
num = 0
for i in range(1,101):
    num += i
print num
'''
'''
for _ in range(10):
    print 'hello'
'''
'''
a = range(1,10)
b = iter(a)
print b.next()
print b.next()
for _ in range(10):
    print next(b),
'''
'''
if True:
    for i in range(10):
        print i
        break
    #(��ֹѭ��)
else:
    print 'hello'
'''
    #while ѭ��(û�д������ƣ���ѭ��)
'''
a = 20
while a > 10:
    print 'hello'
    break
'''
'''
a = 0
num = 0
while a <= 100:
    num += a
    a += 1
print num
'''  
'''
a = 0
while a <= 100:
    a += 1
    if a % 5 == 0:
        continue
    #����������ѭ����
    else:
        print a,
'''        
#��ȡ���̵�����
    #input ��ȡ���̵�ԭ������
    #raw_input �Ѽ������������ת��Ϊ�ַ���

'''
from random import choice
guess = ['ʯͷ','����','��']
compare = [('ʯͷ','����'),('����','��'),('��','ʯͷ')]
a = []
b = []
while True:
    computer = choice(guess)
    person = raw_input('>>>')
    if (person,computer) in compare:
        print '���Ӯ'
       # a.append('���Ӯ')
    elif (computer,person) in compare: 
        print '�����Ӯ'
        #b.append('�����Ӯ')
    else:
        print 'ƽ��'
    if len(a) >= 2:
        print '���Ӯ'
        break
    elif len(b) >= 2:
        print '�����Ӯ'
        break
'''

'''
com = 10
count = 3
while count:
    person = input('��hai��%s�λ���'%count + '>>>')
    if person > com:
        print '���˴���'
        count -= 1
    elif person < com:
        print '��ѽ��С�ˣ�С��'
        count -= 1
    else:
        print '��ϲ��������������'
        break
'''

'''
from random import shuffle
puke = []
hua = ['heitao','hongtao','meihua','fangpian']
shu = range(2,11) + list('AJQK')
king = ['boss','BOSS']
for i in hua:
    for j in shu:
        puke.append('%s of %s'%(i,j))
for k in king:
    puke.append(i)
shuffle(puke)
a = puke[0::3]
b = puke[1::3]
c = puke[2::3]
print ','.join(a)
print ','.join(b)
print ','.join(c)
print len(a)
print len(b)
print len(c)
'''

'''
#enumerateö�٣����ͳ����ļ���
a = 'abcdefghijklmn'
b = enumerate(a)
for i,j in b:
    print i,j
'''

#��*��ӡһ��ʵ��������
"""
m=""
i=0
s="* * * * * *"
a=s.count('*')
while i<a:
    m=m+s+"""
"""
    i+=1
print m
"""
#��*��ӡһ������������

'''
s="* * * * * *"
a=s.count('*')
b=2*a-3
i=1
while i<=a :
    if i==1 :
        print s
        i+=1
    elif i>1 and i<a :
        print "*"+(" "*b)+"*"
        i+=1
    else :
        print s
        break
'''

#��*��ӡһ��ֱ��������
'''
s="*"+" "
a=input('>>>')
i=1
while i<a:
    print s*i
    i+=1

 '''   
#��*��ӡһ������������
'''
s=" * "
a=input('>>>')
i=1
while i<a :
    m=(" *"*(i-1))+s+("* "*(i-1))
    print m.center(50)
    i+=1
   ''' 
#��*��ӡһ����������
'''
s=' * * '
a=input('>>>')
i=1
while i<a :
    m=(" *"*(i-1))+s+("* "*(i-1))
    print m.center(50)
    i+=1
    '''
#�žų˷�������ͷ���
"""
list=[9,8,7,6,5,4,3,2,1]
for j in range(0,9) :
    for i in range(1,10):
        if i<=list[j] :
            s=i*list[j]
            print '%d*%d=%d'%(i,list[j],s),
    print '''
'''
1*9=9 2*9=18 3*9=27 4*9=36 5*9=45 6*9=54 7*9=63 8*9=72 9*9=81 

1*8=8 2*8=16 3*8=24 4*8=32 5*8=40 6*8=48 7*8=56 8*8=64 

1*7=7 2*7=14 3*7=21 4*7=28 5*7=35 6*7=42 7*7=49 

1*6=6 2*6=12 3*6=18 4*6=24 5*6=30 6*6=36 

1*5=5 2*5=10 3*5=15 4*5=20 5*5=25 

1*4=4 2*4=8 3*4=12 4*4=16 

1*3=3 2*3=6 3*3=9 

1*2=2 2*2=4 

1*1=1
"""
'''              
for j in range(1,10) :
    for i in range(1,10):
        if j>=i :
            print '%d*%d=%d'%(i,j,j*i),
    print '\n'
 '''
'''
1*1=1 

1*2=2 2*2=4 

1*3=3 2*3=6 3*3=9 

1*4=4 2*4=8 3*4=12 4*4=16 

1*5=5 2*5=10 3*5=15 4*5=20 5*5=25 

1*6=6 2*6=12 3*6=18 4*6=24 5*6=30 6*6=36 

1*7=7 2*7=14 3*7=21 4*7=28 5*7=35 6*7=42 7*7=49 

1*8=8 2*8=16 3*8=24 4*8=32 5*8=40 6*8=48 7*8=56 8*8=64 

1*9=9 2*9=18 3*9=27 4*9=36 5*9=45 6*9=54 7*9=63 8*9=72 9*9=81 
            
'''

    

























