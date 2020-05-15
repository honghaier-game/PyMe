#coding=utf-8
import sys
import tkinter
from   tkinter import *
import Fun

def Button_13_onCommand(className,widgetName):
  root = Fun.GetUIEle(className,'root')
  UIInputDataArray = Fun.UpdateUIInputDataArray(className)
  # print(UIInputDataArray)
  root.destroy()
def Button_14_onCommand(className,widgetName):
  root = Fun.GetUIEle(className,'root')
  root.destroy()