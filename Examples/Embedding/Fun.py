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
        G_UIElementArray[uiName][elementName].configure(AttribName=attribValue)
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
