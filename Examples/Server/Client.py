#coding=utf-8
#import libs 
import Client_cmd
import Client_sty
import Fun
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Client:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.G_UIElementArray[uiName]={}
        Fun.G_UIElementUserDataArray[uiName]={}
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        style = Client_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(None,root,564,287)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 564,height = 287)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'root',root)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Label_2= tkinter.Label(root,text="ServerIP",width = 10,height = 4)
        Label_2.place(x = 15,y = 15,width = 69,height = 20)
        Label_2.configure(bg = "#efefef")
        Label_2.configure(relief = "flat")
        Fun.Register(uiName,'Label_2',Label_2)
        Entry_3_Variable = Fun.AddTKVariable(uiName,'Entry_3','')
        Entry_3= tkinter.Entry(root,textvariable=Entry_3_Variable)
        Entry_3.place(x = 99,y = 15,width = 120,height = 20)
        Entry_3.configure(relief = "sunken")
        Fun.AddUserData(uiName,'Entry_3','IPAddr','string','127.0.0.1',1)
        Fun.Register(uiName,'Entry_3',Entry_3)
        Label_4= tkinter.Label(root,text="ServerPort",width = 10,height = 4)
        Label_4.place(x = 235,y = 14,width = 69,height = 20)
        Label_4.configure(relief = "flat")
        Fun.Register(uiName,'Label_4',Label_4)
        Entry_5_Variable = Fun.AddTKVariable(uiName,'Entry_5','')
        Entry_5= tkinter.Entry(root,textvariable=Entry_5_Variable)
        Entry_5.place(x = 315,y = 13,width = 120,height = 20)
        Entry_5.configure(relief = "sunken")
        Fun.AddUserData(uiName,'Entry_5','Port','int',8888,1)
        Fun.Register(uiName,'Entry_5',Entry_5)
        Label_6= tkinter.Label(root,text="Text",width = 10,height = 4)
        Label_6.place(x = 14,y = 50,width = 69,height = 20)
        Label_6.configure(relief = "flat")
        Fun.Register(uiName,'Label_6',Label_6)
        Entry_7_Variable = Fun.AddTKVariable(uiName,'Entry_7','')
        Entry_7= tkinter.Entry(root,textvariable=Entry_7_Variable)
        Entry_7.place(x = 99,y = 49,width = 335,height = 20)
        Entry_7.configure(relief = "sunken")
        Fun.AddUserData(uiName,'Entry_7','Msg','string','',1)
        Fun.Register(uiName,'Entry_7',Entry_7)
        Button_8= tkinter.Button(root,text="Connection",width = 10,height = 4)
        Button_8.place(x = 448,y = 10,width = 100,height = 28)
        Button_8.configure(command=lambda:Client_cmd.Button_8_onCommand(uiName,"Button_8"))
        Fun.Register(uiName,'Button_8',Button_8)
        Button_9= tkinter.Button(root,text="Send",width = 10,height = 4)
        Button_9.place(x = 448,y = 45,width = 100,height = 28)
        Button_9.configure(command=lambda:Client_cmd.Button_9_onCommand(uiName,"Button_9"))
        Fun.Register(uiName,'Button_9',Button_9)
        ListBox_10= tkinter.Listbox(root)
        ListBox_10.place(x = 98,y = 87,width = 448,height = 160)
        Fun.Register(uiName,'ListBox_10',ListBox_10)
        Label_11= tkinter.Label(root,text="MsgList",width = 10,height = 4)
        Label_11.place(x = 14,y = 89,width = 69,height = 20)
        Label_11.configure(relief = "flat")
        Fun.Register(uiName,'Label_11',Label_11)
        import MySocket
        MySocket_12=MySocket.MySocket()
        #MySocket_12.xy(33,123)
        MySocket_12.set_HOST('127.0.0.1')
        MySocket_12.set_PORT('8888')
        MySocket_12.set_MsgListBox(ListBox_10)
        Fun.Register(uiName,'MySocket_12',MySocket_12)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)
#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Client(root)
    root.mainloop()
