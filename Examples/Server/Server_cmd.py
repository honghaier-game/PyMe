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
def Button_6_onCommand(uiName,widgetName):
    MySocket = Fun.GetElement(uiName,'MySocket_11')
    IPAddr = Fun.GetUserData(uiName,'Entry_3','IPAddr')
    PORT = Fun.GetUserData(uiName,'Entry_4','Port')
    MySocket.createServer(IPAddr,PORT)
def Button_8_onCommand(uiName,widgetName):
    MySocket = Fun.GetElement(uiName,'MySocket_11')
    MsgText = Fun.GetText(uiName,'Entry_9')
    ClientIndex = Fun.GetSelectIndex(uiName,'ListBox_10')
    MySocket.sendMessageToClient(ClientIndex,MsgText)
