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








import GridBase
import DbBase
DbBase.initDb()
def Button_8_onCommand(uiName,widgetName):
    topLevel = tkinter.Toplevel()
    topLevel.attributes("-toolwindow", 1)
    topLevel.wm_attributes("-topmost", 1)
    import add
    add.add(topLevel)
    tkinter.Tk.wait_window(topLevel)
def Button_10_onCommand(uiName,widgetName):
    item = GridBase.deleteSelected(uiName, 'TreeView_12')
    if(item == None):
        Fun.MessageBox("请先选择数据,在进行修改!")
        return
    DbBase.deleteAccount(item[2])
def Button_13_onCommand(uiName,widgetName):
    item = GridBase.getSelected(uiName, 'TreeView_12')
    if(item == None):
        Fun.MessageBox("请先选择数据,在进行修改!")
        return
    topLevel = tkinter.Toplevel()
    topLevel.attributes("-toolwindow", 1)
    topLevel.wm_attributes("-topmost", 1)
    import add
    add.add(topLevel)
    #设置修改页的值
    Fun.SetText('add','Entry_5',item[0])
    Fun.SetText('add','Entry_6',item[1])
    Fun.SetText('add', 'Button_8', '修改')
    tkinter.Tk.wait_window(topLevel)
def Button_14_onCommand(uiName,widgetName):
    treeview = GridBase.clearData(uiName,'TreeView_12')
    res = DbBase.getData()
    for item in res:
        treeview.insert('', 'end', values=(item[1], item[2], item[0]))
