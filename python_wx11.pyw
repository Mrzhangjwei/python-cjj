#coding:gbk


#1、压缩包解压，在CMD中，把目录切换到解压目录找到setup.py ，python setup.py install
#2、.exe
#3、pip install MySQLdb

import wx

'''
app = wx.App()  #实例化一个主循环
frame = wx.Frame(None) #实例化一个图形化窗口组件
frame.Show() #调用窗口组件的显示功能
app.MainLoop() #启动主循环
'''
'''
app = wx.App()
frame = wx.Frame(None)

frame.Show() 
app.MainLoop()
'''
#Frame 窗口组件
    #parent 父组件，如果设置为None，代表该组件为顶级组件
    #id 组件的编号，对组件的标识，同一窗口当中不能出现id相同的组件
        #如果id = -1 ，代表系统自动分配id号。
    #title 窗口的标题
    #pos  窗口的位置，需要一个双元素元组，形成坐标系，来规定窗口距左和距上的距离。
    #size 窗口的大小，需要一个双元素元组，来规定窗口的长和高
    #style 组件的样式
    #name 

#Button 按钮
    #label标签，按钮上的内容

#TextCtrl文本输入框
    #value 值，输入框里面的内容
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
#尺寸器布局BoxSizer
    #panel 画布，窗口的容器
    #1、创建尺寸器wx.BoxSizer()
        #默认为水平尺寸器
        #wx.VERTICAL
    #2、添加组件Add
        #proportion 比例
        #flag 填充
            #填充的样式
                #wx.EXPAND
            #填充的方向 -->组件的边框
                #wx.TOP
                #wx.BOTTOM
                #wx.LEFT
                #wx.RIGHT
                #wx.ALL
        #border

    #3、声明主尺寸器
        #SetSizer

#绑定事件
    #Bind
    #event
    #GetValue 获取值
    #Setvalue 设置值


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

