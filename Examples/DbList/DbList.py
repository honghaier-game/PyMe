#coding=utf-8

#import libs 
import DbList_cmd
import DbList_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  DbList:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        style = DbList_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(uiName,root,689,378)
            root['background'] = '#e3e3e3'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 689,height = 378)
        Form_1.configure(bg = "#e3e3e3")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'root',root)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Button_8= tkinter.Button(root,text="添加",width = 10,height = 4)
        Fun.Register(uiName,'Button_8',Button_8)
        Button_8.place(x = 8,y = 15,width = 100,height = 38)
        Button_8.configure(fg = "#000000")
        Button_8.configure(command=lambda:DbList_cmd.Button_8_onCommand(uiName,"Button_8"))
        Button_8_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_8.configure(font = Button_8_Ft)
        Button_10= tkinter.Button(root,text="删除",width = 10,height = 4)
        Fun.Register(uiName,'Button_10',Button_10)
        Button_10.place(x = 208,y = 15,width = 100,height = 38)
        Button_10.configure(command=lambda:DbList_cmd.Button_10_onCommand(uiName,"Button_10"))
        Button_10_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_10.configure(font = Button_10_Ft)
        TreeView_12= tkinter.ttk.Treeview(root,show="tree")
        Fun.Register(uiName,'TreeView_12',TreeView_12)
        TreeView_12.place(x = 5,y = 62,width = 682,height = 314)
        TreeView_12.configure(show = "headings")
        TreeView_12.configure(selectmode = "extended")
        TreeView_12.configure(columns = ["用户账号","密码","id"])
        TreeView_12.column("用户账号",anchor="center",width=120)
        TreeView_12.heading("用户账号",text="用户账号")
        TreeView_12.column("密码",anchor="center",width=200)
        TreeView_12.heading("密码",text="密码")
        TreeView_12.column("id",anchor="center",width=120)
        TreeView_12.heading("id",text="id")
        Button_13= tkinter.Button(root,text="修改",width = 10,height = 4)
        Fun.Register(uiName,'Button_13',Button_13)
        Button_13.place(x = 108,y = 15,width = 100,height = 38)
        Button_13.configure(command=lambda:DbList_cmd.Button_13_onCommand(uiName,"Button_13"))
        Button_13_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_13.configure(font = Button_13_Ft)
        Button_14= tkinter.Button(root,text="加载数据",width = 10,height = 4)
        Fun.Register(uiName,'Button_14',Button_14)
        Button_14.place(x = 571,y = 15,width = 112,height = 38)
        Button_14.configure(command=lambda:DbList_cmd.Button_14_onCommand(uiName,"Button_14"))
        Button_14_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_14.configure(font = Button_14_Ft)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = DbList(root)
    root.mainloop()
