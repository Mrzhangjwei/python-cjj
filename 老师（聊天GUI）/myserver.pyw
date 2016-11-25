#coding:gbk

import socket,wx,time,thread

class Myserver():
    def __init__(self):
        self.app = wx.App()
        self.frame = wx.Frame(None,title = "服务端")
        self.panel = wx.Panel(self.frame)

        self.chat_con = wx.TextCtrl(self.panel,style = wx.TE_MULTILINE|wx.HSCROLL)

        self.send_con = wx.TextCtrl(self.panel)
        self.chat_send = wx.Button(self.panel,label = "发送")
        self.chat_send.Bind(wx.EVT_BUTTON,self.send)


        self.s_box = wx.BoxSizer()
        self.s_box.Add(self.send_con,proportion = 4,flag = wx.EXPAND|wx.ALL,border = 1)
        self.s_box.Add(self.chat_send,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)

        self.v_box = wx.BoxSizer(wx.VERTICAL)
        self.v_box.Add(self.chat_con,proportion = 8,flag = wx.EXPAND|wx.ALL,border = 1)
        self.v_box.Add(self.s_box,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
    
        self.panel.SetSizer(self.v_box)

    def sock(self):
        self.soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.soc.bind(('',9000))
        self.soc.listen(5)
        self.con,self.add = self.soc.accept()
        
        while True:
            self.recvs = self.con.recv(512)
            if not self.recvs:
                pass
            elif self.recvs == 'esc':
                break
            else:
                self.chat_con.write('客户端' + time.ctime() + '说：\n')
                self.chat_con.write(self.recvs)
                self.chat_con.write('\n')


    def send(self,event):
        self.sends = self.send_con.GetValue()
        if self.sends == 'esc':
            self.chat_con.write('服务端' + time.ctime() + '说:\n')
            self.chat_con.write(u'再见')
            self.con.send('再见')
        else:  
            self.chat_con.write('服务端' + time.ctime() + '说:\n')
            self.chat_con.write(self.sends)
            self.chat_con.write('\n')
            self.con.send(self.sends)
            self.send_con.SetValue('')
        
    def start_new_thread(self):
        thread.start_new_thread(self.sock,())


if __name__ == '__main__':
    mychat = Myserver()
    mychat.start_new_thread()
    mychat.frame.Show()
    mychat.app.MainLoop()
