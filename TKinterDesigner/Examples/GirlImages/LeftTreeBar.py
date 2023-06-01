#coding=utf-8
#import libs 
import LeftTreeBar_cmd
import LeftTreeBar_sty
import Fun
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  LeftTreeBar:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.G_UIElementArray[uiName]={}
        Fun.G_UIElementUserDataArray[uiName]={}
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        style = LeftTreeBar_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            root.wm_attributes("-topmost",1)
            root.geometry("205x549")
            root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 205,height = 549)
        Form_1.configure(bg = "#333333")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'root',root)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        TreeView_2= tkinter.ttk.Treeview(root,show="tree")
        TreeView_2.place(x = 0,y = 0,width = 205,height = 549)
        TreeView_2.configure(selectmode = "extended")
        TreeView_2.bind("<Button-1>",Fun.EventFunction_Adaptor(LeftTreeBar_cmd.TreeView_2_onButton1,uiName=uiName,widgetName="TreeView_2"))
        Fun.Register(uiName,'TreeView_2',TreeView_2)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)
        root.bind('<Configure>',self.Configure)
    def Configure(self,event):
        if self.root == event.widget:
            TreeView_2 = Fun.GetElement(self.__class__.__name__,'TreeView_2')
            TreeView_2.place(x = 0,y = 0,width = event.width,height = event.height)

#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = LeftTreeBar(root)
    root.mainloop()
