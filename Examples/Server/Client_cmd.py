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
def Button_8_onCommand(uiName,widgetName):
    MySocket = Fun.GetElement(uiName,'MySocket_12')
    IPAddr = Fun.GetUserData(uiName,'Entry_3','IPAddr')
    PORT = Fun.GetUserData(uiName,'Entry_5','Port')
    MySocket.connServer(IPAddr,PORT)
def Button_9_onCommand(uiName,widgetName):
    MySocket = Fun.GetElement(uiName,'MySocket_12')
    MsgText = Fun.GetText(uiName,'Entry_7')
    MySocket.sendMessage(MsgText)
