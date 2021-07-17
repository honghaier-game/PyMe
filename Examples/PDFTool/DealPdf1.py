#coding=utf-8

#import libs 
import DealPdf1_cmd
import DealPdf1_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  DealPdf1:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        style = DealPdf1_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(uiName,root,563,375)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 563,height = 375)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'root',root)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Button_3= tkinter.Button(root,text="选择文件：",width = 10,height = 4)
        Fun.Register(uiName,'Button_3',Button_3)
        Button_3.place(x = 16,y = 14,width = 105,height = 38)
        Button_3.configure(command=lambda:DealPdf1_cmd.Button_3_onCommand(uiName,"Button_3"))
        Button_3_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_3.configure(font = Button_3_Ft)
        Entry_4_Variable = Fun.AddTKVariable(uiName,'Entry_4','')
        Entry_4= tkinter.Entry(root,textvariable=Entry_4_Variable)
        Fun.Register(uiName,'Entry_4',Entry_4)
        Entry_4.place(x = 124,y = 14,width = 426,height = 38)
        Entry_4.configure(relief = "sunken")
        Label_5= tkinter.Label(root,text="总页数",width = 10,height = 4)
        Fun.Register(uiName,'Label_5',Label_5)
        Label_5.place(x = 17,y = 61,width = 100,height = 30)
        Label_5.configure(relief = "flat")
        Label_5_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_5.configure(font = Label_5_Ft)
        Entry_6_Variable = Fun.AddTKVariable(uiName,'Entry_6','')
        Entry_6= tkinter.Entry(root,textvariable=Entry_6_Variable)
        Fun.Register(uiName,'Entry_6',Entry_6)
        Entry_6.place(x = 125,y = 56,width = 120,height = 35)
        Entry_6.configure(relief = "sunken")
        Entry_6.configure(state = "disabled")
        Label_7= tkinter.Label(root,text="拆分格式如下，请按照格式填写！将按照输入的页数分隔文件！",width = 10,height = 4)
        Fun.Register(uiName,'Label_7',Label_7)
        Label_7.place(x = 19,y = 103,width = 481,height = 31)
        Label_7.configure(relief = "flat")
        Label_7_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_7.configure(font = Label_7_Ft)
        Entry_8_Variable = Fun.AddTKVariable(uiName,'Entry_8','')
        Entry_8= tkinter.Entry(root,textvariable=Entry_8_Variable)
        Fun.Register(uiName,'Entry_8',Entry_8)
        Entry_8.place(x = 16,y = 141,width = 366,height = 38)
        Entry_8.configure(relief = "sunken")
        Button_12= tkinter.Button(root,text="拆分",width = 10,height = 4)
        Fun.Register(uiName,'Button_12',Button_12)
        Button_12.place(x = 386,y = 141,width = 163,height = 38)
        Button_12.configure(command=lambda:DealPdf1_cmd.Button_12_onCommand(uiName,"Button_12"))
        Button_12_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_12.configure(font = Button_12_Ft)
        ListBox_13= tkinter.Listbox(root)
        Fun.Register(uiName,'ListBox_13',ListBox_13)
        ListBox_13.place(x = 15,y = 233,width = 530,height = 120)
        Label_14= tkinter.Label(root,text="拆分进度:",width = 10,height = 4)
        Fun.Register(uiName,'Label_14',Label_14)
        Label_14.place(x = 16,y = 203,width = 85,height = 28)
        Label_14.configure(relief = "flat")
        Label_14_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_14.configure(font = Label_14_Ft)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        DealPdf1_cmd.Form_1_onLoad(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = DealPdf1(root)
    root.mainloop()
