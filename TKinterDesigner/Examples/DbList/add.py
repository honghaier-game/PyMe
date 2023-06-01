#coding=utf-8

#import libs 
import add_cmd
import add_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  add:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        style = add_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(uiName,root,343,247)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 343,height = 247)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'root',root)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Label_2= tkinter.Label(root,text="账号",width = 10,height = 4)
        Fun.Register(uiName,'Label_2',Label_2)
        Label_2.place(x = 50,y = 0,width = 55,height = 34)
        Label_2.configure(relief = "flat")
        Label_2_Ft=tkinter.font.Font(family='System', size=15,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_2.configure(font = Label_2_Ft)
        Label_3= tkinter.Label(root,text="密码",width = 10,height = 4)
        Fun.Register(uiName,'Label_3',Label_3)
        Label_3.place(x = 54,y = 100,width = 54,height = 35)
        Label_3.configure(relief = "flat")
        Label_3_Ft=tkinter.font.Font(family='System', size=15,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_3.configure(font = Label_3_Ft)
        Entry_5_Variable = Fun.AddTKVariable(uiName,'Entry_5','')
        Entry_5= tkinter.Entry(root,textvariable=Entry_5_Variable)
        Fun.Register(uiName,'Entry_5',Entry_5)
        Entry_5.place(x = 129,y = 38,width = 125,height = 36)
        Entry_5.configure(relief = "sunken")
        Entry_6_Variable = Fun.AddTKVariable(uiName,'Entry_6','')
        Entry_6= tkinter.Entry(root,textvariable=Entry_6_Variable)
        Fun.Register(uiName,'Entry_6',Entry_6)
        Entry_6.place(x = 127,y = 100,width = 125,height = 36)
        Entry_6.configure(relief = "sunken")
        Button_8= tkinter.Button(root,text="添加",width = 10,height = 4)
        Fun.Register(uiName,'Button_8',Button_8)
        Button_8.place(x = 103,y = 160,width = 160,height = 48)
        Button_8.configure(command=lambda:add_cmd.Button_8_onCommand(uiName,"Button_8"))
        Button_8_Ft=tkinter.font.Font(family='System', size=15,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_8.configure(font = Button_8_Ft)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = add(root)
    root.mainloop()
