#coding=utf-8

#import libs 
import Server_cmd
import Fun
import sys
sys.path.append("D:/PyGUIProj/3.Compile-Exe/ModleLibary/Server")
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
Fun.G_UIElementVariableArray['Entry_2']=tkinter.StringVar()
Entry_2= tkinter.Entry(root,textvariable=Fun.G_UIElementVariableArray['Entry_2'])
Entry_2.place(x = 93,y = 20,width = 120,height = 20)
Entry_2.configure(bg = "#ffffff")
Entry_2.configure(relief = "sunken")
BoundingDataArray=[]
BoundingDataArray.append(['IPAddr','string','127.0.0.1',1])
Fun.G_ElementBoundingDataArray.append(['Entry_2',BoundingDataArray])
Fun.G_UIElementArray['Entry_2']=Entry_2
Label_3= tkinter.Label(root,text="端口",width = 10,height = 4)
Label_3.place(x = 216,y = 19,width = 74,height = 20)
Fun.G_UIElementArray['Label_3']=Label_3
Fun.G_UIElementVariableArray['Entry_4']=tkinter.StringVar()
Entry_4= tkinter.Entry(root,textvariable=Fun.G_UIElementVariableArray['Entry_4'])
Entry_4.place(x = 294,y = 19,width = 120,height = 20)
Entry_4.configure(relief = "sunken")
BoundingDataArray=[]
BoundingDataArray.append(['Port','int','8888',1])
Fun.G_ElementBoundingDataArray.append(['Entry_4',BoundingDataArray])
Fun.G_UIElementArray['Entry_4']=Entry_4
Button_5= tkinter.Button(root,text="启动",width = 10,height = 4)
Button_5.place(x = 433,y = 16,width = 100,height = 28)
Button_5.configure(command =Server_cmd.Button_5_onCommand)
Fun.G_UIElementArray['Button_5']=Button_5
ListBox_6= tkinter.Listbox(root)
ListBox_6.place(x = 21,y = 57,width = 394,height = 160)
Fun.G_UIElementArray['ListBox_6']=ListBox_6
Label_7= tkinter.Label(root,text="IP地址",width = 10,height = 4)
Label_7.place(x = 4,y = 21,width = 74,height = 20)
Fun.G_UIElementArray['Label_7']=Label_7
import MySocket
MySocket_8=MySocket.MySocket()
#MySocket_8.xy(4,21)
MySocket_8.set_HOST('127.0.0.1')
MySocket_8.set_PORT('8888')
MySocket_8.set_LISTBOX(None)
Fun.G_UIElementArray['MySocket_8']=MySocket_8
import MySocket
MySocket_8=MySocket.MySocket()
#MySocket_8.xy(4,21)
MySocket_8.set_HOST('127.0.0.1')
MySocket_8.set_PORT('8888')
MySocket_8.set_LISTBOX(ListBox_6)
Fun.G_UIElementArray['MySocket_8']=MySocket_8
#Add Some Logic Code Here: (Keep This Line of comments)
#Inital all element's Data 
Fun.InitElementData()
root.mainloop()

