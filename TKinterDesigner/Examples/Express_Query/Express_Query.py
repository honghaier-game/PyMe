#coding=utf-8

#import libs 
import Express_Query_cmd
import Express_Query_sty
import Fun
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
sys.path.append("D:/TKinterDesigner/Sample/Express")
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Express_Query:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        style = Express_Query_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(uiName,root,432,283)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 432,height = 283)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'root',root)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Label_2= tkinter.Label(root,text="快递公司",width = 10,height = 4)
        Fun.Register(uiName,'Label_2',Label_2)
        Label_2.place(x = 11,y = 15,width = 75,height = 20)
        Label_2.configure(relief = "flat")
        ComboBox_3_Variable = Fun.AddTKVariable(uiName,'ComboBox_3')
        ComboBox_3= tkinter.ttk.Combobox(root,textvariable=ComboBox_3_Variable, state="readonly")
        Fun.Register(uiName,'ComboBox_3',ComboBox_3)
        ComboBox_3.place(x = 107,y = 15,width = 173,height = 20)
        ComboBox_3.configure(state = "readonly")
        Label_4= tkinter.Label(root,text="快递单号",width = 10,height = 4)
        Fun.Register(uiName,'Label_4',Label_4)
        Label_4.place(x = 11,y = 55,width = 75,height = 20)
        Label_4.configure(relief = "flat")
        Entry_5_Variable = Fun.AddTKVariable(uiName,'Entry_5','')
        Entry_5= tkinter.Entry(root,textvariable=Entry_5_Variable)
        Fun.Register(uiName,'Entry_5',Entry_5)
        Entry_5.place(x = 107,y = 56,width = 172,height = 20)
        Entry_5.configure(relief = "sunken")
        Button_6= tkinter.Button(root,text="查询",width = 10,height = 4)
        Fun.Register(uiName,'Button_6',Button_6)
        Button_6.place(x = 297,y = 53,width = 100,height = 28)
        Button_6.configure(command=lambda:Express_Query_cmd.Button_6_onCommand(uiName,"Button_6"))
        ListBox_7= tkinter.Listbox(root)
        Fun.Register(uiName,'ListBox_7',ListBox_7)
        ListBox_7.place(x = 24,y = 101,width = 372,height = 160)
        import Express
        Express_9=Express.Express()
        #Express_9.xy(151,69)
        Express_9.set_CompanyID('4')
        Express_9.set_ExpressNumber('0000001')
        Express_9.set_ComboBox(ComboBox_3)
        Fun.Register(uiName,'Express_9',Express_9)
        CheckButton_10_Variable = Fun.AddTKVariable(uiName,'CheckButton_10')
        CheckButton_10_Variable.set(False)
        CheckButton_10= tkinter.Checkbutton(root,variable=CheckButton_10_Variable,text="多线程查询",anchor=tkinter.W)
        Fun.Register(uiName,'CheckButton_10',CheckButton_10)
        CheckButton_10.place(x = 302,y = 20,width = 100,height = 20)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Express_Query(root)
    root.mainloop()
