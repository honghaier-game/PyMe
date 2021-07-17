#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
from PyPDF2 import PdfFileReader, PdfFileWriter
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 
def Button_3_onCommand(uiName,widgetName):
    filePath = tkinter.filedialog.askopenfilename(initialdir=os.path.abspath('.'), title='选择文件')
    Fun.SetText(uiName, "Entry_4", filePath)
    #input = PdfFileReader(open(filePath, "rb"))
def Button_5_onCommand(uiName,widgetName):
    filePath = tkinter.filedialog.askopenfilename(initialdir=os.path.abspath('.'), title='选择文件')
    Fun.SetText(uiName, "Entry_6", filePath)
def Button_7_onCommand(uiName,widgetName):
    file1 = Fun.GetText(uiName, "Entry_4")
    file2 = Fun.GetText(uiName, "Entry_6")
    input1 = PdfFileReader(open(file1, "rb"))
    input2 = PdfFileReader(open(file2, "rb"))
    pageCount1 = input1.getNumPages()
    outPut1 = PdfFileWriter()
    dirName = os.path.dirname(file1)
    for iPage in range(input1.getNumPages()):
        outPut1.addPage(input1.getPage(iPage))
    for iPage in range(input2.getNumPages()):
        outPut1.addPage(input2.getPage(iPage))
    newFileName = os.path.join(dirName,"merge1.pdf")
    outputStream = open(newFileName, "wb")
    outPut1.write(outputStream)
    outputStream.close()
    Fun.MessageBox("merge finised,new file name is=merge1.pdf")
def Button_10_onCommand(uiName,widgetName):
    dirPath = tkinter.filedialog.askdirectory(initialdir=os.path.abspath('.'), title='打开目录查找')
    Fun.SetText(uiName, "Entry_11", dirPath)
def Button_12_onCommand(uiName,widgetName):
     file_dir = Fun.GetText(uiName, "Entry_11")
     outfile = "out.pdf"
     MergePDF(file_dir, outfile)
def getFileName(filedir):
    file_list = [os.path.join(root, filespath) \
                 for root, dirs, files in os.walk(filedir) \
                 for filespath in files \
                 if str(filespath).endswith('pdf')
                 ]
    return file_list if file_list else []
def MergePDF(filepath, outfile):
    output = PdfFileWriter()
    outputPages = 0
    pdf_fileName = getFileName(filepath)
    if pdf_fileName:
        for pdf_file in pdf_fileName:
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
        Fun.MessageBox("PDF文件合并完成！合并后的文件名为 out.pdf")
        print("PDF文件合并完成！")
    else:
        print("没有可以合并的PDF文件！")
