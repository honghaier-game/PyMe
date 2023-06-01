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



def Form_1_onLoad(uiName):
    pass
    pass
    pass
    pass
    pass
    Fun.SetText(uiName,"Entry_3","http://www.baidu.com")
    Webbrowser_5 = Fun.GetElement(uiName,'Webbrowser_5')
    Entry_3_Variable = Fun.G_UIElementVariableArray[uiName]['Entry_3']
    Webbrowser_5.setURLEntryVariable(Entry_3_Variable)
    Button_7 = Fun.GetElement(uiName,'Button_7')
    Button_7.configure(state="disable")
    Button_8 = Fun.GetElement(uiName,'Button_8')
    Button_8.configure(state="disable")
def Entry_3_onButton1(event,uiName,widgetName):
    #Fun.MessageBox("Entry_5_onButton1")
    event.widget.focus_force()
def Button_4_onCommand(uiName,widgetName):
    UrlText = Fun.GetText(uiName,"Entry_3")
    Webbrowser_5 = Fun.GetElement(uiName,'Webbrowser_5')
    Webbrowser_5.set_URL(UrlText)
    Button_7 = Fun.GetElement(uiName,'Button_7')
    Button_7.configure(state="normal")
    Button_8 = Fun.GetElement(uiName,'Button_8')
    Button_8.configure(state="disable")
def Button_7_onCommand(uiName,widgetName):
    Webbrowser_5 = Fun.GetElement(uiName,'Webbrowser_5')
    Webbrowser_5.goBack()
    if Webbrowser_5.cangoBack() == False:
        Button_7 = Fun.GetElement(uiName,'Button_7')
        Button_7.configure(state="disable")
    else:
        Button_7 = Fun.GetElement(uiName,'Button_7')
        Button_7.configure(state="normal")
    if Webbrowser_5.cangoForward() == False:
        Button_8 = Fun.GetElement(uiName,'Button_8')
        Button_8.configure(state="disable")
    else:
        Button_8 = Fun.GetElement(uiName,'Button_8')
        Button_8.configure(state="normal")
def Button_8_onCommand(uiName,widgetName):
    Webbrowser_5 = Fun.GetElement(uiName,'Webbrowser_5')
    Webbrowser_5.goForward()
    if Webbrowser_5.cangoBack() == False:
        Button_7 = Fun.GetElement(uiName,'Button_7')
        Button_7.configure(state="disable")
    else:
        Button_7 = Fun.GetElement(uiName,'Button_7')
        Button_7.configure(state="normal")
    if Webbrowser_5.cangoForward() == False:
        Button_8 = Fun.GetElement(uiName,'Button_8')
        Button_8.configure(state="disable")
    else:
        Button_8 = Fun.GetElement(uiName,'Button_8')
        Button_8.configure(state="normal")
def Button_9_onCommand(uiName,widgetName):
    Webbrowser_5 = Fun.GetElement(uiName,'Webbrowser_5')
    Webbrowser_5.refresh()
def Button_10_onCommand(uiName,widgetName):
    Webbrowser_5 = Fun.GetElement(uiName,'Webbrowser_5')
    Webbrowser_5.gohome()
