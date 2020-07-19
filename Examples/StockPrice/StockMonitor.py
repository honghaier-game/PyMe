import os
import time
import tushare as ts
import pandas as pd
import threading
from twilio.rest import Client
threadactive = True
def getStockInfo(stock_code):
    df = ts.get_realtime_quotes(stock_code)
    # e = df[['code','name','time','price']]
    c = df[u'code']
    n = df[u'name']
    t = df[u'time']
    p = df[u'price']
    text = c[0] + " " + n[0] + " " + t[0] + " " + p[0]
    print(text)
    return df
class StockMonitor:
    def __init__(self):
        self.StockArray = []
        self.TreeView = None
        self.PhoneNumber = None
        self.Run_Function = None
    def addStock(self,StockCode,MaxPrice,MinPrice):
        self.StockArray.append([StockCode,MaxPrice,MinPrice,False,False])
    def SetMonitorInfo(self,TreeView,PhoneNumber):
        self.TreeView = TreeView
        self.PhoneNumber = PhoneNumber
    def StartMonitoring(self):
        account_sid = ""#改成申请的SID
        auth_token = ""#改成申请的TOKEN
        client = Client(account_sid, auth_token)
        all_items = self.TreeView.get_children()    
        for item in all_items:
            self.TreeView.delete(item)
        for stock_code in self.StockArray:
            df = ts.get_realtime_quotes(stock_code[0])
            e = df[['code','name','price','time']]
            c = df[u'code']
            n = df[u'name']
            p = df[u'price']
            t = df[u'time']
            print(e)
            if float(p[0]) > float(stock_code[2]) :
                self.TreeView.insert('','end',values=(c[0],n[0],t[0],p[0],stock_code[2],stock_code[1],"超过上限"))
                if stock_code[3] == False:
                    # smsText = "您的股票"+n[0]+"("+c[0]+") 已超过设定上限价格"+ stock_code[2] + ",当前价格"+p[0]+",请及时关注!"
                    smsText = "Stock:"+"("+c[0]+") Price:"+p[0]
                    #from_改成得到的试用手机号
                    client.messages.create(to=self.PhoneNumber,from_="+13343784863",body=smsText)
                    stock_code[3] = True
            elif float(p[0]) < float(stock_code[1]):
                self.TreeView.insert('','end',values=(c[0],n[0],t[0],p[0],stock_code[2],stock_code[1],"低于下限"))
                if stock_code[4] == False:
                    # smsText = "您的股票"+n[0]+"("+c[0]+") 已低于设定下限价格"+ stock_code[1] + ",当前价格"+p[0]+",请及时关注!"
                    smsText = "Stock:"+"("+c[0]+") Price:"+p[0]
                    print(smsText)
                    #from_改成得到的试用手机号
                    client.messages.create(to=self.PhoneNumber,from_="+13343784863",body=smsText)
                    stock_code[4] = True
            else:
                self.TreeView.insert('','end',values=(c[0],n[0],t[0],p[0],stock_code[1],stock_code[2],"平稳波动"))
        self.Run_Function = self.TreeView.after(1000, self.StartMonitoring)
    def StopMonitoring(self):
        self.TreeView.after_cancel(self.Run_Function)
        self.StockArray = []
