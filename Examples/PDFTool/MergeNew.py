#coding=utf-8

#import libs 
import MergeNew_cmd
import MergeNew_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  MergeNew:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        style = MergeNew_sty.SetupStyle()
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
        Button_2= tkinter.Button(root,text="打开文件夹",width = 10,height = 4)
        Fun.Register(uiName,'Button_2',Button_2)
        Button_2.place(x = 16,y = 15,width = 109,height = 35)
        Button_2.configure(command=lambda:MergeNew_cmd.Button_2_onCommand(uiName,"Button_2"))
        Button_2_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_2.configure(font = Button_2_Ft)
        ListBox_3= tkinter.Listbox(root)
        Fun.Register(uiName,'ListBox_3',ListBox_3)
        ListBox_3.place(x = 16,y = 57,width = 210,height = 215)
        Button_4= tkinter.Button(root,text=">",width = 10,height = 4)
        Fun.Register(uiName,'Button_4',Button_4)
        Button_4.place(x = 241,y = 86,width = 80,height = 28)
        Button_4.configure(command=lambda:MergeNew_cmd.Button_4_onCommand(uiName,"Button_4"))
        Button_4_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_4.configure(font = Button_4_Ft)
        Button_5= tkinter.Button(root,text=">>",width = 10,height = 4)
        Fun.Register(uiName,'Button_5',Button_5)
        Button_5.place(x = 241,y = 132,width = 80,height = 28)
        Button_5.configure(command=lambda:MergeNew_cmd.Button_5_onCommand(uiName,"Button_5"))
        Button_5_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_5.configure(font = Button_5_Ft)
        Button_6= tkinter.Button(root,text="<",width = 10,height = 4)
        Fun.Register(uiName,'Button_6',Button_6)
        Button_6.place(x = 241,y = 178,width = 80,height = 28)
        Button_6.configure(command=lambda:MergeNew_cmd.Button_6_onCommand(uiName,"Button_6"))
        Button_6_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_6.configure(font = Button_6_Ft)
        Button_7= tkinter.Button(root,text="<<",width = 10,height = 4)
        Fun.Register(uiName,'Button_7',Button_7)
        Button_7.place(x = 241,y = 222,width = 80,height = 28)
        Button_7.configure(command=lambda:MergeNew_cmd.Button_7_onCommand(uiName,"Button_7"))
        Button_7_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_7.configure(font = Button_7_Ft)
        ListBox_8= tkinter.Listbox(root)
        Fun.Register(uiName,'ListBox_8',ListBox_8)
        ListBox_8.place(x = 337,y = 59,width = 210,height = 215)
        Entry_9_Variable = Fun.AddTKVariable(uiName,'Entry_9','')
        Entry_9= tkinter.Entry(root,textvariable=Entry_9_Variable)
        Fun.Register(uiName,'Entry_9',Entry_9)
        Entry_9.place(x = 134,y = 293,width = 199,height = 34)
        Entry_9.configure(relief = "sunken")
        Label_10= tkinter.Label(root,text="合并后文件名",width = 10,height = 4)
        Fun.Register(uiName,'Label_10',Label_10)
        Label_10.place(x = 15,y = 298,width = 111,height = 24)
        Label_10.configure(relief = "flat")
        Label_10_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_10.configure(font = Label_10_Ft)
        Button_11= tkinter.Button(root,text="合并",width = 10,height = 4)
        Fun.Register(uiName,'Button_11',Button_11)
        Button_11.place(x = 370,y = 292,width = 115,height = 36)
        Button_11.configure(command=lambda:MergeNew_cmd.Button_11_onCommand(uiName,"Button_11"))
        Button_11_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_11.configure(font = Button_11_Ft)
        Label_12= tkinter.Label(root,text="需要合并的文件列表",width = 10,height = 4)
        Fun.Register(uiName,'Label_12',Label_12)
        Label_12.place(x = 341,y = 22,width = 205,height = 34)
        Label_12.configure(relief = "flat")
        Label_12_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_12.configure(font = Label_12_Ft)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = MergeNew(root)
    root.mainloop()
