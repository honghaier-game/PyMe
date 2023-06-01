#coding=utf-8

#import libs 
import TicketQuery_cmd
import TicketQuery_sty
import Fun
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  TicketQuery:
    def __init__(self,root,isTKroot = True):
        className = self.__class__.__name__
        Fun.G_UIElementArray[className]={}
        Fun.G_UIElementUserDataArray[className]={}
        Fun.Register(className,'UIClass',self)
        self.root = root
        style = TicketQuery_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(None,root,721,400)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 721,height = 400)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(className,'root',root)
        Fun.Register(className,'Form_1',Form_1)
        #Create the elements of root 
        Label_2= tkinter.Label(root,text="出发",width = 10,height = 4)
        Label_2.place(x = 13,y = 25,width = 44,height = 37)
        Label_2.configure(relief = "flat")
        Label_2_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_2.configure(font = Label_2_Ft)
        Fun.Register(className,'Label_2',Label_2)
        Entry_3_Variable = Fun.AddTKVariable(className,'Entry_3','')
        Entry_3= tkinter.Entry(root,textvariable=Entry_3_Variable)
        Entry_3.place(x = 65,y = 26,width = 120,height = 37)
        Entry_3.configure(relief = "sunken")
        Fun.Register(className,'Entry_3',Entry_3)
        Label_4= tkinter.Label(root,text="到达",width = 10,height = 4)
        Label_4.place(x = 193,y = 32,width = 46,height = 28)
        Label_4.configure(relief = "flat")
        Label_4_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_4.configure(font = Label_4_Ft)
        Fun.Register(className,'Label_4',Label_4)
        Entry_5_Variable = Fun.AddTKVariable(className,'Entry_5','')
        Entry_5= tkinter.Entry(root,textvariable=Entry_5_Variable)
        Entry_5.place(x = 242,y = 26,width = 120,height = 37)
        Entry_5.configure(relief = "sunken")
        Fun.Register(className,'Entry_5',Entry_5)
        Label_6= tkinter.Label(root,text="日期",width = 10,height = 4)
        Label_6.place(x = 364,y = 28,width = 56,height = 35)
        Label_6.configure(relief = "flat")
        Label_6_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_6.configure(font = Label_6_Ft)
        Fun.Register(className,'Label_6',Label_6)
        Entry_8_Variable = Fun.AddTKVariable(className,'Entry_8','')
        Entry_8= tkinter.Entry(root,textvariable=Entry_8_Variable)
        Entry_8.place(x = 422,y = 26,width = 140,height = 37)
        Entry_8.configure(relief = "sunken")
        Fun.Register(className,'Entry_8',Entry_8)
        Button_9= tkinter.Button(root,text="查询",width = 10,height = 4)
        Button_9.place(x = 568,y = 23,width = 119,height = 43)
        Button_9.configure(command=lambda:TicketQuery_cmd.Button_9_onCommand(className,"Button_9"))
        Button_9_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_9.configure(font = Button_9_Ft)
        Fun.Register(className,'Button_9',Button_9)
        ListBox_10= tkinter.Listbox(root)
        ListBox_10.place(x = 13,y = 74,width = 690,height = 309)
        Fun.Register(className,'ListBox_10',ListBox_10)
        #Inital all element's Data 
        Fun.InitElementData(className)
        #Call Form_1's OnLoad Function
        TicketQuery_cmd.Form_1_onLoad(className)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = TicketQuery(root)
    root.mainloop()
