#coding=utf-8

#import libs 
import JSQ_cmd
import Fun
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
G_VarArray=[['Count',0]]
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  JSQ:
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
            root.title("Form1")
            root.geometry("216x215")
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 216,height = 215)
        Form_1.configure(bg = "#efefef")
        Fun.AddElement(className,'root',root)
        Fun.AddElement(className,'Form_1',Form_1)
        #Create the elements of root 
        Label_2= tkinter.Label(root,text="",width = 10,height = 4)
        Label_2.place(x = 10,y = 10,width = 190,height = 30)
        Label_2.configure(bg = "#808080")
        Label_2.configure(fg = "#ffffff")
        Fun.AddUIData(className,'Label_2','Count','float',0.0,1)
        Fun.AddUIData(className,'Label_2','MidCount','float',0.0,0)
        Fun.AddUIData(className,'Label_2','OpType','int',0,0)
        Fun.AddElement(className,'Label_2',Label_2)
        Button_3= tkinter.Button(root,text="1",width = 10,height = 4)
        Button_3.place(x = 10,y = 50,width = 40,height = 30)
        Button_3.configure(relief = "groove")
        Button_3.configure(command=lambda:JSQ_cmd.Button_3_onCommand(className,"Button_3"))
        Fun.AddElement(className,'Button_3',Button_3)
        Button_4= tkinter.Button(root,text="2",width = 10,height = 4)
        Button_4.place(x = 60,y = 50,width = 40,height = 30)
        Button_4.configure(relief = "groove")
        Button_4.configure(command=lambda:JSQ_cmd.Button_4_onCommand(className,"Button_4"))
        Fun.AddElement(className,'Button_4',Button_4)
        Button_5= tkinter.Button(root,text="3",width = 10,height = 4)
        Button_5.place(x = 110,y = 50,width = 40,height = 30)
        Button_5.configure(relief = "groove")
        Button_5.configure(command=lambda:JSQ_cmd.Button_5_onCommand(className,"Button_5"))
        Fun.AddElement(className,'Button_5',Button_5)
        Button_6= tkinter.Button(root,text="4",width = 10,height = 4)
        Button_6.place(x = 10,y = 90,width = 40,height = 30)
        Button_6.configure(relief = "groove")
        Button_6.configure(command=lambda:JSQ_cmd.Button_6_onCommand(className,"Button_6"))
        Fun.AddElement(className,'Button_6',Button_6)
        Button_7= tkinter.Button(root,text="5",width = 10,height = 4)
        Button_7.place(x = 60,y = 90,width = 40,height = 30)
        Button_7.configure(relief = "groove")
        Button_7.configure(command=lambda:JSQ_cmd.Button_7_onCommand(className,"Button_7"))
        Fun.AddElement(className,'Button_7',Button_7)
        Button_8= tkinter.Button(root,text="6",width = 10,height = 4)
        Button_8.place(x = 110,y = 90,width = 40,height = 30)
        Button_8.configure(relief = "groove")
        Button_8.configure(command=lambda:JSQ_cmd.Button_8_onCommand(className,"Button_8"))
        Fun.AddElement(className,'Button_8',Button_8)
        Button_9= tkinter.Button(root,text="7",width = 10,height = 4)
        Button_9.place(x = 10,y = 130,width = 40,height = 30)
        Button_9.configure(relief = "groove")
        Button_9.configure(command=lambda:JSQ_cmd.Button_9_onCommand(className,"Button_9"))
        Fun.AddElement(className,'Button_9',Button_9)
        Button_10= tkinter.Button(root,text="8",width = 10,height = 4)
        Button_10.place(x = 60,y = 130,width = 40,height = 30)
        Button_10.configure(relief = "groove")
        Button_10.configure(command=lambda:JSQ_cmd.Button_10_onCommand(className,"Button_10"))
        Fun.AddElement(className,'Button_10',Button_10)
        Button_11= tkinter.Button(root,text="9",width = 10,height = 4)
        Button_11.place(x = 110,y = 130,width = 40,height = 30)
        Button_11.configure(relief = "groove")
        Button_11.configure(command=lambda:JSQ_cmd.Button_11_onCommand(className,"Button_11"))
        Fun.AddElement(className,'Button_11',Button_11)
        Button_12= tkinter.Button(root,text="0",width = 10,height = 4)
        Button_12.place(x = 10,y = 170,width = 40,height = 30)
        Button_12.configure(relief = "groove")
        Button_12.configure(command=lambda:JSQ_cmd.Button_12_onCommand(className,"Button_12"))
        Fun.AddElement(className,'Button_12',Button_12)
        Button_13= tkinter.Button(root,text="C",width = 10,height = 4)
        Button_13.place(x = 60,y = 170,width = 40,height = 30)
        Button_13.configure(relief = "groove")
        Button_13.configure(command=lambda:JSQ_cmd.Button_13_onCommand(className,"Button_13"))
        Fun.AddElement(className,'Button_13',Button_13)
        Button_14= tkinter.Button(root,text="=",width = 10,height = 4)
        Button_14.place(x = 110,y = 169,width = 40,height = 30)
        Button_14.configure(relief = "groove")
        Button_14.configure(command=lambda:JSQ_cmd.Button_14_onCommand(className,"Button_14"))
        Fun.AddElement(className,'Button_14',Button_14)
        Button_15= tkinter.Button(root,text="+",width = 10,height = 4)
        Button_15.place(x = 160,y = 50,width = 40,height = 30)
        Button_15.configure(relief = "groove")
        Button_15.configure(command=lambda:JSQ_cmd.Button_15_onCommand(className,"Button_15"))
        Fun.AddElement(className,'Button_15',Button_15)
        Button_16= tkinter.Button(root,text="-",width = 10,height = 4)
        Button_16.place(x = 160,y = 90,width = 40,height = 30)
        Button_16.configure(relief = "groove")
        Button_16.configure(command=lambda:JSQ_cmd.Button_16_onCommand(className,"Button_16"))
        Fun.AddElement(className,'Button_16',Button_16)
        Button_17= tkinter.Button(root,text="X",width = 10,height = 4)
        Button_17.place(x = 160,y = 130,width = 40,height = 30)
        Button_17.configure(relief = "groove")
        Button_17.configure(command=lambda:JSQ_cmd.Button_17_onCommand(className,"Button_17"))
        Fun.AddElement(className,'Button_17',Button_17)
        Button_18= tkinter.Button(root,text="/",width = 10,height = 4)
        Button_18.place(x = 160,y = 170,width = 40,height = 30)
        Button_18.configure(relief = "groove")
        Button_18.configure(command=lambda:JSQ_cmd.Button_18_onCommand(className,"Button_18"))
        Fun.AddElement(className,'Button_18',Button_18)
        #Create the Menu of root 
        MainMenu=tkinter.Menu(root)
        root.config(menu = MainMenu)
        A=tkinter.Menu(MainMenu,tearoff = 0)
        A1=tkinter.Menu(A,tearoff = 0)
        A1.add_command(label="A11",command=lambda:JSQ_cmd.Menu_A11(className,"A11"))
        A.add_cascade(label="A1",menu=A1)
        MainMenu.add_cascade(label="A",menu=A)
        B=tkinter.Menu(MainMenu,tearoff = 0)
        B.add_command(label="B2",command=lambda:JSQ_cmd.Menu_B2(className,"B2"))
        MainMenu.add_cascade(label="B",menu=B)
        #Inital all element's Data 
        Fun.InitElementData(className)
        #Add Some Logic Code Here: (Keep This Line of comments)

#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = JSQ(root)
    root.mainloop()
