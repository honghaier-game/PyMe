#coding=utf-8

#import libs 
import WebbrowserProject_cmd
import WebbrowserProject_sty
import Fun
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
from   PIL import Image,ImageTk

ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  WebbrowserProject:
    def __init__(self,root,isTKroot = True):
        className = self.__class__.__name__
        Fun.G_UIElementArray[className]={}
        Fun.G_ElementBindingDataArray[className]={}
        global ElementBGArray
        global ElementBGArray_Resize
        global ElementBGArray_IM
        Fun.AddElement(className,'UIClass',self)
        self.root = root
        style = WebbrowserProject_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            root.wm_attributes("-topmost",1)
            root.geometry("1283x793")
            root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 1283,height = 793)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.AddElement(className,'root',root)
        Fun.AddElement(className,'Form_1',Form_1)
        #Create the elements of root 
        Frame_2= tkinter.Frame(root)
        Frame_2.place(x = 0,y = 30,width = 992,height = 673)
        Frame_2.configure(bg = "#888888")
        Frame_2.configure(relief = "flat")
        Fun.AddElement(className,'Frame_2',Frame_2)
        Entry_3_Variable = Fun.AddElementVariable(className,'Entry_3')
        Entry_3= tkinter.Entry(root,textvariable=Entry_3_Variable)
        Entry_3.place(x = 155,y = 7,width = 710,height = 20)
        Entry_3.configure(relief = "sunken")
        Entry_3.bind("<Button-1>",Fun.EventFunction_Adaptor(WebbrowserProject_cmd.Entry_3_onButton1,className=className,widgetName="Entry_3"))
        Fun.AddElement(className,'Entry_3',Entry_3)
        Button_4= tkinter.Button(root,text="GO",width = 10,height = 4)
        Button_4.place(x = 888,y = 3,width = 100,height = 24)
        Button_4.configure(command=lambda:WebbrowserProject_cmd.Button_4_onCommand(className,"Button_4"))
        Fun.AddElement(className,'Button_4',Button_4)
        import Webbrowser
        Webbrowser_5=Webbrowser.Webbrowser()
        #Webbrowser_5.xy(24,46)
        Webbrowser_5.set_Frame(Frame_2)
        Webbrowser_5.set_URL('http://www.baidu.com')
        Fun.AddElement(className,'Webbrowser_5',Webbrowser_5)
        Button_7= tkinter.Button(root,text="Button",width = 10,height = 4)
        Button_7.place(x = 0,y = 1,width = 32,height = 28)
        ElementBGArray[7]=Image.open("back.png").convert('RGBA')
        ElementBGArray_Resize[7]=ElementBGArray[7].resize((32, 28),Image.ANTIALIAS)
        ElementBGArray_IM[7]=ImageTk.PhotoImage(ElementBGArray_Resize[7])
        Button_7.configure(image = ElementBGArray_IM[7])
        Button_7.configure(command=lambda:WebbrowserProject_cmd.Button_7_onCommand(className,"Button_7"))
        Fun.AddElement(className,'Button_7',Button_7)
        Button_8= tkinter.Button(root,text="Button",width = 10,height = 4)
        Button_8.place(x = 35,y = 1,width = 32,height = 28)
        ElementBGArray[8]=Image.open("front.png").convert('RGBA')
        ElementBGArray_Resize[8]=ElementBGArray[8].resize((32, 28),Image.ANTIALIAS)
        ElementBGArray_IM[8]=ImageTk.PhotoImage(ElementBGArray_Resize[8])
        Button_8.configure(image = ElementBGArray_IM[8])
        Button_8.configure(command=lambda:WebbrowserProject_cmd.Button_8_onCommand(className,"Button_8"))
        Fun.AddElement(className,'Button_8',Button_8)
        Button_9= tkinter.Button(root,text="Button",width = 10,height = 4)
        Button_9.place(x = 70,y = 1,width = 34,height = 28)
        ElementBGArray[9]=Image.open("refresh.png").convert('RGBA')
        ElementBGArray_Resize[9]=ElementBGArray[9].resize((34, 28),Image.ANTIALIAS)
        ElementBGArray_IM[9]=ImageTk.PhotoImage(ElementBGArray_Resize[9])
        Button_9.configure(image = ElementBGArray_IM[9])
        Button_9.configure(command=lambda:WebbrowserProject_cmd.Button_9_onCommand(className,"Button_9"))
        Fun.AddElement(className,'Button_9',Button_9)
        Button_10= tkinter.Button(root,text="Button",width = 10,height = 4)
        Button_10.place(x = 107,y = 1,width = 36,height = 28)
        ElementBGArray[10]=Image.open("home.png").convert('RGBA')
        ElementBGArray_Resize[10]=ElementBGArray[10].resize((36, 28),Image.ANTIALIAS)
        ElementBGArray_IM[10]=ImageTk.PhotoImage(ElementBGArray_Resize[10])
        Button_10.configure(image = ElementBGArray_IM[10])
        Button_10.configure(command=lambda:WebbrowserProject_cmd.Button_10_onCommand(className,"Button_10"))
        Fun.AddElement(className,'Button_10',Button_10)
        #Inital all element's Data 
        Fun.InitElementData(className)
        #Call Form_1's OnLoad Function
        WebbrowserProject_cmd.Form_1_onLoad(className)
        #Add Some Logic Code Here: (Keep This Line of comments)

    def Configure(self,event):
        if self.root == event.widget:
            Frame_2 = Fun.GetUIEle(self.__class__.__name__,'Frame_2')
            Frame_2.place(x = 0,y = 30,width = event.width,height = event.height - 30)
            Webbrowser_5 = Fun.GetUIEle(self.__class__.__name__,'Webbrowser_5')
            Webbrowser_5.resetSize(event.width,event.height - 30)
            Entry_3 = Fun.GetUIEle(self.__class__.__name__,'Entry_3')
            Entry_3.place(x = 157,y = 7,width = event.width-270,height = 20)
            Entry_3.focus_force()
            Button_4 = Fun.GetUIEle(self.__class__.__name__,'Button_4')
            Button_4.place(x = event.width-110,y = 7,width = 100,height = 20)

#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = WebbrowserProject(root)
    root.mainloop()
