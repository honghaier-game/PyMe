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

import threading
import urllib.request
from bs4 import BeautifulSoup
from   PIL import Image,ImageTk,ImageFont,ImageDraw
G_UITreeImageArray={}
G_UITreeItemArray={}
threadAction = True
header = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.8',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive'
}
#代码参考博客：https://www.cnblogs.com/raorao1994/p/10301811.html
def Download(url, picAlt, name):
    global G_UITreeImageArray
    global G_UITreeItemArray
    newPath = os.getcwd() + "\\images\\"+ picAlt + "\\"
    fullPath = '{0}{1}.jpg'.format(newPath, name)
    imageName = '{0}.jpg'.format(name)
    if url.find(".png") >= 0 :
        fullPath = '{0}{1}.png'.format(newPath, name)
        imageName = '{0}.png'.format(name)
    TreeView_2 = Fun.GetElement('LeftTreeBar','TreeView_2')
    parentItem = ''
    if not os.path.exists(newPath):
        os.makedirs(newPath)
        parentItem = TreeView_2.insert('','end',newPath,text=picAlt,values=('1'),tags = ('dirs',))
        G_UITreeItemArray[picAlt] = parentItem
    else:
        if picAlt in G_UITreeItemArray:
            parentItem = G_UITreeItemArray[picAlt]
        else:
            parentItem = TreeView_2.insert('','end',newPath,text=picAlt,values=('1'),tags = ('dirs',))
            G_UITreeItemArray[picAlt] = parentItem
    newTreeItem = TreeView_2.insert(parentItem,'end',fullPath,text=imageName,values=('2'))
    urllib.request.urlretrieve(url, fullPath)
#代码参考博客：https://www.cnblogs.com/raorao1994/p/10301811.html
def run(targetUrl, uiName,beginNUM, endNUM):
    global threadAction
    urlPath, webName = os.path.split(targetUrl)
    Text_2 = Fun.GetElement('RightTextBar','Text_2')
    if threadAction == False:
        output = 'Stop'
        Text_2.insert(tkinter.END,output)
        return
    req = urllib.request.Request(url=targetUrl, headers=header)
    response = urllib.request.urlopen(req)
    html = response.read().decode('gb2312', 'ignore')
    soup = BeautifulSoup(html, 'html.parser')
    Divs = soup.find_all('div', attrs={'id': 'big-pic'})
    nowpage = soup.find('span', attrs={'class': 'nowpage'}).get_text()
    totalpage = soup.find('span', attrs={'class': 'totalpage'}).get_text()
    if beginNUM == endNUM:
        return
    for div in Divs:
        beginNUM = beginNUM + 1
        if div.find('a') is None:
            print('No Images')
            return
        elif div.find('a')['href'] is None or div.find('a')['href'] == "":
            print('No Images')
            return
    labelText = '>>>：Progress ：' + str(beginNUM) + '/' + str(endNUM) + ' ，DownLoading Images：('+ str(nowpage) + '/' + str(totalpage) + ')'
    Fun.SetText(uiName,'Label_9',labelText)
    if int(nowpage) < int(totalpage):
        nextPageLink = urlPath + '//' + (div.find('a')['href'])
    elif int(nowpage) == int(totalpage):
        nextPageLink = (div.find('a')['href'])
    picLink = (div.find('a').find('img')['src'])
    picAlt = (div.find('a').find('img'))['alt']
    output = 'Image Link:'+ picLink + '\n'
    Text_2.insert(tkinter.END,output)
    output = 'DirName：[ '+ picAlt + ' ] ' + '\n'
    Text_2.insert(tkinter.END,output)
    output = 'Start...........\n'
    Text_2.insert(tkinter.END,output)
    Download(picLink, picAlt, nowpage)
    output = 'Finish！\n'
    Text_2.insert(tkinter.END,output)
    output = 'Mext link:'+nextPageLink + '\n'
    Text_2.insert(tkinter.END,output)
    Text_2.see(tkinter.END)
    run(nextPageLink, uiName , beginNUM, endNUM)
    return
def Form_1_onLoad(uiName):
    Fun.SetText(uiName,'Entry_3','http://www.mmonly.cc/mmtp/qcmn/237273_10.html')
    Fun.SetText(uiName,'Entry_5','200')
def Button_6_onCommand(uiName,widgetName):
    global threadAction
    targetUrl = Fun.GetText(uiName,"Entry_3")
    total = Fun.GetText(uiName,"Entry_5")
    Text_2 = Fun.GetElement("RightTextBar","Text_2")
    Text_2.delete('0.0',tkinter.END)
    threadAction = True
    run_thread = threading.Thread(target=run, args=[targetUrl,uiName,0,int(total)])
    run_thread.start()
def Button_7_onCommand(uiName,widgetName):
    global threadAction
    threadAction = False 
