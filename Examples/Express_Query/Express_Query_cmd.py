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






import threading
def ThreadCount(param1,param2,param3):
      param1.set_ExpressNumber(param2)
      param1.Query(param3)
def Button_6_onCommand(uiName,widgetName):
  QueryID = Fun.GetText(uiName,'Entry_5')
  Express = Fun.GetElement(uiName,'Express_9')
  ListBox = Fun.GetElement(uiName,'ListBox_7')
  isThread = Fun.GetTKVariable(uiName,"CheckButton_10")
  print(isThread)
  if isThread == True:
      run_thread = threading.Thread(target=ThreadCount, args=[Express,QueryID,ListBox])
      run_thread.start()
  else:
      Express.set_ExpressNumber(QueryID)
      Express.Query(ListBox)
