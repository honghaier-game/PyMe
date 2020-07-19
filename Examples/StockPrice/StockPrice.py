#coding=utf-8

#import libs 
import StockPrice_cmd
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
class  StockPrice:
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
            root.title("股票监控")
            root.geometry("906x363")
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 906,height = 363)
        Form_1.configure(bg = "#efefef")
        Fun.AddElement(className,'root',root)
        Fun.AddElement(className,'Form_1',Form_1)
        #Create the elements of root 
        Label_2= tkinter.Label(root,text="股票代码",width = 10,height = 4)
        Label_2.place(x = -22,y = 27,width = 107,height = 22)
        Fun.AddElement(className,'Label_2',Label_2)
        Entry_3_Variable = Fun.AddElementVariable(className,'Entry_3')
        Entry_3= tkinter.Entry(root,textvariable=Entry_3_Variable)
        Entry_3.place(x = 68,y = 29,width = 164,height = 20)
        Entry_3.configure(relief = "sunken")
        Fun.AddElement(className,'Entry_3',Entry_3)
        Button_4= tkinter.Button(root,text="增加股票",width = 10,height = 4)
        Button_4.place(x = 463,y = 24,width = 100,height = 28)
        Button_4.configure(command=lambda:StockPrice_cmd.Button_4_onCommand(className,"Button_4"))
        Fun.AddElement(className,'Button_4',Button_4)
        Button_6= tkinter.Button(root,text="启动监控",width = 10,height = 4)
        Button_6.place(x = 790,y = 25,width = 100,height = 28)
        Button_6.configure(command=lambda:StockPrice_cmd.Button_6_onCommand(className,"Button_6"))
        Fun.AddElement(className,'Button_6',Button_6)
        Label_9= tkinter.Label(root,text="最高价",width = 10,height = 4)
        Label_9.place(x = 179,y = 27,width = 55,height = 20)
        Fun.AddElement(className,'Label_9',Label_9)
        Entry_10_Variable = Fun.AddElementVariable(className,'Entry_10')
        Entry_10= tkinter.Entry(root,textvariable=Entry_10_Variable)
        Entry_10.place(x = 380,y = 28,width = 76,height = 20)
        Entry_10.configure(relief = "sunken")
        Fun.AddElement(className,'Entry_10',Entry_10)
        Label_11= tkinter.Label(root,text="最低价",width = 10,height = 4)
        Label_11.place(x = 315,y = 25,width = 55,height = 20)
        Fun.AddElement(className,'Label_11',Label_11)
        Entry_12_Variable = Fun.AddElementVariable(className,'Entry_12')
        Entry_12= tkinter.Entry(root,textvariable=Entry_12_Variable)
        Entry_12.place(x = 235,y = 26,width = 70,height = 20)
        Entry_12.configure(relief = "sunken")
        Fun.AddElement(className,'Entry_12',Entry_12)
        TreeView_13= tkinter.ttk.Treeview(root,show="tree")
        TreeView_13.place(x = 17,y = 65,width = 875,height = 291)
        TreeView_13.configure(show = "headings")
        TreeView_13.configure(selectmode = "extended")
        TreeView_13.configure(columns = ["股票代码","股票名称","当前时间","当前价","限制最高","限制最低","警报"])
        TreeView_13.column("股票代码",anchor="center",width=90)
        TreeView_13.heading("股票代码",text="股票代码")
        TreeView_13.column("股票名称",anchor="center",width=90)
        TreeView_13.heading("股票名称",text="股票名称")
        TreeView_13.column("当前时间",anchor="center",width=90)
        TreeView_13.heading("当前时间",text="当前时间")
        TreeView_13.column("当前价",anchor="center",width=80)
        TreeView_13.heading("当前价",text="当前价")
        TreeView_13.column("限制最高",anchor="center",width=80)
        TreeView_13.heading("限制最高",text="限制最高")
        TreeView_13.column("限制最低",anchor="center",width=80)
        TreeView_13.heading("限制最低",text="限制最低")
        TreeView_13.column("警报",anchor="center",width=100)
        TreeView_13.heading("警报",text="警报")
        Fun.AddUIData(className,'TreeView_13','StockArray','list',[],0)
        Fun.AddElement(className,'TreeView_13',TreeView_13)
        Label_16= tkinter.Label(root,text="通知手机",width = 10,height = 4)
        Label_16.place(x = 571,y = 26,width = 81,height = 23)
        Fun.AddElement(className,'Label_16',Label_16)
        Entry_17_Variable = Fun.AddElementVariable(className,'Entry_17')
        Entry_17= tkinter.Entry(root,textvariable=Entry_17_Variable)
        Entry_17.place(x = 652,y = 28,width = 126,height = 20)
        Entry_17.configure(relief = "sunken")
        Fun.AddElement(className,'Entry_17',Entry_17)
        #Inital all element's Data 
        Fun.InitElementData(className)
        #Add Some Logic Code Here: (Keep This Line of comments)

#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = StockPrice(root)
    root.mainloop()
