#coding:gbk
import wx,time
class Myreader():
    def __init__(self):
        self.app = wx.App()
        self.frame = wx.Frame(None,title = "myreader")
        self.panel = wx.Panel(self.frame)

        self.filename = wx.TextCtrl(self.panel)
        self.bt_open = wx.Button(self.panel,label = "open")
        self.bt_open.Bind(wx.EVT_BUTTON,self.op)

        self.s1_box = wx.BoxSizer()
        self.s1_box.Add(self.filename,proportion = 4,flag = wx.EXPAND|wx.ALL,border = 1)
        self.s1_box.Add(self.bt_open,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
        
        self.content = wx.TextCtrl(self.panel,style = wx.TE_MULTILINE|wx.HSCROLL)
        
        self.hand1 = wx.Button(self.panel,label = "手动")
        self.hand1.Bind(wx.EVT_BUTTON,self.shou)
        self.hand2 = wx.Button(self.panel,label = "自动")
        self.hand2.Bind(wx.EVT_BUTTON,self.zi)
        
        self.s2_box = wx.BoxSizer()
        self.s2_box.Add(self.hand1,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
        self.s2_box.Add(self.hand2,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
        
        self.v_box = wx.BoxSizer(wx.VERTICAL)
        self.v_box.Add(self.s1_box,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
        self.v_box.Add(self.content,proportion = 8,flag = wx.EXPAND|wx.ALL,border = 1)
        self.v_box.Add(self.s2_box,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
        
        self.panel.SetSizer(self.v_box)

    def op(self,event):
        self.path = self.filename.GetValue()
        self.f = open(self.path,'r')
        self.f.seek(0,2)
        self.all=self.f.tell()
        self.f.seek(0,0)
        self.content.SetValue(self.f.read(800))
        
    def shou(self,event):
        self.content.SetValue(self.f.read(800))
    def zi(self,event):
        while True: 
            self.content.SetValue(self.f.read(800))
            time.sleep(2)
            if self.f.tell()==self.all:
                break
            
if __name__ == '__main__':
    a = Myreader()
    a.frame.Show()
    a.app.MainLoop()
