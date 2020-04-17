#coding=utf-8
import sys
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
from   tkinter import *
import Fun
#Set Element 's BoundingData :Fun.setUIData(Param1：elementName，Param2：DataName，Param3：DataValue)
#Get Element's BoundingData :Fun.getUIData(Param1：elementName，Param2：DataName)
#Set Element 's Attrib :Fun.setUIAttrib(Param1：elementName，Param2：AttribName，Param3：AttribValue)
#Get Element's Attrib :Fun.getUIAttrib(Param1：elementName，Param2：AttribName)
#Get Element:Fun.getUIEle(Param1：elementName)
#Set Element's Text :Fun.setUIText(Param1：elementName,Param2:TextValue)
#Get Element's Text :Fun.getUIText(Param1：elementName)
#Update Element's Input Data Array:Fun.UpdateUIInputDataArray()
def Button_2_onCommand():
  topLevel = tkinter.Toplevel()
  topLevel.attributes("-toolwindow", 1)
  topLevel.wm_attributes("-topmost", 1)
  import RegDlg
  RegDlg.RegDlg(topLevel)
  tkinter.Tk.wait_window(topLevel)
  InputDataArray = RegDlg.Fun.G_UIInputDataArray
  print(InputDataArray)
  print('个人简介:'+InputDataArray['Text_12'][0])
  print('姓名:'+InputDataArray['Entry_5'][0])
  IsMan = InputDataArray['Group_1'][0]
  if IsMan == 1:
    print('性别:男')
  else:
    print('性别:女')
  print('邮箱:'+InputDataArray['Entry_10'][0])

