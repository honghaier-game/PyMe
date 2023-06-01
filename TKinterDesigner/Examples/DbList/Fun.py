#This file does not support direct editing

#coding=utf-8
import os
from   os.path import abspath, dirname
import tkinter
import tkinter.simpledialog

G_UIElementUserDataArray={}
G_UIElementArray={}
G_UIElementVariableArray={}
G_UIInputDataArray={} 
G_UIElementAlias={}
G_UIGroupDictionary={}
G_UIStyleDictionary={}
G_CurrentFilePath=None
G_CutContent=None
#Register a control to record it:Param1：uiName, Param2:elementName，Param3：element
def Register(uiName,elementName,element,alias=None,groupName=None,styleName=None):
    if uiName not in G_UIElementArray:
        G_UIElementArray[uiName]={}
        G_UIElementAlias[uiName]={}
        G_UIGroupDictionary[uiName]={}
        G_UIStyleDictionary[uiName]={}
    G_UIElementArray[uiName][elementName]=element
    if alias:
        G_UIElementAlias[uiName][alias]=elementName
    if groupName:
        G_UIGroupDictionary[uiName][elementName]=groupName
    if styleName:
        G_UIStyleDictionary[uiName][elementName]=styleName
#Get the Element:Param1：uiName, Param2：elementName
def GetElement(uiName,elementName):
    if uiName in G_UIElementAlias:
        if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
            elementName = G_UIElementArray[uiName][elementName]
    if uiName in G_UIElementArray:
        if elementName in G_UIElementArray[uiName]:
            return G_UIElementArray[uiName][elementName]
    return None
#Add a TKiner Variable to Control:Param1：uiName, Param2:elementName,Param3:Default Value
def AddTKVariable(uiName,elementName,defaultValue = None):
    if uiName not in G_UIElementVariableArray:
        G_UIElementVariableArray[uiName]={}
    NameLower = elementName.lower()
    if NameLower.find('combobox_') >= 0:
        G_UIElementVariableArray[uiName][elementName]=tkinter.IntVar()
    elif NameLower.find('group_') >= 0:
        G_UIElementVariableArray[uiName][elementName]=tkinter.IntVar()
    elif NameLower.find('checkbutton_') >= 0:
        G_UIElementVariableArray[uiName][elementName]=tkinter.BooleanVar()
    else:
        G_UIElementVariableArray[uiName][elementName]=tkinter.StringVar()
    if defaultValue:
        G_UIElementVariableArray[uiName][elementName].set(defaultValue) 
    return G_UIElementVariableArray[uiName][elementName]
#Set the TKiner Variable of Control:Param1：uiName, Param2:elementName, Param3:value
def SetTKVariable(uiName,elementName,value):
    if uiName in G_UIElementVariableArray:
        if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
            elementName = G_UIElementAlias[uiName][elementName]
        if elementName in G_UIElementVariableArray[uiName]:
            G_UIElementVariableArray[uiName][elementName].set(value)
        if elementName in G_UIGroupDictionary[uiName]:
            GroupName = G_UIGroupDictionary[uiName][elementName]
            if GroupName in G_UIElementVariableArray[uiName]:
                G_UIElementVariableArray[uiName][GroupName].set(value)
#Get the TKiner Variable of Control:Param1：uiName, Param2:elementName
def GetTKVariable(uiName,elementName):
    if uiName in G_UIElementVariableArray:
        if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
            elementName = G_UIElementAlias[uiName][elementName]
        if elementName in G_UIElementVariableArray[uiName]:
            return G_UIElementVariableArray[uiName][elementName].get()
        if elementName in G_UIGroupDictionary[uiName]:
            GroupName = G_UIGroupDictionary[uiName][elementName]
            if GroupName in G_UIElementVariableArray[uiName]:
                return G_UIElementVariableArray[uiName][GroupName].get()
    return None
#Add a user data to control.The parameter dataname is the data name and datatype is the data type, which can include int, float, string, list, dictionary, etc. generally, the control is operated by the right mouse button in the design software and set in the pop-up "bind data variable".The parameter datavalue is the data value, and ismaptotext is whether to directly reflect the data to the text variable of the control
def AddUserData(uiName,elementName,dataName,datatype,datavalue,isMapToText):
    global G_UIElementUserDataArray
    if uiName not in G_UIElementUserDataArray:
        G_UIElementUserDataArray[uiName]={} 
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    if elementName not in G_UIElementUserDataArray[uiName]:
        G_UIElementUserDataArray[uiName][elementName]=[]
    G_UIElementUserDataArray[uiName][elementName].append([dataName,datatype,datavalue,isMapToText])
#Set the user data value of the control.
def SetUserData(uiName,elementName,dataName,datavalue):
    global G_UIElementArray
    global G_UIElementUserDataArray
    if uiName in G_UIElementUserDataArray:
        if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
            elementName = G_UIElementAlias[uiName][elementName]
        if elementName in G_UIElementUserDataArray[uiName]:
            for EBData in G_UIElementUserDataArray[uiName][elementName]:
                if EBData[0] == dataName:
                    EBData[2] = datavalue
                    if EBData[3] == 1:
                        SetText(uiName,elementName,datavalue) 
                    return
#Get the user data value of the control.
def GetUserData(uiName,elementName,dataName):
    global G_UIElementUserDataArray
    if  uiName in G_UIElementUserDataArray:
        if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
            elementName = G_UIElementAlias[uiName][elementName]
        if elementName in G_UIElementUserDataArray[uiName]:
            for EBData in G_UIElementUserDataArray[uiName][elementName]:
                if EBData[0] == dataName:
                    if EBData[1]=='int':
                        return int(EBData[2])
                    elif EBData[1]=='float':
                        return float(EBData[2])
                    else:
                        return EBData[2]
    return None
#Set the tkinter attribute value of the control.
def SetTKAttrib(uiName,elementName,AttribName,attribValue):
    global G_UIElementArray
    if uiName in G_UIElementArray:
        if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
            elementName = G_UIElementAlias[uiName][elementName]
        if AttribName in G_UIElementArray[uiName][elementName].configure().keys():
            G_UIElementArray[uiName][elementName][AttribName]=attribValue
#Get the tkinter attribute value of the control.
def GetTKAttrib(uiName,elementName,AttribName):
    global G_UIElementArray
    if uiName in G_UIElementArray:
        if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
            elementName = G_UIElementAlias[uiName][elementName]
        return G_UIElementArray[uiName][elementName].cget(AttribName)
#Set the text of the control(label, button, entry and text)
def SetText(uiName,elementName,textValue):
    global G_UIElementArray
    global G_UIElementVariableArray
    showtext = str("%s"%textValue)
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    if uiName in G_UIElementVariableArray:
        if elementName in G_UIElementVariableArray[uiName]:
            G_UIElementVariableArray[uiName][elementName].set(showtext)
            return
    if uiName in G_UIElementArray:
        if elementName in G_UIElementArray[uiName]:
            if elementName.find('Text_') >= 0:
                G_UIElementArray[uiName][elementName].delete('0.0',tkinter.END)
                G_UIElementArray[uiName][elementName].insert(tkinter.END,showtext)
            else:
                G_UIElementArray[uiName][elementName].configure(text=showtext)
#Get the text of the control(label, button, entry and text)
def GetText(uiName,elementName):
    global G_UIElementArray
    global G_UIElementVariableArray
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    if uiName in G_UIElementVariableArray:
        if elementName in G_UIElementVariableArray[uiName]:
            return G_UIElementVariableArray[uiName][elementName].get()
    if uiName in G_UIElementArray:
        if elementName in G_UIElementArray[uiName]:
            if elementName.find('Text_') >= 0:
                return G_UIElementArray[uiName][elementName].get('0.0', tkinter.END)
            elif elementName.find('Spinbox_') >= 0:
                return str(G_UIElementArray[uiName][elementName].get())
            else:
                return G_UIElementArray[uiName][elementName].cget('text')
    return str("")
#Set the image of the control(Label,Button).
def SetImage(uiName,elementName,imagePath):
    global G_UIElementVariableArray
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    if elementName.find('Label_') == 0 or elementName.find('Button_') == 0 :
        Control = GetElement(uiName,elementName)
        if Control != None:
            if uiName in G_UIElementUserDataArray:
                if elementName in G_UIElementUserDataArray[uiName]:
                    for EBData in G_UIElementUserDataArray[uiName][elementName]:
                        if EBData[0] == 'image':
                            EBData[1] = imagePath
                            from   PIL import Image,ImageTk
                            image=Image.open(imagePath).convert('RGBA')
                            image_Resize = image.resize((Control.winfo_width(), Control.winfo_height()),Image.ANTIALIAS)
                            EBData[2] = ImageTk.PhotoImage(image_Resize)
                            Control.configure(image = EBData[2])
                            return 
            from   PIL import Image,ImageTk
            image=Image.open(imagePath).convert('RGBA')
            image_Resize = image.resize((Control.winfo_width(), Control.winfo_height()),Image.ANTIALIAS)
            EBData2 = ImageTk.PhotoImage(image_Resize)
            AddUserData(uiName,elementName,'image',imagePath,EBData2,0)
            Control.configure(image = EBData2)
#Get the image file of the control(Label,Button).
def GetImage(uiName,elementName):
    global G_UIElementVariableArray
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    if elementName.find('Label_') == 0 or elementName.find('Button_') == 0 :
        Control = GetElement(uiName,elementName)
        if Control != None:
            if uiName in G_UIElementUserDataArray:
                if elementName in G_UIElementUserDataArray[uiName]:
                    for EBData in G_UIElementUserDataArray[uiName][elementName]:
                        if EBData[0] == 'image':
                            return EBData[1]
    return str("")
#Set the selected index of the combobox or listbox.
def SetSelectIndex(uiName,elementName,index):
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        if elementName.find('ComboBox_') == 0 :
            Control.current(index)
        elif elementName.find('ListBox_') == 0 :
            Control.select_set(index)
#Get the selected index of the combobox or listbox.
def GetSelectIndex(uiName,elementName):
    if uiName in G_UIElementAlias.keys() and elementName in G_UIElementAlias[uiName].keys():
        elementName = G_UIElementAlias[uiName][elementName]
    Control = GetElement(uiName,elementName)
    if Control != None:
        if elementName.find('ComboBox_') == 0 :
            return Control.current()
        elif elementName.find('ListBox_') == 0 :
            currIndex = Control.curselection()
            if len(currIndex) > 0 and currIndex[0] >= 0:
                return currIndex[0]
    return -1
#Initialize all user binding data without manual call.
def InitElementData(uiName):
    global G_UIElementUserDataArray
    if uiName in G_UIElementUserDataArray:
        for elementName in G_UIElementUserDataArray[uiName].keys():
            for EBData in G_UIElementUserDataArray[uiName][elementName]:
                if EBData[3] == 1:
                    SetText(uiName,elementName,EBData[2])
                    SetText(uiName,elementName,EBData[2])
#Initialize all control style without manual call.
def InitElementStyle(uiName,Style):
    StyleArray = ReadStyleFile(Style+".py")
    global G_UIElementArray
    if uiName in G_UIElementArray:
        Root = GetElement(uiName,'root')
        TFormKey = '.TForm'
        if TFormKey in StyleArray:
            if 'background' in StyleArray[TFormKey]:
                Root['background'] = StyleArray[TFormKey]['background']
        for elementName in G_UIElementArray[uiName].keys():
            Widget = G_UIElementArray[uiName][elementName]
            try:
                if  Widget.winfo_exists() == 1:
                    WinClass = Widget.winfo_class()
                    StyleName = ".T"+WinClass
                    for attribute in StyleArray[StyleName].keys():
                        Widget[attribute] = StyleArray[StyleName][attribute]
            except BaseException:
                continue
#Get all the entry data of an interface.
def GetInputDataArray(uiName):
    global G_UIElementArray
    global G_UIInputDataArray
    global G_UIElementVariableArray
    G_UIInputDataArray.clear()
    if uiName in G_UIElementArray:
        for elementName in G_UIElementArray[uiName].keys():
            G_UIInputDataArray[elementName] = []
            Widget = G_UIElementArray[uiName][elementName]
            if elementName.find('Text_') >= 0:
                content = Widget.get('0.0', tkinter.END)
                G_UIInputDataArray[elementName].append(content)
            elif elementName.find('Entry_') >= 0:
                content = G_UIElementVariableArray[uiName][elementName].get()
                G_UIInputDataArray[elementName].append(content)
    if uiName in G_UIElementVariableArray:
        for elementName in G_UIElementVariableArray[uiName].keys():
           if elementName.find('Group_') >= 0:
                ElementIntValue = G_UIElementVariableArray[uiName][elementName].get()
                G_UIInputDataArray[elementName] = []
                G_UIInputDataArray[elementName].append(ElementIntValue)
    return G_UIInputDataArray
#Center a pop-up interface dialog box.
def CenterDlg(uiName,popupDlg,dw=0,dh=0):
    if dw == 0:
        dw = popupDlg.winfo_width()
    if dh == 0:
        dh = popupDlg.winfo_height()
    root = GetElement(uiName,'root')
    if root != None:
       sw = root.winfo_width()
       sh = root.winfo_height()
       sx = root.winfo_x()
       sy = root.winfo_y()
       popupDlg.geometry('%dx%d+%d+%d'%(dw,dh,sx+(sw-dw)/2,sy+(sh-dh)/2))
    else:
       import ctypes
       user32 = ctypes.windll.user32
       sw = user32.GetSystemMetrics(0)
       sh = user32.GetSystemMetrics(1)
       sx = 0
       sy = 0
       popupDlg.geometry('%dx%d+%d+%d'%(dw,dh,sx+(sw-dw)/2,sy+(sh-dh)/2))
#The rounded property of the control is called in the interface Layout Pyfile, but because the interface has not been created, it is necessary to call ShowRoundedRectangle two times later. Note: this function does not cross platform.
def SetRoundedRectangle(control,WidthEllipse=20,HeightEllipse=20):
    if control != None:
       control.after(10, lambda: ShowRoundedRectangle(control,WidthEllipse,HeightEllipse))
#Set the fillet property of the control immediately.Note: this function does not cross platform.
def ShowRoundedRectangle(control,WidthEllipse,HeightEllipse):
    import win32gui
    HRGN = win32gui.CreateRoundRectRgn(0,0,control.winfo_width(),control.winfo_height(),WidthEllipse,HeightEllipse)
    win32gui.SetWindowRgn(control.winfo_id(), HRGN,1)
#Pop up a message dialog box.
def MessageBox(text):
    tkinter.messagebox.showwarning('info',text)
#Pop up a input dialog box.
def InputBox(title,text):
    res = tkinter.simpledialog.askstring(title,'Input Box',initialvalue=text)
    return res
#Pop up a question dialog box,You need choose yes or no.
def AskBox(title,text):
    res = tkinter.messagebox.askyesno(title,text)
    return res
#Returns all the files in the directory.
def WalkAllResFiles(parentPath,alldirs=True,extName=None):
    ResultFilesArray = []
    if os.path.exists(parentPath) == True:
        for fileName in os.listdir(parentPath):
            if '__pycache__' not in fileName:
                if '.git' not in fileName:
                    newPath = parentPath +'\\'+ fileName
                    if os.path.isdir(newPath):
                        if extName == None:
                           ResultFilesArray.append(newPath)
                        if alldirs == True:
                            ResultFilesArray.extend(WalkAllResFiles(newPath,alldirs,extName))
                    else:
                        if extName == None:
                            ResultFilesArray.append(newPath)
                        else:
                            file_extension = os.path.splitext(fileName)[1].replace('.','')
                            file_extension_lower = file_extension.lower().strip()
                            file_extName_lower = extName.lower().strip()
                            if file_extension_lower == file_extName_lower:
                                ResultFilesArray.append(newPath)
    return ResultFilesArray
#Redefine the event response function to have the specified parameter.
def EventFunction_Adaptor(fun,  **params):
    return lambda event, fun=fun, params=params: fun(event, **params)
#Sets the absolute or relative position of the control.
def SetControlPlace(control,x,y,w,h):
    control.place(x=0,y=0,width=0,height=0)
    control.place(relx=0,rely=0,relwidth=0,relheight=0)
    if type(x) == type(1.0):
        if type(y) == type(1.0):
            if type(w) == type(1.0):
                if type(h) == type(1.0):
                   control.place(relx=x,rely=y,relwidth=w,relheight=h)
                else:
                   control.place(relx=x,rely=y,relwidth=w,height=h)
            else:
                if type(h) == type(1.0):
                   control.place(relx=x,rely=y,width=w,relheight=h)
                else:
                   control.place(relx=x,rely=y,width=w,height=h)
        else:
            if type(w) == type(1.0):
                if type(h) == type(1.0):
                   control.place(relx=x,y=y,relwidth=w,relheight=h)
                else:
                   control.place(relx=x,y=y,relwidth=w,height=h)
            else:
                if type(h) == type(1.0):
                   control.place(relx=x,y=y,relwidth=w,relheight=h)
                else:
                   control.place(relx=x,y=y,relwidth=w,height=h)
    else:
        if type(y) == type(1.0):
            if type(w) == type(1.0):
                if type(h) == type(1.0):
                   control.place(x=x,rely=y,relwidth=w,relheight=h)
                else:
                   control.place(x=x,rely=y,relwidth=w,height=h)
            else:
                if type(h) == type(1.0):
                   control.place(x=x,rely=y,width=w,relheight=h)
                else:
                   control.place(x=x,rely=y,width=w,height=h)
        else:
            if type(w) == type(1.0):
                if type(h) == type(1.0):
                   control.place(x=x,y=y,relwidth=w,relheight=h)
                else:
                   control.place(x=x,y=y,relwidth=w,height=h)
            else:
                if type(h) == type(1.0):
                   control.place(x=x,y=y,width=w,relheight=h)
                else:
                   control.place(x=x,y=y,width=w,height=h)
#Define a window class that can drag, move and drag the size of the border.
class WindowDraggable():
    def __init__(self,widget,bordersize = 6,bordercolor = '#444444'):
        self.widget = widget
        widget.bind('<Enter>',self.Enter)
        widget.bind('<Motion>',self.Motion)
        widget.bind('<Leave>',self.Leave)
        widget.bind('<ButtonPress-1>',self.StartDrag)
        widget.bind('<ButtonRelease-1>',self.StopDrag)
        widget.bind('<B1-Motion>',self.MoveDragPos)
        self.bordersize = bordersize
        self.bordercolor = bordercolor
        self.top_drag = None
        self.left_drag = None
        self.right_drag = None
        self.bottom_drag = None
        self.topleft_drag = None
        self.bottomleft_drag = None
        self.topright_drag = None
        self.bottomright_drag = None
        widget.after(10, lambda: self.ShowWindowIcoToBar(widget))
    def ShowWindowIcoToBar(self,widget):
        GWL_EXSTYLE=-20
        WS_EX_APPWINDOW=0x00040000
        WS_EX_TOOLWINDOW=0x00000080
        from ctypes import windll
        hwnd = windll.user32.GetParent(widget.winfo_id())
        style = windll.user32.GetWindowLongPtrW(hwnd, GWL_EXSTYLE)
        style = style & ~WS_EX_TOOLWINDOW
        style = style | WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongPtrW(hwnd, GWL_EXSTYLE, style)
        widget.wm_withdraw()
        widget.after(10, lambda: widget.wm_deiconify())
    def Enter(self,event):
        if self.widget == event.widget or event.widget.winfo_class() =="Canvas":
            formx = self.widget.winfo_x() 
            formy = self.widget.winfo_y() 
            formw = self.widget.winfo_width() 
            formh = self.widget.winfo_height()
            x = event.x_root - formx
            y = event.y_root - formy
    def Motion(self,event):
        if self.widget == event.widget or event.widget.winfo_class() =="Canvas":
            formx = self.widget.winfo_x() 
            formy = self.widget.winfo_y() 
            formw = self.widget.winfo_width() 
            formh = self.widget.winfo_height()
            x = event.x_root - formx
            y = event.y_root - formy
            if ((x >= 0) and (x <= self.bordersize) and (y >= 0) and (y <= self.bordersize)):
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TL)
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_TL)
                self.top_drag.place(x = 0,y = 0,width = formw,height = self.bordersize)
                self.top_drag.configure(bg = self.bordercolor)
                self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = formh)
                self.left_drag.configure(bg = self.bordercolor)
            if ((y >= 0) and (y <= self.bordersize)):
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_V1)
                self.top_drag.bind('<Motion>',self.MotionDragBorder)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder)
                self.top_drag.place(x = 0,y = 0,width = formw,height = self.bordersize)
                self.top_drag.configure(bg = self.bordercolor)
            if ((y >= (formh - self.bordersize)) and (y <= formh)):
                if self.bottom_drag == None:
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_V2)
                self.bottom_drag.bind('<Motion>',self.MotionDragBorder)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder)
                self.bottom_drag.place(x = 0,y = (formh - self.bordersize),width = formw,height = self.bordersize)
                self.bottom_drag.configure(bg = self.bordercolor)
            if ((x >= 0 ) and (x <= self.bordersize)):
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_H1)
                self.left_drag.bind('<Motion>',self.MotionDragBorder)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder)
                self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = formh)
                self.left_drag.configure(bg = self.bordercolor)
            if ((x >= (formw - self.bordersize)) and (x <= formw)):
                if self.right_drag == None:
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_H2)
                self.right_drag.bind('<Motion>',self.MotionDragBorder)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder)
                self.right_drag.place(x = (formw - self.bordersize),y = 0,width = self.bordersize,height = formh)
                self.right_drag.configure(bg = self.bordercolor)
    def Leave(self,event):
        if self.widget == event.widget or event.widget.winfo_class() =="Canvas":
            pass
    def StartDrag(self,event):
        self.x = event.x_root
        self.y = event.y_root
    def StopDrag(self,event):
        self.x = None
        self.y = None
        self.widget.configure(cursor='arrow')
    def MoveDragPos(self,event):
        if self.widget == event.widget or event.widget.winfo_class() =="Canvas":
            formx = self.widget.winfo_x() 
            formy = self.widget.winfo_y() 
            formw = self.widget.winfo_width() 
            formh = self.widget.winfo_height()
            x = event.x_root - formx
            y = event.y_root - formy
            deltaX = event.x_root - self.x
            deltaY = event.y_root - self.y
            newX = self.widget.winfo_x() + deltaX
            newY = self.widget.winfo_y() + deltaY
            geoinfo = str('%dx%d+%d+%d'%(self.widget.winfo_width(),self.widget.winfo_height(),newX,newY))
            self.widget.geometry(geoinfo)
            self.x = event.x_root
            self.y = event.y_root
    def MoveDragSize_H1(self,event):
        deltaX = event.x_root - self.x
        formx = self.widget.winfo_x() + deltaX
        newW = self.widget.winfo_width() - deltaX
        geoinfo = str('%dx%d+%d+%d'%(newW,self.widget.winfo_height(),formx,self.widget.winfo_y()))
        self.widget.geometry(geoinfo)
        self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = self.widget.winfo_height())
        self.x = event.x_root
        self.widget.configure(cursor='plus')
    def MoveDragSize_H2(self,event):
        deltaX = event.x_root - self.x
        formw = self.widget.winfo_width() 
        formh = self.widget.winfo_height()
        newW = self.widget.winfo_width() + deltaX
        geoinfo = str('%dx%d+%d+%d'%(newW,self.widget.winfo_height(),self.widget.winfo_x(),self.widget.winfo_y()))
        self.widget.geometry(geoinfo)
        self.right_drag.place(x = newW-self.bordersize,y = 0,width = self.bordersize,height = formh)
        self.x = event.x_root
        self.widget.configure(cursor='plus')
    def MoveDragSize_V1(self,event):
        deltaY = event.y_root - self.y
        formy = self.widget.winfo_y() + deltaY
        newH = self.widget.winfo_height() - deltaY
        geoinfo = str('%dx%d+%d+%d'%(self.widget.winfo_width() ,newH,self.widget.winfo_x(),formy))
        self.widget.geometry(geoinfo)
        self.top_drag.place(x = 0,y = 0,width = self.widget.winfo_width(),height = self.bordersize)
        self.y = event.y_root
        self.widget.configure(cursor='plus')
    def MoveDragSize_V2(self,event):
        deltaY = event.y_root - self.y
        newH = self.widget.winfo_height() + deltaY
        geoinfo = str('%dx%d+%d+%d'%(self.widget.winfo_width(),newH,self.widget.winfo_x(),self.widget.winfo_y()))
        self.widget.geometry(geoinfo)
        self.bottom_drag.place(x = 0,y = (newH - self.bordersize),width = self.widget.winfo_width(),height = self.bordersize)
        self.y = event.y_root
        self.widget.configure(cursor='plus')
    def MotionDragBorder(self,event):
        formx = self.widget.winfo_x() 
        formy = self.widget.winfo_y() 
        formw = self.widget.winfo_width() 
        formh = self.widget.winfo_height() 
        x = event.x_root - formx
        y = event.y_root - formy
        if event.widget == self.left_drag:
            if y >=0 and y <= self.bordersize:
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.place(x = 0,y = 0,width = formw,height = self.bordersize)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TL)
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_TL)
            if y >=(formh-self.bordersize) and y <= formh:
                if self.bottom_drag == None:
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.place(x = 0,y = formh-self.bordersize,width = formw,height = self.bordersize)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_BL)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder_BL)
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_BL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_BL)
        if event.widget == self.right_drag:
            if y >=0 and y <= self.bordersize:
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.place(x = 0,y = 0,width = formw,height = self.bordersize)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TR)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TR)
                if self.right_drag == None:
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_TR)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder_TR)
            if y >=(formh-self.bordersize) and y <= formh:
                if self.bottom_drag == None:
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.place(x = 0,y = formh-self.bordersize,width = formw,height = self.bordersize)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_BR)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder_BR)
                if self.right_drag == None:
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_BR)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder_BR)
        if event.widget == self.top_drag:
            if x >=0 and x <= self.bordersize:
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TL)
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = formh)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_TL)
            if x >=(formw-self.bordersize) and x <= formw:
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TR)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TR)
                if self.right_drag == None:
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.place(x = formw-self.bordersize,y = 0,width = self.bordersize,height = formh)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_TR)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder_TR)
        if event.widget == self.bottom_drag:
            if x >=0 and x <= self.bordersize:
                if self.bottom_drag == None:
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_BL)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder_BL)
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = formh)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_BL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_BL)
            if x >=(formw-self.bordersize) and x <= formw:
                if self.bottom_drag == None:
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_BR)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder_BR)  
                if self.right_drag == None:
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.place(x = formw-self.bordersize,y = 0,width = self.bordersize,height = formh)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_BR)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder_BR)
    def LeaveDragBorder(self,event):
        event.widget.place_forget()
    def MoveDragSize_TL(self,event):
        deltaX = event.x_root - self.x
        deltaY = event.y_root - self.y
        formx = self.widget.winfo_x() + deltaX
        newW = self.widget.winfo_width() - deltaX
        formy = self.widget.winfo_y() + deltaY
        newH = self.widget.winfo_height() - deltaY
        geoinfo = str('%dx%d+%d+%d'%(newW,newH,formx,formy))
        self.widget.geometry(geoinfo)
        self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = self.widget.winfo_height())
        self.top_drag.place(x = 0,y = 0,width = self.widget.winfo_width(),height = self.bordersize)
        self.x = event.x_root
        self.y = event.y_root
        self.widget.configure(cursor='plus')
    def LeaveDragBorder_TL(self,event):
        self.left_drag.place_forget()
        self.top_drag.place_forget()
        self.widget.configure(cursor='arrow')
    def MoveDragSize_TR(self,event):
        deltaX = event.x_root - self.x
        deltaY = event.y_root - self.y
        formx = self.widget.winfo_x()
        newW = self.widget.winfo_width() + deltaX
        formy = self.widget.winfo_y() + deltaY
        newH = self.widget.winfo_height() - deltaY
        geoinfo = str('%dx%d+%d+%d'%(newW,newH,formx,formy))
        self.widget.geometry(geoinfo)
        self.right_drag.place(x = newW-self.bordersize,y = 0,width = self.bordersize,height = self.widget.winfo_height())
        self.top_drag.place(x = 0,y = 0,width = self.widget.winfo_width(),height = self.bordersize)
        self.x = event.x_root
        self.y = event.y_root
        self.widget.configure(cursor='plus')
    def LeaveDragBorder_TR(self,event):
        self.right_drag.place_forget()
        self.top_drag.place_forget()
        self.widget.configure(cursor='arrow')
    def MoveDragSize_BL(self,event):
        deltaX = event.x_root - self.x
        deltaY = event.y_root - self.y
        formx = self.widget.winfo_x() + deltaX
        newW = self.widget.winfo_width() - deltaX
        formy = self.widget.winfo_y()
        newH = self.widget.winfo_height() + deltaY
        geoinfo = str('%dx%d+%d+%d'%(newW,newH,formx,formy))
        self.widget.geometry(geoinfo)
        self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = self.widget.winfo_height())
        self.bottom_drag.place(x = 0,y = newH-self.bordersize,width = self.widget.winfo_width(),height = self.bordersize)
        self.x = event.x_root
        self.y = event.y_root
        self.widget.configure(cursor='plus')
    def LeaveDragBorder_BL(self,event):
        self.left_drag.place_forget()
        self.bottom_drag.place_forget()
        self.widget.configure(cursor='arrow')
    def MoveDragSize_BR(self,event):
        deltaX = event.x_root - self.x
        deltaY = event.y_root - self.y
        formx = self.widget.winfo_x()
        newW = self.widget.winfo_width() + deltaX
        formy = self.widget.winfo_y()
        newH = self.widget.winfo_height() + deltaY
        geoinfo = str('%dx%d+%d+%d'%(newW,newH,formx,formy))
        self.widget.geometry(geoinfo)
        self.right_drag.place(x = newW-self.bordersize,y = 0,width = self.bordersize,height = self.widget.winfo_height())
        self.bottom_drag.place(x = 0,y = newH-self.bordersize,width = self.widget.winfo_width(),height = self.bordersize)
        self.x = event.x_root
        self.y = event.y_root
        self.widget.configure(cursor='plus')
    def LeaveDragBorder_BR(self,event):
        self.right_drag.place_forget()
        self.bottom_drag.place_forget() 
        self.widget.configure(cursor='arrow')
#Set the fillet parameter of TK root, support cross platform.
def SetRootRoundRectangle(canvas,x1, y1, x2, y2, radius=25,**kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)
#Read content from file.
def ReadFromFile(filePath):
    content = None
    if filePath != None:
        if os.path.exists(filePath) == True: 
            f = open(filePath,mode='r',encoding='utf-8')
            if f != None:
                content = f.read()
                f.close()
    return content
#Writing content to a file.
def WriteToFile(filePath,content):
    if filePath != None:
        f = open(filePath,mode='w',encoding='utf-8')
        if f != None:
            if content != None:
                f.write(content)
            f.close()
            return True
    return False
#Read style file.
def ReadStyleFile(filePath):
    StyleArray = {}
    if len(filePath)==0 :
        return StyleArray
    if os.path.exists(filePath) == False:
        return StyleArray
    f = open(filePath,encoding='utf-8')
    line =""
    while True:
        line = f.readline()
        if not line:
            break
        text = line.strip()
        if not text:
            continue
        if text.find('style = tkinter.ttk.Style()') >= 0:
            continue
        if text.find('style.configure(') >= 0:
            splitarray1 = text.partition('style.configure(')
            stylename = None
            splitarray2 = None
            if splitarray1[2].find(',') >= 0:
                splitarray2 = splitarray1[2].partition(',')
                stylename = splitarray2[0].replace('"','')
            else:
                splitarray2 = splitarray1[2].partition(')')
                stylename = splitarray2[0].replace('"','')
            sytleValueText = splitarray2[2]
            fontindex_begin = sytleValueText.find('font=(')
            fontindex_end = fontindex_begin
            StyleArray[stylename] = {}
            othertext = sytleValueText
            if fontindex_begin >= 0:
                fontindex_end = sytleValueText.find(')')
                fonttext = sytleValueText[fontindex_begin+6:fontindex_end]
                fontsplitarray = fonttext.split(',')
                StyleArray[stylename]['font'] = tkinter.font.Font(family=fontsplitarray[0].replace('"','').strip(), size=int(fontsplitarray[1].replace('"','').strip()),weight=fontsplitarray[2].replace('"','').strip())
                othertext = sytleValueText[0:fontindex_begin] + sytleValueText[fontindex_end+1:-1]
            else:
                splitarray4 = sytleValueText.partition(')')
                othertext = splitarray4[0]
            splitarray3 = othertext.split(',')
            for stylecfgtext in splitarray3:
                if stylecfgtext.find('=') > 0:
                    splitarray4 = stylecfgtext.partition('=')
                    key = splitarray4[0].replace('"','').strip()
                    value = splitarray4[2].replace('"','').strip()
                    StyleArray[stylename][key] = value
            continue
        if text.find('style.map(') >= 0:
            continue
    f.close()
    return StyleArray 
