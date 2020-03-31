#coding=utf-8

#import libs 
import RT_cmd
import Fun
import sys
sys.path.append("D:/TKinterDesigner/Sample/Server")
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
Form_1.place(x = 0,y = 0,width = 548,height = 239)
Form_1.configure(bg = "#efefef")
root.geometry("548x239")
#Create the elements of root 
import MySocket
MySocket_2=MySocket.MySocket()
#MySocket_2.xy(437,57)
setattr(MySocket_2,'HOST','127.0.0.1')
setattr(MySocket_2,'PORT','8888')
Fun.G_UIElementArray['MySocket_2']=MySocket_2
Fun.G_UIElementVariableArray['Entry_3']=tkinter.StringVar()
Entry_3= tkinter.Entry(root,textvariable=Fun.G_UIElementVariableArray['Entry_3'])
Entry_3.place(x = 85,y = 19,width = 120,height = 20)
Entry_3.configure(bg = "#efefef")
Entry_3.configure(relief = "sunken")
BoundingDataArray=[]
BoundingDataArray.append(['IPAddr','string','127.0.0.1',1])
Fun.G_ElementBoundingDataArray.append(['Entry_3',BoundingDataArray])
Fun.G_UIElementArray['Entry_3']=Entry_3
Label_4= tkinter.Label(root,text="端口",width = 10,height = 4)
Label_4.place(x = 216,y = 19,width = 74,height = 20)
Fun.G_UIElementArray['Label_4']=Label_4
Fun.G_UIElementVariableArray['Entry_5']=tkinter.StringVar()
Entry_5= tkinter.Entry(root,textvariable=Fun.G_UIElementVariableArray['Entry_5'])
Entry_5.place(x = 294,y = 19,width = 120,height = 20)
Entry_5.configure(relief = "sunken")
BoundingDataArray=[]
BoundingDataArray.append(['Port','int','8888',1])
Fun.G_ElementBoundingDataArray.append(['Entry_5',BoundingDataArray])
Fun.G_UIElementArray['Entry_5']=Entry_5
Button_6= tkinter.Button(root,text="启动",width = 10,height = 4)
Button_6.place(x = 433,y = 16,width = 100,height = 28)
Button_6.configure(command =RT_cmd.Button_6_onCommand)
Fun.G_UIElementArray['Button_6']=Button_6
ListBox_7= tkinter.Listbox(root)
ListBox_7.place(x = 21,y = 57,width = 394,height = 160)
Fun.G_UIElementArray['ListBox_7']=ListBox_7
#Add Some Logic Code Here: (Keep This Line of comments)
#Inital all element's Data 
Fun.InitElementData()
root.mainloop()

