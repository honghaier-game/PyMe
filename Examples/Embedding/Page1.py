#coding=utf-8

#import libs 
import Page1_cmd
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
class  Page1:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        if isTKroot == True:
            root.title("Form1")
            root.geometry("574x150")
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 574,height = 150)
        Form_1.configure(bg = "#efefef")
        Fun.Register(uiName,'Form_1',Form_1)
        Group_1_Variable = Fun.AddTKVariable(uiName,'Group_1')
        Group_1_Variable.set(1)
        #Create the elements of root 
        Label_2= tkinter.Label(root,text="姓名",width = 10,height = 4)
        Label_2.place(x = 18,y = 13,width = 82,height = 20)
        Fun.Register(uiName,'Label_2',Label_2)
        Entry_3_Variable = Fun.AddTKVariable(uiName,'Entry_3')
        Entry_3= tkinter.Entry(root,textvariable=Entry_3_Variable)
        Entry_3.place(x = 120,y = 14,width = 120,height = 20)
        Entry_3.configure(relief = "sunken")
        Fun.Register(uiName,'Entry_3',Entry_3)
        Label_4= tkinter.Label(root,text="性别",width = 10,height = 4)
        Label_4.place(x = 18,y = 44,width = 82,height = 20)
        Fun.Register(uiName,'Label_4',Label_4)
        RadioButton_5= tkinter.Radiobutton(root,variable=Group_1_Variable,value=1,text="男",anchor=tkinter.W)
        RadioButton_5.place(x = 116,y = 45,width = 68,height = 19)
        Fun.Register(uiName,'RadioButton_5',RadioButton_5,None,'Group_1')
        RadioButton_6= tkinter.Radiobutton(root,variable=Group_1_Variable,value=2,text="女",anchor=tkinter.W)
        RadioButton_6.place(x = 191,y = 44,width = 100,height = 20)
        Fun.Register(uiName,'RadioButton_6',RadioButton_6,None,'Group_1')
        Label_7= tkinter.Label(root,text="年龄",width = 10,height = 4)
        Label_7.place(x = 18,y = 78,width = 82,height = 20)
        Fun.Register(uiName,'Label_7',Label_7)
        Entry_8_Variable = Fun.AddTKVariable(uiName,'Entry_8')
        Entry_8= tkinter.Entry(root,textvariable=Entry_8_Variable)
        Entry_8.place(x = 121,y = 75,width = 120,height = 20)
        Entry_8.configure(relief = "sunken")
        Fun.Register(uiName,'Entry_8',Entry_8)
        Label_9= tkinter.Label(root,text="地址",width = 10,height = 4)
        Label_9.place(x = 18,y = 110,width = 82,height = 20)
        Fun.Register(uiName,'Label_9',Label_9)
        ComboBox_10_Variable = Fun.AddTKVariable(uiName,'ComboBox_10')
        ComboBox_10= tkinter.ttk.Combobox(root,textvariable=ComboBox_10_Variable, state="readonly")
        ComboBox_10.place(x = 120,y = 110,width = 124,height = 20)
        ComboBox_10.configure(state = "readonly")
        ComboBox_10["values"]=['北京','天津','上海']
        ComboBox_10.current(0)
        Fun.Register(uiName,'ComboBox_10',ComboBox_10)
        Button_11= tkinter.Button(root,text="增加",width = 10,height = 4)
        Button_11.place(x = 448,y = 103,width = 100,height = 28)
        Button_11.configure(command=lambda:Page1_cmd.Button_11_onCommand(uiName,"Button_11"))
        Fun.Register(uiName,'Button_11',Button_11)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)

#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Page1(root)
    root.mainloop()
