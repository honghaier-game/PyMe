#coding=utf-8
import sys
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
from   tkinter import *
import Fun
#Set Element 's BoundingData :Fun.setUIData(Param1：elementName，Param2：DataName，Param3：DataValue)
#Get Element's BoundingData :Fun.getUIData(Param1：elementName，Param2：DataName)
#Set Element 's Attrib :Fun.setUIAttrib(Param1：elementName，Param2：AttribName，Param3：AttribValue)
#Get Element's Attrib :Fun.getUIAttrib(Param1：elementName，Param2：AttribName)
#Get Element:Fun.getUIEle(Param1：elementName)
#Set Element's Text :Fun.setUIText(Param1：elementName,Param2:TextValue)
#Get Element's Text :Fun.getUIText(Param1：elementName)
#Update Element's Input Data Array:Fun.UpdateUIInputDataArray()
def Button_5_onCommand():
  MySocket = Fun.getUIEle('MySocket_9')
  IPAddr = Fun.getUIData('Entry_2','IPAddr')
  PORT = Fun.getUIData('Entry_4','Port')
  MySocket.createServer(IPAddr,PORT)


