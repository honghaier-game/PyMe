#coding=utf-8

#import libs 
import Client_cmd
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
Form_1.place(x = 0,y = 0,width = 564,height = 305)
Form_1.configure(bg = "#efefef")
root.geometry("564x305")
#Create the elements of root 
Label_2= tkinter.Label(root,text="服务器IP",width = 10,height = 4)
Label_2.place(x = 15,y = 15,width = 69,height = 20)
Label_2.configure(bg = "#efefef")
Fun.G_UIElementArray['Label_2']=Label_2
Fun.G_UIElementVariableArray['Entry_3']=tkinter.StringVar()
Entry_3= tkinter.Entry(root,textvariable=Fun.G_UIElementVariableArray['Entry_3'])
Entry_3.place(x = 99,y = 15,width = 120,height = 20)
Entry_3.configure(relief = "sunken")
BoundingDataArray=[]
BoundingDataArray.append(['IPAddr','string','127.0.0.1',1])
Fun.G_ElementBoundingDataArray.append(['Entry_3',BoundingDataArray])
Fun.G_UIElementArray['Entry_3']=Entry_3
Label_4= tkinter.Label(root,text="服务器端口",width = 10,height = 4)
Label_4.place(x = 235,y = 14,width = 69,height = 20)
Fun.G_UIElementArray['Label_4']=Label_4
Fun.G_UIElementVariableArray['Entry_5']=tkinter.StringVar()
Entry_5= tkinter.Entry(root,textvariable=Fun.G_UIElementVariableArray['Entry_5'])
Entry_5.place(x = 315,y = 13,width = 120,height = 20)
Entry_5.configure(relief = "sunken")
BoundingDataArray=[]
BoundingDataArray.append(['Port','int','8888',1])
Fun.G_ElementBoundingDataArray.append(['Entry_5',BoundingDataArray])
Fun.G_UIElementArray['Entry_5']=Entry_5
Label_6= tkinter.Label(root,text="发送内容",width = 10,height = 4)
Label_6.place(x = 14,y = 49,width = 69,height = 20)
Fun.G_UIElementArray['Label_6']=Label_6
Fun.G_UIElementVariableArray['Entry_7']=tkinter.StringVar()
Entry_7= tkinter.Entry(root,textvariable=Fun.G_UIElementVariableArray['Entry_7'])
Entry_7.place(x = 99,y = 49,width = 335,height = 20)
Entry_7.configure(relief = "sunken")
BoundingDataArray=[]
BoundingDataArray.append(['Msg','string','',1])
Fun.G_ElementBoundingDataArray.append(['Entry_7',BoundingDataArray])
Fun.G_UIElementArray['Entry_7']=Entry_7
Button_8= tkinter.Button(root,text="连接",width = 10,height = 4)
Button_8.place(x = 448,y = 10,width = 100,height = 28)
Button_8.configure(command =Client_cmd.Button_8_onCommand)
Fun.G_UIElementArray['Button_8']=Button_8
Button_9= tkinter.Button(root,text="发送",width = 10,height = 4)
Button_9.place(x = 448,y = 45,width = 100,height = 28)
Button_9.configure(command =Client_cmd.Button_9_onCommand)
Fun.G_UIElementArray['Button_9']=Button_9
ListBox_11= tkinter.Listbox(root)
ListBox_11.place(x = 21,y = 87,width = 528,height = 197)
Fun.G_UIElementArray['ListBox_11']=ListBox_11
import MySocket
MySocket_11=MySocket.MySocket()
#MySocket_11.xy(21,87)
MySocket_11.set_HOST('127.0.0.1')
MySocket_11.set_PORT('8888')
MySocket_11.set_LISTBOX(ListBox_11)
Fun.G_UIElementArray['MySocket_11']=MySocket_11
#Add Some Logic Code Here: (Keep This Line of comments)
#Inital all element's Data 
Fun.InitElementData()
root.mainloop()
