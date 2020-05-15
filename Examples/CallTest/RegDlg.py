#coding=utf-8

#import libs 
import RegDlg_cmd
import Fun
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
from   PIL import Image,ImageTk

ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  RegDlg:
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
          root.geometry("454x410")
      Form_1= tkinter.Canvas(root,width = 10,height = 4)
      Form_1.place(x = 0,y = 0,width = 454,height = 410)
      Form_1.configure(bg = "#efefef")
      Fun.AddElement(className,'root',root)
      Fun.AddElement(className,'Form_1',Form_1)
      Group_1_Variable = Fun.AddElementVariable(className,'Group_1')
      Group_1_Variable.set(1)
      #Create the elements of root 
      Label_2= tkinter.Label(root,text="",width = 10,height = 4)
      Label_2.place(x = 48,y = 33,width = 77,height = 48)
      ElementBGArray[2]=Image.open("ico1.png")
      ElementBGArray_Resize[2]=ElementBGArray[2].resize((77, 48),Image.ANTIALIAS)
      ElementBGArray_IM[2]=ImageTk.PhotoImage(ElementBGArray_Resize[2])
      Label_2.configure(image = ElementBGArray_IM[2])
      Label_2_Ft=tkinter.font.Font(family='System', size=24,weight='bold',slant='roman',underline=0,overstrike=0)
      Label_2.configure(font = Label_2_Ft)
      Fun.AddElement(className,'Label_2',Label_2)
      Label_3= tkinter.Label(root,text="注册信息",width = 10,height = 4)
      Label_3.place(x = 134,y = 34,width = 256,height = 45)
      Label_3_Ft=tkinter.font.Font(family='System', size=29,weight='bold',slant='roman',underline=0,overstrike=0)
      Label_3.configure(font = Label_3_Ft)
      Fun.AddElement(className,'Label_3',Label_3)
      Label_4= tkinter.Label(root,text="姓名",width = 10,height = 4)
      Label_4.place(x = 53,y = 111,width = 100,height = 20)
      Fun.AddElement(className,'Label_4',Label_4)
      Entry_5_Variable = Fun.AddElementVariable(className,'Entry_5')
      Entry_5= tkinter.Entry(root,textvariable=Entry_5_Variable)
      Entry_5.place(x = 175,y = 110,width = 120,height = 20)
      Entry_5.configure(relief = "sunken")
      Fun.AddElement(className,'Entry_5',Entry_5)
      Label_6= tkinter.Label(root,text="性别",width = 10,height = 4)
      Label_6.place(x = 54,y = 146,width = 100,height = 20)
      Fun.AddElement(className,'Label_6',Label_6)
      RadioButton_7= tkinter.Radiobutton(root,variable=Group_1_Variable,value=1,text="男",anchor=tkinter.W)
      RadioButton_7.place(x = 173,y = 147,width = 48,height = 20)
      Fun.AddElement(className,'RadioButton_7',RadioButton_7)
      RadioButton_8= tkinter.Radiobutton(root,variable=Group_1_Variable,value=2,text="女",anchor=tkinter.W)
      RadioButton_8.place(x = 243,y = 149,width = 48,height = 20)
      Fun.AddElement(className,'RadioButton_8',RadioButton_8)
      Label_9= tkinter.Label(root,text="邮箱",width = 10,height = 4)
      Label_9.place(x = 54,y = 181,width = 100,height = 20)
      Fun.AddElement(className,'Label_9',Label_9)
      Entry_10_Variable = Fun.AddElementVariable(className,'Entry_10')
      Entry_10= tkinter.Entry(root,textvariable=Entry_10_Variable)
      Entry_10.place(x = 175,y = 185,width = 195,height = 20)
      Entry_10.configure(relief = "sunken")
      Fun.AddElement(className,'Entry_10',Entry_10)
      Label_11= tkinter.Label(root,text="个人简介",width = 10,height = 4)
      Label_11.place(x = 55,y = 220,width = 100,height = 20)
      Fun.AddElement(className,'Label_11',Label_11)
      Text_12= tkinter.Text(root)
      Text_12.place(x = 175,y = 220,width = 240,height = 120)
      Text_12.configure(relief = "sunken")
      Fun.AddElement(className,'Text_12',Text_12)
      Button_13= tkinter.Button(root,text="确定",width = 10,height = 4)
      Button_13.place(x = 176,y = 354,width = 100,height = 28)
      Button_13.configure(command =lambda:RegDlg_cmd.Button_13_onCommand(className,"Button_13"))
      Fun.AddElement(className,'Button_13',Button_13)
      Button_14= tkinter.Button(root,text="取消",width = 10,height = 4)
      Button_14.place(x = 310,y = 354,width = 100,height = 28)
      Button_14.configure(command =lambda:RegDlg_cmd.Button_14_onCommand(className,"Button_14"))
      Fun.AddElement(className,'Button_14',Button_14)
      #Inital all element's Data 
      Fun.InitElementData(className)
      #Add Some Logic Code Here: (Keep This Line of comments)

#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = RegDlg(root)
    root.mainloop()
