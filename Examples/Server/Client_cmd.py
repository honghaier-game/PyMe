#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
def Button_8_onCommand(className,widgetName):
  MySocket = Fun.GetUIEle(className,'MySocket_11')
  IPAddr = Fun.GetUIData(className,'Entry_3','IPAddr')
  PORT = Fun.GetUIData(className,'Entry_5','Port')
  MySocket.connServer(IPAddr,PORT)
def Button_9_onCommand(className,widgetName):
  MySocket = Fun.GetUIEle(className,'MySocket_11')
  MsgText = Fun.GetUIText(className,'Entry_7')
  MySocket.sendMessage(MsgText)

