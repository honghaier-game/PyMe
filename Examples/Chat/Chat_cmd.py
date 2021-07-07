#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 



from Common import CSelectServerManger
from Common import CClientSocketManger
def Button_6_onCommand(uiName,widgetName):
    ip=Fun.GetText(uiName,"Entry_3")
    port=Fun.GetText(uiName,"Entry_5")
    if(len(ip) <= 0 or len(port) <=0):
        CSelectServerManger.startService()
    else:
        CSelectServerManger.startService(ip, port)
def Button_7_onCommand(uiName,widgetName):
    #root=Fun.GetElement(uiName,"root")
    #root.destroy()
    isOk = CSelectServerManger.stopService()
    if(isOk):
        listBox = Fun.GetElement(uiName, "ListBox_8")
        listBox.insert(tkinter.END, "Server has been stopped!")
def Button_11_onCommand(uiName,widgetName):
    ip = Fun.GetText(uiName, "Entry_3")
    port = Fun.GetText(uiName, "Entry_5")
    if (len(ip) <= 0 or len(port) <= 0):
        CClientSocketManger.startService()
    else:
        CClientSocketManger.startService(ip, port)
def Button_13_onCommand(uiName,widgetName):
    msg = Fun.GetText(uiName, "Entry_10")
    service = CClientSocketManger.getService()
    if(service == None):
        Fun.MessageBox("连接已经关闭，不能发送消息！")
    else:
        service.sendMessage(msg)
