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

import DbBase
from DbBase import Cdb
import GridBase
def Button_8_onCommand(uiName,widgetName):
    userId = Fun.GetText(uiName, 'Entry_5')
    passWd = Fun.GetText(uiName, 'Entry_6')
    txt = Fun.GetText('add', 'Button_8')
    if(txt == "修改"):
        item = GridBase.editSelected('DbList', 'TreeView_12',userId,passWd)
        DbBase.editAccountInfo(item[2],userId,passWd)
    else:
        id = DbBase.addAccountInfo(userId,passWd)
        GridBase.addItem('DbList', 'TreeView_12',userId,passWd,id)
    root = Fun.GetElement(uiName, 'root')
    root.destroy()
