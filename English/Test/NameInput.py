#coding=utf-8

#import libs 
import NameInput_cmd
import Fun
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

#Add your Varial Here: (Keep This Line of comments)
#Create the root of Kinter 
root = tkinter.Tk()
root.title("Form1")
Form_1= tkinter.Canvas(root,width = 10,height = 4)
Form_1.place(x = 0,y = 0,width = 500,height = 400)
Form_1.configure(bg = "#efefef")
root.geometry("500x400")
#Create the elements of root 
Label_2= tkinter.Label(root,text="Name",width = 10,height = 4)
Label_2.place(x = 20,y = 30,width = 100,height = 20)
Label_2.configure(bg = "#efefef")
Fun.G_UIElementArray['Label_2']=Label_2
Fun.G_UIElementVariableArray['Entry_3']=tkinter.StringVar()
Entry_3= tkinter.Entry(root,textvariable=Fun.G_UIElementVariableArray['Entry_3'])
Entry_3.place(x = 160,y = 30,width = 260,height = 20)
Entry_3.configure(relief = "sunken")
BoundingDataArray=[]
BoundingDataArray.append(['Name','string','Mr.Green',1])
Fun.G_ElementBoundingDataArray.append(['Entry_3',BoundingDataArray])
Fun.G_UIElementArray['Entry_3']=Entry_3
Button_4= tkinter.Button(root,text="OK",width = 10,height = 4)
Button_4.place(x = 160,y = 90,width = 100,height = 28)
Button_4.configure(command =NameInput_cmd.Button_4_onCommand)
Fun.G_UIElementArray['Button_4']=Button_4
Label_5= tkinter.Label(root,text="Label",width = 10,height = 4)
Label_5.place(x = 20,y = 80,width = 100,height = 20)
Fun.G_UIElementArray['Label_5']=Label_5
#Create the Menu of root 
MainMenu=tkinter.Menu(root)
root.config(menu = MainMenu)
File=tkinter.Menu(MainMenu,tearoff = 0)
File.add_command(label="Open",command=NameInput_cmd.Menu_Open)
MainMenu.add_cascade(label="File",menu=File)
MainMenu.add_command(label="Operate",command=NameInput_cmd.Menu_Operate)
#Add Some Logic Code Here: (Keep This Line of comments)
#Inital all element's Data 
Fun.InitElementData()
root.mainloop()
