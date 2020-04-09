#coding=utf-8
import sys
import tkinter
from   tkinter import *
import Fun

from   tkinter.messagebox import showwarning
G_VarArray={'Count':0}
G_UIElementArray={}
G_TempCount = 0.0
G_OpType = 0
#Set Element 's BoundingData :Fun.setUIData(Param1：elementName，Param2：DataName，Param3：DataValue)
#Get Element's BoundingData :Fun.getUIData(Param1：elementName，Param2：DataName)
#Set Element 's Attrib :Fun.setUIAttrib(Param1：elementName，Param2：AttribName，Param3：AttribValue)
#Get Element's Attrib :Fun.getUIAttrib(Param1：elementName，Param2：AttribName)
#Get Element:Fun.getUIEle(Param1：elementName)
#Set Element's Text :Fun.setUIText(Param1：elementName,Param2:TextValue)
#Get Element's Text :Fun.getUIText(Param1：elementName)
def Button_3_onCommand():
  count =Fun.getUIData('Label_2','Count')
  count = count * 10.0 + 1
  Fun.setUIData('Label_2','Count',count)



def Button_4_onCommand():
  count =Fun.getUIData('Label_2','Count')
  count = count * 10.0 + 2
  Fun.setUIData('Label_2','Count',count)



def Button_5_onCommand():
  count =Fun.getUIData('Label_2','Count')
  count = count * 10.0 + 3
  Fun.setUIData('Label_2','Count',count)



def Button_6_onCommand():
  count =Fun.getUIData('Label_2','Count')
  count = count * 10.0 + 4
  Fun.setUIData('Label_2','Count',count)



def Button_7_onCommand():
  count =Fun.getUIData('Label_2','Count')
  count = count * 10.0 + 5
  Fun.setUIData('Label_2','Count',count)



def Button_8_onCommand():
  count =Fun.getUIData('Label_2','Count')
  count = count * 10.0 + 6
  Fun.setUIData('Label_2','Count',count)



def Button_9_onCommand():
  count =Fun.getUIData('Label_2','Count')
  count = count * 10.0 + 7
  Fun.setUIData('Label_2','Count',count)



def Button_10_onCommand():
  count =Fun.getUIData('Label_2','Count')
  count = count * 10.0 + 8
  Fun.setUIData('Label_2','Count',count)



def Button_11_onCommand():
  count =Fun.getUIData('Label_2','Count')
  count = count * 10.0 + 9
  Fun.setUIData('Label_2','Count',count)



def Button_12_onCommand():
  count =Fun.getUIData('Label_2','Count')
  count = count * 10.0
  Fun.setUIData('Label_2','Count',count)
  


def Button_13_onCommand():
  Fun.setUIData('Label_2','Count',0.0)



def Button_14_onCommand():
  global G_TempCount
  global G_OpType
  count =Fun.getUIData('Label_2','Count')
  if G_OpType == 1:
    count = G_TempCount  + count
  elif G_OpType == 2:
    count = G_TempCount  - count
  elif G_OpType == 3:
    count = G_TempCount  * count
  elif G_OpType == 4:
    count = G_TempCount / count
  Fun.setUIData('Label_2','Count',count)



def Button_15_onCommand():
  global G_OpType
  global G_TempCount
  G_TempCount =Fun.getUIData('Label_2','Count')
  G_OpType = 1
  Fun.setUIData('Label_2','Count',0.0)


def Button_16_onCommand():
  global G_OpType
  G_TempCount =Fun.getUIData('Label_2','Count')
  G_OpType = 2
  Fun.setUIData('Label_2','Count',0.0)


def Button_17_onCommand():
  global G_OpType
  G_TempCount =Fun.getUIData('Label_2','Count')
  G_OpType = 3
  Fun.setUIData('Label_2','Count',0.0)


def Button_18_onCommand():
  global G_OpType
  G_TempCount =Fun.getUIData('Label_2','Count')
  G_OpType = 4
  Fun.setUIData('Label_2','Count',0.0)


def Menu_A11():
  pass
def Menu_B2():
  pass
