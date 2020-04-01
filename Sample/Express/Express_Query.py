#coding=utf-8

#import libs 
import Express_Query_cmd
import Fun
import sys
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

#Add your Varial Here: (Keep This Line of comments)
#Create the root of Kinter 
root = tkinter.Tk()
root.title("Form1")
Form_1= tkinter.Canvas(root,width = 10,height = 4)
Form_1.place(x = 0,y = 0,width = 422,height = 279)
Form_1.configure(bg = "#efefef")
root.geometry("422x279")
#Create the elements of root 
Label_2= tkinter.Label(root,text="快递公司",width = 10,height = 4)
Label_2.place(x = 11,y = 15,width = 75,height = 20)
Fun.G_UIElementArray['Label_2']=Label_2
Fun.G_UIElementVariableArray['ComboBox_3']=tkinter.IntVar()
ComboBox_3= tkinter.ttk.Combobox(root,textvariable=Fun.G_UIElementVariableArray['ComboBox_3'], state="readonly")
ComboBox_3.place(x = 107,y = 15,width = 173,height = 20)
ComboBox_3.configure(state = "readonly")
Fun.G_UIElementArray['ComboBox_3']=ComboBox_3
Label_4= tkinter.Label(root,text="快递单号",width = 10,height = 4)
Label_4.place(x = 11,y = 55,width = 75,height = 20)
Fun.G_UIElementArray['Label_4']=Label_4
Fun.G_UIElementVariableArray['Entry_5']=tkinter.StringVar()
Entry_5= tkinter.Entry(root,textvariable=Fun.G_UIElementVariableArray['Entry_5'])
Entry_5.place(x = 107,y = 56,width = 172,height = 20)
Entry_5.configure(relief = "sunken")
Fun.G_UIElementArray['Entry_5']=Entry_5
Button_6= tkinter.Button(root,text="查询",width = 10,height = 4)
Button_6.place(x = 297,y = 53,width = 100,height = 28)
Button_6.configure(command =Express_Query_cmd.Button_6_onCommand)
Fun.G_UIElementArray['Button_6']=Button_6
ListBox_7= tkinter.Listbox(root)
ListBox_7.place(x = 24,y = 101,width = 372,height = 160)
Fun.G_UIElementArray['ListBox_7']=ListBox_7
import Express
Express_8=Express.Express()
#Express_8.xy(24,101)
Express_8.set_CompanyID(4)
Express_8.set_ExpressNumber('0000001')
Express_8.set_ComboBox(ComboBox_3)
Fun.G_UIElementArray['Express_8']=Express_8
#Add Some Logic Code Here: (Keep This Line of comments)
#Inital all element's Data 
Fun.InitElementData()
root.mainloop()
