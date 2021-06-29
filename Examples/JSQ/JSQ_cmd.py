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


from   tkinter.messagebox import showwarning
def Button_3_onCommand(uiName,widgetName):
  Count = Fun.GetUserData(uiName,'Label_2','Count')
  Count = Count * 10.0 + 1
  Fun.SetUserData(uiName,'Label_2','Count',Count)
def Button_4_onCommand(uiName,widgetName):
  Count = Fun.GetUserData(uiName,'Label_2','Count')
  Count = Count * 10.0 + 2
  Fun.SetUserData(uiName,'Label_2','Count',Count)
def Button_5_onCommand(uiName,widgetName):
  Count = Fun.GetUserData(uiName,'Label_2','Count')
  Count = Count * 10.0 + 3
  Fun.SetUserData(uiName,'Label_2','Count',Count)
def Button_6_onCommand(uiName,widgetName):
  Count = Fun.GetUserData(uiName,'Label_2','Count')
  Count = Count * 10.0 + 4
  Fun.SetUserData(uiName,'Label_2','Count',Count)
def Button_7_onCommand(uiName,widgetName):
  Count = Fun.GetUserData(uiName,'Label_2','Count')
  Count = Count * 10.0 + 5
  Fun.SetUserData(uiName,'Label_2','Count',Count)
def Button_8_onCommand(uiName,widgetName):
  Count = Fun.GetUserData(uiName,'Label_2','Count')
  Count = Count * 10.0 + 6
  Fun.SetUserData(uiName,'Label_2','Count',Count)
def Button_9_onCommand(uiName,widgetName):
  Count = Fun.GetUserData(uiName,'Label_2','Count')
  Count = Count * 10.0 + 7
  Fun.SetUserData(uiName,'Label_2','Count',Count)
def Button_10_onCommand(uiName,widgetName):
  Count = Fun.GetUserData(uiName,'Label_2','Count')
  Count = Count * 10.0 + 8
  Fun.SetUserData(uiName,'Label_2','Count',Count)
def Button_11_onCommand(uiName,widgetName):
  Count = Fun.GetUserData(uiName,'Label_2','Count')
  Count = Count * 10.0 + 9
  Fun.SetUserData(uiName,'Label_2','Count',Count)
def Button_12_onCommand(uiName,widgetName):
  Count = Fun.GetUserData(uiName,'Label_2','Count')
  Count = Count * 10.0
  Fun.SetUserData(uiName,'Label_2','Count',Count)
def Button_13_onCommand(uiName,widgetName):
  Fun.SetUserData(uiName,'Label_2','Count',0.0)
  Fun.SetUserData(uiName,'Label_2','MidCount',0.0)
  Fun.SetUserData(uiName,'Label_2','OpType',0)
def Button_14_onCommand(uiName,widgetName):
  OpType = Fun.GetUserData(uiName,'Label_2','OpType')
  Count = Fun.GetUserData(uiName,'Label_2','Count')
  MidCount = Fun.GetUserData(uiName,'Label_2','MidCount')
  if OpType == 1:
    Count = MidCount  + Count
  elif OpType == 2:
    Count = MidCount  - Count
  elif OpType == 3:
    Count = MidCount  * Count
  elif OpType == 4:
    Count = MidCount / Count
  Fun.SetUserData(uiName,'Label_2','Count',Count)
def Button_15_onCommand(uiName,widgetName):
  MidCount = Fun.GetUserData(uiName,'Label_2','Count')
  Fun.SetUserData(uiName,'Label_2','OpType',1)
  Fun.SetUserData(uiName,'Label_2','MidCount',MidCount)
  Fun.SetUserData(uiName,'Label_2','Count',0.0)
def Button_16_onCommand(uiName,widgetName):
  MidCount = Fun.GetUserData(uiName,'Label_2','Count')
  Fun.SetUserData(uiName,'Label_2','OpType',2)
  Fun.SetUserData(uiName,'Label_2','MidCount',MidCount)
  Fun.SetUserData(uiName,'Label_2','Count',0.0)
def Button_17_onCommand(uiName,widgetName):
  MidCount = Fun.GetUserData(uiName,'Label_2','Count')
  Fun.SetUserData(uiName,'Label_2','OpType',3)
  Fun.SetUserData(uiName,'Label_2','MidCount',MidCount)
  Fun.SetUserData(uiName,'Label_2','Count',0.0)
def Button_18_onCommand(uiName,widgetName):
  MidCount = Fun.GetUserData(uiName,'Label_2','Count')
  Fun.SetUserData(uiName,'Label_2','OpType',4)
  Fun.SetUserData(uiName,'Label_2','MidCount',MidCount)
  Fun.SetUserData(uiName,'Label_2','Count',0.0)
def Menu_A11(uiName,itemName):
  pass
def Menu_B3(uiName,itemName):
    pass
def Menu_B2(uiName,itemName):
  pass
