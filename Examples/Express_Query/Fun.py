#coding=utf-8
import tkinter
import tkinter.simpledialog

G_ElementBoundingDataArray=[]
G_UIElementArray={}
G_UIElementVariableArray={} 
G_UIInputDataArray={} 
#Set Element 's BoundingData :Param1：elementName，Param2：DataName，Param3：DataValue
def setUIData(elementName,dataName,datavalue):
    global G_UIElementArray
    global G_ElementBoundingDataArray
    for Element in G_ElementBoundingDataArray:
        if Element[0]==elementName:
            if len(Element[1]) > 0:
                for EBData in Element[1]:
                    if EBData[0] == dataName:
                        EBData[2] = datavalue
                        if EBData[3] == 1:
                           setUIText(elementName,datavalue) 
                        return
#Get Element 's BoundingData :Param1：elementName，Param2：DataName
def getUIData(elementName,dataName):
    global G_ElementBoundingDataArray
    for Element in G_ElementBoundingDataArray:
        if Element[0]==elementName:
            if len(Element[1]) > 0:
                for EBData in Element[1]:
                    if EBData[0] == dataName:
                        if EBData[1]=='int':
                            return int(EBData[2])
                        elif EBData[1]=='float':
                            return float(EBData[2])
                        else:
                            return EBData[2]
    return None
#Set Element 's Attrib :Param1：elementName，Param2：AttribName，Param3：AttribValue
def setUIAttrib(elementName,AttribName,attribValue):
    global G_UIElementArray
    G_UIElementArray[elementName].configure(AttribName=attribValue)
#Get Element's Attrib :Param1：elementName，Param2：attributeName
def getUIAttrib(elementName,AttribName):
    global G_UIElementArray
    return G_UIElementArray[elementName].cget(AttribName)
#Get Element:Param1：elementName
def getUIEle(elementName):
    global G_UIElementArray
    return G_UIElementArray[elementName]
#Set Element 's Text:Param1：elementName,Param2:textValue
def setUIText(elementName,textValue):
    global G_UIElementArray
    global G_UIElementVariableArray
    showtext = str("%s"%textValue)
    if elementName in G_UIElementVariableArray:
        G_UIElementVariableArray[elementName].set(showtext)
    elif elementName in G_UIElementArray:
        G_UIElementArray[elementName].configure(text=showtext)
#Get Element 's Text:Param1：elementName
def getUIText(elementName):
    global G_UIElementArray
    global G_UIElementVariableArray
    if elementName in G_UIElementVariableArray:
        return G_UIElementVariableArray[elementName].get()
    elif elementName in G_UIElementArray:
        if elementName.find('Text_') >= 0:
            return G_UIElementArray[elementName].get('0.0', tkinter.END)
        else:
            return G_UIElementArray[elementName].cget('text')
    return str("")
#Init Element 's Data
def InitElementData():
    global G_ElementBoundingDataArray
    for Element in G_ElementBoundingDataArray:
        if len(Element[1]) > 0:
            for EBData in Element[1]:
                if EBData[3] == 1:
                    setUIText(Element[0],EBData[2])
                    setUIText(Element[0],EBData[2])
#Update Element 's Input Data Array
def UpdateUIInputDataArray():
    global G_UIElementArray
    global G_UIInputDataArray
    global G_UIElementVariableArray
    G_UIInputDataArray.clear()
    for elementName in G_UIElementArray:
        G_UIInputDataArray[elementName] = []
        Widget = G_UIElementArray[elementName]
        if elementName.find('Text_') >= 0:
            content = Widget.get('0.0', tkinter.END)
            G_UIInputDataArray[elementName].append(content)
        elif elementName.find('Entry_') >= 0:
            content = G_UIElementVariableArray[elementName].get()
            G_UIInputDataArray[elementName].append(content)
    for elementName in G_UIElementVariableArray:
       if elementName.find('Group_') >= 0:
            ElementIntValue = G_UIElementVariableArray[elementName].get()
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
