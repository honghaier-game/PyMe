#coding=utf-8

#import libs 
import Client_cmd
import Client_sty
import Fun
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Client:
    def __init__(self,root,isTKroot = True):
        className = self.__class__.__name__
        Fun.G_UIElementArray[className]={}
        Fun.G_ElementBindingDataArray[className]={}
        global ElementBGArray
        global ElementBGArray_Resize
        global ElementBGArray_IM
        Fun.AddElement(className,'UIClass',self)
        self.root = root
        style = Client_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            root.geometry("564x296")
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 564,height = 296)
        Form_1.configure(bg = "#efefef")
        Fun.AddElement(className,'root',root)
        Fun.AddElement(className,'Form_1',Form_1)
        #Create the elements of root 
        Label_2= tkinter.Label(root,text="服务器IP",width = 10,height = 4)
        Label_2.place(x = 15,y = 15,width = 69,height = 20)
        Label_2.configure(bg = "#efefef")
        Label_2_Ft