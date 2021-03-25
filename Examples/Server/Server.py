#coding=utf-8

#import libs 
import Server_cmd
import Server_sty
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
class  Server:
    def __init__(self,root,isTKroot = True):
        className = self.__class__.__name__
        Fun.G_UIElementArray[className]={}
        Fun.G_ElementBindingDataArray[className]={}
        global ElementBGArray
        global ElementBGArray_Resize
        global ElementBGArray_IM
        Fun.AddElement(className,'UIClass',self)
        self.root = root
        style = Server_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            root.geometry("543x244")
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 543,height = 244)
        Form_1.configure(bg = "#efefef")
        Fun.AddElement(className,'root',root)
        Fun.AddElement(className,'Form_1',Form_1)
        #Create the elements of root 
        Entry_2_Variable = Fun.AddElementVariable(className,'Entry_2')
        Entry_2= tkinter.Entry(root,textvariable=Entry_2_Variable)
        Entry_2.place(x = 93,y = 20,width = 120,height = 20)
        Entry_2.configure(bg = "#ffffff")
        Entry_2.configure(relief = "sunken")
        Fun.AddUIData(className,'Entry_2','IPAddr','string','127.0.0.1',1)
        Fun.AddElement(className,'Entry_2',Entry_2)
        Label_3= tkinter.Label(root,text="端口",width = 10,height = 4)
        Label_3.place(x = 216,y = 19,width = 74,height = 20)
        Label_3_Ft