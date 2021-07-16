#coding=utf-8
#import libs 
import Merge_cmd
import Merge_sty
import Fun
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Merge:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.G_UIElementArray[uiName]={}
        Fun.G_UIElementUserDataArray[uiName]={}
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        style = Merge_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(None,root,563,375)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 563,height = 375)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'root',root)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Button_3= tkinter.Button(root,text="选择文件1",width = 10,height = 4)
        Button_3.place(x = 20,y = 39,width = 153,height = 46)
        Button_3.configure(command=lambda:Merge_cmd.Button_3_onCommand(uiName,"Button_3"))
        Button_3_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_3.configure(font = Button_3_Ft)
        Fun.Register(uiName,'Button_3',Button_3)
        Entry_4_Variable = Fun.AddTKVariable(uiName,'Entry_4','')
        Entry_4= tkinter.Entry(root,textvariable=Entry_4_Variable)
        Entry_4.place(x = 174,y = 43,width = 364,height = 42)
        Entry_4.configure(relief = "sunken")
        Fun.Register(uiName,'Entry_4',Entry_4)
        Button_5= tkinter.Button(root,text="选择文件2",width = 10,height = 4)
        Button_5.place(x = 20,y = 88,width = 153,height = 44)
        Button_5.configure(command=lambda:Merge_cmd.Button_5_onCommand(uiName,"Button_5"))
        Button_5_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_5.configure(font = Button_5_Ft)
        Fun.Register(uiName,'Button_5',Button_5)
        Entry_6_Variable = Fun.AddTKVariable(uiName,'Entry_6','')
        Entry_6= tkinter.Entry(root,textvariable=Entry_6_Variable)
        Entry_6.place(x = 174,y = 90,width = 363,height = 41)
        Entry_6.configure(relief = "sunken")
        Fun.Register(uiName,'Entry_6',Entry_6)
        Button_7= tkinter.Button(root,text="合并以上两个文件",width = 10,height = 4)
        Button_7.place(x = 171,y = 151,width = 230,height = 46)
        Button_7.configure(command=lambda:Merge_cmd.Button_7_onCommand(uiName,"Button_7"))
        Button_7_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_7.configure(font = Button_7_Ft)
        Fun.Register(uiName,'Button_7',Button_7)
        Label_8= tkinter.Label(root,text="选择文件合并:",width = 10,height = 4)
        Label_8.place(x = 20,y = 7,width = 181,height = 30)
        Label_8.configure(relief = "flat")
        Label_8_Ft=tkinter.font.Font(family='System', size=20,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_8.configure(font = Label_8_Ft)
        Fun.Register(uiName,'Label_8',Label_8)
        Label_9= tkinter.Label(root,text="按照文件夹合并",width = 10,height = 4)
        Label_9.place(x = 20,y = 213,width = 195,height = 40)
        Label_9.configure(relief = "flat")
        Label_9_Ft=tkinter.font.Font(family='System', size=20,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_9.configure(font = Label_9_Ft)
        Fun.Register(uiName,'Label_9',Label_9)
        Button_10= tkinter.Button(root,text="选择文件夹:",width = 10,height = 4)
        Button_10.place(x = 19,y = 253,width = 153,height = 46)
        Button_10.configure(command=lambda:Merge_cmd.Button_10_onCommand(uiName,"Button_10"))
        Button_10_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_10.configure(font = Button_10_Ft)
        Fun.Register(uiName,'Button_10',Button_10)
        Entry_11_Variable = Fun.AddTKVariable(uiName,'Entry_11','')
        Entry_11= tkinter.Entry(root,textvariable=Entry_11_Variable)
        Entry_11.place(x = 174,y = 255,width = 364,height = 42)
        Entry_11.configure(relief = "sunken")
        Fun.Register(uiName,'Entry_11',Entry_11)
        Button_12= tkinter.Button(root,text="合并文件夹内所有文件",width = 10,height = 4)
        Button_12.place(x = 168,y = 312,width = 234,height = 48)
        Button_12.configure(command=lambda:Merge_cmd.Button_12_onCommand(uiName,"Button_12"))
        Button_12_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_12.configure(font = Button_12_Ft)
        Fun.Register(uiName,'Button_12',Button_12)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)
#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Merge(root)
    root.mainloop()
