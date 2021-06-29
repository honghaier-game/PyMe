#coding=utf-8

#import libs 
import CallTest_cmd
import CallTest_sty
import Fun
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  CallTest:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.G_UIElementArray[uiName]={}
        Fun.G_UIElementUserDataArray[uiName]={}
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        style = CallTest_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(uiName,root,500,400)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 500,height = 400)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'root',root)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Button_2= tkinter.Button(root,text="调用注册",width = 10,height = 4)
        Button_2.place(x = 190,y = 139,width = 100,height = 28)
        Button_2.configure(command=lambda:CallTest_cmd.Button_2_onCommand(uiName,"Button_2"))
        Fun.Register(uiName,'Button_2',Button_2)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = CallTest(root)
    root.mainloop()
