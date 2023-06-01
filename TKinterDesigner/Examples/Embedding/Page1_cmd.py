#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
def Button_11_onCommand(uiName,widgetName):
    name = Fun.GetText(uiName,'Entry_3')
    gender = Fun.GetTKVariable(uiName,'Group_1')
    if gender  == 1:
        gender  ='男'
    else:
        gender  ='女'   
    age = Fun.GetText(uiName,'Entry_8')
    combobox = Fun.GetElement(uiName,'ComboBox_10')
    address=combobox.get()
    treeview = Fun.GetElement('TabPage1','TreeView_2')
    treeview.insert('','end',values=(name,gender,age,address))
    Fun.SetText(uiName,'Entry_3','')
    Fun.SetTKVariable(uiName,'Group_1',1)
    Fun.SetText(uiName,'Entry_8',0)
    combobox.current(0)
