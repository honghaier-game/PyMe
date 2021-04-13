#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
def Form_1_onLoad(className):
    pass
    pass
    pass
    pass
    pass
    Fun.SetUIText(className,"Entry_3","http://www.baidu.com")
    Webbrowser_5 = Fun.GetUIEle(className,'Webbrowser_5')
    Entry_3_Variable = Fun.G_UIElementVariableArray[className]['Entry_3']
    Webbrowser_5.setURLEntryVariable(Entry_3_Variable)
    Button_7 = Fun.GetUIEle(className,'Button_7')
    Button_7.configure(state="disable")
    Button_8 = Fun.GetUIEle(className,'Button_8')
    Button_8.configure(state="disable")
def Entry_3_onButton1(event,className,widgetName):
    #Fun.MessageBox("Entry_5_onButton1")
    event.widget.focus_force()
def Button_4_onCommand(className,widgetName):
    UrlText = Fun.GetUIText(className,"Entry_3")
    Webbrowser_5 = Fun.GetUIEle(className,'Webbrowser_5')
    Webbrowser_5.set_URL(UrlText)
    Button_7 = Fun.GetUIEle(className,'Button_7')
    Button_7.configure(state="normal")
    Button_8 = Fun.GetUIEle(className,'Button_8')
    Button_8.configure(state="disable")
def Button_7_onCommand(className,widgetName):
    Webbrowser_5 = Fun.GetUIEle(className,'Webbrowser_5')
    Webbrowser_5.goBack()
    if Webbrowser_5.cangoBack() == False:
        Button_7 = Fun.GetUIEle(className,'Button_7')
        Button_7.configure(state="disable")
    else:
        Button_7 = Fun.GetUIEle(className,'Button_7')
        Button_7.configure(state="normal")
    if Webbrowser_5.cangoForward() == False:
        Button_8 = Fun.GetUIEle(className,'Button_8')
        Button_8.configure(state="disable")
    else:
        Button_8 = Fun.GetUIEle(className,'Button_8')
        Button_8.configure(state="normal")
def Button_8_onCommand(className,widgetName):
    Webbrowser_5 = Fun.GetUIEle(className,'Webbrowser_5')
    Webbrowser_5.goForward()
    if Webbrowser_5.cangoBack() == False:
        Button_7 = Fun.GetUIEle(className,'Button_7')
        Button_7.configure(state="disable")
    else:
        Button_7 = Fun.GetUIEle(className,'Button_7')
        Button_7.configure(state="normal")
    if Webbrowser_5.cangoForward() == False:
        Button_8 = Fun.GetUIEle(className,'Button_8')
        Button_8.configure(state="disable")
    else:
        Button_8 = Fun.GetUIEle(className,'Button_8')
        Button_8.configure(state="normal")
def Button_9_onCommand(className,widgetName):
    Webbrowser_5 = Fun.GetUIEle(className,'Webbrowser_5')
    Webbrowser_5.refresh()
def Button_10_onCommand(className,widgetName):
    Webbrowser_5 = Fun.GetUIEle(className,'Webbrowser_5')
    Webbrowser_5.gohome()
