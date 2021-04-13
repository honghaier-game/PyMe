#This file does not support direct editing
#coding=utf-8
import os
from   os.path import abspath, dirname
import tkinter
import tkinter.simpledialog

G_ElementBindingDataArray={}
G_UIElementArray={}
G_UIElementVariableArray={}
G_UIInputDataArray={} 
G_CurrentFilePath=None
G_CutContent=None
#Add Element to G_UIElementArray:Param1：uiName, Param2:elementName，Param3：element
def AddElement(uiName,elementName,element):
    if uiName not in G_UIElementArray:
        G_UIElementArray[uiName]={}
    G_UIElementArray[uiName][elementName]=element
#Add Data to G_UIElementVariableArray:Param1：uiName, Param2:elementName
def AddElementVariable(uiName,elementName):
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
    return G_UIElementVariableArray[uiName][elementName]
#Set Data of G_UIElementVariableArray:Param1：uiName, Param2:elementName, Param3:value
def SetElementVariable(uiName,elementName,value):
    if uiName in G_UIElementVariableArray:
        if elementName in G_UIElementVariableArray[uiName]:
            G_UIElementVariableArray[uiName][elementName].set(value)
#Get Data of G_UIElementVariableArray:Param1：uiName, Param2:elementName
def GetElementVariable(uiName,elementName):
    if uiName in G_UIElementVariableArray:
        if elementName in G_UIElementVariableArray[uiName]:
            return G_UIElementVariableArray[uiName][elementName].get()
#Add Element 's BindingData :Param1：uiName, Param2:elementName，Param3：DataName，Param4：datatype, Param5: DataValue, Param6: isMapToText
def AddUIData(uiName,elementName,dataName,datatype,datavalue,isMapToText):
    global G_ElementBindingDataArray
    if uiName not in G_ElementBindingDataArray:
        G_ElementBindingDataArray[uiName]={} 
    if elementName not in G_ElementBindingDataArray[uiName]:
        G_ElementBindingDataArray[uiName][elementName]=[]
    G_ElementBindingDataArray[uiName][elementName].append([dataName,datatype,datavalue,isMapToText])
#Set Element 's BindingData :Param1：uiName, Param2:elementName，Param3：DataName，Param4：DataValue
def SetUIData(uiName,elementName,dataName,datavalue):
    global G_UIElementArray
    global G_ElementBindingDataArray
    if uiName in G_ElementBindingDataArray:
        if elementName in G_ElementBindingDataArray[uiName]:
            for EBData in G_ElementBindingDataArray[uiName][elementName]:
                if EBData[0] == dataName:
                    EBData[2] = datavalue
                    if EBData[3] == 1:
                        SetUIText(uiName,elementName,datavalue) 
                    return
#Get Element 's BindingData :Param1：uiName, Param2：elementName，Param3：DataName
def GetUIData(uiName,elementName,dataName):
    global G_ElementBindingDataArray
    if  uiName in G_ElementBindingDataArray:
        if elementName in G_ElementBindingDataArray[uiName]:
            for EBData in G_ElementBindingDataArray[uiName][elementName]:
                if EBData[0] == dataName:
                    if EBData[1]=='int':
                        return int(EBData[2])
                    elif EBData[1]=='float':
                        return float(EBData[2])
                    else:
                        return EBData[2]
    return None
#Set Element 's Attrib :Param1：uiName, Param2：elementName，Param3：AttribName，Param4：AttribValue
def SetUIAttrib(uiName,elementName,AttribName,attribValue):
    global G_UIElementArray
    if uiName in G_UIElementArray:
        if AttribName in G_UIElementArray[uiName][elementName].configure().keys():
            G_UIElementArray[uiName][elementName][AttribName]=attribValue
#Get Element's Attrib :Param1：uiName, Param2：elementName，Param3：attributeName
def GetUIAttrib(uiName,elementName,AttribName):
    global G_UIElementArray
    if uiName in G_UIElementArray:
        return G_UIElementArray[uiName][elementName].cget(AttribName)
    return None
#Get Element:Param1：uiName, Param2：elementName
def GetUIEle(uiName,elementName):
    global G_UIElementArray
    if uiName in G_UIElementArray:
        return G_UIElementArray[uiName][elementName]
#Set Element 's Text:Param1：uiName, Param2：elementName,Param3:textValue
def SetUIText(uiName,elementName,textValue):
    global G_UIElementArray
    global G_UIElementVariableArray
    showtext = str("%s"%textValue)
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
#Get Element 's Text:Param1：uiName, Param2：elementName
def GetUIText(uiName,elementName):
    global G_UIElementArray
    global G_UIElementVariableArray
    if uiName in G_UIElementVariableArray:
        if elementName in G_UIElementVariableArray[uiName]:
            return G_UIElementVariableArray[uiName][elementName].get()
    if uiName in G_UIElementArray:
        if elementName in G_UIElementArray[uiName]:
            if elementName.find('Text_') >= 0:
                return G_UIElementArray[uiName][elementName].get('0.0', tkinter.END)
            else:
                return G_UIElementArray[uiName][elementName].cget('text')
    return str("")
#Init Element 's Data:Param1：uiName
def InitElementData(uiName):
    global G_ElementBindingDataArray
    if uiName in G_ElementBindingDataArray:
        for elementName in G_ElementBindingDataArray[uiName].keys():
            for EBData in G_ElementBindingDataArray[uiName][elementName]:
                if EBData[3] == 1:
                    SetUIText(uiName,elementName,EBData[2])
                    SetUIText(uiName,elementName,EBData[2])
#Init Element 's Style:Param1：uiName,Param2:Style
def InitElementStyle(uiName,Style):
    StyleArray = ReadStyleFile(Style+".py")
    global G_UIElementArray
    if uiName in G_UIElementArray:
        for elementName in G_UIElementArray[uiName].keys():
            Widget = G_UIElementArray[uiName][elementName]
            try:
                if  Widget.winfo_exists() == 1:
                    WinClass = Widget.winfo_class()
                    StyleName = ".T"+WinClass
                    if  StyleName == '.TLabel':
                        Root = GetUIEle(uiName,'root')
                        Root['background'] = StyleArray[StyleName]['background']
                    for attribute in StyleArray[StyleName].keys():
                        Widget[attribute] = StyleArray[StyleName][attribute]
            except BaseException:
                continue
#Update Element 's Input Data Array:Param1：uiName
def UpdateUIInputDataArray(uiName):
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
#MessageBox
def MessageBox(text):
    tkinter.messagebox.showwarning('info',text)
#InputBox
def InputBox(title,text):
    res = tkinter.simpledialog.askstring(title,'Input Box',initialvalue=text)
    return res
#AskBox
def AskBox(title,text):
    res = tkinter.messagebox.askyesno(title,text)
    return res
#Return a file list from dir
def WalkAllResFiles(parentPath,alldirs=True):
    ResultFilesArray = []
    if os.path.exists(parentPath) == True:
        for fileName in os.listdir(parentPath):
            if '__pycache__' not in fileName:
                if '.git' not in fileName:
                    newPath = parentPath +'\\'+ fileName
                    if os.path.isdir(newPath):
                        ResultFilesArray.append(newPath)
                        if alldirs == True:
                            ResultFilesArray.extend(WalkAllResFiles(newPath,alldirs))
                    else:
                        ResultFilesArray.append(newPath)
    return ResultFilesArray
#Add params to event functions
def EventFunction_Adaptor(fun,  **params):
    return lambda event, fun=fun, params=params: fun(event, **params)
#Set Control Place functions
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
#WriteDragWidgetFunctions
class WindowDraggable():
    def __init__(self,widget):
        self.widget = widget
        widget.bind('<ButtonPress-1>',self.StartMove)
        widget.bind('<ButtonRelease-1>',self.StopMove)
        widget.bind('<B1-Motion>',self.OnMotion)
    def StartMove(self,event):
        if self.widget == event.widget or event.widget.winfo_class() =="Canvas":
            self.x = event.x_root
            self.y = event.y_root
    def StopMove(self,event):
        if self.widget == event.widget or event.widget.winfo_class() =="Canvas":
            self.x = None
            self.y = None
    def OnMotion(self,event):
        if self.widget == event.widget or event.widget.winfo_class() =="Canvas":
            deltaX = event.x_root - self.x
            deltaY = event.y_root - self.y
            newX = self.widget.winfo_x() + deltaX
            newY = self.widget.winfo_y() + deltaY
            geoinfo = str('%dx%d+%d+%d'%(self.widget.winfo_width(),self.widget.winfo_height(),newX,newY))
            self.widget.geometry(geoinfo)
            self.x = event.x_root
            self.y = event.y_root
#WriteCreateRoundRectangleFunctions
def CreateRoundRectangle(canvas,x1, y1, x2, y2, radius=25,**kwargs):
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
#Read from file
def ReadFromFile(filePath):
    content = None
    if filePath != None:
        if os.path.exists(filePath) == True: 
            f = open(filePath,mode='r',encoding='utf-8')
            if f != None:
                content = f.read()
                f.close()
    return content
#Write to file
def WriteToFile(filePath,content):
    if filePath != None:
        f = open(filePath,mode='w',encoding='utf-8')
        if f != None:
            if content != None:
                f.write(content)
            f.close()
            return True
    return False
#Read Style File
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
