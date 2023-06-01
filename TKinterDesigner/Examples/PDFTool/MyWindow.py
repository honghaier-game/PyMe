#coding=utf-8

#import libs 
import MyWindow_cmd
import MyWindow_sty
import Fun
import os
import MergeNew
import DealPdf1
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  MyWindow:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        style = MyWindow_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(uiName,root,580,393)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 580,height = 393)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'root',root)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        NoteBook_2= tkinter.ttk.Notebook(root)
        Fun.Register(uiName,'NoteBook_2',NoteBook_2)
        NoteBook_2.place(x = 6,y = 2,width = 571,height = 383)
        PageFrame_1 = tkinter.ttk.Frame(NoteBook_2)
        PageFrame_1.place(x = 11,y = 27,width = 561,height = 353)
        MergeNew.MergeNew(PageFrame_1,False)
        NoteBook_2.add(PageFrame_1,text = "合并(Merge")
        PageFrame_2 = tkinter.ttk.Frame(NoteBook_2)
        PageFrame_2.place(x = 11,y = 27,width = 561,height = 353)
        DealPdf1.DealPdf1(PageFrame_2,False)
        NoteBook_2.add(PageFrame_2,text = "拆分(split")
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = MyWindow(root)
    root.mainloop()
