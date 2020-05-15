#coding=utf-8

#import libs 
import Server_cmd
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
class  Server:
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
            root.geometry("543x244")
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 543,height = 244)
        Form_1.configure(bg = "#efefef")
        Fun.AddElement(className,'root',root)
        Fun.AddElement(className,'Form_1',Form_1)
        #Create the elements of root 
        Entry_2_Variable = Fun.AddElementVariable(className,'Entry_2')
        Entry_2= tkinter.Entry(root,textvariable=Entry_2_Variable)
        Entry_2.place(x = 93,y = 20,width = 120,height = 20)
        Entry_2.configure(bg = "#ffffff")
        Entry_2.configure(relief = "sunken")
        Fun.AddUIData(className,'Entry_2','IPAddr','string','127.0.0.1',1)
        Fun.AddElement(className,'Entry_2',Entry_2)
        Label_3= tkinter.Label(root,text="端口",width = 10,height = 4)
        Label_3.place(x = 216,y = 19,width = 74,height = 20)
        Fun.AddElement(className,'Label_3',Label_3)
        Entry_4_Variable = Fun.AddElementVariable(className,'Entry_4')
        Entry_4= tkinter.Entry(root,textvariable=Entry_4_Variable)
        Entry_4.place(x = 294,y = 19,width = 120,height = 20)
        Entry_4.configure(relief = "sunken")
        Fun.AddUIData(className,'Entry_4','Port','int',8888,1)
        Fun.AddElement(className,'Entry_4',Entry_4)
        Button_5= tkinter.Button(root,text="启动",width = 10,height = 4)
        Button_5.place(x = 433,y = 16,width = 100,height = 28)
        Button_5.configure(command=lambda:Server_cmd.Button_5_onCommand(className,"Button_5"))
        Fun.AddElement(className,'Button_5',Button_5)
        ListBox_6= tkinter.Listbox(root)
        ListBox_6.place(x = 21,y = 57,width = 394,height = 160)
        Fun.AddElement(className,'ListBox_6',ListBox_6)
        Label_7= tkinter.Label(root,text="IP地址",width = 10,height = 4)
        Label_7.place(x = 4,y = 21,width = 74,height = 20)
        Fun.AddElement(className,'Label_7',Label_7)
        import MySocket
        MySocket_9=MySocket.MySocket()
        #MySocket_9.xy(4,21)
        MySocket_9.set_HOST('127.0.0.1')
        MySocket_9.set_PORT('8888')
        MySocket_9.set_LISTBOX(ListBox_6)
        Fun.AddElement(className,'MySocket_9',MySocket_9)
        #Inital all element's Data 
        Fun.InitElementData(className)
        #Add Some Logic Code Here: (Keep This Line of comments)

#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Server(root)
    root.mainloop()
