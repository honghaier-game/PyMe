#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
def Button_11_onCommand(className,widgetName):
    name = Fun.GetUIText(className,'Entry_3')
    gender = Fun.GetElementVariable(className,'Group_1')
    if gender  == 1:
        gender  ='男'
    else:
        gender  ='女'   
    age = Fun.GetUIText(className,'Entry_8')
    combobox = Fun.GetUIEle(className,'ComboBox_10')
    address=combobox.get()
    treeview = Fun.GetUIEle('TabPage1','TreeView_2')
    treeview.insert('','end',values=(name,gender,age,address))
    Fun.SetUIText(className,'Entry_3','')
    Fun.SetElementVariable(className,'Group_1',1)
    Fun.SetUIText(className,'Entry_8',0)
    combobox.current(0)
