#coding=utf-8
#import libs 
import TabPage1_cmd
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
class  TabPage1:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.G_UIElementArray[uiName]={}
        Fun.G_UIElementUserDataArray[uiName]={}
        global ElementBGArray
        global ElementBGArray_Resize
        global ElementBGArray_IM
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        if isTKroot == True:
            root.title("Form1")
            root.geometry("611x320")
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 611,height = 320)
        Form_1.configure(bg = "#efefef")
        Fun.Register(uiName,'root',root)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        TreeView_2= tkinter.ttk.Treeview(root,show="tree")
        TreeView_2.place(x = 8,y = 8,width = 593,height = 301)
        TreeView_2.configure(show = "headings")
        TreeView_2.configure(selectmode = "extended")
        TreeView_2.configure(columns = ["姓名","性别","年龄","地址"])
        TreeView_2.column("姓名",anchor="center",width=100)
        TreeView_2.heading("姓名",text="姓名")
        TreeView_2.column("性别",anchor="center",width=100)
        TreeView_2.heading("性别",text="性别")
        TreeView_2.column("年龄",anchor="center",width=100)
        TreeView_2.heading("年龄",text="年龄")
        TreeView_2.column("地址",anchor="center",width=240)
        TreeView_2.heading("地址",text="地址")
        Fun.Register(uiName,'TreeView_2',TreeView_2)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)
#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = TabPage1(root)
    root.mainloop()
