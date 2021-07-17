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

import time
from Ticket import Ticket
def Form_1_onLoad(className):
    Fun.SetText(className, "Entry_3","北京")
    Fun.SetText(className, "Entry_5","昆明")
    date = time.strftime("%Y-%m-%d", time.localtime())
    Fun.SetText(className, "Entry_8",date)

def Button_9_onCommand(className,widgetName):
    start = Fun.GetText(className,"Entry_3")
    to = Fun.GetText(className, "Entry_5")
    date = Fun.GetText(className, "Entry_8")
    listBox = Fun.GetElement(className,"ListBox_10")
    ticket = Ticket()
    ticket.set_FromStation(start)
    ticket.set_ToStation(to)
    ticket.set_TicketDate(date)
    ticket.curlData(listBox)
