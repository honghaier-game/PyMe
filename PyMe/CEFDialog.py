
# -- coding=utf8 --
import os
import sys
import platform
import tkinter
import tkinter.messagebox
import tkinter.ttk
import ctypes
import json
import socket
from cefpython3 import cefpython as cef
ThisDialog = None
TargetURL = "http://www.py-me.com"
if len(sys.argv) > 1:
    TargetURL = sys.argv[1]
WINDOWS = (platform.system() == "Windows")
#用于嵌入浏览器
class Visitor(object):
    def SetCallBack(self,callback):
        self.callback = callback

    def Visit(self, value):
        #print(value)
        if self.callback:
            self.callback(value)
#Frame中的浏览器
class BrowserFrame(tkinter.ttk.Frame):
    def __init__(self, master, navigation_bar=None):
        try:
            cef.Initialize()
            self.navigation_bar = navigation_bar
            self.closing = False
            self.browser = None
            self.URL = "http://www.py-me.com"
            self.stringVisitor = Visitor()
            tkinter.ttk.Frame.__init__(self, master)
            self.bind("<Configure>", self.on_configure)
            print("BrowserFrame")
        except Exception as ex:
            tkinter.messagebox.showwarning("__init__",str(ex))
    def setURL(self,url):
        self.URL = url
        try:
            if self.browser:
                self.browser.LoadUrl(self.URL)
                print("setURL:"+self.URL)
        except Exception as ex:
            tkinter.messagebox.showwarning("setURL",str(ex))
    def getSourceCode(self):
        if self.browser:
            try:
                #获取源码
                mainFrame = self.browser.GetMainFrame()
                winhandle = self.get_window_handle()
                if mainFrame and winhandle:
                    mainFrame.GetSource(self.stringVisitor)
            except Exception as ex:
                tkinter.messagebox.showwarning("getSourceCode",str(ex))
        return self.stringVisitor    
    def embed_browser(self,width,heith):
        try:
            window_info = cef.WindowInfo()
            rect = [0, 0, width, heith]
            window_info.SetAsChild(self.get_window_handle(), rect)
            self.browser = cef.CreateBrowserSync(window_info,url=self.URL)
            assert self.browser
            self.message_loop_work()
        except Exception as ex:
            tkinter.messagebox.showwarning("embed_browser",str(ex))

    def get_window_handle(self):
        if self.winfo_id() > 0:
            return self.winfo_id()
        else:
            raise Exception("Couldn't obtain window handle")
    def message_loop_work(self):
        try:
            cef.MessageLoopWork()
            self.after(10, self.message_loop_work)
        except Exception as ex:
            tkinter.messagebox.showwarning("message_loop_work",str(ex))
    def on_configure(self,event):
        try:
            print("on_configure")
            if not self.browser:
                print("embed_browser")
                self.embed_browser(event.width,event.height)
            else:
                print("on_mainframe_configure")
                self.on_mainframe_configure(event.width,event.height)
        except Exception as ex:
            tkinter.messagebox.showwarning("on_configure",str(ex))
    def on_root_configure(self):
        try:
            if self.browser:
                self.browser.NotifyMoveOrResizeStarted()
        except Exception as ex:
            tkinter.messagebox.showwarning("on_root_configure",str(ex))
    def on_mainframe_configure(self, width, height):
        try:
            if self.browser:
                ctypes.windll.user32.SetWindowPos(self.browser.GetWindowHandle(), 0, 0, 0, width, height, 0x0002)
                self.browser.NotifyMoveOrResizeStarted()
        except Exception as ex:
            tkinter.messagebox.showwarning("on_mainframe_configure",str(ex))
    def on_focus_in(self, _):
        if self.browser:
            self.browser.SetFocus(True)
    def on_focus_out(self, _):
        if self.browser:
            self.browser.SetFocus(False)
    def on_root_close(self):
        if self.browser:
            self.browser.CloseBrowser(True)
            self.clear_browser_references()
        self.destroy()
        cef.Shutdown()
        ThisDialog.destroy()
    def clear_browser_references(self):
        self.browser = None
#WEB浏览器控件
class   Webbrowser:
    def __init__(self):
        self.URL = ""
        self.URLArray = []
        self.URLIndex = -1
        self.WebFrame = None
        self.URLEntryVariable = None
        self.thread = None
        self.Width = 1000
        self.Height = 600
        print("Webbrowser")
    #设置Entry
    def setURLEntryVariable(self,entrytextvariable):
        print("set_Entry")
        self.URLEntryVariable = entrytextvariable
    #设置Frame
    def set_Frame(self,frame):
        print("set_Frame")
        self.WebFrame = BrowserFrame(frame)
    #设置URL
    def set_URL(self,url):
        if self.URL != url:
            self.URL = url
            self.URLArray.append(url)
            self.URLIndex = self.URLIndex + 1
            print("set_URL:%d"%(self.URLIndex))
            print(self.URLArray)
            if self.WebFrame != None:
                self.WebFrame.setURL(self.URL)
    #获取源代码
    def getSourceCode(self):
        if self.WebFrame != None:
            return self.WebFrame.getSourceCode()
        return None
    #后退       
    def goBack(self):
        print("goBack:%d"%(self.URLIndex))
        if self.WebFrame != None:
            if self.URLIndex > 0:
               self.URLIndex = self.URLIndex - 1
               url = self.URLArray[self.URLIndex]
               print(url)
               self.WebFrame.setURL(url)
               self.URLEntryVariable.set(url)
    #是否可以后退
    def cangoBack(self):
        if self.URLIndex > 0:
            return True
        return False
    #前进
    def goForward(self):
        print("GoForward:%d"%(self.URLIndex))
        if self.WebFrame != None:
            if self.URLIndex < len(self.URLArray)-1:
               self.URLIndex = self.URLIndex + 1
               url = self.URLArray[self.URLIndex]
               print(url)
               self.WebFrame.setURL(url)
               self.URLEntryVariable.set(url)
    #是否可以后退
    def cangoForward(self):
        if self.URLIndex < len(self.URLArray)-1:
            return True
        return False
    #刷新
    def refresh(self):
        print("refresh:%d"%(self.URLIndex))
        if self.WebFrame != None:
            self.WebFrame.setURL(self.URLArray[self.URLIndex])
    #主页 
    def gohome(self):
        print("gohome:%d"%(self.URLIndex))
        self.set_URL("www.py-me.com")
        self.URLEntryVariable.set("www.py-me.com")
    #设置Frame
    def resetSize(self,W,H):
        self.Width = W
        self.Height = H
        if self.WebFrame != None:
            self.WebFrame.place(x=0,y=0,width=W,height=H)


ThisDialog = tkinter.Tk()
#ThisDialog.wm_overrideredirect(1)
ThisDialog.attributes("-toolwindow", 1)
ThisDialog.title("微信登录PyMe") 
ThisDialog.resizable(0,0) 
ThisDialog.attributes("-topmost", 1)
ThisDialog.config(bg='#000000')
Form = tkinter.Canvas(ThisDialog,bg = '#FFFFFF',width = 340,height=360,highlightthickness=0,bd=0)
Form.pack(expand=1, fill='both')
QRCodeWebbrowser = Webbrowser()
QRCodeLabel = tkinter.Frame(Form,bg = '#FFFFFF',width = 100,height = 200)
QRCodeLabel.place(x = 20,y = 50,width = 300,height = 300)   
QRCodeWebbrowser.set_Frame(QRCodeLabel)
QRCodeWebbrowser.set_URL(TargetURL)
QRCodeWebbrowser.resetSize(300,300)


#检测源代码
def CheckSourceCode(code):
    global ThisDialog
    if code.find('login_success.png') > 0:
        title_begin = code.find('<title>')
        title_end = code.find('</title>')
        title_text = code[title_begin+7:title_end]
        title_splitarray = title_text.split(',')
        userid = title_splitarray[0]
        wechat_nickname = title_splitarray[1].replace('\'','"')
        wechat_token = title_splitarray[2].replace('\'','"')
        client = socket.socket()
        client.connect(('localhost',9656))
        data = userid + "," +wechat_nickname+","+wechat_token
        client.send(data.encode('utf-8'))
        client.close()
        ThisDialog.destroy()

#检查登录成功
def CheckLoginSuccess():
    global ThisDialog
    sourceCode = QRCodeWebbrowser.getSourceCode()
    sourceCode.SetCallBack(CheckSourceCode)
    ThisDialog.after(3,CheckLoginSuccess)

ThisDialog.after(3,CheckLoginSuccess)
#居中显示
sx = 0
sy = 0
sw = ThisDialog.winfo_screenwidth()
sh = ThisDialog.winfo_screenheight()
nx = sx + (sw - 340)/2
ny = sy + (sh - 360)/2
geoinfo = str('%dx%d+%d+%d'%(340,360,nx,ny))
ThisDialog.geometry(geoinfo)  
ThisDialog.mainloop()
