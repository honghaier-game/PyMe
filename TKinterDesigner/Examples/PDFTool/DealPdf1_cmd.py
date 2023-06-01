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
from PyPDF2 import PdfFileReader, PdfFileWriter
def getRange(srcList,pageNo):
    for item in sorted(srcList):
        if(pageNo < int(item)):
            return item
    return "0"
def showMsg(uiName,msg):
    listBox = Fun.GetElement(uiName,"ListBox_13")
    listBox.insert(tkinter.END, msg)
def Form_1_onLoad(uiName):
    Fun.SetText(uiName, "Entry_8","10,35,100")
def Button_3_onCommand(uiName,widgetName):
    filePath= tkinter.filedialog.askopenfilename(initialdir=os.path.abspath('.'),title='选择文件')
    Fun.SetText(uiName,"Entry_4",filePath)
    input = PdfFileReader(open(filePath, "rb"))
    pageCount = input.getNumPages()
    Fun.SetText(uiName,"Entry_6",pageCount)
def Button_12_onCommand(uiName,widgetName):
    openPath= tkinter.filedialog.askdirectory(initialdir=os.path.abspath('.'),title='打开目录查找')
    # 文件信息
    try:
        filePath = Fun.GetText(uiName,"Entry_4")
        input = PdfFileReader(open(filePath, "rb"))
    except Exception as e:
        Fun.MessageBox("文件异常，请检查！")
        return
    pageCount = input.getNumPages()
    dirName = os.path.dirname(filePath)
    # 分隔方式
    content = Fun.GetText(uiName,"Entry_8")
    if(len(content) <= 0):
        Fun.MessageBox("数据格式不对，请重新输入")
        return
    strList = content.split(",")
    #print(strList)
    # 检查参数是否正常
    try:
        for i in strList:
            if(len(i) <= 0):
                Fun.MessageBox("数据格式不对，请重新输入")
                return
            pageNum = int(i)
            if(pageNum >= pageCount):
                Fun.MessageBox("要分割的页数不能超过总页数啊！")
                return
    except Exception as e:
        print(e)
        Fun.MessageBox("数据格式不对，请重新输入")
        return
    outPutDic = {}
    for iPage in range(pageCount):
        rang = getRange(strList,iPage)
        if(rang == "0"):
            rang = str(pageCount)
        if(outPutDic.get(rang,-1) == -1):
            outPutDic[rang]  = {"fileName":rang+".pdf","outPut":PdfFileWriter()}
            outPutDic[rang]['outPut'].addPage(input.getPage(iPage))
        else:
            if(outPutDic[rang] == None):
                outPutDic[rang] = {"fileName": rang + ".pdf", "outPut": PdfFileWriter()}
                outPutDic[rang]['outPut'].addPage(input.getPage(iPage))
            else:
                outPutDic[rang]['outPut'].addPage(input.getPage(iPage))
    for item in outPutDic.values():
        newFileName = os.path.join(dirName,item['fileName'])
        outputStream = open(newFileName, "wb")
        item['outPut'].write(outputStream)
        outputStream.close()
        msg = item['fileName'] + "  has been created!"
        showMsg(uiName,msg)
    showMsg(uiName, "split pdf file over!")
    '''
    output = PdfFileWriter()
    # 分别将page添加到输出output中
    for iPage in range(int(strList[0])):
        output.addPage(input.getPage(iPage))
    newFileName = os.path.join(dirName,strList[0] + ".pdf")
    outputStream = open(newFileName, "wb")
    output.write(outputStream)
    outputStream.close()
    '''

