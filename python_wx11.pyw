#coding:gbk


#1��ѹ������ѹ����CMD�У���Ŀ¼�л�����ѹĿ¼�ҵ�setup.py ��python setup.py install
#2��.exe
#3��pip install MySQLdb

import wx

'''
app = wx.App()  #ʵ����һ����ѭ��
frame = wx.Frame(None) #ʵ����һ��ͼ�λ��������
frame.Show() #���ô����������ʾ����
app.MainLoop() #������ѭ��
'''
'''
app = wx.App()
frame = wx.Frame(None)

frame.Show() 
app.MainLoop()
'''
#Frame �������
    #parent ��������������ΪNone����������Ϊ�������
    #id ����ı�ţ�������ı�ʶ��ͬһ���ڵ��в��ܳ���id��ͬ�����
        #���id = -1 ������ϵͳ�Զ�����id�š�
    #title ���ڵı���
    #pos  ���ڵ�λ�ã���Ҫһ��˫Ԫ��Ԫ�飬�γ�����ϵ�����涨���ھ���;��ϵľ��롣
    #size ���ڵĴ�С����Ҫһ��˫Ԫ��Ԫ�飬���涨���ڵĳ��͸�
    #style �������ʽ
    #name 

#Button ��ť
    #label��ǩ����ť�ϵ�����

#TextCtrl�ı������
    #value ֵ����������������
'''
import wx
app = wx.App()
win = wx.Frame(None,title = 'simple Editor',size = (410,335))
win.Show()
bt1 = wx.Button(win,label = "open",pos = (225,5),size = (80,25))
bt2 = wx.Button(win,label = "save",pos = (315,5),size = (80,25))

filename = wx.TextCtrl(win,pos = (5,5),size = (210,25))
content = wx.TextCtrl(win,pos = (5,35),size = (390,260),style = wx.TE_MULTILINE|wx.HSCROLL)
app.MainLoop()
'''
#�ߴ�������BoxSizer
    #panel ���������ڵ�����
    #1�������ߴ���wx.BoxSizer()
        #Ĭ��Ϊˮƽ�ߴ���
        #wx.VERTICAL
    #2��������Add
        #proportion ����
        #flag ���
            #������ʽ
                #wx.EXPAND
            #���ķ��� -->����ı߿�
                #wx.TOP
                #wx.BOTTOM
                #wx.LEFT
                #wx.RIGHT
                #wx.ALL
        #border

    #3���������ߴ���
        #SetSizer

#���¼�
    #Bind
    #event
    #GetValue ��ȡֵ
    #Setvalue ����ֵ


import wx

def op(event):
    path = filename.GetValue()
    f = open(path,'r')
    content.SetValue(f.read())
    f.close()

def sa(event):
    path = filename.GetValue()
    f = open(path,'a')
    f.write(content.GetValue())
    f.close()
    
app = wx.App()
win = wx.Frame(None,title = 'simple Editor')
panel = wx.Panel(win)


bt1 = wx.Button(panel,label = "open")
bt1.Bind(wx.EVT_BUTTON,op)

bt2 = wx.Button(panel,label = "save")
bt2.Bind(wx.EVT_BUTTON,sa)

filename = wx.TextCtrl(panel)

s_box = wx.BoxSizer()
s_box.Add(filename,proportion = 10,flag = wx.EXPAND|wx.ALL,border = 1)
s_box.Add(bt1,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
s_box.Add(bt2,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)

content = wx.TextCtrl(panel,style = wx.TE_MULTILINE|wx.HSCROLL)

v_box = wx.BoxSizer(wx.VERTICAL)
v_box.Add(s_box,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
v_box.Add(content,proportion = 9,flag = wx.EXPAND|wx.ALL,border = 1)

panel.SetSizer(v_box)
win.Show()
app.MainLoop()

