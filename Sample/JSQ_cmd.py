#coding=utf-8
import JSQ_fun

from   tkinter.messagebox import showwarning
G_VarArray={'Count':0}
G_UIElementArray={}
G_TempCount = 0.0
G_OpType = 0
#Set Element 's BoundingData :JSQ_fun.setUIData(Param1：elementName，Param2：DataName，Param3：DataValue)
#Get Element's BoundingData :JSQ_fun.getUIData(Param1：elementName，Param2：DataName)
#Set Element 's Attrib :JSQ_fun.setUIAttrib(Param1：elementName，Param2：AttribName，Param3：AttribValue)
#Get Element's Attrib :JSQ_fun.getUIAttrib(Param1：elementName，Param2：AttribName)
#Get Element:JSQ_fun.getUIEle(Param1：elementName)
#Get Element:JSQ_fun.setUIText(Param1：elementName,Param2:TextValue)
def Button_3_onCommand():
  count =JSQ_fun.getUIData('Label_2','Count')
  count = count * 10.0 + 1
  JSQ_fun.setUIData('Label_2','Count',count)



def Button_4_onCommand():
  count =JSQ_fun.getUIData('Label_2','Count')
  count = count * 10.0 + 2
  JSQ_fun.setUIData('Label_2','Count',count)



def Button_5_onCommand():
  count =JSQ_fun.getUIData('Label_2','Count')
  count = count * 10.0 + 3
  JSQ_fun.setUIData('Label_2','Count',count)



def Button_6_onCommand():
  count =JSQ_fun.getUIData('Label_2','Count')
  count = count * 10.0 + 4
  JSQ_fun.setUIData('Label_2','Count',count)



def Button_7_onCommand():
  count =JSQ_fun.getUIData('Label_2','Count')
  count = count * 10.0 + 5
  JSQ_fun.setUIData('Label_2','Count',count)



def Button_8_onCommand():
  count =JSQ_fun.getUIData('Label_2','Count')
  count = count * 10.0 + 6
  JSQ_fun.setUIData('Label_2','Count',count)



def Button_9_onCommand():
  count =JSQ_fun.getUIData('Label_2','Count')
  count = count * 10.0 + 7
  JSQ_fun.setUIData('Label_2','Count',count)



def Button_10_onCommand():
  count =JSQ_fun.getUIData('Label_2','Count')
  count = count * 10.0 + 8
  JSQ_fun.setUIData('Label_2','Count',count)



def Button_11_onCommand():
  count =JSQ_fun.getUIData('Label_2','Count')
  count = count * 10.0 + 9
  JSQ_fun.setUIData('Label_2','Count',count)



def Button_12_onCommand():
  count =JSQ_fun.getUIData('Label_2','Count')
  count = count * 10.0
  JSQ_fun.setUIData('Label_2','Count',count)
  


def Button_13_onCommand():
  JSQ_fun.setUIData('Label_2','Count',0.0)



def Button_14_onCommand():
  global G_TempCount
  global G_OpType
  count =JSQ_fun.getUIData('Label_2','Count')
  if G_OpType == 1:
    count = G_TempCount  + count
  elif G_OpType == 2:
    count = G_TempCount  - count
  elif G_OpType == 3:
    count = G_TempCount  * count
  elif G_OpType == 4:
    count = G_TempCount / count
  JSQ_fun.setUIData('Label_2','Count',count)



def Button_15_onCommand():
  global G_OpType
  global G_TempCount
  G_TempCount =JSQ_fun.getUIData('Label_2','Count')
  G_OpType = 1
  JSQ_fun.setUIData('Label_2','Count',0.0)


def Button_16_onCommand():
  global G_OpType
  G_TempCount =JSQ_fun.getUIData('Label_2','Count')
  G_OpType = 2
  JSQ_fun.setUIData('Label_2','Count',0.0)


def Button_17_onCommand():
  global G_OpType
  G_TempCount =JSQ_fun.getUIData('Label_2','Count')
  G_OpType = 3
  JSQ_fun.setUIData('Label_2','Count',0.0)


def Button_18_onCommand():
  global G_OpType
  G_TempCount =JSQ_fun.getUIData('Label_2','Count')
  G_OpType = 4
  JSQ_fun.setUIData('Label_2','Count',0.0)


def Menu_A11():
  pass
def Menu_B2():
  pass
