#coding=utf-8
#import libs
#import MyWindow_cmd
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
class MyWindow:
    def __init__(self,root):
        global ElementBGArray
        global ElementBGArray_Resize
        global ElementBGArray_IM
        Fun.G_UIElementArray['UIClass']=self
        self.root = root
        root.title("Form1")
        root.geometry("480x320")
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 480,height = 320)
        Form_1.configure(bg = "#efefef")
        Fun.G_UIElementArray['root']=root
        Fun.G_UIElementArray['Form_1']=Form_1
        #Create the elements of root
        #Inital all element's Data
        Fun.InitElementData()
        #Add Some Logic Code Here: (Keep This Line of comments)
#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = MyWindow(root)
root.mainloop()
