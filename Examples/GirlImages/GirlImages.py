#coding=utf-8
#import libs 
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import GirlImages_cmd
import GirlImages_sty
import Fun
import os
import LeftTreeBar
import RightTextBar
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  GirlImages:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        style = GirlImages_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(uiName,root,820,660)
            root['background'] = '#efefef'
            root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 820,height = 660)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'root',root)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Label_2= tkinter.Label(root,text="网址",width = 10,height = 4)
        Fun.Register(uiName,'Label_2',Label_2)
        Label_2.place(x = 10,y = 2,width = 50,height = 24)
        Label_2.configure(relief = "flat")
        Entry_3_Variable = Fun.AddTKVariable(uiName,'Entry_3','')
        Entry_3= tkinter.Entry(root,textvariable=Entry_3_Variable)
        Fun.Register(uiName,'Entry_3',Entry_3)
        Entry_3.place(x = 60,y = 2,width = 500,height = 24)
        Entry_3.configure(relief = "sunken")
        Label_4= tkinter.Label(root,text="最大数量",width = 10,height = 4)
        Fun.Register(uiName,'Label_4',Label_4)
        Label_4.place(x = 560,y = 2,width = 60,height = 24)
        Label_4.configure(relief = "flat")
        Entry_5_Variable = Fun.AddTKVariable(uiName,'Entry_5','')
        Entry_5= tkinter.Entry(root,textvariable=Entry_5_Variable)
        Fun.Register(uiName,'Entry_5',Entry_5)
        Entry_5.place(x = 620,y = 2,width = 70,height = 24)
        Entry_5.configure(relief = "sunken")
        Button_6= tkinter.Button(root,text="开始",width = 10,height = 4)
        Fun.Register(uiName,'Button_6',Button_6)
        Button_6.place(x = 710,y = 2,width = 50,height = 24)
        Button_6.configure(command=lambda:GirlImages_cmd.Button_6_onCommand(uiName,"Button_6"))
        Button_7= tkinter.Button(root,text="停止",width = 10,height = 4)
        Fun.Register(uiName,'Button_7',Button_7)
        Button_7.place(x = 770,y = 2,width = 50,height = 24)
        Button_7.configure(command=lambda:GirlImages_cmd.Button_7_onCommand(uiName,"Button_7"))
        PanedWindow_8= tkinter.PanedWindow(root)
        Fun.Register(uiName,'PanedWindow_8',PanedWindow_8)
        PanedWindow_8.place(x = 0,y = 30,width = 871,height = 610)
        PanedWindow_8.configure(orient = tkinter.HORIZONTAL)
        PanedWindow_8.configure(showhandle = "0")
        PanedWindow_8.configure(sashrelief = "flat")
        PanedWindow_8.configure(sashwidth = "4")
        PanedWindow_8_child1= tkinter.Canvas(PanedWindow_8,bg="#FFDD94",name="child1")
        PanedWindow_8_child1.place(x = 1,y = 1,width = 261,height = 608)
        LeftTreeBar.LeftTreeBar(PanedWindow_8_child1,False)
        PanedWindow_8.add(PanedWindow_8_child1,width =261)
        PanedWindow_8_child2= tkinter.Canvas(PanedWindow_8,bg="#D0E6A5",name="child2")
        Fun.Register(uiName,'PanedWindow_8_child1',PanedWindow_8_child1)
        Fun.Register(uiName,'PanedWindow_8_child2',PanedWindow_8_child2)
        PanedWindow_8_child2.place(x = 266,y = 1,width = 604,height = 608)
        RightTextBar.RightTextBar(PanedWindow_8_child2,False)
        PanedWindow_8.add(PanedWindow_8_child2,width =604)
        Fun.Register(uiName,'PanedWindow_8_child1',PanedWindow_8_child1)
        Fun.Register(uiName,'PanedWindow_8_child2',PanedWindow_8_child2)
        Label_9= tkinter.Label(root,text="Label",width = 10,height = 4)
        Fun.Register(uiName,'Label_9',Label_9)
        Label_9.place(x = 0,y = 640,width = 820,height = 20)
        Label_9.configure(relief = "flat")
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        GirlImages_cmd.Form_1_onLoad(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)

    def Configure(self,event):
        if self.root == event.widget:
            PanedWindow_8 = Fun.GetElement(self.__class__.__name__,'PanedWindow_8')
            Label_9 = Fun.GetElement(self.__class__.__name__,'Label_9')
            PanedWindow_8.place(x = 0,y = 50,width = event.width,height = event.height - 51 - 20)
            Label_9.place(x = 0,y = event.height - 20,width = event.width,height = 20)

#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = GirlImages(root)
    root.mainloop()
