#coding=utf-8

#import libs 
import CallTest_cmd
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
class  CallTest:
    def __init__(self,root):
      global ElementBGArray
      global ElementBGArray_Resize
      global ElementBGArray_IM
      Fun.G_UIElementArray['UIClass']=self
      self.root = root
      root.title("Form1")
      root.geometry("500x400")
      Form_1= tkinter.Canvas(root,width = 10,height = 4)
      Form_1.place(x = 0,y = 0,width = 500,height = 400)
      Form_1.configure(bg = "#efefef")
      Fun.G_UIElementArray['root']=root
      Fun.G_UIElementArray['Form_1']=Form_1
      #Create the elements of root 
      Button_2= tkinter.Button(root,text="调用注册",width = 10,height = 4)
      Button_2.place(x = 190,y = 139,width = 100,height = 28)
      Button_2.configure(command =CallTest_cmd.Button_2_onCommand)
      Fun.G_UIElementArray['Button_2']=Button_2
      #Inital all element's Data 
      Fun.InitElementData()
      #Add Some Logic Code Here: (Keep This Line of comments)

#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = CallTest(root)
    root.mainloop()

