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
DirPath=""
def getFileName(filedir):
    file_list = [os.path.join(root, filespath) \
                 for root, dirs, files in os.walk(filedir) \
                 for filespath in files \
                 if str(filespath).endswith('pdf')
                 ]
    return file_list if file_list else []
def moveSelectedItem(strList,dstList):
    items = strList.curselection()
    for i in items:
        dstList.insert(tkinter.END, strList.get(i))
    for i in items:
        strList.delete(i)
def moveAllItem(strList,dstList):
    count = strList.size()
    for i in range(count):
        dstList.insert(tkinter.END,strList.get(i))
    strList.delete(0, "end")
def MergePDF(filepath, outfile,listBox):
    output = PdfFileWriter()
    outputPages = 0
    #pdf_fileName = getFileName(filepath)
    #for pdf_file in pdf_fileName:
    count = listBox.size()
    for i in range(count):
        item = listBox.get(i)
        pdf_file = os.path.join(filepath,item)
        print("路径：%s"%pdf_file)
        # 读取源PDF文件
        input = PdfFileReader(open(pdf_file, "rb"))
        # 获得源PDF文件中页面总数
        pageCount = input.getNumPages()
        outputPages += pageCount
        print("页数：%d"%pageCount)
        Fun.SetTKAttrib("Project4", "Progress_3", "value",pageCount)
        # 分别将page添加到输出output中
        for iPage in range(pageCount):
            output.addPage(input.getPage(iPage))
    print("合并后的总页数:%d."%outputPages)
    # 写入到目标PDF文件
    outputStream = open(os.path.join(filepath, outfile), "wb")
    output.write(outputStream)
    outputStream.close()
    Fun.MessageBox("PDF文件合并完成！该文件在打开的文件夹里!")
    print("PDF文件合并完成！")
def Button_2_onCommand(uiName,widgetName):
    listBox = Fun.GetElement(uiName, "ListBox_3")
    listBox8 = Fun.GetElement(uiName, "ListBox_8")
    listBox.delete(0, "end")
    listBox8.delete(0, "end")
    filepath = tkinter.filedialog.askdirectory(initialdir=os.path.abspath('.'), title='打开目录查找')
    #Fun.SetText(uiName, "Entry_11", dirPath)
    global DirPath
    DirPath = filepath
    pdf_fileName = getFileName(filepath)
    if(not pdf_fileName):
        Fun.MessageBox("没有发现pdf文件！")
        return
    #listBox = Fun.GetElement(uiName,"ListBox_3")
    for item in pdf_fileName:
        file = item.replace(filepath,"").replace("\\","")
        listBox.insert(tkinter.END, file)
def Button_4_onCommand(uiName,widgetName):
    listBox = Fun.GetElement(uiName, "ListBox_3")
    listBox8 = Fun.GetElement(uiName, "ListBox_8")
    moveSelectedItem(listBox,listBox8)
def Button_5_onCommand(uiName,widgetName):
    listBox = Fun.GetElement(uiName, "ListBox_3")
    listBox8 = Fun.GetElement(uiName, "ListBox_8")
    moveAllItem(listBox,listBox8)
def Button_6_onCommand(uiName,widgetName):
    listBox = Fun.GetElement(uiName, "ListBox_3")
    listBox8 = Fun.GetElement(uiName, "ListBox_8")
    moveSelectedItem(listBox8, listBox)
def Button_7_onCommand(uiName,widgetName):
    listBox = Fun.GetElement(uiName, "ListBox_3")
    listBox8 = Fun.GetElement(uiName, "ListBox_8")
    moveAllItem(listBox8, listBox)
def Button_11_onCommand(uiName,widgetName):
    savePath = tkinter.filedialog.asksaveasfilename(initialdir=os.path.abspath('.'),title='Save Python File',filetypes=[('Python File','*.py'),('All files','*')])
    
    if(savePath == "" or len(savePath) <= 0):
        Fun.MessageBox("请输入合并后的文件名！")
        return
    listBox8 = Fun.GetElement(uiName, "ListBox_8")
    count = listBox8.size()
    if(count < 2):
        Fun.MessageBox("至少要选择两个文件进行合并!")
        return
    MergePDF(DirPath,openPath,listBox8)

