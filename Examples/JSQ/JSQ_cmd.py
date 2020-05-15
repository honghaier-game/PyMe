#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
from   tkinter.messagebox import showwarning

def Button_3_onCommand(className,widgetName):
  Count = Fun.GetUIData(className,'Label_2','Count')
  Count = Count * 10.0 + 1
  Fun.SetUIData(className,'Label_2','Count',Count)


def Button_4_onCommand(className,widgetName):
  Count = Fun.GetUIData(className,'Label_2','Count')
  Count = Count * 10.0 + 2
  Fun.SetUIData(className,'Label_2','Count',Count)



def Button_5_onCommand(className,widgetName):
  Count = Fun.GetUIData(className,'Label_2','Count')
  Count = Count * 10.0 + 3
  Fun.SetUIData(className,'Label_2','Count',Count)



def Button_6_onCommand(className,widgetName):
  Count = Fun.GetUIData(className,'Label_2','Count')
  Count = Count * 10.0 + 4
  Fun.SetUIData(className,'Label_2','Count',Count)



def Button_7_onCommand(className,widgetName):
  Count = Fun.GetUIData(className,'Label_2','Count')
  Count = Count * 10.0 + 5
  Fun.SetUIData(className,'Label_2','Count',Count)



def Button_8_onCommand(className,widgetName):
  Count = Fun.GetUIData(className,'Label_2','Count')
  Count = Count * 10.0 + 6
  Fun.SetUIData(className,'Label_2','Count',Count)



def Button_9_onCommand(className,widgetName):
  Count = Fun.GetUIData(className,'Label_2','Count')
  Count = Count * 10.0 + 7
  Fun.SetUIData(className,'Label_2','Count',Count)



def Button_10_onCommand(className,widgetName):
  Count = Fun.GetUIData(className,'Label_2','Count')
  Count = Count * 10.0 + 8
  Fun.SetUIData(className,'Label_2','Count',Count)



def Button_11_onCommand(className,widgetName):
  Count = Fun.GetUIData(className,'Label_2','Count')
  Count = Count * 10.0 + 9
  Fun.SetUIData(className,'Label_2','Count',Count)



def Button_12_onCommand(className,widgetName):
  Count = Fun.GetUIData(className,'Label_2','Count')
  Count = Count * 10.0
  Fun.SetUIData(className,'Label_2','Count',Count)
  


def Button_13_onCommand(className,widgetName):
  Fun.SetUIData(className,'Label_2','Count',0.0)
  Fun.SetUIData(className,'Label_2','MidCount',0.0)
  Fun.SetUIData(className,'Label_2','OpType',0)

def Button_14_onCommand(className,widgetName):
  OpType = Fun.GetUIData(className,'Label_2','OpType')
  Count = Fun.GetUIData(className,'Label_2','Count')
  MidCount = Fun.GetUIData(className,'Label_2','MidCount')
  if OpType == 1:
    Count = MidCount  + Count
  elif OpType == 2:
    Count = MidCount  - Count
  elif OpType == 3:
    Count = MidCount  * Count
  elif OpType == 4:
    Count = MidCount / Count
  Fun.SetUIData(className,'Label_2','Count',Count)


def Button_15_onCommand(className,widgetName):
  MidCount = Fun.GetUIData(className,'Label_2','Count')
  Fun.SetUIData(className,'Label_2','OpType',1)
  Fun.SetUIData(className,'Label_2','MidCount',MidCount)
  Fun.SetUIData(className,'Label_2','Count',0.0)


def Button_16_onCommand(className,widgetName):
  MidCount = Fun.GetUIData(className,'Label_2','Count')
  Fun.SetUIData(className,'Label_2','OpType',2)
  Fun.SetUIData(className,'Label_2','MidCount',MidCount)
  Fun.SetUIData(className,'Label_2','Count',0.0)


def Button_17_onCommand(className,widgetName):
  MidCount = Fun.GetUIData(className,'Label_2','Count')
  Fun.SetUIData(className,'Label_2','OpType',3)
  Fun.SetUIData(className,'Label_2','MidCount',MidCount)
  Fun.SetUIData(className,'Label_2','Count',0.0)


def Button_18_onCommand(className,widgetName):
  MidCount = Fun.GetUIData(className,'Label_2','Count')
  Fun.SetUIData(className,'Label_2','OpType',4)
  Fun.SetUIData(className,'Label_2','MidCount',MidCount)
  Fun.SetUIData(className,'Label_2','Count',0.0)


def Menu_A11(className,itemName):
  pass
def Menu_B2(className,itemName):
  pass
