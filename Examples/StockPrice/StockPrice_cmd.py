#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

import StockMonitor
def Button_4_onCommand(uiName,widgetName):
    StockCode = Fun.GetText(uiName,"Entry_3")
    StockInfo = StockMonitor.getStockInfo(StockCode)
    StockCode = StockInfo[u'code']
    StockName = StockInfo[u'name']
    StockTime = StockInfo[u'time']
    StockPrice = StockInfo[u'price']
    MaxPrice = Fun.GetText(uiName,"Entry_10")
    MinPrice =Fun.GetText(uiName,"Entry_12")
    TreeView13 = Fun.GetElement(uiName,"TreeView_13")
    TreeView13 .insert('','end',values=(StockCode[0],StockName[0],StockTime[0],StockPrice[0],MinPrice,MaxPrice))
    StockArray = Fun.GetUserData(uiName,"TreeView_13","StockArray")
    StockArray.append([StockCode[0],MaxPrice,MinPrice])
StockMonitorInst = None
def Button_6_onCommand(uiName,widgetName):
    global StockMonitorInst
    BtnText = Fun.GetText(uiName,widgetName)
    if BtnText == "启动监控":
        if StockMonitorInst == None:
            StockMonitorInst = StockMonitor.StockMonitor()
        StockArray = Fun.GetUserData(uiName,"TreeView_13","StockArray")
        for stockcode in StockArray:
            StockMonitorInst.addStock(stockcode[0],stockcode[1],stockcode[2])
        TreeView = Fun.GetElement(uiName,"TreeView_13")
        PhoneNumber=Fun.GetText(uiName,"Entry_17")
        StockMonitorInst.SetMonitorInfo(TreeView,PhoneNumber)       
        StockMonitorInst.StartMonitoring()    
        Fun.SetText(uiName,widgetName,"停止监控")
    else:
        StockMonitorInst.StopMonitoring()
        Fun.SetText(uiName,widgetName,"启动监控")
