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
def Button_2_onCommand(uiName,widgetName):
  topLevel = tkinter.Toplevel()
  topLevel.attributes("-toolwindow", 1)
  topLevel.wm_attributes("-topmost", 1)
  import RegDlg
  RegDlg.RegDlg(topLevel)
  tkinter.Tk.wait_window(topLevel)
  InputDataArray = Fun.G_UIInputDataArray
  print(InputDataArray)
  print('个人简介:'+InputDataArray['Text_12'][0])
  print('姓名:'+InputDataArray['Entry_5'][0])
  IsMan = InputDataArray['Group_1'][0]
  if IsMan == 1:
    print('性别:男')
  else:
    print('性别:女')
  print('邮箱:'+InputDataArray['Entry_10'][0])

