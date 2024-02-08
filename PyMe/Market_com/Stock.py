import os
import time
import tushare as ts
import pandas as pd
import threading

threadactive = True

def Thread_GetStock(param_array):
    global threadactive 
    threadactive = True
    while threadactive == True:
        for stock_code in param_array:
            df = ts.get_realtime_quotes(stock_code[0])
            e = df[['code','name','price','time']]
            p = df[u'price']
            print(e)
            if float(p[0]) > float(stock_code[2]) :
                stock_code[3].configure(text = "超过上限")  
            elif float(p[0]) < float(stock_code[1]):
                stock_code[3].configure(text = "低于上限")  
            else:
                stock_code[3].configure(text = "监控中")  
        time.sleep(1)

class StockMonitor:
    def __init__(self):
        self.StockArray = []
        self.run_thread = None

    def addStock(self,code,low,high,label):
        self.StockArray.append([code,low,high,label])
        
    def Start(self):
        global threadactive 
        threadactive = True
        self.run_thread = threading.Thread(target=Thread_GetStock, args=[self.StockArray])
        self.run_thread.start()

    def Stop(self):
        global threadactive 
        threadactive = False
