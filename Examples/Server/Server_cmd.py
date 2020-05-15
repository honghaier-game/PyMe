#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
def Button_5_onCommand(className,widgetName):
  MySocket = Fun.GetUIEle(className,'MySocket_9')
  IPAddr = Fun.GetUIData(className,'Entry_2','IPAddr')
  PORT = Fun.GetUIData(className,'Entry_4','Port')
  MySocket.createServer(IPAddr,PORT)

