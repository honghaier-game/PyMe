#coding=utf-8
#import libs 
import Server_cmd
import Server_sty
import Fun
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Server:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.G_UIElementArray[uiName]={}
        Fun.G_UIElementUserDataArray[uiName]={}
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        style = Server_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(None,root,573,320)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 573,height = 320)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'root',root)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Label_2= tkinter.Label(root,text="IP",width = 10,height = 4)
        Label_2.place(x = 10,y = 19,width = 74,height = 20)
        Label_2.configure(relief = "flat")
        Fun.Register(uiName,'Label_2',Label_2)
        Entry_3_Variable = Fun.AddTKVariable(uiName,'Entry_3','127.0.0.1')
        Entry_3= tkinter.Entry(root,textvariable=Entry_3_Variable)
        Entry_3.place(x = 85,y = 19,width = 120,height = 20)
        Entry_3.configure(bg = "#efefef")
        Entry_3.configure(relief = "sunken")
        Fun.Register(uiName,'Entry_3',Entry_3)
        Label_4= tkinter.Label(root,text="Port",width = 10,height = 4)
        Label_4.place(x = 216,y = 19,width = 74,height = 20)
        Label_4.configure(relief = "flat")
        Fun.Register(uiName,'Label_4',Label_4)
        Entry_5_Variable = Fun.AddTKVariable(uiName,'Entry_5','')
        Entry_5= tkinter.Entry(root,textvariable=Entry_5_Variable)
        Entry_5.place(x = 294,y = 19,width = 120,height = 20)
        Entry_5.configure(relief = "sunken")
        Fun.AddUserData(uiName,'Entry_5','Port','int',8888,1)
        Fun.Register(uiName,'Entry_5',Entry_5)
        Button_6= tkinter.Button(root,text="Start",width = 10,height = 4)
        Button_6.place(x = 433,y = 16,width = 100,height = 28)
        Button_6.configure(command=lambda:Server_cmd.Button_6_onCommand(uiName,"Button_6"))
        Fun.Register(uiName,'Button_6',Button_6)
        ListBox_7= tkinter.Listbox(root)
        ListBox_7.place(x = 139,y = 52,width = 394,height = 160)
        Fun.Register(uiName,'ListBox_7',ListBox_7)
        Button_8= tkinter.Button(root,text="Send",width = 10,height = 4)
        Button_8.place(x = 431,y = 227,width = 100,height = 28)
        Button_8.configure(command=lambda:Server_cmd.Button_8_onCommand(uiName,"Button_8"))
        Fun.Register(uiName,'Button_8',Button_8)
        Entry_9_Variable = Fun.AddTKVariable(uiName,'Entry_9','')
        Entry_9= tkinter.Entry(root,textvariable=Entry_9_Variable)
        Entry_9.place(x = 14,y = 225,width = 407,height = 30)
        Entry_9.configure(relief = "sunken")
        Fun.Register(uiName,'Entry_9',Entry_9)
        ListBox_10= tkinter.Listbox(root)
        ListBox_10.place(x = 12,y = 53,width = 120,height = 158)
        Fun.AddUserData(uiName,'ListBox_10','ClientSocketArray','list',[],0)
        Fun.Register(uiName,'ListBox_10',ListBox_10)
        import MySocket
        MySocket_11=MySocket.MySocket()
        #MySocket_11.xy(193,265)
        MySocket_11.set_HOST('127.0.0.1')
        MySocket_11.set_PORT('8888')
        MySocket_11.set_MsgListBox(ListBox_7)
        MySocket_11.set_ClientListBox(ListBox_10)
        Fun.Register(uiName,'MySocket_11',MySocket_11)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)
#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Server(root)
    root.mainloop()
