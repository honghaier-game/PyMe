import tkinter
import tkinter.ttk
import os
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
        import BrowserFrame
        self.WebFrame = BrowserFrame.BrowserFrame(frame)
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
        self.set_URL("http://www.baidu.com")
        self.URLEntryVariable.set("http://www.baidu.com")
    #设置Frame
    def resetSize(self,W,H):
        self.Width = W
        self.Height = H
        if self.WebFrame != None:
            self.WebFrame.place(x=0,y=0,width=W,height=H)