#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
import StockMonitor
def Button_4_onCommand(className,widgetName):
    StockCode = Fun.GetUIText(className,"Entry_3")
    StockInfo = StockMonitor.getStockInfo(StockCode)
    StockCode = StockInfo[u'code']
    StockName = StockInfo[u'name']
    StockTime = StockInfo[u'time']
    StockPrice = StockInfo[u'price']
    MaxPrice = Fun.GetUIText(className,"Entry_10")
    MinPrice =Fun.GetUIText(className,"Entry_12")
    TreeView13 = Fun.GetUIEle(className,"TreeView_13")
    TreeView13 .insert('','end',values=(StockCode[0],StockName[0],StockTime[0],StockPrice[0],MinPrice,MaxPrice))
    StockArray = Fun.GetUIData(className,"TreeView_13","StockArray")
    StockArray.append([StockCode[0],MaxPrice,MinPrice])
StockMonitorInst = None
def Button_6_onCommand(className,widgetName):
    global StockMonitorInst
    BtnText = Fun.GetUIText(className,widgetName)
    if BtnText == "启动监控":
        if StockMonitorInst == None:
            StockMonitorInst = StockMonitor.StockMonitor()
        StockArray = Fun.GetUIData(className,"TreeView_13","StockArray")
        for stockcode in StockArray:
            StockMonitorInst.addStock(stockcode[0],stockcode[1],stockcode[2])
        TreeView = Fun.GetUIEle(className,"TreeView_13")
        PhoneNumber=Fun.GetUIText(className,"Entry_17")
        StockMonitorInst.SetMonitorInfo(TreeView,PhoneNumber)       
        StockMonitorInst.StartMonitoring()    
        Fun.SetUIText(className,widgetName,"停止监控")
    else:
        StockMonitorInst.StopMonitoring()
        Fun.SetUIText(className,widgetName,"启动监控")

