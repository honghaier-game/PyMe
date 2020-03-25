#coding=utf-8

G_ElementBoundingDataArray=[]
G_UIElementArray={}
G_UIElementVariableArray={} 
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
   return G_UIElementArray[elementName].cget('+AttribName+')
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
#Init Element 's Data
def InitElementData():
   global G_ElementBoundingDataArray
   for Element in G_ElementBoundingDataArray:
       if len(Element[1]) > 0:
           for EBData in Element[1]:
               if EBData[3] == 1:
                   setUIText(Element[0],EBData[2])
                   setUIText(Element[0],EBData[2])
