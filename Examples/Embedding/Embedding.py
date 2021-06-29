#coding=utf-8

#import libs 
import Embedding_cmd
import Embedding_sty
import Fun
import TabPage1
import TabPage2
import Page1
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Embedding:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.G_UIElementArray[uiName]={}
        Fun.G_UIElementUserDataArray[uiName]={}
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        style = Embedding_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(uiName,root,629,510)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 629,height = 510)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'root',root)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Canvas_2= tkinter.Canvas(root)
        Canvas_2.place(x = 9,y = 13,width = 609,height = 160)
        Canvas_2.configure(bg = "#ffffff")
        Page1.Page1(Canvas_2,False)
        Fun.Register(uiName,'Canvas_2',Canvas_2)
        NoteBook_3= tkinter.ttk.Notebook(root)
        NoteBook_3.place(x = 10,y = 188,width = 606,height = 312)
        PageFrame_1 = tkinter.ttk.Frame(NoteBook_3)
        PageFrame_1.place(x = 15,y = 213,width = 596,height = 282)
        TabPage1.TabPage1(PageFrame_1,False)
        NoteBook_3.add(PageFrame_1,text = "TabPage1")
        PageFrame_2 = tkinter.ttk.Frame(NoteBook_3)
        PageFrame_2.place(x = 15,y = 213,width = 596,height = 282)
        TabPage2.TabPage2(PageFrame_2,False)
        NoteBook_3.add(PageFrame_2,text = "TabPage2")
        Fun.Register(uiName,'NoteBook_3',NoteBook_3)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Embedding(root)
    root.mainloop()
