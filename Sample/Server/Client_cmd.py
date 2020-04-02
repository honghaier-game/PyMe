#coding=utf-8
import Fun
#Set Element 's BoundingData :Fun.setUIData(Param1：elementName，Param2：DataName，Param3：DataValue)
#Get Element's BoundingData :Fun.getUIData(Param1：elementName，Param2：DataName)
#Set Element 's Attrib :Fun.setUIAttrib(Param1：elementName，Param2：AttribName，Param3：AttribValue)
#Get Element's Attrib :Fun.getUIAttrib(Param1：elementName，Param2：AttribName)
#Get Element:Fun.getUIEle(Param1：elementName)
#Set Element's Text :Fun.setUIText(Param1：elementName,Param2:TextValue)
#Get Element's Text :Fun.getUIText(Param1：elementName)
def Button_8_onCommand():
  MySocket = Fun.getUIEle('MySocket_11')
  IPAddr = Fun.getUIData('Entry_3','IPAddr')
  PORT = Fun.getUIData('Entry_5','Port')
  MySocket.connServer(IPAddr,PORT)
def Button_9_onCommand():
  MySocket = Fun.getUIEle('MySocket_11')
  MsgText = Fun.getUIText('Entry_7')
  MySocket.sendMessage(MsgText)


