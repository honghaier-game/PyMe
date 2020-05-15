#coding=utf-8

#import libs 
import Client_cmd
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
#Define UI Class
class  Client:
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
          root.geometry("564x296")
      Form_1= tkinter.Canvas(root,width = 10,height = 4)
      Form_1.place(x = 0,y = 0,width = 564,height = 296)
      Form_1.configure(bg = "#efefef")
      Fun.AddElement(className,'root',root)
      Fun.AddElement(className,'Form_1',Form_1)
      #Create the elements of root 
      Label_2= tkinter.Label(root,text="服务器IP",width = 10,height = 4)
      Label_2.place(x = 15,y = 15,width = 69,height = 20)
      Label_2.configure(bg = "#efefef")
      Fun.AddElement(className,'Label_2',Label_2)
      Entry_3_Variable = Fun.AddElementVariable(className,'Entry_3')
      Entry_3= tkinter.Entry(root,textvariable=Entry_3_Variable)
      Entry_3.place(x = 99,y = 15,width = 120,height = 20)
      Entry_3.configure(relief = "sunken")
      Fun.AddUIData(className,'Entry_3','IPAddr','string','127.0.0.1',1)
      Fun.AddElement(className,'Entry_3',Entry_3)
      Label_4= tkinter.Label(root,text="服务器端口",width = 10,height = 4)
      Label_4.place(x = 235,y = 14,width = 69,height = 20)
      Fun.AddElement(className,'Label_4',Label_4)
      Entry_5_Variable = Fun.AddElementVariable(className,'Entry_5')
      Entry_5= tkinter.Entry(root,textvariable=Entry_5_Variable)
      Entry_5.place(x = 315,y = 13,width = 120,height = 20)
      Entry_5.configure(relief = "sunken")
      Fun.AddUIData(className,'Entry_5','Port','int','8888',1)
      Fun.AddElement(className,'Entry_5',Entry_5)
      Label_6= tkinter.Label(root,text="发送内容",width = 10,height = 4)
      Label_6.place(x = 14,y = 49,width = 69,height = 20)
      Fun.AddElement(className,'Label_6',Label_6)
      Entry_7_Variable = Fun.AddElementVariable(className,'Entry_7')
      Entry_7= tkinter.Entry(root,textvariable=Entry_7_Variable)
      Entry_7.place(x = 99,y = 49,width = 335,height = 20)
      Entry_7.configure(relief = "sunken")
      Fun.AddElement(className,'Entry_7',Entry_7)
      Button_8= tkinter.Button(root,text="连接",width = 10,height = 4)
      Button_8.place(x = 448,y = 10,width = 100,height = 28)
      Button_8.configure(command =lambda:Client_cmd.Button_8_onCommand(className,"Button_8"))
      Fun.AddElement(className,'Button_8',Button_8)
      Button_9= tkinter.Button(root,text="发送",width = 10,height = 4)
      Button_9.place(x = 448,y = 45,width = 100,height = 28)
      Button_9.configure(command =lambda:Client_cmd.Button_9_onCommand(className,"Button_9"))
      Fun.AddElement(className,'Button_9',Button_9)
      ListBox_10= tkinter.Listbox(root)
      ListBox_10.place(x = 21,y = 87,width = 528,height = 197)
      Fun.AddElement(className,'ListBox_10',ListBox_10)
      import MySocket
      MySocket_11=MySocket.MySocket()
      #MySocket_11.xy(21,87)
      MySocket_11.set_HOST('127.0.0.1')
      MySocket_11.set_PORT('8888')
      MySocket_11.set_LISTBOX(ListBox_10)
      Fun.AddElement(className,'MySocket_11',MySocket_11)
      #Inital all element's Data 
      Fun.InitElementData(className)
      #Add Some Logic Code Here: (Keep This Line of comments)

#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Client(root)
    root.mainloop()
