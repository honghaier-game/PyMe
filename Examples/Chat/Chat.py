#coding=utf-8

#import libs 
import Chat_cmd
import Chat_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Chat:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        style = Chat_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(uiName,root,688,384)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 688,height = 384)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'root',root)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Label_2= tkinter.Label(root,text="ip",width = 10,height = 4)
        Fun.Register(uiName,'Label_2',Label_2)
        Label_2.place(x = 14,y = 23,width = 27,height = 23)
        Label_2.configure(relief = "flat")
        Label_2_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_2.configure(font = Label_2_Ft)
        Entry_3_Variable = Fun.AddTKVariable(uiName,'Entry_3','')
        Entry_3= tkinter.Entry(root,textvariable=Entry_3_Variable)
        Fun.Register(uiName,'Entry_3',Entry_3)
        Entry_3.place(x = 45,y = 16,width = 160,height = 33)
        Entry_3.configure(relief = "sunken")
        Entry_3.configure(state = "disabled")
        Label_4= tkinter.Label(root,text="端口",width = 10,height = 4)
        Fun.Register(uiName,'Label_4',Label_4)
        Label_4.place(x = 211,y = 25,width = 45,height = 23)
        Label_4.configure(relief = "flat")
        Label_4_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_4.configure(font = Label_4_Ft)
        Entry_5_Variable = Fun.AddTKVariable(uiName,'Entry_5','')
        Entry_5= tkinter.Entry(root,textvariable=Entry_5_Variable)
        Fun.Register(uiName,'Entry_5',Entry_5)
        Entry_5.place(x = 269,y = 17,width = 160,height = 33)
        Entry_5.configure(relief = "sunken")
        Button_6= tkinter.Button(root,text="启动服务器",width = 10,height = 4)
        Fun.Register(uiName,'Button_6',Button_6)
        Button_6.place(x = 435,y = 15,width = 120,height = 37)
        Button_6.configure(command=lambda:Chat_cmd.Button_6_onCommand(uiName,"Button_6"))
        Button_6_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_6.configure(font = Button_6_Ft)
        Button_7= tkinter.Button(root,text="关闭服务器",width = 10,height = 4)
        Fun.Register(uiName,'Button_7',Button_7)
        Button_7.place(x = 558,y = 15,width = 120,height = 37)
        Button_7.configure(command=lambda:Chat_cmd.Button_7_onCommand(uiName,"Button_7"))
        Button_7_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_7.configure(font = Button_7_Ft)
        ListBox_8= tkinter.Listbox(root)
        Fun.Register(uiName,'ListBox_8',ListBox_8)
        ListBox_8.place(x = 11,y = 55,width = 666,height = 127)
        ListBox_9= tkinter.Listbox(root)
        Fun.Register(uiName,'ListBox_9',ListBox_9)
        ListBox_9.place(x = 11,y = 226,width = 666,height = 106)
        Entry_10_Variable = Fun.AddTKVariable(uiName,'Entry_10','')
        Entry_10= tkinter.Entry(root,textvariable=Entry_10_Variable)
        Fun.Register(uiName,'Entry_10',Entry_10)
        Entry_10.place(x = 11,y = 337,width = 492,height = 39)
        Entry_10.configure(relief = "sunken")
        Button_11= tkinter.Button(root,text="连接服务器",width = 10,height = 4)
        Fun.Register(uiName,'Button_11',Button_11)
        Button_11.place(x = 280,y = 188,width = 120,height = 37)
        Button_11.configure(command=lambda:Chat_cmd.Button_11_onCommand(uiName,"Button_11"))
        Button_11_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_11.configure(font = Button_11_Ft)
        Label_12= tkinter.Label(root,text="客户端：[服务器端口同上]",width = 10,height = 4)
        Fun.Register(uiName,'Label_12',Label_12)
        Label_12.place(x = 9,y = 193,width = 249,height = 31)
        Label_12.configure(relief = "flat")
        Label_12_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_12.configure(font = Label_12_Ft)
        Button_13= tkinter.Button(root,text="发送消息",width = 10,height = 4)
        Fun.Register(uiName,'Button_13',Button_13)
        Button_13.place(x = 504,y = 336,width = 173,height = 39)
        Button_13.configure(command=lambda:Chat_cmd.Button_13_onCommand(uiName,"Button_13"))
        Button_13_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_13.configure(font = Button_13_Ft)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Chat(root)
    root.mainloop()
