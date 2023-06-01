#coding=utf-8
import sys
import tkinter
from   tkinter import *
import Fun
def Button_13_onCommand(uiName,widgetName):
  root = Fun.GetElement(uiName,'root')
  UIInputDataArray = Fun.GetInputDataArray(uiName)
  # print(UIInputDataArray)
  root.destroy()
def Button_14_onCommand(uiName,widgetName):
  root = Fun.GetElement(uiName,'root')
  root.destroy()