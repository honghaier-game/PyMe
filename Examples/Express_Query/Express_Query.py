#coding=utf-8

#import libs 
import Express_Query_cmd
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
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Express_Query:
    def __init__(self,root,isTKroot = True):
        className = self.__class__.__name__
        Fun.G_UIElementArray[className]={}
        Fun.G_ElementBindingDataArray[className]={}
        global ElementBGArray
        global ElementBGArray_Resize
        global ElementBGArray_IM
        Fun.AddElement(className,'UIClass',self)
        self.root = root
        if isTKroot == True:
            root.title("Form1")
            root.geometry("432x283")
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 432,height = 283)
        Form_1.configure(bg = "#efefef")
        Fun.AddElement(className,'root',root)
        Fun.AddElement(className,'Form_1',Form_1)
        #Create the elements of root 
        Label_2= tkinter.Label(root,text="快递公司",width = 10,height = 4)
        Label_2.place(x = 11,y = 15,width = 75,height = 20)
        Fun.AddElement(className,'Label_2',Label_2)
        ComboBox_3_Variable = Fun.AddElementVariable(className,'ComboBox_3')
        ComboBox_3= tkinter.ttk.Combobox(root,textvariable=ComboBox_3_Variable, state="readonly")
        ComboBox_3.place(x = 107,y = 15,width = 173,height = 20)
        ComboBox_3.configure(state = "readonly")
        Fun.AddElement(className,'ComboBox_3',ComboBox_3)
        Label_4= tkinter.Label(root,text="快递单号",width = 10,height = 4)
        Label_4.place(x = 11,y = 55,width = 75,height = 20)
        Fun.AddElement(className,'Label_4',Label_4)
        Entry_5_Variable = Fun.AddElementVariable(className,'Entry_5')
        Entry_5= tkinter.Entry(root,textvariable=Entry_5_Variable)
        Entry_5.place(x = 107,y = 56,width = 172,height = 20)
        Entry_5.configure(relief = "sunken")
        Fun.AddElement(className,'Entry_5',Entry_5)
        Button_6= tkinter.Button(root,text="查询",width = 10,height = 4)
        Button_6.place(x = 297,y = 53,width = 100,height = 28)
        Button_6.configure(command=lambda:Express_Query_cmd.Button_6_onCommand(className,"Button_6"))
        Fun.AddElement(className,'Button_6',Button_6)
        ListBox_7= tkinter.Listbox(root)
        ListBox_7.place(x = 24,y = 101,width = 372,height = 160)
        Fun.AddElement(className,'ListBox_7',ListBox_7)
        import Express
        Express_9=Express.Express()
        #Express_9.xy(186,74)
        Express_9.set_CompanyID('4')
        Express_9.set_ExpressNumber('0000001')
        Express_9.set_ComboBox(ComboBox_3)
        Fun.AddElement(className,'Express_9',Express_9)
        CheckButton_10_Variable = Fun.AddElementVariable(className,'CheckButton_10')
        CheckButton_10_Variable.set(False)
        CheckButton_10= tkinter.Checkbutton(root,variable=CheckButton_10_Variable,text="多线程查询",anchor=tkinter.W)
        CheckButton_10.place(x = 302,y = 20,width = 100,height = 20)
        Fun.AddElement(className,'CheckButton_10',CheckButton_10)
        #Inital all element's Data 
        Fun.InitElementData(className)
        #Add Some Logic Code Here: (Keep This Line of comments)

#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Express_Query(root)
    root.mainloop()
