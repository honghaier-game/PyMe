#coding=utf-8
import sys 
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
from PIL import Image
import Fun
def TreeView_2_onButton1(event,uiName,widgetName):
    TreeCtrl = Fun.GetElement(uiName,widgetName)
    item = TreeCtrl.identify("item",event.x,event.y)
    if item is not None and item is not "":
        filename_lower = str(item).lower()
        if filename_lower.find(".png") >= 0 or filename_lower.find(".jpg") >= 0 :
            img= Image.open(filename_lower)
            img.show()
