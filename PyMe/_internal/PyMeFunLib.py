import os
Language = None
#写入工具类函数
def WriteToolFunctions(f):
    code='''
def IsInt(text):
    """'+Language.G_Language[8000]+'"""
    if text.isdigit() == True:
        return True
    return False
def IsFloat(text):
    """'+Language.G_Language[8001]+'"""
    if text.count('.') == 1:
        left = text.split('.')[0]
        right = text.split('.')[1]
        lright = ''
        if left.count('-') == 1 and left[0] == '-':
            lright = left.split('-')[1]
        elif left.count('-') == 0:
            lright = left
        if right.isdigit() and lright.isdigit():
            return True
    return False
def IsNumeric(text):
    """'+Language.G_Language[8002]+'"""
    if IsInt(text) == True or IsFloat(text) == True:
        return True
    return False
def CheckSpecialChar(text):
    """'+Language.G_Language[8003]+'"""
    string = \'~!@#$%^&*()+-*/<>,.[]、‘’\\\'"{}/^\'
    for i in string:
        if i in text:
            return True
    return False
def IsMobilePhone(text):
    """'+Language.G_Language[8004]+'"""
    ret = re.match(r"^1[35789]\d{9}$", text)
    if ret:
        return True
    return False
def IsEmail(text):
    """'+Language.G_Language[8005]+'"""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, text) is not None
def RandNumber(begin=0,end=100):
    """'+Language.G_Language[9000]+'"""
    import random
    return random.randint(begin,end)
def GetCurrTime(splitChar=\':\'):
    """'+Language.G_Language[9001]+'"""
    import datetime
    nowDateTime = datetime.datetime.now()
    currTime = str("%d%s%d%s%d"%(nowDateTime.hour,splitChar,nowDateTime.minute,splitChar,nowDateTime.second))
    return currTime
def GetCurrDate(splitChar=\':\'):
    """'+Language.G_Language[9002]+'"""
    import datetime
    nowDateTime = datetime.datetime.now()
    currDate = str("%d%s%d%s%d"%(nowDateTime.year,splitChar,nowDateTime.month,splitChar,nowDateTime.day))
    return currDate
def Sleep(second=1):
    """'+Language.G_Language[9354]+'"""
    import time
    time.sleep(second)
def OutputProcessToText(cmdText,uiName,elementName):
    """'+Language.G_Language[9009]+'"""
    DelAllLines(uiName,elementName)
    try:
        import subprocess
        process = subprocess.Popen(cmdText,shell=True, bufsize=0, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,stdin=subprocess.PIPE,encoding=\'utf-8\')
        outputString = process.stdout.readline()
        Result = 0
        while outputString:
            AddLineText(uiName,elementName,outputString)
            outputString = process.stdout.readline()
        process.stdout.close()
    except Exception as ex:
        if uiName and elementName:
            AddLineText(uiName,elementName,str(ex))
        else:
            print(str(ex))'''
    f.write(code)

#写入增加控件到字典的函数
def WriteRegisterElementFunction(f):
    code='''
def GetUIName(root,className):
    global G_UIRootIDDictionary
    global G_UIElementDictionary
    uiName = className
    if className in G_UIRootIDDictionary and G_UIRootIDDictionary[className] == root:
        return uiName
    if G_UIElementDictionary:
        classIndex = 0
        while uiName in G_UIElementDictionary:
            classIndex = classIndex + 1
            uiName = className + "_" + str(classIndex)
    G_UIRootIDDictionary[className] = root
    return uiName

def GetUIParams(uiName):
    """'+Language.G_Language[1492]+'"""
    global G_UIParamsDictionary
    if uiName in G_UIParamsDictionary:
        return G_UIParamsDictionary[uiName]
    else:
        G_UIParamsDictionary[uiName] = uiName
    return uiName

def HScrollBar_Config(event,scrollBar):
    parentinfo = event.widget.winfo_parent()
    parentWidget = event.widget._nametowidget(parentinfo)
    top = parentWidget.winfo_height()-20
    width = parentWidget.winfo_width()
    if top >= 0 and width >= 0:
        scrollBar.place(x = 0,y = top,width = width ,height = 20)
def VScrollBar_Config(event,scrollBar):
    parentinfo = event.widget.winfo_parent()
    parentWidget = event.widget._nametowidget(parentinfo)
    left = parentWidget.winfo_width()-20
    height = parentWidget.winfo_height()
    if left >= 0 and height >= 0:
        scrollBar.place(x = left,y = 0,width = 20,height = height)
def Register(uiName,elementName,element,alias=None,groupName=None,styleName=None):
    """'+Language.G_Language[1201]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementLayerDictionary
    global G_UIRootSizeDictionary
    global G_UIActiveDictionary
    global G_UICommandDictionary
    global G_UIElementPlaceDictionary
    global G_UIElementRoundRectangleDictionary
    global G_UIGroupDictionary
    global G_UIStyleDictionary
    global G_UIRadioButtonGroupArray
    global G_CanvasSizeDictionary
    global G_CanvasShapeDictionary
    global G_CanvasParamDictionary
    global G_CanvasFontDictionary
    global G_CanvasImageDictionary
    global G_CanvasEventDictionary
    global G_CanvasPointDictionary
    global G_ListViewTagDictionary
    global G_UIElementVariableArray
    global G_UIElementIconDictionary
    if uiName not in G_UIElementDictionary:
        G_UIElementDictionary[uiName]={}
        G_UIElementLayerDictionary[uiName]={}
        G_UIRootSizeDictionary[uiName]={}
        G_UICommandDictionary[uiName]={}
        G_UIActiveDictionary[uiName]={}
        G_UIElementAliasDictionary[uiName]={}
        G_UIElementPlaceDictionary[uiName]={}
        G_UIElementRoundRectangleDictionary[uiName]={}
        G_UIGroupDictionary[uiName]={}
        G_UIStyleDictionary[uiName]={}
        G_UIRadioButtonGroupArray[uiName]={}
        G_CanvasSizeDictionary[uiName]={}
        G_CanvasShapeDictionary[uiName]={}
        G_CanvasParamDictionary[uiName]={}  
        G_CanvasFontDictionary[uiName]={}
        G_CanvasImageDictionary[uiName]={}
        G_CanvasEventDictionary[uiName]={}
        G_CanvasPointDictionary[uiName]={}
        G_CanvasPointDictionary[uiName]={}
        G_UIElementVariableArray[uiName]={}
        G_ListViewTagDictionary[uiName]={}
        G_UIElementIconDictionary[uiName]={}
        G_UIElementIconDictionary[uiName]['MainMenu'] = {}
        G_UIElementIconDictionary[uiName]['SysTray'] = {}
    G_UIElementDictionary[uiName][elementName]=element 
    if elementName == 'UIClass': 
        G_UIElementAliasDictionary[uiName].clear() 
    if alias: 
        G_UIElementAliasDictionary[uiName][alias]=elementName 
    if groupName: 
        G_UIGroupDictionary[uiName][elementName]=groupName 
    if styleName: 
        G_UIStyleDictionary[uiName][elementName]=styleName 
    if elementName.find('TreeView_') >= 0:
        G_UIElementIconDictionary[uiName][elementName]={}
    if elementName.find('ListView_') >= 0:
        G_ListViewTagDictionary[uiName][elementName]=[]
    if elementName.find('_HScrollbar') >= 0:
        FrameName = elementName.replace('_HScrollbar','')
        if FrameName:
            FrameWidget = G_UIElementDictionary[uiName][FrameName]
            FrameWidget.bind('<Configure>',EventFunction_Adaptor(HScrollBar_Config,scrollBar = element))
    if elementName.find('_VScrollbar') >= 0:
        FrameName = elementName.replace('_VScrollbar','')
        if FrameName:
            FrameWidget = G_UIElementDictionary[uiName][FrameName]
            FrameWidget.bind('<Configure>',EventFunction_Adaptor(VScrollBar_Config,scrollBar = element))
''' 
    f.write(code)
#写入设置暗色标题栏
def WriteSetTitleBar(f):
    code='''
def SetTitleBar(root,titleText=\'\',isDarkMode=False,isDropTitle=False):
    """'+Language.G_Language[1494]+'"""
    try :
        root.update()
        root.title(titleText)
        if isDarkMode == True and isDropTitle == False:
            DARK_MODE = 20
            DwmSetWindowAttribute = ctypes.windll.dwmapi.DwmSetWindowAttribute
            WindowHandle = ctypes.windll.user32.GetParent(root.winfo_id())
            value = ctypes.c_int(2)
            DwmSetWindowAttribute(WindowHandle, DARK_MODE, ctypes.byref(value), ctypes.sizeof(value))
            root.update()
        if isDropTitle == True:
            root.overrideredirect(True)
    # f.write('            from win32gui import GetParent, SetWindowPos, UpdateWindow, SetWindowLong, GetWindowLong, ReleaseCapture, SendMessage
    # f.write('            from win32con import NULL, SWP_NOSIZE, SWP_NOMOVE, SWP_NOZORDER, SWP_DRAWFRAME, GWL_STYLE, WS_CAPTION, WM_SYSCOMMAND, SC_MOVE, HTCAPTION, WS_THICKFRAME
    # f.write('            WindowHandle = ctypes.windll.user32.GetParent(root.winfo_id())    
    # f.write('            SetWindowLong(WindowHandle, GWL_STYLE, GetWindowLong(WindowHandle, GWL_STYLE) & ~WS_CAPTION & ~WS_THICKFRAME)
    # f.write('            SetWindowPos(WindowHandle, NULL, 0, 0, 0, 0, SWP_DRAWFRAME)
    # f.write('            UpdateWindow(WindowHandle)
    except Exception:
        root.title(titleText)


''' 
    f.write(code)
#写入增加控件到字典的函数
def WriteDestroyUI(f):
    code='''
    #f.write(Language.G_Language[1300]+'
def PlayDestroyDialogAction(uiName,result,topLevel,animation='zoomout'):
    def FadeOut(topLevel,alpha):
        try :
            hwnd = windll.user32.GetParent(topLevel.winfo_id())
            _winlib = ctypes.windll.user32
            style = _winlib.GetWindowLongA( hwnd, 0xffffffec ) | 0x00080000
            _winlib.SetWindowLongA( hwnd, 0xffffffec, style )
            _winlib.SetLayeredWindowAttributes( hwnd, 0, alpha+1, 2 )
            alpha = alpha - 1
        except ImportError:
            pass
        if alpha > 0:
            topLevel.after(1,lambda:FadeOut(topLevel = topLevel,alpha = alpha))
        else:
            DestroyUI(uiName,result)
            print("结束")
    def ZoomOut(topLevel,zoom,win_x,win_y,win_width,win_height):
        try :
            center_x = win_x + int(win_width/2)
            center_y = win_y + int(win_height/2)
            zw = int(win_width * zoom)
            zh = int(win_height * zoom)
            zx = center_x - int(zw/2)
            zy = center_y - int(zh/2)
            topLevel.geometry('%dx%d+%d+%d'%(zw,zh,zx,zy))
            zoom = zoom - 0.01
        except ImportError:
            pass
        if zoom > 0.0:
            topLevel.after(1,lambda:ZoomOut(topLevel = topLevel,zoom = zoom ,win_x = win_x,win_y = win_y,win_width=win_width,win_height=win_height))
        else:
            DestroyUI(uiName,result)
            print("结束")
    if animation == "fadeout":
        try :
            hwnd = windll.user32.GetParent(topLevel.winfo_id())
            _winlib = ctypes.windll.user32
            style = _winlib.GetWindowLongA( hwnd, 0xffffffec ) | 0x00080000
            _winlib.SetWindowLongA( hwnd, 0xffffffec, style )
            _winlib.SetLayeredWindowAttributes( hwnd, 0, 0, 2 )
            topLevel.deiconify()
            topLevel.after(1,lambda:FadeOut(topLevel = topLevel,alpha = 255))
        except ImportError:
            pass
    elif animation == "zoomout":
        try :
            win_x = topLevel.winfo_x()
            win_y = topLevel.winfo_y()
            win_width = topLevel.winfo_width()
            win_height = topLevel.winfo_height()
            topLevel.after(1,lambda:ZoomOut(topLevel = topLevel,zoom = 1.0,win_x = win_x,win_y = win_y,win_width=win_width,win_height=win_height))
        except ImportError:
            pass
def DestroyUI(uiName,result=0,animation=''):
    """'+Language.G_Language[1300]+'"""
    global G_UIElementAliasDictionary
    global G_UIRootSizeDictionary
    global G_UIElementDictionary
    global G_UIElementLayerDictionary
    global G_UICommandDictionary
    global G_UIElementPlaceDictionary
    global G_UIElementRoundRectangleDictionary
    global G_UIGroupDictionary
    global G_UIStyleDictionary
    global G_UIRadioButtonGroupArray
    global G_CanvasSizeDictionary
    global G_CanvasShapeDictionary
    global G_CanvasParamDictionary
    global G_CanvasFontDictionary
    global G_CanvasImageDictionary
    global G_CanvasEventDictionary
    global G_CanvasPointDictionary
    global G_UIElementIconDictionary
    global G_UIInputDataArray
    global G_TopDialog
    #f.write('    global G_UIElementUserDataArray
    if uiName in G_UIElementDictionary:
        root = GetElement(uiName,"root")
        if root is not None:
            if G_TopDialog is root:
                G_TopDialog = None
            animation = animation.lower()
            if animation != '':
                PlayDestroyDialogAction(uiName,result,root,animation)
                return
            if root.master:
                try:
                    GetUIDataDictionary(uiName)
                except:
                    pass
            try:
                if root.master != None or result == 0:
                    root.withdraw()
                    for childName in root.children.keys():
                        child = root.children[childName]
                        try:
                            child.pack_forget()
                        except:
                            pass
                        try:
                            child.grid_forget()
                        except:
                            pass
                        try:
                            child.place_forget()
                        except:
                            pass
                    root.destroy()
            except:
                pass
        G_UIElementDictionary.pop(uiName)
        G_UIElementLayerDictionary.pop(uiName)
        G_UIRootSizeDictionary.pop(uiName)
        G_UICommandDictionary.pop(uiName)
        G_UIElementAliasDictionary.pop(uiName)
        G_UIElementPlaceDictionary.pop(uiName)
        G_UIElementRoundRectangleDictionary.pop(uiName)
        G_UIGroupDictionary.pop(uiName)
        G_UIStyleDictionary.pop(uiName)
        G_UIRadioButtonGroupArray.pop(uiName)
        G_CanvasSizeDictionary.pop(uiName)
        G_CanvasShapeDictionary.pop(uiName)
        G_CanvasParamDictionary.pop(uiName)
        G_CanvasFontDictionary.pop(uiName)
        G_CanvasImageDictionary.pop(uiName)
        G_CanvasEventDictionary.pop(uiName)
        G_CanvasPointDictionary.pop(uiName)
        G_UIElementIconDictionary.pop(uiName)
        G_UIInputDataArray[\'PFunc\'] = GetParentCallFunc()
        G_UIInputDataArray[\'result\'] = result

''' 
    f.write(code)
#写入增加控件到字典的函数
def WriteDestroyUI_App(f):
    code='''
    #f.write(Language.G_Language[1300]+'
def DestroyUI(uiName,result=0):
    """'+Language.G_Language[1300]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementLayerDictionary
    global G_UICommandDictionary
    global G_UIElementPlaceDictionary
    global G_UIElementRoundRectangleDictionary
    global G_UIGroupDictionary
    global G_UIStyleDictionary
    global G_UIRadioButtonGroupArray
    global G_CanvasSizeDictionary
    global G_CanvasShapeDictionary
    global G_CanvasParamDictionary
    global G_CanvasFontDictionary
    global G_CanvasImageDictionary
    global G_CanvasEventDictionary
    global G_CanvasPointDictionary
    global G_UIElementIconDictionary
    global G_UIInputDataArray
    #f.write('    global G_UIElementUserDataArray
    if uiName in G_UIElementDictionary:
        root = GetElement(uiName,"root")
        if root is not None:
            root.SetVisible(False)
        G_UIElementDictionary.pop(uiName)
        G_UIElementLayerDictionary.pop(uiName)
        G_UICommandDictionary.pop(uiName)
        G_UIElementAliasDictionary.pop(uiName)
        G_UIElementPlaceDictionary.pop(uiName)
        G_UIElementRoundRectangleDictionary.pop(uiName)
        G_UIGroupDictionary.pop(uiName)
        G_UIStyleDictionary.pop(uiName)
        G_UIRadioButtonGroupArray.pop(uiName)
        G_CanvasSizeDictionary.pop(uiName)
        G_CanvasShapeDictionary.pop(uiName)
        G_CanvasParamDictionary.pop(uiName)
        G_CanvasFontDictionary.pop(uiName)
        G_CanvasImageDictionary.pop(uiName)
        G_CanvasEventDictionary.pop(uiName)
        G_CanvasPointDictionary.pop(uiName)
        G_UIElementIconDictionary.pop(uiName)
    #f.write('        G_UIElementUserDataArray.pop(uiName)
        G_UIInputDataArray[\'result\'] = result
        if len(G_UIElementDictionary) == 0:
            QuitApplication()
            
''' 
    f.write(code)
#写入输出到界面的函数
def WriteGetElementFunction(f):
    code='''
    #f.write(Language.G_Language[1202]+'
def GetElement(uiName,elementName):
    """'+Language.G_Language[1202]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary:
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            return G_UIElementDictionary[uiName][elementName]
        if elementName.find("TreeView") >= 0:
            elementName = elementName.replace("TreeView","ListView")
            if elementName in G_UIElementDictionary[uiName]:
                return G_UIElementDictionary[uiName][elementName]
    return None
    #f.write(Language.G_Language[1246]+'
def GetElementName(element,isAliasName=True):
    """'+Language.G_Language[1246]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    for uiName in G_UIElementDictionary:
        for elementName in G_UIElementDictionary[uiName]:
            Control = G_UIElementDictionary[uiName][elementName]
            if Control == element:
                if isAliasName == True:
                    for aliasName in  G_UIElementAliasDictionary[uiName].keys():
                        if G_UIElementAliasDictionary[uiName][aliasName] == elementName:
                            return uiName,aliasName
                return uiName,elementName
            if hasattr(Control,"GetEntry") == True:
                ChildWidget = Control.GetEntry()
                if ChildWidget is element:
                    if isAliasName == True:
                        for aliasName in  G_UIElementAliasDictionary[uiName].keys():
                            if G_UIElementAliasDictionary[uiName][aliasName] == elementName:
                                return uiName,aliasName
                    return uiName,elementName
            if hasattr(Control,"GetWidget") == True:
                ChildWidget = Control.GetWidget()
                if ChildWidget is element:
                    if isAliasName == True:
                        for aliasName in  G_UIElementAliasDictionary[uiName].keys():
                            if G_UIElementAliasDictionary[uiName][aliasName] == elementName:
                                return uiName,aliasName
                    return uiName,elementName
    return None,None
#注册Form_1的回调函数:
def SetForm1_CallBack(uiName,eventType,onLoadCallBack=None):
    pass
#运行Form_1的回调函数:
def RunForm1_CallBack(uiName,eventType,onLoadCallBack=None):
    if onLoadCallBack:
        return onLoadCallBack(uiName)
def PrepareDisplayUI(uiName,form1,onLoadCallBack=None):
    global G_UIActiveDictionary
    children = form1.winfo_children()
    for child in children:
        uiName,elementName = GetElementName(child)
        if elementName and uiName in G_UIActiveDictionary.keys():
            G_UIActiveDictionary[uiName][elementName] = child
    if uiName in G_UIActiveDictionary.keys():
        G_UIActiveDictionary[uiName]['onLoad'] = onLoadCallBack
def ActiveElement(uiName,element):
    global G_UIActiveDictionary
    if uiName in G_UIActiveDictionary:
        for elementName in G_UIActiveDictionary[uiName].keys():
            if G_UIActiveDictionary[uiName][elementName] == element:
                G_UIActiveDictionary[uiName].pop(elementName)
                break
    if uiName in G_UIElementDictionary.keys():
        if uiName in G_UIElementRoundRectangleDictionary:
            for elementName in G_UIElementRoundRectangleDictionary[uiName]:
                Control = G_UIElementDictionary[uiName][elementName]
                if Control == element:
                    RRInfo = G_UIElementRoundRectangleDictionary[uiName][elementName]
                    ShowRoundedRectangle(Control,RRInfo[0],RRInfo[1])
        Form_1 = GetElement(uiName,"Form_1")
        if Form_1 == element:
    #这会导致不正常的显示所有的界面
    #f.write('        UpdateAllElementPlace(uiName)
            return
        for uiName in G_UIElementPlaceDictionary.keys():
            for elementName in G_UIElementPlaceDictionary[uiName]:
                if elementName in G_UIElementDictionary[uiName].keys():
                    Control = G_UIElementDictionary[uiName][elementName]
                    if hasattr(Control,"GetEntry") == True:
                        Control = Control.GetEntry()
                    elif hasattr(Control,"GetWidget") == True:
                        Control = Control.GetWidget()
                    if Control == element:
                        UpdateElementPlace(uiName,elementName)
                    else:
                        try:
                            parentInfo = Control.winfo_parent()
                            parentWidget = Control._nametowidget(parentInfo)
                            UIRoot = GetElement(uiName,'root')
                            Form1 = GetElement(uiName,'Form_1')
                            if Form1:
                                while parentWidget is not None and parentWidget is not Form1 and parentWidget is not UIRoot:
                                    if parentWidget == element:
                                        UpdateElementPlace(uiName,elementName)
                                        break
                                    parentInfo = parentWidget.winfo_parent()
                                    parentWidget = Control._nametowidget(parentInfo)
                        except Exception as ex:
                            print(ex)
        if uiName in G_UIActiveDictionary.keys() and len(G_UIActiveDictionary[uiName]) == 1:
            if G_UIActiveDictionary[uiName]['onLoad'] is not None:
                G_UIActiveDictionary[uiName]['onLoad'](uiName)
                G_UIActiveDictionary[uiName].clear()
                ReDrawCanvasRecord(uiName)
                UpdateAllElementPlace(uiName)
def ActiveFrameChildsElement_InEditor(uiName,element):
    children = element.winfo_children()
    for child in children:
        uiName2,elementName = GetElementName(child)
        if uiName2 and elementName:
            realElementName = elementName
            if uiName2 in G_UIElementAliasDictionary.keys() and realElementName in G_UIElementAliasDictionary[uiName2].keys():
                realElementName = G_UIElementAliasDictionary[uiName2][realElementName]
            if realElementName:
                UpdateElementPlace(uiName2,realElementName)
def DestroyElement(uiName,elementName):
    """'+Language.G_Language[9329]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName)
    if hasattr(Control,"GetEntry") == True:
        Control = Control.GetEntry()
    elif hasattr(Control,"GetWidget") == True:
        Control = Control.GetWidget()
    if Control:
        Control.destroy()
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            G_UIElementAliasDictionary[uiName].pop(elementName)
        elif elementName in G_UIElementDictionary[uiName].keys():
            G_UIElementDictionary[uiName].pop(elementName)
''' 
    f.write(code)
#写入创建控件的函数
def WriteCreateElementFunction(f):
    code='''
def GenNewElementName(uiName,elementType):
    elementIndex = 1
    for elementName in G_UIElementDictionary[uiName]:
        if elementName.find('_') >= 0:
            splitArray = elementName.split('_')
            elementIndex = splitArray[-1]
    elementIndex = int(elementIndex) + 1
    elementName = elementType+'_'+str(elementIndex)
    return elementName

def CreateElementFromEXUIControl(uiName,ParentElement,elementType):
    try:
        uiClass = 'EXUIControl'
        import importlib
        from   importlib import import_module
        importModule = importlib.import_module(uiClass)
        importModule = importlib.reload(importModule)
        if hasattr(importModule,elementType) == True:
            importModule.G_ExeDir = G_ExeDir
            importModule.G_ResDir = G_ResDir
            ElementClass = getattr(importModule,elementType)
            newElement = ElementClass(ParentElement)
            return newElement
    except Exception as ex:
        MessageBox('请返回工程主界面保存，由系统生成复合控件代码。')

def CreateLabel(uiName,parentName='Form_1',elementName=''):
    """'+Language.G_Language[9300]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newLabel = tkinter.Label(ParentElement,text="Label")
            labelName = GenNewElementName(uiName,'Label')
            Register(uiName,labelName,newLabel,elementName)
            return newLabel
    return None
def CreateButton(uiName,parentName='Form_1',elementName=''):
    """'+Language.G_Language[9301]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newButton = tkinter.Button(ParentElement,text="Button")
            buttonName = GenNewElementName(uiName,'Button')
            Register(uiName,buttonName,newButton,elementName)
            return newButton
    return None
def CreateLabelButton(uiName,parentName='Form_1',elementName=''):
    """'+Language.G_Language[9302]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'LabelButton')
            if newElement:
                labelButtonName = GenNewElementName(uiName,'LabelButton')
                Register(uiName,labelButtonName,newElement,elementName)
                return newElement
    return None
def CreateEntry(uiName,parentName='Form_1',elementName=''):
    """'+Language.G_Language[9303]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'CustomEntry')
            if newElement:
                entryName = GenNewElementName(uiName,'Entry')
                Register(uiName,entryName,newElement,elementName)
                return newElement
    return None
def CreateText(uiName,parentName='Form_1',elementName=''):
    """'+Language.G_Language[9304]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newText = tkinter.Text(ParentElement)
            textName = GenNewElementName(uiName,'Text')
            Register(uiName,textName,newText,elementName)
            return newText
    return None
def CreateListBox(uiName,parentName='Form_1',elementName=''):
    """'+Language.G_Language[9305]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newListBox = tkinter.Listbox(ParentElement)
            listBoxName = GenNewElementName(uiName,'ListBox')
            Register(uiName,listBoxName,newListBox,elementName)
            return newListBox
    return None
def CreateComboBox(uiName,parentName='Form_1',elementName=''):
    """'+Language.G_Language[9306]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            comboBoxName = GenNewElementName(uiName,'ComboBox')
            comboBoxVariable = AddTKVariable(uiName,comboBoxName)
            newComboBox = tkinter.ttk.Combobox(ParentElement,textvariable=comboBoxVariable, state="readonly")
            Register(uiName,comboBoxName,newComboBox,elementName)
            return newComboBox
    return None
def CreateRadioButtonGroup(uiName,parentName='Form_1',groupName='',defaultValue=1):
    """'+Language.G_Language[9310]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            groupVariable = AddTKVariable(uiName,groupName,defaultValue)
            AddUserData(uiName,parentName,groupName,"radiogroup",groupVariable,0)
            return groupVariable
    return None
def CreateRadioButton(uiName,parentName='Form_1',elementName='',groupName='',defaultValue=1,style='indicatoron'):
    """'+Language.G_Language[9307]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            radioButtonName = GenNewElementName(uiName,'RadioButton')
            groupVariable = GetUserData(uiName,parentName,groupName)
            newRadioButton = tkinter.Radiobutton(ParentElement,variable=groupVariable,value=defaultValue,text="RadioButton",anchor=tkinter.W)
            Register(uiName,radioButtonName,newRadioButton,elementName,groupName)
            if style == 'normal':
                newRadioButton.configure(indicatoron = False)
            elif style == 'selfdrawing':
                SetRadioButtonPyMeStyle(uiName,radioButtonName,groupVariable.get(),defaultValue,'#000000','#000000')
            return newRadioButton
    return None
def CreateCheckButton(uiName,parentName='Form_1',elementName='',defaultValue=False,style='indicatoron'):
    """'+Language.G_Language[9308]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            checkButtonName = GenNewElementName(uiName,'CheckButton')
            checkButtonVariable = AddTKVariable(uiName,checkButtonName)
            checkButtonVariable.set(defaultValue)
            newCheckButton = tkinter.Checkbutton(ParentElement,variable=checkButtonVariable,text="CheckButton",anchor=tkinter.W)
            Register(uiName,checkButtonName,newCheckButton,elementName)
            if style == 'normal':
                newCheckButton.configure(indicatoron = False)
            elif style == 'selfdrawing':
                SetCheckButtonPyMeStyle(uiName,checkButtonName,defaultValue,'#000000','#000000')
            return newCheckButton
    return None
def CreateSwitchButton(uiName,parentName='Form_1',elementName=''):
    """'+Language.G_Language[9309]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'SwitchButton')
            if newElement:
                switchButtonName = GenNewElementName(uiName,'SwitchButton')
                Register(uiName,switchButtonName,newElement,elementName)
                return newElement
    return None
def CreateLabelFrame(uiName,parentName='Form_1',elementName=''):
    """'+Language.G_Language[9311]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newLabelFrame = tkinter.LabelFrame(ParentElement)
            labelFrameName = GenNewElementName(uiName,'LabelFrame')
            Register(uiName,labelFrameName,newLabelFrame,elementName)
            return newLabelFrame
    return None
def CreateFrame(uiName,parentName='Form_1',elementName=''):
    """'+Language.G_Language[9312]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newFrame = tkinter.Frame(ParentElement)
            frameName = GenNewElementName(uiName,'Frame')
            Register(uiName,frameName,newFrame,elementName)
            return newFrame
    return None
def CreateCanvas(uiName,parentName='Form_1',elementName=''):
    """'+Language.G_Language[9320]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newCanvas = tkinter.Canvas(ParentElement)
            canvasName = GenNewElementName(uiName,'Canvas')
            Register(uiName,canvasName,newCanvas,elementName)
            return newCanvas
    return None
def CreateScale(uiName,parentName='Form_1',elementName='',orient = tkinter.HORIZONTAL):
    """'+Language.G_Language[9313]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newScale = tkinter.Scale(ParentElement,orient = tkinter.HORIZONTAL)
            scaleName = GenNewElementName(uiName,'Scale')
            Register(uiName,scaleName,newScale,elementName)
            return newScale
    return None
def CreateSlider(uiName,parentName='Form_1',elementName='',orient = tkinter.HORIZONTAL):
    """'+Language.G_Language[9314]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'Slider')
            if newElement:
                sliderName = GenNewElementName(uiName,'Slider')
                Register(uiName,sliderName,newElement,elementName)
                return newElement
    return None
def CreateProgress(uiName,parentName='Form_1',elementName='',orient = tkinter.HORIZONTAL):
    """'+Language.G_Language[9315]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newProgress = tkinter.ttk.Progressbar(ParentElement,orient = orient)
            progressName = GenNewElementName(uiName,'Progress')
            Register(uiName,progressName,newProgress,elementName)
            return newProgress
    return None
def CreateProgressDial(uiName,parentName='Form_1',elementName=''):
    """'+Language.G_Language[9316]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'ProgressDial')
            if newElement:
                progressDialName = GenNewElementName(uiName,'ProgressDial')
                Register(uiName,progressDialName,newElement,elementName)
                return newElement
    return None
def CreateSpinBox(uiName,parentName='Form_1',elementName=''):
    """'+Language.G_Language[9317]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newSpinBox = tkinter.Spinbox(ParentElement)
            spinBoxName = GenNewElementName(uiName,'SpinBox')
            Register(uiName,spinBoxName,newSpinBox,elementName)
            return newSpinBox
    return None
def CreateTreeView(uiName,parentName='Form_1',elementName=''):
    """'+Language.G_Language[9318]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newTreeView = tkinter.ttk.Treeview(ParentElement,show="tree")
            treeViewName = GenNewElementName(uiName,'TreeView')
            Register(uiName,treeViewName,newTreeView,elementName)
            return newTreeView
    return None
def CreateListView(uiName,parentName='Form_1',elementName=''):
    """'+Language.G_Language[9319]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newListView = tkinter.ttk.Treeview(ParentElement,show="headings")
            listViewName = GenNewElementName(uiName,'ListView')
            Register(uiName,listViewName,newListView,elementName)
            return newListView
    return None
def CreateNoteBook(uiName,parentName='Form_1',elementName=''):
    """'+Language.G_Language[9321]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newNoteBook = tkinter.ttk.Notebook(ParentElement)
            noteBookName = GenNewElementName(uiName,'NoteBook')
            Register(uiName,noteBookName,newNoteBook,elementName)
            return newNoteBook
    return None
def CreatePanedWindow(uiName,parentName='Form_1',elementName='',orient = tkinter.HORIZONTAL):
    """'+Language.G_Language[9322]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newPanedWindow = tkinter.PanedWindow(ParentElement)
            panedWindowName = GenNewElementName(uiName,'PanedWindow')
            Register(uiName,panedWindowName,newPanedWindow,elementName)
            newPanedWindow.configure(showhandle = '0')
            newPanedWindow.configure(sashrelief = 'flat')
            newPanedWindow.configure(sashwidth = '4')
            newPanedWindow.configure(orient = orient)
            return newPanedWindow
    return None
def CreateCalendar(uiName,parentName='Form_1',elementName=''):
    """'+Language.G_Language[9323]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'Calendar')
            if newElement:
                calendarName = GenNewElementName(uiName,'Calendar')
                Register(uiName,calendarName,newElement,elementName)
                return newElement
    return None
def CreateDatePicker(uiName,parentName='Form_1',elementName=''):
    """'+Language.G_Language[9324]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'DatePicker')
            if newElement:
                datepickerName = GenNewElementName(uiName,'DatePicker')
                Register(uiName,datepickerName,newElement,elementName)
                return newElement
    return None

def CreateNavigation(uiName,parentName='Form_1',elementName='',direction = tkinter.HORIZONTAL):
    """'+Language.G_Language[9325]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'Navigation')
            if newElement:
                navigationName = GenNewElementName(uiName,'Navigation')
                Register(uiName,navigationName,newElement,elementName)
                return newElement
    return None

def CreateListMenu(uiName,parentName='Form_1',elementName=''):
    """'+Language.G_Language[9326]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'ListMenu')
            if newElement:
                listmenuName = GenNewElementName(uiName,'ListMenu')
                Register(uiName,listmenuName,newElement,elementName)
                return newElement
    return None

def CreateSwitchPage(uiName,parentName='Form_1',elementName=''):
    """'+Language.G_Language[9327]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'SwitchPage')
            if newElement:
                listmenuName = GenNewElementName(uiName,'SwitchPage')
                Register(uiName,listmenuName,newElement,elementName)
                return newElement
    return None

def CreateShowCase(uiName,parentName='Form_1',elementName=''):
    """'+Language.G_Language[9328]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementAliasDictionary[uiName].keys():
            return None
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'ShowCase')
            if newElement:
                listmenuName = GenNewElementName(uiName,'ShowCase')
                Register(uiName,listmenuName,newElement,elementName)
                return newElement
    return None

def SetBindEventFunction(uiName,elementName,eventName,callbackFunction=None):
    """'+Language.G_Language[9203]+'"""
    Control = GetElement(uiName,elementName)
    if hasattr(Control,"GetEntry") == True:
        Control = Control.GetEntry()
    elif hasattr(Control,"GetWidget") == True:
        Control = Control.GetWidget()
    if Control and callbackFunction:
        RealElementName = elementName
        if uiName in G_UIElementAliasDictionary.keys() and RealElementName in G_UIElementAliasDictionary[uiName].keys():
            RealElementName = G_UIElementAliasDictionary[uiName][RealElementName] 
        if eventName == 'Command':
            if RealElementName.find(\'Scale_\') >= 0: 
                Control.configure(command=SetValueChangedFunction(callbackFunction,uiName = uiName,widgetName = elementName))
            else: 
                Control.configure(command=lambda:CommandFunction_Adaptor(callbackFunction,uiName,elementName))
    # f.write("        elif :
    # f.write("            bindEventName = str('<<'+eventName+'>>')
    # f.write("            Control.bind(bindEventName,EventFunction_Adaptor(callbackFunction,uiName = uiName,widgetName = elementName,callbackFunc=callbackFunction),add=True)
        elif eventName == 'TreeviewSelect' or eventName == 'TreeviewOpen' or eventName == 'TreeviewClose' or eventName == 'ListboxSelect' or eventName == 'ComboboxSelected' or eventName == 'NotebookTabChanged':
            bindEventName = str('<<'+eventName+'>>')
            Control.bind(bindEventName,EventFunction_Adaptor(callbackFunction,uiName = uiName,widgetName = elementName),add=True)
        elif eventName == 'ListviewCellSelected':
            Control.bind('<Button-1>',EventFunction_Adaptor(OnListViewCellClicked,uiName = uiName,widgetName = elementName,callbackFunc=callbackFunction),add=True)
        elif eventName == 'ListViewHeadingClicked':
            Columns = Control.cget('column')
            for columnName in Columns:
                Control.heading(columnName,command=partial(callbackFunction,uiName = uiName,widgetName = elementName,columnname=columnName))
        else:
            bindEventName = str('<'+eventName+'>')
            Control.bind(bindEventName,EventFunction_Adaptor(callbackFunction,uiName = uiName,widgetName = elementName))
''' 
    f.write(code)
#写入取得界面类型的函数
def WriteGetElementTypeFunction(f):
    code='''
    #f.write(Language.G_Language[1245]+'
def GetElementType(uiName,elementName):
    """'+Language.G_Language[1245]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    
    if uiName in G_UIElementAliasDictionary:
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            splitArray = elementName.split('_')
            elementType = splitArray[0]
            if elementType == "PyMe":
                elementType = splitArray[1]
            return elementType
    return None
''' 
    f.write(code)
#写入取得界面矩形信息的函数
def WriteGetElementRectFunction(f):
    code='''
def GetElementXYWH(uiName,elementName):
    """'+Language.G_Language[1318]+'"""
    element = GetElement(uiName,elementName)
    if element:
        x = element.winfo_x()
        y = element.winfo_y()
        width = element.winfo_width()
        height = element.winfo_height()
        return (x,y,width,height)
    return None
def SetElementXY(uiName,elementName,x,y):
    """'+Language.G_Language[9508]+'"""
    element = GetElement(uiName,elementName)
    if element:
        element.place(x=x,y=y)
def SetElementWH(uiName,elementName,width,height):
    """'+Language.G_Language[9509]+'"""
    element = GetElement(uiName,elementName)
    if element:
        element.place(width=width,height=height)
def SetElementXYWH(uiName,elementName,x,y,width,height):
    """'+Language.G_Language[9507]+'"""
    element = GetElement(uiName,elementName)
    if element:
        element.place(x=x,y=y,width=width,height=height)
    
''' 
    f.write(code)
#写入增加控件内置变量的函数
def WriteAddTKVariableFunction(f):
    code='''
    #f.write(Language.G_Language[1203]+'
def AddTKVariable(uiName,elementName,defaultValue = None):
    """'+Language.G_Language[1203]+'"""
    global G_UIElementVariableArray
    
    if uiName not in G_UIElementVariableArray: 
        G_UIElementVariableArray[uiName]={} 
    NameLower = elementName.lower() 
    if NameLower.find(\'combobox_\') >= 0: 
        G_UIElementVariableArray[uiName][elementName]=tkinter.StringVar() 
    elif NameLower.find(\'group_\') >= 0: 
        G_UIElementVariableArray[uiName][elementName]=tkinter.IntVar() 
    elif NameLower.find(\'checkbutton_\') >= 0: 
        G_UIElementVariableArray[uiName][elementName]=tkinter.BooleanVar() 
    else: 
        G_UIElementVariableArray[uiName][elementName]=tkinter.StringVar() 
    if defaultValue: 
        G_UIElementVariableArray[uiName][elementName].set(defaultValue)  
    return G_UIElementVariableArray[uiName][elementName] 


''' 
    f.write(code)
#写入WEB端的
def WriteWebUIClass_HTML(f):
    code='''
class PyMeWeb_ComboBox(dict):
    def __init__(self,uiName,elementName):
        self.values = []
        self.Current = 0 
        self.uiName = uiName 
        self.elementName = elementName 
    def current(self,index):
        self.Current = index
class PyMeWeb_ListBox(dict):
    def __init__(self,uiName,elementName):
        self.values = []
        self.Current = 0 
        self.uiName = uiName 
        self.elementName = elementName 
    def delete(self,startIndex,endIndex='end'):
        if endIndex == 'end':
            endIndex = len(self.values)
        for i in range(startIndex,endIndex):
            self.values.pop(startIndex)
        G_UIElementVariableArray[self.uiName][self.elementName] = self.values
    def insert(self,index,value):
        if index == 'end':
            index = len(self.values)
        if len(self.values) <= index:
            self.values.append(value)
        else:
            self.values.insert(index,value)
        G_UIElementVariableArray[self.uiName][self.elementName] = self.values
    def current(self,index):
        self.Current = index

''' 
    f.write(code)
#写入增加控件内置变量的函数
def WriteAddTKVariableFunction_HTML(f):
    code='''
    #f.write(Language.G_Language[1203]+'
def AddTKVariable(uiName,elementName,defaultValue = None):
    """'+Language.G_Language[1203]+'"""
    global G_UIElementVariableArray
    
    if uiName not in G_UIElementVariableArray: 
        G_UIElementVariableArray[uiName]={} 
    G_UIElementVariableArray[uiName][elementName] = defaultValue  
    return G_UIElementVariableArray[uiName][elementName] 
''' 
    f.write(code)
#写入设置控件内置变量的函数
def WriteSetTKVariableFunction(f):
    code='''
    #f.write(Language.G_Language[1204]+'
def SetTKVariable(uiName,elementName,value):
    """'+Language.G_Language[1204]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    
    if uiName in G_UIElementVariableArray: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName]  
        if elementName in G_UIElementVariableArray[uiName]: 
            G_UIElementVariableArray[uiName][elementName].set(value) 
        if elementName in G_UIGroupDictionary[uiName]: 
            GroupName = G_UIGroupDictionary[uiName][elementName]
            if GroupName in G_UIElementVariableArray[uiName]: 
                G_UIElementVariableArray[uiName][GroupName].set(value) 
''' 
    f.write(code)
#写入设置控件内置变量的函数
def WriteSetTKVariableFunction_HTML(f):
    code='''
    #f.write(Language.G_Language[1204]+'
def SetTKVariable(uiName,elementName,value):
    """'+Language.G_Language[1204]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    
    if uiName in G_UIElementVariableArray: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName]  
        if elementName in G_UIElementVariableArray[uiName]: 
            G_UIElementVariableArray[uiName][elementName] = value  
''' 
    f.write(code)
#写入获取控件内置变量的函数
def WriteGetTKVariableFunction(f):
    code='''
    #f.write(Language.G_Language[1205]+'
def GetTKVariable(uiName,elementName):
    """'+Language.G_Language[1205]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    
    if uiName in G_UIElementVariableArray: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName in G_UIElementVariableArray[uiName]: 
            return G_UIElementVariableArray[uiName][elementName].get()  
        if elementName in G_UIGroupDictionary[uiName]: 
            GroupName = G_UIGroupDictionary[uiName][elementName]
            if GroupName in G_UIElementVariableArray[uiName]: 
                return G_UIElementVariableArray[uiName][GroupName].get()  
    return None
''' 
    f.write(code)
#写入获取控件内置变量的函数
def WriteGetTKVariableFunction_HTML(f):
    code='''
    #f.write(Language.G_Language[1205]+'
def GetTKVariable(uiName,elementName):
    """'+Language.G_Language[1205]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    
    if uiName in G_UIElementVariableArray: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName in G_UIElementVariableArray[uiName]: 
            return G_UIElementVariableArray[uiName][elementName]  
    return None
''' 
    f.write(code)
#写入输出到界面的函数
def WriteAddUserDataFunction(f):
    code='''  
    #f.write(Language.G_Language[1206]+'
def AddUserData(uiName,elementName,dataName,datatype,datavalue,isMapToText = 0):
    """'+Language.G_Language[1206]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementUserDataArray
    if uiName not in G_UIElementUserDataArray:
        G_UIElementUserDataArray[uiName]={} 
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if elementName not in G_UIElementUserDataArray[uiName]:
        G_UIElementUserDataArray[uiName][elementName]=[]
    else:
        for EBData in G_UIElementUserDataArray[uiName][elementName]:
            if EBData[0] == dataName:
                EBData[1] = datatype
                EBData[2] = datavalue
                EBData[3] = isMapToText
                if EBData[3] == 1:
                    SetText(uiName,elementName,datavalue,False)     
                return
    G_UIElementUserDataArray[uiName][elementName].append([dataName,datatype,datavalue,isMapToText])
def DelUserData(uiName,elementName,dataName):
    """'+Language.G_Language[3110]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementUserDataArray   
    if uiName in G_UIElementUserDataArray:   
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName in G_UIElementUserDataArray[uiName]:
            dataIndex = 0
            for EBData in G_UIElementUserDataArray[uiName][elementName]:
                if EBData[0] == dataName:
                    G_UIElementUserDataArray[uiName][elementName].pop(dataIndex)
                    return 
                dataIndex = dataIndex + 1
''' 
    f.write(code)
#写入输出到界面的函数
def WriteAddUserDataFunction_HTML(f):
    code='''  
    #f.write(Language.G_Language[1206]+'
def AddUserData(uiName,elementName,dataName,datatype,datavalue,isMapToText = 0):
    """'+Language.G_Language[1206]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementUserDataArray
    if uiName not in G_UIElementUserDataArray:
        G_UIElementUserDataArray[uiName]={} 
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if elementName not in G_UIElementUserDataArray[uiName]:
        G_UIElementUserDataArray[uiName][elementName]=[]
    else:
        for EBData in G_UIElementUserDataArray[uiName][elementName]:
            if EBData[0] == dataName:
                return
    G_UIElementUserDataArray[uiName][elementName].append([dataName,datatype,datavalue,isMapToText])
def DelUserData(uiName,elementName,dataName):
    """'+Language.G_Language[3110]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementUserDataArray   
    if uiName in G_UIElementUserDataArray:   
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName in G_UIElementUserDataArray[uiName]:
            dataIndex = 0
            for EBData in G_UIElementUserDataArray[uiName][elementName]:
                if EBData[0] == dataName:
                    G_UIElementUserDataArray[uiName][elementName].pop(dataIndex)
                    return 
                dataIndex = dataIndex + 1
''' 
    f.write(code)
#写入输出到界面的函数
def WriteSetUserDataFunction(f):
    code='''
    #f.write(Language.G_Language[1207]+'
def SetUserData(uiName,elementName,dataName,datavalue):
    """'+Language.G_Language[1207]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementUserDataArray   
    if uiName in G_UIElementUserDataArray:   
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName in G_UIElementUserDataArray[uiName]:
            for EBData in G_UIElementUserDataArray[uiName][elementName]:
                if EBData[0] == dataName:
                    EBData[2] = datavalue
                    if EBData[3] == 1:
                        SetText(uiName,elementName,datavalue,False)     
                    return
''' 
    f.write(code)
#写入输出到界面的函数
def WriteGetUserDataFunction(f):
    code='''
    #f.write(Language.G_Language[1208]+'
def GetUserData(uiName,elementName,dataName):
    """'+Language.G_Language[1208]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementUserDataArray
    
    if  uiName in G_UIElementUserDataArray:
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName in G_UIElementUserDataArray[uiName]:
            for EBData in G_UIElementUserDataArray[uiName][elementName]:
                if EBData[0] == dataName:
                    if EBData[1]==\'int\':
                        return int(EBData[2])
                    elif EBData[1]==\'float\':
                        return float(EBData[2])
                    else:
                        return EBData[2]
    return None
''' 
    f.write(code)
#写入输出到界面的函数
def WriteSetTKAttribFunction(f):
    code='''
    #f.write(Language.G_Language[1209]+'
def SetTKAttrib(uiName,elementName,AttribName,attribValue):
    """'+Language.G_Language[1209]+'"""
    Control = GetElement(uiName,elementName)
    if hasattr(Control,"GetEntry") == True:
        Control = Control.GetEntry()
    elif hasattr(Control,"GetWidget") == True:
        Control = Control.GetWidget()
    if Control:
        if AttribName in Control.configure().keys():
            Control[AttribName]=attribValue
    
''' 
    f.write(code)
#写入输出到界面的函数
def WriteGetTKAttribFunction(f):
    code='''
    #f.write(Language.G_Language[1210]+'
def GetTKAttrib(uiName,elementName,AttribName):
    """'+Language.G_Language[1210]+'"""
    Control = GetElement(uiName,elementName)
    if hasattr(Control,"GetEntry") == True:
        Control = Control.GetEntry()
    elif hasattr(Control,"GetWidget") == True:
        Control = Control.GetWidget()
    if Control:
        return Control.cget(AttribName)
    return None
''' 
    f.write(code)
#写入设置控件显示的函数
def WriteSetElementVisibleFunction(f):
    code='''
    #f.write(Language.G_Language[1239]+'
def SetElementVisible(uiName,elementName,Visible):
    """'+Language.G_Language[1870]+'"""
    Control = GetElement(uiName,elementName)
    if Control is None:
        return 
    if hasattr(Control,"GetWidget") == True:
        Control = Control.GetWidget()
    RealElementName = elementName
    if uiName in G_UIElementAliasDictionary.keys() and RealElementName in G_UIElementAliasDictionary[uiName].keys():
        RealElementName = G_UIElementAliasDictionary[uiName][RealElementName] 
    G_UIElementPlaceDictionary[uiName][RealElementName]["visible"] = Visible
    if Visible == True :
        if G_UIElementPlaceDictionary[uiName][RealElementName]["type"] == "pack":
            fill = G_UIElementPlaceDictionary[uiName][RealElementName]["fill"]
            side = G_UIElementPlaceDictionary[uiName][RealElementName]["side"]
            padx = G_UIElementPlaceDictionary[uiName][RealElementName]["padx"]
            pady = G_UIElementPlaceDictionary[uiName][RealElementName]["pady"]
            expand = G_UIElementPlaceDictionary[uiName][RealElementName]["expand"]
            SetControlPack(uiName,elementName,fill,side,padx,pady,expand)
        elif G_UIElementPlaceDictionary[uiName][RealElementName]["type"] == "grid":
            row = G_UIElementPlaceDictionary[uiName][RealElementName]["row"]
            column = G_UIElementPlaceDictionary[uiName][RealElementName]["column"]
            rowspan = G_UIElementPlaceDictionary[uiName][RealElementName]["rowspan"]
            columnspan = G_UIElementPlaceDictionary[uiName][RealElementName]["columnspan"]
            SetControlGrid(uiName,elementName,row,column,rowspan,columnspan)
        elif G_UIElementPlaceDictionary[uiName][RealElementName]["type"] == "place":
            x = 0
            if "relx" in G_UIElementPlaceDictionary[uiName][RealElementName]:
                x = G_UIElementPlaceDictionary[uiName][RealElementName]["relx"]
            else:
                x = G_UIElementPlaceDictionary[uiName][RealElementName]["x"]
            y = 0
            if "rely" in G_UIElementPlaceDictionary[uiName][RealElementName]:
                y = G_UIElementPlaceDictionary[uiName][RealElementName]["rely"]
            else:
                y = G_UIElementPlaceDictionary[uiName][RealElementName]["y"]
            w = 0
            if "relwidth" in G_UIElementPlaceDictionary[uiName][RealElementName]:
                w = G_UIElementPlaceDictionary[uiName][RealElementName]["relwidth"]
            else:
                w = G_UIElementPlaceDictionary[uiName][RealElementName]["width"]
            h = 0
            if "relheight" in G_UIElementPlaceDictionary[uiName][RealElementName]:
                h = G_UIElementPlaceDictionary[uiName][RealElementName]["relheight"]
            else:
                h = G_UIElementPlaceDictionary[uiName][RealElementName]["height"]
            SetControlPlace(uiName,elementName,x,y,w,h)
    else:
        if G_UIElementPlaceDictionary[uiName][RealElementName]["type"] == "pack":
            Control.pack_forget()
        elif G_UIElementPlaceDictionary[uiName][RealElementName]["type"] == "grid":
            Control.grid_forget()
        elif G_UIElementPlaceDictionary[uiName][RealElementName]["type"] == "place":
            Control.place_forget()
        G_UIElementPlaceDictionary[uiName][RealElementName]['visible'] = False
def SetVisible(uiName,elementName,Visible):
    """'+Language.G_Language[1239]+'"""
    SetElementVisible(uiName,elementName,Visible)
def SetElementEnable(uiName,elementName,Enable):
    """'+Language.G_Language[1872]+'"""
    element = GetElement(uiName,elementName)
    if element:
        if elementName and uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find('Frame_') >= 0 or elementName.find('LabelFrame_') >= 0:
            def SetChildrenState(child,state):
                childlist = child.winfo_children()
                for child in childlist:
                    try:
                        child.configure(state=state)
                    except:
                        pass
                    SetChildrenState(child,state)
            if Enable == True:
                SetChildrenState(element,'normal')
            else:
                SetChildrenState(element,'disabled')
        if elementName.find(\'Entry_\') >= 0 or elementName.find(\'LabelButton_\') >= 0:
            if Enable == True:
                element.SetState('normal')
            else:
                element.SetState('disabled')
        else:
            if hasattr(element,"GetEntry") == True:
                element = element.GetEntry()
            elif hasattr(element,"GetWidget") == True:
                element = element.GetWidget()
            try:
                if Enable == True:
                    element.configure(state='normal')
                else:
                    element.configure(state='disabled')
            except:
                pass
def SetEnable(uiName,elementName,Enable):
    """'+Language.G_Language[2641]+'"""
    SetElementEnable(uiName,elementName,Enable)
''' 
    f.write(code)
#写入设置控件显示的函数
def WriteIsElementVisibleFunction(f):
    code='''
    #f.write(Language.G_Language[1240]+'
def IsElementVisible(uiName,elementName):
    """'+Language.G_Language[1871]+'"""
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    return G_UIElementPlaceDictionary[uiName][elementName]['visible']
def IsVisible(uiName,elementName):
    """'+Language.G_Language[1240]+'"""
    return IsElementVisible(uiName,elementName)
def IsElementEnable(uiName,elementName):
    """'+Language.G_Language[1873]+'"""
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if elementName.find(\'Entry_\') >= 0 or elementName.find(\'LabelButton_\') >= 0:
        return G_UIElementDictionary[uiName][elementName].GetState()
    else:
        ElementState = G_UIElementDictionary[uiName][elementName].cget('state')
        ElementState = str(ElementState)
        if ElementState == 'disabled':
            return False
        else:
            return True
def IsEnable(uiName,elementName):
    """'+Language.G_Language[2642]+'"""
    return IsElementEnable(uiName,elementName)

''' 
    f.write(code)
#写入设置控件显示的函数
def WriteSetElementVisibleFunction_Mobile(f):
    code='''
    #f.write(Language.G_Language[1239]+'
def SetElementVisible(uiName,elementName,Visible):
    """'+Language.G_Language[1870]+'"""
    element = GetElement(uiName,elementName)
    if element:
        element.SetVisible(Visible)
def SetVisible(uiName,elementName,Visible):
    """'+Language.G_Language[1239]+'"""
    SetElementVisible(uiName,elementName,Visible)
def SetElementEnable(uiName,elementName,Enable):
    """'+Language.G_Language[1872]+'"""
    element = GetElement(uiName,elementName)
    if element:
        element.SetEnable(Enable)
def SetEnable(uiName,elementName,Enable):
    """'+Language.G_Language[2641]+'"""
    SetElementEnable(uiName,elementName,Enable)

''' 
    f.write(code)
#写入设置控件显示的函数
def WriteIsElementVisibleFunction_Mobile(f):
    code='''
    #f.write(Language.G_Language[1240]+'
def IsElementVisible(uiName,elementName):
    """'+Language.G_Language[1871]+'"""
    element = GetElement(uiName,elementName)
    if element:
        return element.IsVisible()
def IsVisible(uiName,elementName):
    """'+Language.G_Language[1240]+'"""
    return IsElementVisible(uiName,elementName)
def IsElementEnable(uiName,elementName):
    """'+Language.G_Language[1873]+'"""
    element = GetElement(uiName,elementName)
    if element:
        return element.IsEnable()
def IsEnable(uiName,elementName):
    """'+Language.G_Language[2642]+'"""
    return IsElementEnable(uiName,elementName)

''' 
    f.write(code)
#写入更新到文字
def WriteSetTextFunction(f):
    code='''
    #f.write(Language.G_Language[1211]+'
def SetText(uiName,elementName,textValue,aliasName=True):
    """'+Language.G_Language[1211]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    showtext = str(\"%s\"%textValue)
    if aliasName and uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if uiName in G_UIElementVariableArray: 
        if elementName in G_UIElementVariableArray[uiName]:
            G_UIElementVariableArray[uiName][elementName].set(showtext)
            return
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:   
            try:
                if elementName == "root":
                    G_UIElementDictionary[uiName][elementName].title(textValue)
                elif elementName.find(\'Text_\') >= 0:
                    Control = G_UIElementDictionary[uiName][elementName]
                    if hasattr(Control,"GetEntry") == True:
                        Control = Control.GetEntry()
                    Control.delete(\'0.0\',tkinter.END)
                    if len(showtext) > 0:
                        Control.insert(tkinter.END,showtext)
                        Control.see(tkinter.END)
                elif elementName.find(\'Entry_\') >= 0 or elementName.find(\'LabelButton_\') >= 0:
                    G_UIElementDictionary[uiName][elementName].SetText(showtext) 
                else:
                    G_UIElementDictionary[uiName][elementName].configure(text=showtext)
            except Exception as ex:
                print(ex)
def InsertText(uiName,elementName,position=tkinter.END,textValue='',tag=''):
    """'+Language.G_Language[1328]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    showtext = str(\"%s\"%textValue)
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:   
            if elementName.find(\'Text_\') >= 0:
                if len(showtext) > 0:
                    Control = G_UIElementDictionary[uiName][elementName]
                    if hasattr(Control,"GetEntry") == True:
                        Control = Control.GetEntry()
                    Control.mark_set(tkinter.INSERT,position)
                    Control.insert(position,showtext,tag)
                    currentLine = Control.index(tkinter.INSERT)
                    Control.see(currentLine)
                    return  currentLine
    return  None
def GetCurrentLine(uiName,elementName):
    """'+Language.G_Language[9072]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    element = GetElement(uiName,elementName)
    if element:
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:   
            if elementName.find(\'Text_\') >= 0:
                if hasattr(element,"GetEntry") == True:
                    element = element.GetEntry()
                return element.index(tkinter.INSERT)
    return  None
def DeleteContent(uiName,elementName,fromPosition='',toPosition=None):
    """'+Language.G_Language[9073]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    element = GetElement(uiName,elementName)
    if element:
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:   
            if elementName.find(\'Text_\') >= 0:
                if hasattr(element,"GetEntry") == True:
                    element = element.GetEntry()
                if toPosition:
                    element.delete(fromPosition,toPosition)
                else:
                    element.delete(fromPosition)
''' 
    f.write(code)
#写入更新到文字
def WriteSetFontFunction(f):
    code='''
def CreateFont(fontName,fontSize,fontWeight=\'normal\',fontSlant=\'roman\',fontUnderline=0,fontOverstrike=0):
    """'+Language.G_Language[1493]+'"""
    return tkinter.font.Font(family=fontName, size=fontSize,weight=fontWeight,slant=fontSlant,underline=fontUnderline,overstrike=fontOverstrike)
    #f.write(Language.G_Language[1211]+'
def SetFont(uiName,elementName,fontName,fontSize,fontWeight=\'normal\',fontSlant=\'roman\',fontUnderline=0,fontOverstrike=0):
    """'+Language.G_Language[1341]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_CanvasFontDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:   
            newFont = None
            if elementName in G_CanvasFontDictionary[uiName]:   
                for fontInfo in G_CanvasFontDictionary[uiName][elementName]:
                    if fontInfo[1] == fontName and fontInfo[2] == str(fontSize) and fontInfo[3] == fontWeight and fontInfo[4] == fontSlant and fontInfo[5] == str(fontUnderline) and fontInfo[6] == str(fontOverstrike):
                        newFont = fontInfo[0]                
                        break
            else:
                G_CanvasFontDictionary[uiName][elementName] = []
            if newFont is None:
                newFont = tkinter.font.Font(family=fontName, size=fontSize,weight=fontWeight,slant=fontSlant,underline=fontUnderline,overstrike=fontOverstrike)
            if elementName.find('Entry_') >= 0 or elementName.find('LabelButton_') >= 0:
                G_UIElementDictionary[uiName][elementName].SetFont(font=newFont)
            elif elementName.find('Canvas_') < 0 and elementName.find('Form_') < 0:
                G_UIElementDictionary[uiName][elementName].configure(font=newFont)
            G_CanvasFontDictionary[uiName][elementName].append([newFont,fontName,str(fontSize),fontWeight,fontSlant,str(fontUnderline),str(fontOverstrike)])                
def GetFont(uiName,elementName,fontName,fontSize,fontWeight=\'normal\',fontSlant=\'roman\',fontUnderline=0,fontOverstrike=0,createifnofind=False):
    """'+Language.G_Language[1571]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_CanvasFontDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:   
            if elementName in G_CanvasFontDictionary[uiName]:   
                for fontInfo in G_CanvasFontDictionary[uiName][elementName]:
                    if fontInfo[1] == fontName and fontInfo[2] == str(fontSize) and fontInfo[3] == fontWeight and fontInfo[4] == fontSlant and fontInfo[5] == str(fontUnderline) and fontInfo[6] == str(fontOverstrike):
                        return fontInfo[0]
            else:
                G_CanvasFontDictionary[uiName][elementName] = []
            if createifnofind == True:
                newFont = tkinter.font.Font(family=fontName, size=fontSize,weight=fontWeight,slant=fontSlant,underline=fontUnderline,overstrike=fontOverstrike)
                G_CanvasFontDictionary[uiName][elementName].append([newFont,fontName,str(fontSize),fontWeight,fontSlant,str(fontUnderline),str(fontOverstrike)])                
                return newFont
    return None
''' 
    f.write(code)
#写入更新到文字
def WriteSetFontFunction_App(f):
    code='''
    #f.write(Language.G_Language[1211]+'
def SetFont(uiName,elementName,fontName,fontSize,fontWeight=\'normal\',fontSlant=\'roman\',fontUnderline=0,fontOverstrike=0):
    """'+Language.G_Language[1341]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:   
            bold = False
            if fontWeight == 'bold':
                bold = True
            italic = False
            if fontSlant == 'italic':
                italic = True
            underline = False
            if fontUnderline == 1:
                underline = True
            G_UIElementDictionary[uiName][elementName].SetFont(fontName,fontSize,bold,italic,underline)
''' 
    f.write(code)
#写入更新到文字
def WriteSetTextFunction_HTML(f):
    code='''
    #f.write(Language.G_Language[1211]+'
def SetText(uiName,elementName,textValue,aliasName=True):
    """'+Language.G_Language[1211]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    showtext = str(\"%s\"%textValue)
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if uiName in G_UIElementVariableArray: 
        G_UIElementVariableArray[uiName][elementName] = showtext
    
''' 
    f.write(code)
#写入更新到文字
def WriteSetTextFunction_APP(f):
    code='''
    #f.write(Language.G_Language[1211]+'
def SetText(uiName,elementName,textValue,aliasName=True):
    """'+Language.G_Language[1211]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    showtext = str(\"%s\"%textValue)
    if aliasName and uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if uiName in G_UIElementDictionary: 
        if elementName in G_UIElementDictionary[uiName]:
            G_UIElementDictionary[uiName][elementName].SetText(showtext)
def InsertText(uiName,elementName,position,textValue='',tag=''):
    """'+Language.G_Language[1328]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    showtext = str(\"%s\"%textValue)
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if uiName in G_UIElementDictionary: 
        if elementName in G_UIElementDictionary[uiName]:
            G_UIElementDictionary[uiName][elementName].insert(position,textValue,tag)
''' 
    f.write(code)
#写入更新到文字
def WriteGetTextFunction(f):
    code='''
    #f.write(Language.G_Language[1212]+'
def GetText(uiName,elementName):
    """'+Language.G_Language[1212]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:   
            if elementName.find(\'Text_\') >= 0:
                Control = G_UIElementDictionary[uiName][elementName]
                if hasattr(Control,"GetEntry") == True:
                    Control = Control.GetEntry()
                return Control.get(\'0.0\', tkinter.END)
            elif elementName.find(\'Spinbox_\') >= 0:
                return str(G_UIElementDictionary[uiName][elementName].get())
            elif elementName.find(\'ComboBox_\') >= 0:
                return str(G_UIElementDictionary[uiName][elementName].get())
            elif elementName.find(\'ListBox_\') >= 0:
                currIndex = G_UIElementDictionary[uiName][elementName].curselection()
                if len(currIndex) > 0 and currIndex[0] >= 0:
                    return  G_UIElementDictionary[uiName][elementName].get(currIndex[0])
            elif elementName.find(\'Entry_\') >= 0:
                if elementName in  G_UIElementVariableArray[uiName]:  
                    text = G_UIElementVariableArray[uiName][elementName].get()  
                else:  
                    text = G_UIElementDictionary[uiName][elementName].GetText() 
                return text
            elif elementName.find(\'LabelButton_\') >= 0:
                text = G_UIElementDictionary[uiName][elementName].GetText() 
                return text
            else:
                if uiName in G_UIElementVariableArray: 
                    if elementName in G_UIElementVariableArray[uiName]:
                        text = G_UIElementVariableArray[uiName][elementName].get()
                        return text
                return G_UIElementDictionary[uiName][elementName].cget(\'text\')
    return str("")


''' 
    f.write(code)
#写入设置背景颜色
def WriteSetBGColorFunction(f):
    code='''
    #f.write(Language.G_Language[1211]+'
def SetBGColor(uiName,elementName,RGBColor):
    """'+Language.G_Language[1334]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:   
            Control = G_UIElementDictionary[uiName][elementName]
            if hasattr(Control,"SetBGColor") == True:
                Control.SetBGColor(RGBColor)
            else:
                Control.configure(bg=RGBColor)
def SetRadioButtonSelectedColor(uiName,elementName,GroupID,BGColor,FGColor):
    """'+Language.G_Language[9971]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    global G_UIRadioButtonGroupArray
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:   
            Control = G_UIElementDictionary[uiName][elementName]
            if GroupID not in G_UIRadioButtonGroupArray[uiName]:
                G_UIRadioButtonGroupArray[uiName][GroupID] = {}
            if elementName not in G_UIRadioButtonGroupArray[uiName][GroupID]:  
                G_UIRadioButtonGroupArray[uiName][GroupID][elementName]=[Control.cget('bg'),Control.cget('fg')]
            def OnRadioButtonSelected(event,uiName,elementName,BGColor,FGColor):
                for RadioButtonName in G_UIRadioButtonGroupArray[uiName][GroupID]:
                    OriBGColor = G_UIRadioButtonGroupArray[uiName][GroupID][RadioButtonName][0]
                    OriFGColor = G_UIRadioButtonGroupArray[uiName][GroupID][RadioButtonName][1]
                    if RadioButtonName != elementName:
                        SetBGColor(uiName,RadioButtonName,OriBGColor)
                        SetTextColor(uiName,RadioButtonName,OriFGColor)
                    else:
                        SetBGColor(uiName,RadioButtonName,BGColor)
                        SetTextColor(uiName,RadioButtonName,FGColor)
            Control.bind('<ButtonPress-1>',EventFunction_Adaptor(OnRadioButtonSelected,uiName = uiName,elementName = elementName,BGColor = BGColor,FGColor = FGColor))
def SetCheckButtonSelectedColor(uiName,elementName,BGColor,FGColor):
    """'+Language.G_Language[9972]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    global G_UIRadioButtonGroupArray
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:   
            Control = G_UIElementDictionary[uiName][elementName]
            if elementName not in G_UIRadioButtonGroupArray[uiName]:
                G_UIRadioButtonGroupArray[uiName][elementName] = {}
            G_UIRadioButtonGroupArray[uiName][elementName]=[Control.cget('bg'),Control.cget('fg')]
            def OnCheckButtonSelected(event,uiName,elementName,BGColor,FGColor):
                if elementName in G_UIRadioButtonGroupArray[uiName].keys():
                    CheckValue = GetTKVariable(uiName,elementName)
                    if CheckValue == False:
                        SetBGColor(uiName,elementName,BGColor)
                        SetTextColor(uiName,elementName,FGColor)
                    else:
                        OriBGColor = G_UIRadioButtonGroupArray[uiName][elementName][0]
                        OriFGColor = G_UIRadioButtonGroupArray[uiName][elementName][1]
                        SetBGColor(uiName,elementName,OriBGColor)
                        SetTextColor(uiName,elementName,OriFGColor)
            Control.bind('<ButtonPress-1>',EventFunction_Adaptor(OnCheckButtonSelected,uiName = uiName,elementName = elementName,BGColor = BGColor,FGColor = FGColor))
def SetComboBoxListColor(uiName,elementName,BGColor,FGColor):
    """'+Language.G_Language[9970]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    global G_UIRadioButtonGroupArray
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:   
            Control = G_UIElementDictionary[uiName][elementName]
            Control.tk.eval('[ttk::combobox::PopdownWindow %s].f.l configure -foreground %s -background %s' % (Control,FGColor,BGColor))
    
''' 
    f.write(code)
#写入取得背景颜色
def WriteGetBGColorFunction(f):
    code='''
    #f.write(Language.G_Language[1211]+'
def GetBGColor(uiName,elementName):
    """'+Language.G_Language[1335]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:   
            Control = G_UIElementDictionary[uiName][elementName]
            if hasattr(elementName,"GetBGColor") == True:
                return Control.GetBGColor()
            else:
                return Control.cget(\'bg\')
    return None

''' 
    f.write(code)
#写入设置文字颜色
def WriteSetTextColorFunction(f):
    code='''
    #f.write(Language.G_Language[1211]+'
def SetTextColor(uiName,elementName,RGBColor):
    """'+Language.G_Language[1336]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:   
            Control = G_UIElementDictionary[uiName][elementName]
            if hasattr(Control,"SetFGColor") == True:
                Control.SetFGColor(RGBColor)
            else:
                Control.configure(fg=RGBColor)


''' 
    f.write(code)
#写入取得文字颜色
def WriteGetTextColorFunction(f):
    code='''
    #f.write(Language.G_Language[1211]+'
def GetTextColor(uiName,elementName):
    """'+Language.G_Language[1337]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:   
            Control = G_UIElementDictionary[uiName][elementName]
            if hasattr(elementName,"GetFGColor") == True:
                return Control.GetFGColor()
            else:
                return Control.cget(\'fg\')
    return None

''' 
    f.write(code)
#写入更新到文字
def WriteGetTextFunction_HTML(f):
    code='''
    #f.write(Language.G_Language[1212]+'
def GetText(uiName,elementName):
    """'+Language.G_Language[1212]+'"""
    global G_UIElementVariableArray
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if uiName in G_UIElementVariableArray: 
        if elementName in G_UIElementVariableArray[uiName]:
            return G_UIElementVariableArray[uiName][elementName]
    return str("")

''' 
    f.write(code)
#写入更新到文字
def WriteMessageBoxFunction_HTML(f):
    code='''  
    #f.write(Language.G_Language[1221]+'
def MessageBox(text="",title="info",type="info",parent=None):
    """'+Language.G_Language[1221]+'"""
    global G_UrlParamMessageBox
    parent_func,func_params = GetParentCallFunc()
    if parent_func:
       if parent_func.find('_cmd') >= 0:
           uiName = parent_func.split('_cmd')[0]
           print(uiName)
           G_UrlParamMessageBox = [title,text,type]
    # f.write("           import flask
    # f.write('           G_FlaskReturnContent = flask.render_template(uiName+".html",url_param_messagebox=[title,text,type])
''' 
    f.write(code)
#写入更新到文字
def WriteGetTextFunction_APP(f):
    code='''
    #f.write(Language.G_Language[1212]+'
def GetText(uiName,elementName):
    """'+Language.G_Language[1212]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    if uiName in G_UIElementDictionary: 
         if elementName in G_UIElementDictionary[uiName]:
            return G_UIElementDictionary[uiName][elementName].GetText()
    return str("")

''' 
    f.write(code)
#设置列表项颜色
def WriteSetItemColorFunction(f):
    code='''
def SetItemBGColor(uiName,elementName,lineIndex,color):
    """'+Language.G_Language[6486]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ComboBox_') >= 0 or elementName.find('ListBox_') >= 0:
                    G_UIElementDictionary[uiName][elementName].itemconfig(lineIndex, {\'bg\':color})
def SetItemFGColor(uiName,elementName,lineIndex,color):
    """'+Language.G_Language[6492]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ComboBox_') >= 0 or elementName.find('ListBox_') >= 0:
                    G_UIElementDictionary[uiName][elementName].itemconfig(lineIndex, {\'fg\':color})
'''
    f.write(code)
#写入更新到文字
def WriteAddItemTextFunction(f,runMode):
    #f.write(Language.G_Language[1243]+'
    coede='''
def AddItemText(uiName,elementName,text,lineIndex="end",set_see=False):
    """'+Language.G_Language[1243]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ComboBox_') >= 0:
    if runMode == 'android':
                    G_UIElementDictionary[uiName][elementName].AddTextLine(text,lineIndex)
    else:
                    ValueArray = list(G_UIElementDictionary[uiName][elementName]['value'])
                    if type(lineIndex)==type(1):
                        ValueArray.insert(lineIndex,text)
                    else:
                       ValueArray.append(text)
                    G_UIElementDictionary[uiName][elementName]['value'] = ValueArray
            elif elementName.find('ListBox_') >= 0:
                Control = G_UIElementDictionary[uiName][elementName]
                if type(lineIndex)==type(1):
                    Control.insert(lineIndex,text)
                else:
                    Control.insert(lineIndex, text)
                if set_see == True:
                    Control.see(lineIndex)
def GetItemText(uiName,elementName,lineIndex=0):
    """'+Language.G_Language[8024]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            Control = G_UIElementDictionary[uiName][elementName]
            if elementName.find('ComboBox_') >= 0:
    if runMode == 'android':
                    return  Control.GetValueByIndex(lineIndex)
    else:
                    ValueArray = list(Control['value'])
                    if lineIndex < len(ValueArray):
                        return ValueArray[lineIndex]
            elif elementName.find('ListBox_') >= 0:
    if runMode == 'android':
                    return  Control.GetValueByIndex(lineIndex)
    else:
                    return Control.get(lineIndex)
    #f.write(Language.G_Language[1247]+'
def AddLineText(uiName,elementName,text,lineIndex="end",textTag=\'\',set_see=False):
    """'+Language.G_Language[1247]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('Text_') >= 0:
                Control = G_UIElementDictionary[uiName][elementName]
                if hasattr(Control,"GetEntry") == True:
                    Control = Control.GetEntry()
                if type(lineIndex)==type(1):
                    lineIndex = lineIndex + 1
                    if textTag != '':
                        Control.insert("%d.0"%lineIndex,text,textTag)
                    else:
                        Control.insert("%d.0"%lineIndex,text)
                else:
                    if textTag != '':
                        Control.insert(lineIndex,text,textTag)
                    else:
                        Control.insert(lineIndex,text)
                if set_see == True:
                    Control.see(lineIndex)
            if elementName.find('ListBox_') >= 0:
                Control = G_UIElementDictionary[uiName][elementName]
                if type(lineIndex)==type(1):
                    if textTag != '' :
                        Control.insert("%d"%lineIndex, text,textTag)
                    else:
                        Control.insert("%d"%lineIndex, text)
                else:
                    if textTag != '':
                        Control.insert(lineIndex,text,textTag)
                    else:
                        Control.insert(lineIndex,text)
                if set_see == True:
                    Control.see(lineIndex)
def GetLineText(uiName,elementName,lineIndex=0):
    """'+Language.G_Language[8025]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            Control = G_UIElementDictionary[uiName][elementName]
            if elementName.find('Text_') >= 0:
    if runMode == 'android':
                    return  Control.GetValueByIndex(lineIndex)
    else:
                    linestart = str("%s.0" % (lineIndex))
                    lineend = str("%s.end" % (lineIndex))
                    return Control.get(linestart, lineend).strip().replace('\\n','')
            elif elementName.find('ListBox_') >= 0:
    if runMode == 'android':
                    return  Control.get(lineIndex)
    else:
                    return Control.get(lineIndex)
def AddPage(uiName,elementName,text,iconFile="",targetUIName=\'\'):
    """'+Language.G_Language[8008]+'"""
    global G_ResourcesFileList
    NoteBook = GetElement(uiName,elementName)
    PageFrame = tkinter.Frame(NoteBook)
    PageFrame.place(relx = 0.0,rely = 0.0,relwidth = 1.0,relheight = 1.0)
    PageFrame.configure(bg='#888888')
    if targetUIName and len(targetUIName) > 0:
        try:
            uiClass = targetUIName
            if targetUIName.find(".py") > 0:
                UIPath, UIFile = os.path.split(targetUIName)
                if UIPath.find(":") < 0:
                    UIPath = os.path.join(G_ExeDir,UIPath)
                import sys
                sys.path.append(UIPath)
                uiClass, extension = os.path.splitext(UIFile)
            import importlib
            from   importlib import import_module
            importModule = importlib.import_module(uiClass)
            importModule = importlib.reload(importModule)
            if hasattr(importModule,"Fun") == True:
                importModule.Fun.G_ExeDir = G_ExeDir
                importModule.Fun.G_ResDir = G_ResDir
                if hasattr(importModule,"EXUIControl") == True:
                    importModule.EXUIControl.G_ExeDir = G_ExeDir
                    importModule.EXUIControl.G_ResDir = G_ResDir
            if uiClass.find('Modules.') == 0:
                LibNameArray =  uiClass.partition("Modules.")
                uiClass = LibNameArray[2]
                newClass = getattr(importModule, uiClass)
            else:
                newClass = getattr(importModule, uiClass)
            newClassInstance = newClass(PageFrame,False)
        except Exception as ex:
            MessageBox(str(ex))
    if len(iconFile) > 0 and os.path.exists(iconFile) == True:
        if elementName not in G_UIElementIconDictionary[uiName]:
            G_UIElementIconDictionary[uiName][elementName]= {}
        G_UIElementIconDictionary[uiName][elementName][text] = ImageTk.PhotoImage(file=iconFile) 
        NoteBook.add(PageFrame,text = text,image=G_UIElementIconDictionary[uiName][elementName][text],compound="left")
    else:
        NoteBook.add(PageFrame,text = text)
def GetPage(uiName,elementName,index=0):
    """'+Language.G_Language[8026]+'"""
    NoteBook = GetElement(uiName,elementName)
    if NoteBook:
        Pages = NoteBook.winfo_children()
        if index >= 0 and index < len(Pages):
            return Pages[index]
    return None
def SelectPage(uiName,elementName,index=0):
    """'+Language.G_Language[8010]+'"""
    NoteBook = GetElement(uiName,elementName)
    if NoteBook:
        Pages = NoteBook.winfo_children()
        if index >= 0 and index < len(Pages):
            NoteBook.select(index)

def GetSelectedPageIndex(uiName,elementName):
    """'+Language.G_Language[8014]+'"""
    NoteBook = GetElement(uiName,elementName)
    if NoteBook:
        return NoteBook.index("current")
    return -1

def GetPageText(uiName,elementName,index=0):
    """'+Language.G_Language[8015]+'"""
    NoteBook = GetElement(uiName,elementName)
    if NoteBook:
        return NoteBook.tab(index,"text")
    return -1

def GetPageIndex(uiName,elementName,title):
    """'+Language.G_Language[8016]+'"""
    NoteBook = GetElement(uiName,elementName)
    if NoteBook:
        Tabs = NoteBook.tabs()
        for i in range(0,len(Tabs)):
            tabTitle = NoteBook.tab(i,"text")
            if tabTitle == title:
                return i
    return -1

def HidePage(uiName,elementName,index=0):
    """'+Language.G_Language[8011]+'"""
    NoteBook = GetElement(uiName,elementName)
    if NoteBook:
        Pages = NoteBook.winfo_children()
        if index >= 0 and index < len(Pages):
            NoteBook.hide(index)
def DelPage(uiName,elementName,index=0):
    """'+Language.G_Language[8009]+'"""
    NoteBook = GetElement(uiName,elementName)
    if NoteBook:
        Pages = NoteBook.winfo_children()
        if index >= 0 and index < len(Pages):
            NoteBook.forget(Pages[index])
            DestoryChild(Pages[index])

def AddPanedWindowPage(uiName,elementName='',WidthOrHeight=10):
    """'+Language.G_Language[8012]+'"""
    realElementName = elementName
    if uiName in G_UIElementAliasDictionary:
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            realElementName = G_UIElementAliasDictionary[uiName][elementName]
        PanedWindow = GetElement(uiName,elementName)
        if PanedWindow:
            PanedWindow_child = tkinter.Canvas(PanedWindow,bg="#888888")
            if PanedWindow.cget('orient') == tkinter.HORIZONTAL:
                PanedWindow.add(PanedWindow_child,width = WidthOrHeight)
            else:
                PanedWindow.add(PanedWindow_child,height = WidthOrHeight)
            Pages = PanedWindow.panes()
            PageCount = len(Pages)
            realChildName = str('%s_child%s'%(realElementName,PageCount+1))
            aliasChildName = str('%s_child%s'%(elementName,PageCount+1))
            Register(uiName,realChildName,PanedWindow_child,aliasChildName)
            return PanedWindow_child
    return None

def DelPanedWindowPage(uiName,elementName='',index=0):
    """'+Language.G_Language[8013]+'"""
    PanedWindow = GetElement(uiName,elementName)
    if PanedWindow:
        Pages = PanedWindow.panes()
        if index >= 0 and index < len(Pages):
            PanedWindow.forget(Pages[index])

    # f.write('def AddImage(uiName,elementName,text,lineIndex="end",textTag=\'\'):
    # f.write('    """'+Language.G_Language[1247]+'"""
    # f.write('    global G_UIElementAliasDictionary
    # f.write('    global G_UIElementDictionary
    # f.write('    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
    # f.write('        elementName = G_UIElementAliasDictionary[uiName][elementName]
    # f.write('    if uiName in G_UIElementDictionary:
    # f.write('        if elementName in G_UIElementDictionary[uiName]:
    # f.write("            if elementName.find('Text_') >= 0 or elementName.find('ListBox_') >= 0:
    # f.write('                if type(lineIndex)==type(1):
    # f.write("                    if textTag != '' and elementName.find('Text_') >= 0 :
    # f.write('                        G_UIElementDictionary[uiName][elementName].insert("%d.0"%(lineIndex+1), text,textTag)
    # f.write('                    else:
    # f.write('                        G_UIElementDictionary[uiName][elementName].insert("%d.0"%(lineIndex+1), text)
    # f.write('                else:
    # f.write("                    if textTag != '' and elementName.find('Text_') >= 0 :
    # f.write('                        G_UIElementDictionary[uiName][elementName].insert(lineIndex,text,textTag)
    # f.write('                    else:
    # f.write('                        G_UIElementDictionary[uiName][elementName].insert(lineIndex,text)
    #f.write(Language.G_Language[1280]+'
def AddTreeItem(uiName,elementName,parentItem="",insertItemPosition="end",itemName="",itemText="",itemValues=(),iconName="",tag=""):
    """'+Language.G_Language[1280]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementIconDictionary
    global G_ResourcesFileList
    Item = None
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:
                if iconName != "":
                    if iconName in G_UIElementIconDictionary[uiName][elementName]:
                        ItemIcon = G_UIElementIconDictionary[uiName][elementName][iconName]
                        Item = G_UIElementDictionary[uiName][elementName].insert(parentItem,insertItemPosition,itemName,text=itemText,values=itemValues,image=ItemIcon,tag=tag)
                    else:
                        ItemIcon = None
                        if os.path.exists(iconName) == True:
                            ItemIcon = ImageTk.PhotoImage(file = iconName)
                        else:
                            imagePath = iconName
                            iconName_Lower = iconName.lower()
                            if iconName_Lower in G_ResourcesFileList:
                               imagePath = G_ResourcesFileList[iconName_Lower]
                            if os.path.exists(imagePath) == True:
                                ItemIcon = ImageTk.PhotoImage(file = imagePath)
                        if ItemIcon:
                            Item = G_UIElementDictionary[uiName][elementName].insert(parentItem,insertItemPosition,itemName,text=itemText,values=itemValues,image=ItemIcon,tag=tag)
                            G_UIElementIconDictionary[uiName][elementName][Item] = ItemIcon
                        else:
                            Item = G_UIElementDictionary[uiName][elementName].insert(parentItem,insertItemPosition,itemName,text=itemText,values=itemValues,tag=tag)
                else:
                    Item = G_UIElementDictionary[uiName][elementName].insert(parentItem,insertItemPosition,itemName,text=itemText,values=itemValues,tag=tag)
    return Item
    #f.write(Language.G_Language[1281]+'
def SetTreeItemText(uiName,elementName,itemName,text):
    """'+Language.G_Language[1281]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:
                G_UIElementDictionary[uiName][elementName].item(itemName,text=text)
def GetTreeItemText(uiName,elementName,itemName):
    """'+Language.G_Language[1474]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:
                item_text = G_UIElementDictionary[uiName][elementName].item(itemName,"text")
                return item_text
    return None
def SetTreeItemValues(uiName,elementName,itemName,itemValues):
    """'+Language.G_Language[1282]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:
                G_UIElementDictionary[uiName][elementName].item(itemName,values=itemValues)
def GetTreeItemValues(uiName,elementName,itemName):
    """'+Language.G_Language[1475]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:
                item_value = G_UIElementDictionary[uiName][elementName].item(itemName,"values")
                return item_value
    return None
    #f.write(Language.G_Language[1283]+'
def SetTreeItemIcon(uiName,elementName,itemName,iconName=""):
    """'+Language.G_Language[1283]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_ResourcesFileList
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:
                if iconName != "":
                    if iconName in G_UIElementIconDictionary[uiName][elementName]:
                        ItemIcon = G_UIElementIconDictionary[uiName][elementName][iconName]
                        G_UIElementDictionary[uiName][elementName].item(itemName,image=ItemIcon)
                        G_UIElementIconDictionary[uiName][elementName][itemName]=ItemIcon
                    else:
                        ItemIcon = None
                        if os.path.exists(iconName) == True:
                            ItemIcon = ImageTk.PhotoImage(file = iconName)
                        else:
                            imagePath = iconName
                            iconName_Lower = iconName.lower()
                            if iconName_Lower in G_ResourcesFileList:
                               imagePath = G_ResourcesFileList[iconName_Lower]
                            if os.path.exists(imagePath) == True:
                                ItemIcon = ImageTk.PhotoImage(file = imagePath)
                        if ItemIcon:
                            G_UIElementDictionary[uiName][elementName].item(itemName,image=ItemIcon)
                            G_UIElementIconDictionary[uiName][elementName][itemName]=ItemIcon
    #f.write(Language.G_Language[1284]+'
def ExpandTreeItem(uiName,elementName,itemName,expand=True):
    """'+Language.G_Language[1284]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:
                G_UIElementDictionary[uiName][elementName].item(itemName,open=expand)
    
def SetColumnList(uiName,elementName,columnList):
    """'+Language.G_Language[3164]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0 :
                G_UIElementDictionary[uiName][elementName].configure(columns = columnList)
                for columnName in columnList:
                    G_UIElementDictionary[uiName][elementName].column(columnName,anchor='center',width=100,stretch=True)
                    G_UIElementDictionary[uiName][elementName].heading(columnName,anchor='center',text=columnName)

def SetColumnInfo(uiName,elementName,columnName='',anchor='center',width=100,stretch=True):
    """'+Language.G_Language[3165]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0 :
                columnList = G_UIElementDictionary[uiName][elementName].cget(\'columns\')
                for columnName in columnList:
                    G_UIElementDictionary[uiName][elementName].column(columnName,anchor=anchor,width=width,stretch=stretch)
                    G_UIElementDictionary[uiName][elementName].heading(columnName,anchor=anchor,text=columnName)

def AddRowText(uiName,elementName,rowIndex =\'end\',values=(''),tag=\'\'):
    """'+Language.G_Language[1962]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_ListViewTagDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                if rowIndex == '':
                    rowIndex = 'end'
                values_list = []
                if isinstance(values,str) == True:
                    values_list = values.split(',')
                else:
                    values_list = list(values)
                for i in range(len(values_list)):
                    if isinstance(values_list[i],bool) == True:
                        if values_list[i] == True:
                            values_list[i] = '☑'
                        elif values_list[i] == False:
                            values_list[i] = '☐'
                ListView = G_UIElementDictionary[uiName][elementName]
                currentRowIndex = len(ListView.get_children())
                if isinstance(rowIndex,int):
                    currentRowIndex = rowIndex
                if tag == '':
                    tag = 'even'
                    if currentRowIndex%2 == 0:
                        tag = 'even'
                    else:
                        tag = 'odd'
                G_UIElementDictionary[uiName][elementName].insert(\'\',rowIndex, values=values_list,tag=tag)
                G_ListViewTagDictionary[uiName][elementName].append(tag)
                return currentRowIndex
    return -1

def AddMultiRowText(uiName,elementName,rowIndex =\'end\',rowValuesList=[],tagList=[]):
    """'+Language.G_Language[2036]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_ListViewTagDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                if rowIndex == '':
                    rowIndex = 'end'
                values_list = []
                ListView = G_UIElementDictionary[uiName][elementName]
                currentRowIndex = len(ListView.get_children())
                if isinstance(rowIndex,int):
                    currentRowIndex = rowIndex
                rowCount = len(rowValuesList)
                tagCount = len(tagList)
                for rowOffset in range(rowCount):
                    rowValues = rowValuesList[rowOffset]
                    if isinstance(rowValues,str) == True:
                        values_list = rowValues.split(',')
                    else:
                        values_list = list(rowValues)
                    for i in range(len(values_list)):
                        if isinstance(values_list[i],bool) == True:
                            if values_list[i] == True:
                                values_list[i] = '☑'
                            elif values_list[i] == False:
                                values_list[i] = '☐'
                    if rowOffset < tagCount:
                        tag = tagList[rowOffset]
                    else:
                        tag = 'even'
                        if (currentRowIndex + rowOffset)%2 == 0:
                            tag = 'even'
                        else:
                            tag = 'odd'
                    ListView.insert(\'\',rowIndex, values=values_list,tag=tag)
                    G_ListViewTagDictionary[uiName][elementName].append(tag)
                return currentRowIndex
    return -1

def GetRowTextList(uiName,elementName,rowIndex):
    """'+Language.G_Language[1973]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                ListView = G_UIElementDictionary[uiName][elementName]
                rowHandle = ListView.get_children()[rowIndex]
                rowValues = list(ListView.item(rowHandle,"values"))
                for i in range(len(rowValues)):
                    if rowValues[i] == '☑':
                        rowValues[i] = True
                    elif rowValues[i] == '☐':
                        rowValues[i] = False
                return rowValues
    return None

def GetColumnTextList(uiName,elementName,columnIndex):
    """'+Language.G_Language[2037]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                ListView = G_UIElementDictionary[uiName][elementName]
                RowList = ListView.get_children() 
                ColumnTextlist = [] 
                for rowHandle in RowList:
                    rowValues = ListView.item(rowHandle,"values")
                    columnText = rowValues[columnIndex]
                    if columnText == '☑':
                        ColumnTextlist.append(True)
                    elif columnText == '☐':
                        ColumnTextlist.append(False)
                    else:
                        ColumnTextlist.append(columnText)
                return ColumnTextlist
    return None

def GetAllRowTextList(uiName,elementName):
    """'+Language.G_Language[2038]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                ListView = G_UIElementDictionary[uiName][elementName]
                allrowValues = []
                for rowHandle in ListView.get_children():
                    rowValues = list(ListView.item(rowHandle,"values"))
                    allrowValues.append(rowValues)
                return allrowValues
    return None
    

def GetCellText(uiName,elementName,rowIndex,columnIndex):
    """'+Language.G_Language[1974]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                ListView = G_UIElementDictionary[uiName][elementName]
                rowHandle = ListView.get_children()[rowIndex]
    if runMode == 'android':
                    rowValues = ListView.item(rowHandle)["values"]
    else:
                    rowValues = ListView.item(rowHandle,"values")
                if rowValues[columnIndex] == '☑':
                    return True
                elif rowValues[columnIndex] == '☐':
                    return False
                return rowValues[columnIndex]
    return None
def SetCellText(uiName,elementName,rowIndex,columnIndex,text):
    """'+Language.G_Language[1963]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                rowHandle = G_UIElementDictionary[uiName][elementName].get_children()[rowIndex]
                G_UIElementDictionary[uiName][elementName].set(rowHandle,column=columnIndex,value=text)
def SetCellCheckBox(uiName,elementName,rowIndex,columnIndex,value=True):
    """'+Language.G_Language[2030]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                rowHandle = G_UIElementDictionary[uiName][elementName].get_children()[rowIndex]
                if value == True:
                    G_UIElementDictionary[uiName][elementName].set(rowHandle,column=columnIndex,value='☑')
                else:
                    G_UIElementDictionary[uiName][elementName].set(rowHandle,column=columnIndex,value='☐')
def SetColumnCheckBox(uiName,elementName,beginRowIndex=0,endRowIndex=-1,columnIndex=0,value=True):
    """'+Language.G_Language[2031]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                if endRowIndex == -1:
                    endRowIndex = len(G_UIElementDictionary[uiName][elementName].get_children())
                rowHandleList = G_UIElementDictionary[uiName][elementName].get_children()[beginRowIndex:endRowIndex]
                for rowHandle in rowHandleList:
                    if value == True:
                        G_UIElementDictionary[uiName][elementName].set(rowHandle,column=columnIndex,value='☑') 
                    else:
                        G_UIElementDictionary[uiName][elementName].set(rowHandle,column=columnIndex,value='☐')

def DeleteRow(uiName,elementName,rowIndex):
    """'+Language.G_Language[1964]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                rowHandle = G_UIElementDictionary[uiName][elementName].get_children()[rowIndex]
                G_UIElementDictionary[uiName][elementName].delete(rowHandle)
    
def DeleteAllRows(uiName,elementName):
    """'+Language.G_Language[1965]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                ListView = G_UIElementDictionary[uiName][elementName]
    if runMode == 'android':
                    ListView.clear()
    else:
                    RootChildren = ListView.get_children()
                    ListView.delete(*RootChildren)
        # f.write('                for Item in RootChildren:
        # f.write('                    ListView.delete(Item)

def CheckPickedRow(uiName,elementName,x,y):
    """'+Language.G_Language[1966]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                ListView = G_UIElementDictionary[uiName][elementName]
                PickedItem = ListView.identify("item",x,y)
                if PickedItem:
                   RootChildren = ListView.get_children()
                   return RootChildren.index(PickedItem)
    return None
def CheckPickedCell(uiName,elementName,x,y):
    """'+Language.G_Language[1982]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                ListView = G_UIElementDictionary[uiName][elementName]
                PickedItem = ListView.identify("item",x,y)
                if PickedItem:
    # f.write('                   row = ListView.identify_row(y)
    # f.write('                   row = row.replace("I","")
    # f.write('                   row = int(row) - 1
                    row = ListView.index(PickedItem)
                    column = ListView.identify_column(x)
                    column = column.replace("#","")
                    column = int(column) - 1
                    return (row,column)
    return (-1,-1)
def OnListViewCellClicked(event,uiName,widgetName,callbackFunc):
    # f.write('    rowIndex,columnIndex = CheckPickedCell(uiName,widgetName,event.x,event.y)
    # f.write('    if callbackFunc:
    # f.write('        callbackFunc(uiName,widgetName,rowIndex,columnIndex)
    """'+Language.G_Language[1727]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    elementName = widgetName
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                ListView = G_UIElementDictionary[uiName][elementName]
                PickedItem = ListView.identify("item",event.x,event.y)
                if PickedItem:
                    rowIndex = ListView.index(PickedItem)
                    rowHandle = ListView.get_children()[rowIndex]
                    rowValues = ListView.item(rowHandle,"values")
                    column = ListView.identify_column(event.x)
                    column = column.replace("#","")
                    columnIndex = int(column) - 1
                    if rowValues[columnIndex] == '☑':
                        ListView.set(rowHandle,column=columnIndex,value='☐')
                    elif rowValues[columnIndex] == '☐':
                        ListView.set(rowHandle,column=columnIndex,value='☑')
                    if callbackFunc:
                        callbackFunc(uiName,widgetName,rowIndex,columnIndex)
def SelectRow(uiName,elementName,beginrowIndex=0,endrowIndex=0):
    """'+Language.G_Language[2039]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                ListView = G_UIElementDictionary[uiName][elementName]
                RootChildren = ListView.get_children()
                RowCount = len(RootChildren)
                if beginrowIndex >= 0 or beginrowIndex < RowCount:
                    select = []
                    if endrowIndex < 0:
                        endrowIndex = RowCount + endrowIndex
                    elif endrowIndex == 0:
                        endrowIndex = beginrowIndex
                    for index in range(beginrowIndex,endrowIndex+1):
                        select.append(RootChildren[index])
                    ListView.selection_set(select)
def GetSelectedRowIndex(uiName,elementName):
    """'+Language.G_Language[9013]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                ListView = G_UIElementDictionary[uiName][elementName]
                selectionList = ListView.selection()
                if selectionList and len(selectionList) > 0:
                    if len(selectionList) == 1:
                        rowHandle = selectionList[0]
                        rowIndex = ListView.index(rowHandle)
                        return rowIndex
                    else:
                        rowIndexList = []
                        for rowHandle in selectionList:
                            rowIndex = ListView.index(rowHandle)
                            rowIndexList.append(rowIndex)
                        return rowIndexList
    return -1
def SortLineByColumn(uiName,elementName,columnIndex=0,reverse = False):
    """'+Language.G_Language[2032]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                ListView = G_UIElementDictionary[uiName][elementName]
                AllLineValues = []
                RootChildren = ListView.get_children()
                for Item in RootChildren:
                    itemInfo = ListView.item(Item)
                    AllLineValues.append(itemInfo["values"])
                    AllLineValues.sort(key=lambda x:str(x[columnIndex]),reverse=reverse)
                for Item in RootChildren:
                    ListView.delete(Item)
                for line in AllLineValues:
                    itemHandle = ListView.insert("",0,text=line[0],values=line)
def SetRowStyle(uiName,elementName,rowIndex='even',bgColor='lightblue',fgColor='#000000',textFont=None):
    """'+Language.G_Language[2035]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_ListViewTagDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                ListView = G_UIElementDictionary[uiName][elementName]
                if rowIndex == 'even':
                    if textFont:
                        ListView.tag_configure('even', background=bgColor,font=textFont,foreground=fgColor)
                    else:
                        ListView.tag_configure('even', background=bgColor,foreground=fgColor)
                    RootChildren = ListView.get_children()
                    row = 0
                    rowTag = 'even'
                    for Item in RootChildren:
                        if row/2 != int(row/2):
                            rowTag = 'even'
                        else:
                            rowTag = 'odd'
                        ListView.item(Item,tag=rowTag)
                        row = row + 1
                elif rowIndex == 'odd':
                    if textFont:
                        ListView.tag_configure('odd', background=bgColor,font=textFont,foreground=fgColor)
                    else:
                        ListView.tag_configure('odd', background=bgColor,foreground=fgColor)
                    RootChildren = ListView.get_children()
                    row = 0
                    rowTag = 'even'
                    for Item in RootChildren:
                        if row/2 != int(row/2):
                            rowTag = 'even'
                        else:
                            rowTag = 'odd'
                        ListView.item(Item,tag=rowTag)
                        row = row + 1
                elif rowIndex == 'all':
                    if textFont:
                        ListView.tag_configure('all', background=bgColor,font=textFont,foreground=fgColor)
                    else:
                        ListView.tag_configure('all', background=bgColor,foreground=fgColor)
                    RootChildren = ListView.get_children()
                    rowTag = 'all'
                    for Item in RootChildren:
                        ListView.item(Item,tag=rowTag)
                elif rowIndex == 'hover':
                    if textFont:
                        ListView.tag_configure('hover', background=bgColor,font=textFont,foreground=fgColor)
                    else:
                        ListView.tag_configure('hover', background=bgColor,foreground=fgColor)
                    AddUserData(uiName,elementName,'HoverItem','list',[None,None,bgColor],0)
                else:
                    if textFont:
                        ListView.tag_configure(str('row_%d'%rowIndex), background=bgColor,font=textFont,foreground=fgColor)
                    else:
                        ListView.tag_configure(str('row_%d'%rowIndex), background=bgColor,foreground=fgColor)
                    RootChildren = ListView.get_children()
                    Item = RootChildren[rowIndex]
                    ListView.item(Item,tag=str('row_%d'%rowIndex))
def SetRowBGColor(uiName,elementName,rowIndex='even',bgColor='lightblue'):
    """'+Language.G_Language[2033]+'"""
    SetRowStyle(uiName,elementName,rowIndex=rowIndex,bgColor=bgColor,fgColor='#000000',textFont=None)

def OnListViewRowMouseMotion(event,uiName,widgetName):
    """'+Language.G_Language[2034]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    elementName = widgetName
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                ListView = G_UIElementDictionary[uiName][elementName]
                PickedItem = ListView.identify("item",event.x,event.y)
                if PickedItem:
                    RootChildren = ListView.get_children()
                    RowIndex =  RootChildren.index(PickedItem)
                    if RowIndex >= 0:
                        HoverItem = GetUserData(uiName,elementName,"HoverItem")
                        if HoverItem:
                            LastItem = HoverItem[0]
                            LastItemTag = HoverItem[1]
                            LastItemBG = HoverItem[2]
                            if LastItem:
                                ListView.item(LastItem,tag=LastItemTag)
                            RootChildren = ListView.get_children()
                            NewItem = RootChildren[RowIndex]
                            NewItemTag = ListView.item(NewItem,'tag')
                            ListView.item(NewItem,tag=str('hover'))
                            if HoverItem:
                                SetUserData(uiName,elementName,'HoverItem',[NewItem,NewItemTag,LastItemBG])
                            else:
                                AddUserData(uiName,elementName,'HoverItem','list',[NewItem,NewItemTag,LastItemBG],0)

''' 
    f.write(code)
#写入WEB端的
def WriteAddItemTextFunction_HTML(f):
    code='''
def AddRowText(uiName,elementName,rowIndex =\'end\',values=(''),tag=\'\'):
    """'+Language.G_Language[1962]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    global G_ListViewTagDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary.keys():
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                if rowIndex == '':
                    rowIndex = 'end'
                values_list = []
                if isinstance(values,str) == True:
                    values_list = values.split(',')
                else:
                    values_list = list(values)
                for i in range(len(values_list)):
                    if isinstance(values_list[i],bool) == True:
                        if values_list[i] == True:
                            values_list[i] = '☑'
                        elif values_list[i] == False:
                            values_list[i] = '☐'
                if elementName not in G_UIElementVariableArray[uiName].keys():
                    G_UIElementVariableArray[uiName][elementName] = []
                currentRowIndex = len(G_UIElementVariableArray[uiName][elementName])
                if isinstance(rowIndex,int):
                    currentRowIndex = rowIndex
                if tag == '':
                    tag = 'even'
                    if currentRowIndex%2 == 0:
                        tag = 'even'
                    else:
                        tag = 'odd'
                if rowIndex == 'end':
                    G_UIElementVariableArray[uiName][elementName].append(values_list)
                else:
                    G_UIElementVariableArray[uiName][elementName].insert(currentRowIndex, values_list)
                G_ListViewTagDictionary[uiName][elementName].append(tag)
                return currentRowIndex
    return -1
def SetCellText(uiName,elementName,rowIndex,columnIndex,text=''):
    """'+Language.G_Language[1963]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                if elementName not in G_UIElementVariableArray[uiName].keys():
                    G_UIElementVariableArray[uiName][elementName] = []
                if rowIndex < len(G_UIElementVariableArray[uiName][elementName]):
                    valueList = G_UIElementVariableArray[uiName][elementName][rowIndex]
                    columnCount = len(valueList)
                    if columnIndex >= columnCount:
                        for i in range(columnCount,columnIndex+1):
                            G_UIElementVariableArray[uiName][elementName][rowIndex].append('')
                    G_UIElementVariableArray[uiName][elementName][rowIndex][columnIndex]=text
def DeleteRow(uiName,elementName,rowIndex):
    """'+Language.G_Language[1964]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                if elementName in G_UIElementVariableArray[uiName].keys():
                    G_UIElementVariableArray[uiName][elementName].pop(rowIndex)
def DeleteAllRows(uiName,elementName):
    """'+Language.G_Language[1965]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListView_') >= 0:
                if elementName in G_UIElementVariableArray[uiName].keys():
                    G_UIElementVariableArray[uiName][elementName].clear()
''' 
    f.write(code)
#写入移动树结点
def WriteCheckPickedTreeItemFunction(f):
    code='''
def CheckPickedTreeItem(uiName,elementName,x,y):
    """'+Language.G_Language[1310]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0:
                return G_UIElementDictionary[uiName][elementName].identify("item",x,y)
    return None
def CheckClickedTreeItem(uiName,elementName,x,y):
    """'+Language.G_Language[1310]+'"""
    return CheckPickedTreeItem(uiName,elementName,x,y)
def SelectTreeItem(uiName,elementName,item):
    """'+Language.G_Language[1327]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0:
                G_UIElementDictionary[uiName][elementName].selection_set(item)
def GetSelectedTreeItem(uiName,elementName):
    """'+Language.G_Language[1359]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0:
                return G_UIElementDictionary[uiName][elementName].selection()
    return None
def UnSelecteTreeItem(uiName,elementName):
    """'+Language.G_Language[1364]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0:
                selected_item = G_UIElementDictionary[uiName][elementName].selection()
                if selected_item:
                    G_UIElementDictionary[uiName][elementName].selection_remove(selected_item)
''' 
    f.write(code)
#写入移动树结点
def WriteMoveTreeItemFunction(f):
    code='''
def MoveTreeItem(uiName,elementName,itemName,parentItem="",insertItemPosition="end"):
    """'+Language.G_Language[1311]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:
                G_UIElementDictionary[uiName][elementName].move(itemName,parentItem,insertItemPosition)

''' 
    f.write(code)
#写入更新到文字
def WriteDelItemTextFunction(f):
    code='''
    #f.write(Language.G_Language[1244]+'
def DelItemText(uiName,elementName,lineIndexOrText):
    """'+Language.G_Language[1244]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ComboBox_') >= 0:
                ValueArray = list(G_UIElementDictionary[uiName][elementName]['value'])
                if type(lineIndexOrText)==type(1):
                    ValueArray.pop(lineIndexOrText)
                    G_UIElementDictionary[uiName][elementName]['value'] = ValueArray
                else:
                    ValueIndex = ValueArray.index(lineIndexOrText)
                    if ValueIndex >= 0:
                        ValueArray.pop(ValueIndex)
                    G_UIElementDictionary[uiName][elementName]['value'] = ValueArray
            elif elementName.find('ListBox_') >= 0:
                if type(lineIndexOrText)==type(1):
                    G_UIElementDictionary[uiName][elementName].delete(lineIndexOrText)
                else:
                    ValueArray = G_UIElementDictionary[uiName][elementName].get(0,tkinter.END)
                    ValueIndex = ValueArray.index(lineIndexOrText)
                    if ValueIndex >= 0:
                        G_UIElementDictionary[uiName][elementName].delete(ValueIndex)
    #f.write(Language.G_Language[1248]+'
def DelLineText(uiName,elementName,lineIndex="end"):
    """'+Language.G_Language[1248]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('Text_') >= 0:
                Control = G_UIElementDictionary[uiName][elementName]
                if hasattr(Control,"GetEntry") == True:
                    Control = Control.GetEntry()
                if type(lineIndex)==type(1):
                    lineIndex = lineIndex + 1
                    beginIndex = str("%d.0"%lineIndex)
                    endIndex = str("%d.0"%(lineIndex+1))
                    Control.delete(beginIndex,endIndex)
                else:
                    beginIndex = str("%s.0"%lineIndex)
                    endIndex = str("%s.end"%lineIndex)
                    Control.delete(beginIndex,endIndex)
            elif elementName.find('ListBox_') >= 0:
                if type(lineIndex)==type(1):
                    G_UIElementDictionary[uiName][elementName].delete("%d"%lineIndex)
                else:
                    G_UIElementDictionary[uiName][elementName].delete("%s"%lineIndex)
def DelTreeItem(uiName,elementName,item):
    """'+Language.G_Language[1285]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0:
                G_UIElementDictionary[uiName][elementName].delete(item)
def DelAllTreeItem(uiName,elementName):
    """'+Language.G_Language[1312]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('TreeView_') >= 0:
                TreeView = G_UIElementDictionary[uiName][elementName]
                RootChildren = TreeView.get_children()
                for Item in RootChildren:
                    TreeView.delete(Item)
def DelAllLines(uiName,elementName):
    """'+Language.G_Language[1338]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ListBox_') >= 0:
                G_UIElementDictionary[uiName][elementName].delete(0,tkinter.END)
            elif elementName.find('Text_') >= 0:
                Control = G_UIElementDictionary[uiName][elementName]
                if hasattr(Control,"GetEntry") == True:
                    Control = Control.GetEntry()
                Control.delete(\'0.0\',tkinter.END)
def DelAllItemText(uiName,elementName):
    """'+Language.G_Language[1814]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName]
    if uiName in G_UIElementDictionary:
        if elementName in G_UIElementDictionary[uiName]:
            if elementName.find('ComboBox_') >= 0:
                G_UIElementDictionary[uiName][elementName]['value'] = []
'''
    f.write(code)                
#写入更新到文字
def WriteSetImageFunction(f,exportMode = False,usePME = False):
    code='''
def LoadImageFromPMEFile(imagePath):
    if usePME == False:
        return None
    else:
        global PMEPassword
        pathName,fileName = os.path.split(imagePath)
        shotName,extension = os.path.splitext(fileName)
        imagePath = os.path.join(pathName,shotName+".pme")
        if os.path.exists(imagePath) == True:
            #从加密文件中读取图片
            result,image = PyMeEncryption.LoadFromEncryptionFile(imagePath,PMEPassword)
            if result == True:
                return image
            else:
                return None
        imagePath_Lower = imagePath.lower()
        if imagePath_Lower in G_ResourcesFileList:
            imagePath = G_ResourcesFileList[imagePath_Lower]
            if os.path.exists(imagePath) == False:
                return None
            #从加密文件中读取图片
            result,image = PyMeEncryption.LoadFromEncryptionFile(imagePath,PMEPassword)
            if result == True:
                return image
        return None
    #f.write(Language.G_Language[1213]+'
def SetImage(uiName,elementName,imagePath,autoSize = True,format=\'RGBA\'):
    """'+Language.G_Language[1213]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    global G_ResourcesFileList
    from   PIL import Image,ImageTk
    Control = GetElement(uiName,elementName) 
    if Control : 
        Control_Width = Control.winfo_width() 
        Control_Height = Control.winfo_height() 
        if isinstance(imagePath,str) == True:
            pathName,fileName = os.path.split(imagePath)
            shotName,extension = os.path.splitext(fileName)
            if extension.lower() == \'.gif\':
                if autoSize == True:
                    LoadGIF(uiName,elementName,imagePath,Control_Width,Control_Height)
                else:
                    LoadGIF(uiName,elementName,imagePath)
                return
        image = None
        if isinstance(imagePath,str) == True:
            imagePath_Lower = imagePath.lower()
            if os.path.exists(imagePath) == False:
                if imagePath_Lower in G_ResourcesFileList:
                    imagePath = G_ResourcesFileList[imagePath_Lower]
                if os.path.exists(imagePath) == False:
'''
    f.write(code)

    if exportMode == False:
        code='''
                        Control.configure(image = '')
                        return
                image = Image.open(imagePath).convert(format)
'''
        f.write(code)
    else:
        code='''
                        image = LoadImageFromPMEFile(imagePath)
                        if image is None:
                            Control.configure(image = '')
                            return
                if image is None:
                    image = Image.open(imagePath).convert(format)
        elif isinstance(imagePath,Image.Image) == True:
            image = imagePath.convert(format)
        if image is None:
            Control.configure(image = '')
            return
        realElementName = elementName 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            realElementName = G_UIElementAliasDictionary[uiName][elementName] 
        if realElementName.find(\'Label_\') >= 0 or realElementName.find(\'Button_\') >= 0 :
            if uiName in G_UIElementUserDataArray:
                if realElementName in G_UIElementUserDataArray[uiName]:
                    for EBData in G_UIElementUserDataArray[uiName][realElementName]:   
                        if EBData[0] == \'image\' and EBData[1] == \'imageInfo\':
                            EBData[2][1] = imagePath
                            if autoSize == True:
                                image_Resize = image.resize((Control_Width, Control_Height),Image.LANCZOS)
                            else:
                                image_Resize = image
                            EBData[2][0] = ImageTk.PhotoImage(image_Resize)
                            EBData[2][2] = autoSize
                            Control.configure(image = EBData[2][0])
                            return 
            if autoSize == True:
                image_Resize = image.resize((Control_Width, Control_Height),Image.LANCZOS)
            else:
                image_Resize = image
            newPTImage = ImageTk.PhotoImage(image_Resize)
            AddUserData(uiName,elementName,\'image\',\'imageInfo\',[newPTImage,imagePath,autoSize],0)
            Control.configure(image = newPTImage)
        if realElementName.find(\'Text_\') >= 0:
            if hasattr(Control,"GetEntry") == True:
                Control = Control.GetEntry()
            Control.delete(\'0.0\',tkinter.END)
            imagePath_Lower = imagePath.lower()
            if autoSize == True:
                image_Resize = image.resize((Control_Width, Control_Height),Image.LANCZOS)
            else:
                image_Resize = image
            newPTImage = ImageTk.PhotoImage(image_Resize)
            Control.image_create(tkinter.END, image=newPTImage)
            AddUserData(uiName,elementName,\'image\',\'imageInfo\',[newPTImage,imagePath,autoSize],0)
        if realElementName.find(\'Form_\') >= 0 or realElementName.find(\'Canvas_\') >= 0:
            if autoSize == True:
               SetCanvasBGImage(uiName,elementName,imagePath)
            else:
               SetCanvasBGImage(uiName,elementName,imagePath,\'\')
    
def InsertImage(uiName,elementName,position=tkinter.END,imagePath='',reSize=None):
    """'+Language.G_Language[9071]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    global G_ResourcesFileList
    Control = GetElement(uiName,elementName) 
    if Control == True: 
        from   PIL import Image,ImageTk
        image = None
        if isinstance(imagePath,str) == True:
            imagePath_Lower = imagePath.lower()
            if os.path.exists(imagePath) == False:
                if imagePath_Lower in G_ResourcesFileList:
                    imagePath = G_ResourcesFileList[imagePath_Lower]
                if os.path.exists(imagePath) == False:
'''
        f.write(code)

    if exportMode == False:
        code='''
                        return

                image = Image.open(imagePath).convert(format)
'''
        f.write(code)

    else:
        code='''
                        image = LoadImageFromPMEFile(imagePath)
                        if image is None:
                            return
                if image is None:
                    image = Image.open(imagePath).convert(format)
        elif isinstance(imagePath,Image.Image) == True:
            image = imagePath.convert(format)
        if image:
            image_Resize = image
            if reSize:
                image_Resize = image.resize(reSize,Image.LANCZOS)
            newPTImage = ImageTk.PhotoImage(image_Resize)
            Control.image_create(position, image=newPTImage)
            AddUserData(uiName,elementName,\'image\',\'imageInfo\',[newPTImage,imagePath,False],0)
            currentLine = Control.index(tkinter.INSERT)
            return  currentLine
    
    #f.write(Language.G_Language[1213]+'
def SetCanvasBGImage(uiName,elementName,imagePath,wrapType='Zoom'):
    """'+Language.G_Language[1813]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    global G_ResourcesFileList
    Control = GetElement(uiName,elementName) 
    if Control: 
        realElementName = elementName 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            realElementName = G_UIElementAliasDictionary[uiName][elementName] 
        if realElementName.find(\'Form_\') >= 0 or realElementName.find(\'Canvas_\') >= 0 :
            Control.delete('BGImage')
            newImage = None
            if imagePath:
                if isinstance(imagePath,str) == True:
                    imagePath_Lower = imagePath.lower()
                    if os.path.exists(imagePath) == False:
                        if imagePath_Lower in G_ResourcesFileList:
                            imagePath = G_ResourcesFileList[imagePath_Lower]
                        if os.path.exists(imagePath) == False:
'''
        f.write(code)
    if exportMode == False:
        code='''
                                return
                        newImage = Image.open(imagePath).convert(\'RGBA\')
'''
        f.write(code)
    else:
        code='''
                                newImage = LoadImageFromPMEFile(imagePath)
                        if newImage is None:
                            newImage = Image.open(imagePath).convert(\'RGBA\')
                else:
                    newImage = imagePath
            if newImage is None:
                return
            Control_Width = Control.winfo_width()
            Control_Height = Control.winfo_height()
            try:
                Form_1_Pack = Control.pack_info()
                if  len(Form_1_Pack) > 0:
                    if uiName in G_UIRootSizeDictionary.keys() and "width" in G_UIRootSizeDictionary[uiName].keys():
                        Control_Width = G_UIRootSizeDictionary[uiName]["width"]
                    elif G_RootSize:
                        Control_Width = G_RootSize[0]
                    if uiName in G_UIRootSizeDictionary.keys() and "height" in G_UIRootSizeDictionary[uiName].keys():
                        Control_Height = G_UIRootSizeDictionary[uiName]["height"]
                    elif G_RootSize:
                        Control_Height = G_RootSize[1]
            except:
                pass
            if wrapType == "Zoom" :
                reSizeImage = newImage.resize((Control_Width, Control_Height),Image.LANCZOS)
                newPTImage = ImageTk.PhotoImage(reSizeImage)
                AddUserData(uiName,elementName,'BGImage','imageInfo',[newPTImage,imagePath,wrapType],0)
                Control.create_image(0,0,anchor=tkinter.NW,image=newPTImage,tag="BGImage")
            elif wrapType == "Tiling" :
                newPTImage = ImageTk.PhotoImage(newImage)
                AddUserData(uiName,elementName,'BGImage','imageInfo',[newPTImage,imagePath,wrapType],0)
                RepeatRow = int(Control_Width / newImage.height) + 1
                RepeatCow = int(Control_Height / newImage.width) + 1
                for r in range(RepeatRow):
                    for c in range(RepeatCow):
                        Control.create_image(c * newImage.width, r * newImage.height,anchor=tkinter.NW,image=newPTImage,tag="BGImage")
            else:
                newPTImage = ImageTk.PhotoImage(newImage)
                AddUserData(uiName,elementName,'BGImage','imageInfo',[newPTImage,imagePath,wrapType],0)
                Control.create_image(0,0,anchor=tkinter.NW,image=newPTImage,tag="BGImage")
        ReDrawCanvasShape(uiName,elementName)
g_DownLoadImageDictionary = {}
def SetImageFromURL(uiName,elementName,url,autoSize = True):
    """'+Language.G_Language[1815]+'"""
    global g_DownLoadImageDictionary
    Control = GetElement(uiName,elementName) 
    ControlType = "Label"
    if elementName.find(\'Form_\') >= 0 or elementName.find(\'Canvas_\') >= 0 :
        ControlType = "Canvas"
    if elementName.find(\'Text_\') >= 0 :
        ControlType = "Text"
    if Control:
        def DownLoadImageFromURL(Control,ControlType,url,autoSize):
            try:
                if url in g_DownLoadImageDictionary:    
                    if ControlType == "Canvas":   
                        Control.delete('BGImage')
                        Control.create_image(0,0,anchor=tkinter.NW,image=g_DownLoadImageDictionary[url],tag="BGImage")
                    elif ControlType == "Text":   
                        if hasattr(Control,"GetEntry") == True:
                            Control = Control.GetEntry()
                        Control.delete(\'0.0\',tkinter.END)
                        Control.image_create(tkinter.END, image=g_DownLoadImageDictionary[url])
                    else:   
                        Control.configure(image=g_DownLoadImageDictionary[url])    
                else: 
                    urlOpen = urlopen(url) 
                    if urlOpen : 
                        image_bytes = urlOpen.read() 
                        data_stream = io.BytesIO(image_bytes) 
                        pil_image = Image.open(data_stream) 
                        if autoSize == True: 
                            pil_image = pil_image.resize((Control.winfo_width(), Control.winfo_height()),Image.LANCZOS) 
                        g_DownLoadImageDictionary[url] = ImageTk.PhotoImage(pil_image) 
                        if ControlType == "Canvas":   
                            Control.delete('BGImage')
                            Control.create_image(0,0,anchor=tkinter.NW,image=g_DownLoadImageDictionary[url],tag="BGImage")
                        elif ControlType == "Text":   
                            Control.delete(\'0.0\',tkinter.END)
                            Control.image_create(tkinter.END, image=g_DownLoadImageDictionary[url])
                        else:   
                            Control.configure(image=g_DownLoadImageDictionary[url]) 
            except Exception as ex:
                print(ex)
        run_thread = threading.Thread(target=DownLoadImageFromURL, args=[Control,ControlType,url,autoSize])
        run_thread.Daemon = True
        run_thread.start() 
def RemoveImage(uiName,elementName):
    """'+Language.G_Language[9503]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    Control = GetElement(uiName,elementName) 
    if Control: 
        DelUserData(uiName,elementName,\'image\')
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find(\'Label_\') >= 0 or elementName.find(\'Button_\') >= 0 :
            Control.configure(image = '')
        if elementName.find(\'Form_\') >= 0 or elementName.find(\'Canvas_\') >= 0 :
            Control.delete('BGImage')
''' 
        f.write(code)
#写入更新到文字
def WriteGetImageFunction(f):
    code='''
    #f.write(Language.G_Language[1214]+'
def GetImage(uiName,elementName):
    """'+Language.G_Language[1214]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find(\'Label_\') >= 0 or elementName.find(\'Button_\') >= 0 :
            if uiName in G_UIElementUserDataArray:
                if elementName in G_UIElementUserDataArray[uiName]:
                    for EBData in G_UIElementUserDataArray[uiName][elementName]:   
                        if EBData[0] == \'image\' and EBData[1] ==\'imageInfo\':
                            return EBData[2][0]
        if elementName.find(\'Form_\') >= 0 or elementName.find(\'Canvas_\') >= 0 :
            if uiName in G_UIElementUserDataArray:
                if elementName in G_UIElementUserDataArray[uiName]:
                    for EBData in G_UIElementUserDataArray[uiName][elementName]:   
                        if EBData[0] == \'BGImage\' and EBData[1] ==\'imageInfo\':
                            return EBData[2][0]
    return str("")
def GetImageFileName(uiName,elementName):
    """'+Language.G_Language[6595]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find(\'Label_\') >= 0 or elementName.find(\'Button_\') >= 0 :
            if uiName in G_UIElementUserDataArray:
                if elementName in G_UIElementUserDataArray[uiName]:
                    for EBData in G_UIElementUserDataArray[uiName][elementName]:   
                        if EBData[0] == \'image\' and EBData[1] ==\'imageInfo\':
                            return EBData[2][1]
        if elementName.find(\'Form_\') >= 0 or elementName.find(\'Canvas_\') >= 0 :
            if uiName in G_UIElementUserDataArray:
                if elementName in G_UIElementUserDataArray[uiName]:
                    for EBData in G_UIElementUserDataArray[uiName][elementName]:   
                        if EBData[0] == \'BGImage\' and EBData[1] ==\'imageInfo\':
                            return EBData[2][1]
    return str("")
def LoadImageFromFile(imagefile,reSize=None,uiName=None,elementName=None):
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_ResourcesFileList
    """'+Language.G_Language[6594]+'"""
    if imagefile != None:
        resourPath = imagefile
        newImage = None
        if os.path.exists(resourPath) == False:
            resourPath, imagefile = os.path.split(imagefile)
            imagefile_Lower = imagefile.lower()
            if imagefile_Lower in G_ResourcesFileList:
                resourPath = G_ResourcesFileList[imagefile_Lower]
    # f.write('                if os.path.exists(resourPath) == False:
    # f.write('                    return None
            else:
                newImage = LoadImageFromPMEFile(imagefile)
        try:
            if os.path.exists(resourPath) == True and newImage is None:
                pathname_noext, extension = os.path.splitext(resourPath)
                newImage = None
                extension = extension.lower()
                if extension == ".png" or extension == ".gif":
                    newImage = Image.open(resourPath).convert(\'RGBA\')
                elif extension == ".jpg" or extension == ".bmp":
                    newImage = Image.open(resourPath).convert(\'RGB\')
                else:
                    return None
            if newImage == None:
                return None
            if reSize:
                newImage = newImage.resize((reSize[0],reSize[1]),Image.LANCZOS)
            if uiName and elementName:
                realElementName = elementName
                if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
                    realElementName = G_UIElementAliasDictionary[uiName][elementName]
                newPTImage = ImageTk.PhotoImage(newImage)
                if realElementName.find('Form_') >= 0 or realElementName.find('Canvas_') >= 0 :
                    AddUserData(uiName,elementName,'BGImage','imageInfo',[newPTImage,resourPath,False],0)
                else:
                    AddUserData(uiName,elementName,'image','imageInfo',[newPTImage,resourPath,False],0)
            return newImage
        except Exception as ex:
            print(imagefile+":'+Language.G_Language[1706]+'")
    return None
def LoadGIF(uiName,elementName,imagefile,w=0,h=0):
    """'+Language.G_Language[6590]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    global G_ResourcesFileList
    newImage = None
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find('Label_') >= 0 or elementName.find('Button_') >= 0 or elementName.find('RadioButton_') >= 0 or elementName.find('CheckButton_') >= 0 or elementName.find('Text_') >= 0:
            hasGIFAnimation = False
            if imagefile != None:
                resourPath = imagefile 
                if os.path.exists(resourPath) == False:
                    resourPath, imagefile = os.path.split(imagefile)
                    imagefile_Lower = imagefile.lower()
                    if imagefile_Lower in G_ResourcesFileList:
                        resourPath = G_ResourcesFileList[imagefile_Lower]
                if os.path.exists(resourPath) == True:
                    try:
                        if imagefile.find('.gif') >= 0:
                            GifData = Image.open(resourPath)
                            seq = []
                            try:
                                while 1:
                                    imageRGBA = GifData.copy().convert('RGBA')
                                    if newImage is None:
                                        newImage = imageRGBA
                                    if w > 0 and h > 0:
                                        resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                        newFrame = ImageTk.PhotoImage(resizeImage)
                                    else:
                                        newFrame = ImageTk.PhotoImage(imageRGBA)
                                    seq.append(newFrame)
                                    GifData.seek(len(seq))
                            except EOFError:
                                pass
                            delay = 100
                            try:
                                delay = GifData.info['duration']
                            except KeyError:
                                delay = 100
                            if delay == 0:
                                delay = 100
                            hasGIFAnimation = True
                            if elementName not in G_CanvasImageDictionary[uiName]:
                                G_CanvasImageDictionary[uiName][elementName] = []
                            G_CanvasImageDictionary[uiName][elementName].append([imagefile,[seq,delay,0,None],w,h])
                        else:
                            newImage = Image.open(resourPath).convert('RGBA')
                    except:
                        return newImage
                if hasGIFAnimation == True:
                    Control.after(100,lambda: updateGIFFrame(uiName,elementName))
    return newImage
def StopGIF(uiName,elementName):
    """'+Language.G_Language[6591]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    global G_ResourcesFileList
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find('Label_') >= 0 or elementName.find('Button_') >= 0 or elementName.find('RadioButton_') >= 0 or elementName.find('CheckButton_') >= 0 or elementName.find('Text_') >= 0:
            Control.after_cancel(updateGIFFrame)
            if elementName in G_CanvasImageDictionary[uiName]:
                G_CanvasImageDictionary[uiName][elementName].clear()
'''
    f.write(code)
#写入更新到文字
def WriteSetImageFunction_Mobile(f,exportMode = False,usePME = False):
    code='''
def LoadImageFromPMEFile(imagePath):
    if usePME == False:
        return None
    else:
        global PMEPassword
        pathName,fileName = os.path.split(imagePath)
        shotName,extension = os.path.splitext(fileName)
        imagePath = os.path.join(pathName,shotName+".pme")
        if os.path.exists(imagePath) == True:
            #从加密文件中读取图片
            result,image = PyMeEncryption.LoadFromEncryptionFile(imagePath,PMEPassword)
            if result == True:
                return image
            else:
                return None
        imagePath_Lower = imagePath.lower()
        if imagePath_Lower in G_ResourcesFileList:
            imagePath = G_ResourcesFileList[imagePath_Lower]
            if os.path.exists(imagePath) == False:
                return None
            #从加密文件中读取图片
            result,image = PyMeEncryption.LoadFromEncryptionFile(imagePath,PMEPassword)
            if result == True:
                return image
        return None
    #f.write(Language.G_Language[1213]+'
def SetImage(uiName,elementName,imagePath,autoSize = True,format=\'RGBA\'):
    """'+Language.G_Language[1213]+'"""
    global G_UIElementAliasDictionary
    Control = GetElement(uiName,elementName) 
    if Control and isinstance(imagePath,str) == True: 
        if autoSize == True:
            Control.SetImage(imagePath,"IMG_2_NODE")
        else:
            Control.SetImage(imagePath,None)
def InsertImage(uiName,elementName,position=tkinter.END,imagePath='',reSize=None):
    """'+Language.G_Language[9071]+'"""
    global G_UIElementAliasDictionary
    Control = GetElement(uiName,elementName) 
    if Control and isinstance(imagePath,str) == True: 
        Control.SetImage(imagePath,None)
    #f.write('        currentLine = Control.index(tkinter.INSERT)
        return  currentLine
    #f.write(Language.G_Language[1213]+'
def SetCanvasBGImage(uiName,elementName,imagePath,wrapType='Zoom'):
    """'+Language.G_Language[1813]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global G_UIElementVariableArray
    global G_ResourcesFileList
    Control = GetElement(uiName,elementName) 
    if Control: 
        realElementName = elementName 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            realElementName = G_UIElementAliasDictionary[uiName][elementName] 
        if realElementName.find(\'Form_\') >= 0 or realElementName.find(\'Canvas_\') >= 0 :
            ControlWidth = Control.GetWidth()
            ControlHeight = Control.GetHeight()
            if wrapType == "Zoom" :
                Control.SetImage(imagePath,"IMG_2_NODE")
            elif wrapType == "Tiling" :
                pass
    # f.write('                newPTImage = ImageTk.PhotoImage(newImage)
    # f.write("                AddUserData(uiName,elementName,'BGImage','imageInfo',[newPTImage,imagePath,wrapType],0)
    # f.write("                RepeatRow = int(ControlHeight/ newImage.height) + 1
    # f.write("                RepeatCow = int(ControlWidth/ newImage.width) + 1
    # f.write("                for r in range(RepeatRow):
    # f.write("                    for c in range(RepeatCow):
    # f.write('                        Control.create_image(c * newImage.width, r * newImage.height,anchor=tkinter.NW,image=newPTImage,tag="BGImage")
    # f.write('                        DrawImage(uiName,elementName,c * newImage.width, r * newImage.height,ControlWidth,ControlHeight,imagePath,shapeTag='')
            else:
                Control.SetImage(imagePath,None)


g_DownLoadImageDictionary = {}
def SetImageFromURL(uiName,elementName,url,autoSize = True):
    """'+Language.G_Language[1815]+'"""
    global g_DownLoadImageDictionary
    Control = GetElement(uiName,elementName) 
    ControlType = "Label"
    if elementName.find(\'Form_\') >= 0 or elementName.find(\'Canvas_\') >= 0 :
        ControlType = "Canvas"
    if elementName.find(\'Text_\') >= 0 :
        ControlType = "Text"
    if Control:
        def DownLoadImageFromURL(widget,ControlType,url,autoSize):
            try:
                if url in g_DownLoadImageDictionary:    
                    if ControlType == "Canvas":   
                        Control.delete('BGImage')
                        Control.create_image(0,0,anchor=tkinter.NW,image=g_DownLoadImageDictionary[url],tag="BGImage")
                    elif ControlType == "Text":   
                        Control.delete(\'0.0\',tkinter.END)
                        Control.image_create(tkinter.END, image=g_DownLoadImageDictionary[url])
                    else:   
                        widget.configure(image=g_DownLoadImageDictionary[url])    
                else: 
                    urlOpen = urlopen(url) 
                    if urlOpen : 
                        image_bytes = urlOpen.read() 
                        data_stream = io.BytesIO(image_bytes) 
                        pil_image = Image.open(data_stream) 
                        if autoSize == True: 
                            pil_image = pil_image.resize((Control.winfo_width(), Control.winfo_height()),Image.LANCZOS) 
                        g_DownLoadImageDictionary[url] = ImageTk.PhotoImage(pil_image) 
                        if ControlType == "Canvas":   
                            Control.delete('BGImage')
                            Control.create_image(0,0,anchor=tkinter.NW,image=g_DownLoadImageDictionary[url],tag="BGImage")
                        elif ControlType == "Text":   
                            Control.delete(\'0.0\',tkinter.END)
                            Control.image_create(tkinter.END, image=g_DownLoadImageDictionary[url])
                        else:   
                            widget.configure(image=g_DownLoadImageDictionary[url]) 
            except Exception as ex:
                print(ex)
        run_thread = threading.Thread(target=DownLoadImageFromURL, args=[Control,ControlType,url,autoSize])
        run_thread.Daemon = True
        run_thread.start() 


''' 
    f.write(code)
#把树结点写入文件
def WriteLoadTreeItemIconFunction(f):
    code='''
    #f.write(Language.G_Language[1249]+'
def LoadImageToIconList(uiName,elementName,ItemName,imageFile):
    """'+Language.G_Language[1249]+'"""
    global G_ResourcesFileList
    imagePath = imageFile
    imageFile_Lower = imageFile.lower()
    if imageFile_Lower in G_ResourcesFileList:
        imagePath = G_ResourcesFileList[imageFile_Lower]
    if os.path.exists(imagePath) == True:
        image = ImageTk.PhotoImage(file = imagePath)
        if elementName not in G_UIElementIconDictionary[uiName].keys():
            G_UIElementIconDictionary[uiName][elementName] = {}
        G_UIElementIconDictionary[uiName][elementName][ItemName] = image
        return image
    return None

''' 
    f.write(code)
#取得当前选中文本
def WriteGetSelectTextFunction(f):
    code='''
def GetSelectText(uiName,elementName):
    """'+Language.G_Language[9070]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find(\'Text_\') >= 0 : 
            if hasattr(Control,"GetEntry") == True:
                Control = Control.GetEntry()
            return Control.get(tkinter.SEL_FIRST,tkinter.SEL_LAST)
    return None

''' 
    f.write(code)
#删除当前选中文本
def WriteDelSelectTextFunction(f):
    code='''
def DelSelectText(uiName,elementName):
    """'+Language.G_Language[9014]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find(\'Text_\') >= 0 :
            if hasattr(Control,"GetEntry") == True:
                Control = Control.GetEntry()
            return Control.delete(tkinter.SEL_FIRST,tkinter.SEL_LAST)
    return None

''' 
    f.write(code)
#写入设置当前值
def WriteSetCurrentValueFunction(f):
    code='''
    #f.write(Language.G_Language[1232]+'
def SetCurrentValue(uiName,elementName,value):
    """'+Language.G_Language[1292]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find(\'RadioButton_\') >= 0 : 
            SetTKVariable(uiName,elementName,value)
        if elementName in G_UIGroupDictionary[uiName]: 
            GroupName = G_UIGroupDictionary[uiName][elementName]
            if GroupName.find("Group_") == 0:
                GroupText = GroupName[6:] 
                GroupID = int(GroupText) 
                OnRadioButtonClick(GroupID,value) 
        elif elementName.find(\'CheckButton_\') >= 0 : 
            event = ChartEvent(0,0,Control)
            if value != GetCurrentValue(uiName,elementName):
                OnCheckButtonClick(event,uiName,elementName)
            SetTKVariable(uiName,elementName,value)
        elif elementName.find(\'ComboBox_\') >= 0 : 
            Control.set(value)
        elif elementName.find(\'Scale_\') >= 0 : 
            Control.set(value)
        elif elementName.find(\'SpinBox_\') >= 0 : 
            SetTKVariable(uiName,elementName,value)
        elif elementName.find(\'SwitchButton_\') >= 0 : 
            Control.SetCurrValue(value)
        elif elementName.find(\'Slider_\') >= 0 : 
            Control.SetCurrValue(value)
        elif elementName.find(\'Slider_\') >= 0 : 
            Control.SetCurrValue(value)
        elif elementName.find(\'ProgressDial_\') >= 0 : 
            Control.SetCurrValue(value)
        elif elementName.find(\'ListBox_\') >= 0 :
            Control.selection_clear(0,tkinter.END)  
            itemCount = Control.size()  
            for itemIndex in range(0,itemCount):   
                itemText = Control.get(itemIndex)   
                if itemText == value:   
                    Control.select_set(itemIndex)   
                    break   
        elif elementName.find(\'Progress_\') >= 0 : 
            Control["value"] = value 
def SetCurrentIndex(uiName,elementName,index):
    """'+Language.G_Language[1231]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find(\'ComboBox_\') >= 0 : 
            Control.current(index)
        elif elementName.find(\'ListBox_\') >= 0 :
            Control.selection_clear(0,tkinter.END)   
            Control.selection_set(index)   
        elif elementName.find(\'Navigation_\') >= 0 :
            Control.SetCurrentIndex(index)   
''' 
    f.write(code)
#写入设置当前值
def WriteSetCurrentValueFunction_APP(f):
    code='''
    #f.write(Language.G_Language[1232]+'
def SetCurrentValue(uiName,elementName,value):
    """'+Language.G_Language[1292]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find(\'RadioButton_\') >= 0 : 
            Control.SetRadioValue(value)
        elif elementName.find(\'CheckButton_\') >= 0 : 
            Control.SetChecked(value)
        elif elementName.find(\'ComboBox_\') >= 0 : 
            Control.SelectText(value)
        elif elementName.find(\'Scale_\') >= 0 : 
            Control.SetValue(value)
        elif elementName.find(\'Slider_\') >= 0 : 
            Control.SetCurrValue(value)
        elif elementName.find(\'SpinBox_\') >= 0 : 
            Control.SetValue(value)
        elif elementName.find(\'ListBox_\') >= 0 :
            Control.SelectText(value)   
        elif elementName.find(\'Progress_\') >= 0 : 
            Control.SetValue(value)
        elif elementName.find(\'ProgressDial_\') >= 0 : 
            Control.SetCurrValue(value)
''' 
    f.write(code)
#弹出对话框
def WriteMessageBoxFunction_APP(f):
    code='''
    #f.write(Language.G_Language[1221]+'
def MessageBox(text="",title="info",type="info"):
    """'+Language.G_Language[1221]+'"""
    GameLib.MessageBox(text)

''' 
    f.write(code)
#写入设置滑动条
def WriteSetScaleFunction(f):
    code='''
def SetScale(uiName,elementName,minimum,maximum,tickinterval):
    """'+Language.G_Language[1293]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find(\'Scale_\') >= 0 : 
            Control.configure(from_=minimum) 
            Control.configure(to=maximum) 
            Control.configure(tickinterval=tickinterval) 
def SetSlider(uiName,elementName,minimum,maximum,value=0):
    """'+Language.G_Language[1108]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find(\'Slider_\') >= 0 : 
            Control.SetMinValue(minimum) 
            Control.SetMaxValue(maximum) 
            Control.SetCurrValue(value) 
''' 
    f.write(code)
#写入设置滑动条
def WriteSetProgressFunction(f):
    code='''
def SetProgress(uiName,elementName,maximum,value=0):
    """'+Language.G_Language[1299]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find("ProgressDial_") >= 0:
            Control.SetMaxValue(maximum)
            Control.GetCurrValue(value)
        elif elementName.find("Progress_") >= 0:
            Control.configure(maximum=maximum) 
            Control.configure(value=value) 

''' 
    f.write(code)
#写入设置滑动条
def WriteMoveFrameFunction(f):
    code='''
def MovingChildPageXViewOffset(uiName,elementName,step=1):
    """'+Language.G_Language[1805]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        elementName = elementName + "_Child"
        ChildPage = GetElement(uiName,elementName)
        if ChildPage: 
            ChildPage.xview("scroll",step,"units")
def MovingChildPageYViewOffset(uiName,elementName,step=1):
    """'+Language.G_Language[1806]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        elementName = elementName + "_Child"
        ChildPage = GetElement(uiName,elementName)
        if ChildPage: 
            ChildPage.yview("scroll",step,"units")
def MovingChildPageXViewTo(uiName,elementName,x=1.0):
    """'+Language.G_Language[1807]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        elementName = elementName + "_Child"
        ChildPage = GetElement(uiName,elementName)
        if ChildPage: 
            ChildPage.xview_moveto(x)
def MovingChildPageYViewTo(uiName,elementName,y=1.0):
    """'+Language.G_Language[1808]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        elementName = elementName + "_Child"
        ChildPage = GetElement(uiName,elementName)
        if ChildPage: 
            ChildPage.yview_moveto(y)
''' 
    f.write(code)
#写入取得的日期
def WriteGetDateFunction(f):
    code='''
def GetDate(uiName,elementName):
    """'+Language.G_Language[1296]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        return Control.GetDate() 
    return None 
def SetDate(uiName,elementName,year,month,day):
    """'+Language.G_Language[1473]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        return Control.SetDate(year,month,day) 
    return None 
''' 
    f.write(code)
#写入取得当前ListBox和ComboBox值列表的函数
def WriteGetValueListFunction(f):
    code='''
def GetValueList(uiName,elementName):
    """'+Language.G_Language[1958]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find(\'ComboBox_\') >= 0 : 
            return Control["values"]
        elif elementName.find(\'ListBox_\') >= 0 :
            listValueList = Control.get(0,tkinter.END)   
            return listValueList   
        elif elementName.find(\'SpinBox_\') >= 0 : 
            return Control["values"]
    return None
def GetSelectedValueList(uiName,elementName):
    """'+Language.G_Language[9023]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find(\'ListBox_\') >= 0 :
            selectedIndexList = Control.curselection()   
            selectedValueList = []   
            for index in selectedIndexList:   
                itemText = Control.get(index)   
                selectedValueList.append(itemText)   
            return selectedValueList   
    return None
''' 
    f.write(code)
#写入取得当前ListBox和ComboBox值列表的函数
def WriteGetValueListFunction_APP(f):
    code='''
def GetValueList(uiName,elementName):
    """'+Language.G_Language[1958]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find(\'ComboBox_\') >= 0 : 
            return Control.GetValueList()
        elif elementName.find(\'ListBox_\') >= 0 :
            return Control.GetValueList() 
        elif elementName.find(\'SpinBox_\') >= 0 : 
            return Control.GetValueList()
    return None

''' 
    f.write(code)
#写入设置当前ListBox和ComboBox值列表的函数
def WriteSetValueListFunction(f):
    code='''
def SetValueList(uiName,elementName,valueList):
    """'+Language.G_Language[1959]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find(\'ComboBox_\') >= 0 : 
            Control["values"] = valueList
        elif elementName.find(\'ListBox_\') >= 0 :
            Control.delete(0,tkinter.END)   
            for value in valueList:   
                Control.insert(tkinter.END,value)   
        elif elementName.find(\'SpinBox_\') >= 0 : 
            Control["values"] = valueList

''' 
    f.write(code)
#写入设置当前ListBox和ComboBox值列表的函数
def WriteSetValueListFunction_APP(f):
    code='''
def SetValueList(uiName,elementName,valueList):
    """'+Language.G_Language[1959]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find(\'ComboBox_\') >= 0 : 
            Control.SetValueList(valueList)
        elif elementName.find(\'ListBox_\') >= 0 :
            Control.SetValueList(valueList)
        elif elementName.find(\'SpinBox_\') >= 0 : 
            Control.SetValueList(valueList)
''' 
    f.write(code)
#写入取得当前值
def WriteGetCurrentValueFunction(f):
    code='''
def OnListBoxSelect(event,uiName,widgetName):
    ListBox_Index = GetCurrentIndex(uiName,widgetName)
    if ListBox_Index < 0:
        if widgetName in  G_UIElementVariableArray[uiName]: 
            ListBox_Index = G_UIElementVariableArray[uiName][widgetName].get()
            SetCurrentIndex(uiName,widgetName,ListBox_Index)
def OnListBoxFocusOut(event,uiName,widgetName):
    ListBox_Index = GetCurrentIndex(uiName,widgetName)
    if ListBox_Index >= 0:
        G_UIElementVariableArray[uiName][widgetName].set(ListBox_Index)
    #f.write(Language.G_Language[1232]+'
def GetCurrentValue(uiName,elementName):
    """'+Language.G_Language[1291]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find(\'RadioButton_\') >= 0 : 
            return GetTKVariable(uiName,elementName)
        elif elementName.find(\'CheckButton_\') >= 0 : 
            return GetTKVariable(uiName,elementName)
        elif elementName.find(\'ComboBox_\') >= 0 : 
            return Control.get()
        elif elementName.find(\'Scale_\') >= 0 : 
            return Control.get()
        elif elementName.find(\'SpinBox_\') >= 0 : 
            return Control.get()
        elif elementName.find(\'SwitchButton_\') >= 0 : 
            return Control.GetCurrValue()
        elif elementName.find(\'ProgressDial_\') >= 0 : 
            return Control.GetCurrValue()
        elif elementName.find(\'Slider_\') >= 0 : 
            return Control.GetCurrValue()
        elif elementName.find(\'ListBox_\') >= 0 :
            currIndex = Control.curselection()   
            if len(currIndex) > 0 and currIndex[0] >= 0:   
                return Control.get(currIndex[0])   
        elif elementName.find(\'Progress_\') >= 0 : 
            return Control["value"]
        elif elementName.find(\'Navigation_\') >= 0 : 
            return Control.GetCurrentItemValue()
    return -1
def GetCurrentIndex(uiName,elementName):
    """'+Language.G_Language[1232]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find(\'ComboBox_\') >= 0 : 
            return Control.current()
        elif elementName.find(\'ListBox_\') >= 0 :
            currIndex = Control.curselection()   
            if len(currIndex) > 0 and currIndex[0] >= 0:   
                return currIndex[0]   
        if elementName.find(\'Navigation_\') >= 0 : 
            return Control.GetCurrentIndex()
    return -1

    
''' 
    f.write(code)
#写入取得当前值
def WriteGetCurrentValueFunction_APP(f):
    code='''
    #f.write(Language.G_Language[1232]+'
def GetCurrentValue(uiName,elementName):
    """'+Language.G_Language[1291]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find(\'RadioButton_\') >= 0 : 
            return Control.GetRadioValue()
        elif elementName.find(\'CheckButton_\') >= 0 : 
            return Control.IsChecked()
        elif elementName.find(\'ComboBox_\') >= 0 : 
            return Control.GetSelectedText()
        elif elementName.find(\'Scale_\') >= 0 : 
            return Control.GetValue()
        elif elementName.find(\'Slider_\') >= 0 : 
            return Control.GetCurrValue()
        elif elementName.find(\'SpinBox_\') >= 0 : 
            return Control.GetValue()
        elif elementName.find(\'ListBox_\') >= 0 :
            return Control.GetSelectedText()   
        elif elementName.find(\'Progress_\') >= 0 : 
            return Control.GetValue()
        elif elementName.find(\'ProgressDial_\') >= 0 : 
            return Control.GetCurrValue()
        elif elementName.find(\'SwitchButton_\') >= 0 : 
            return Control.GetCurrValue()
        elif elementName.find(\'ProgressDial_\') >= 0 : 
            return Control.GetCurrValue()
    return -1
def GetCurrentIndex(uiName,elementName):
    """'+Language.G_Language[1314]+'"""
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if elementName.find(\'ComboBox_\') >= 0 : 
            return Control.GetSelectedIndex()
        elif elementName.find(\'ListBox_\') >= 0 :
            return Control.GetSelectedIndex()   
    return -1
#写入更新到文字
'''
    f.write(code)
def WriteInitFunction(f,HasCanvas,UseDataBase):
    code='''
    #f.write(Language.G_Language[1215]+'
def InitElementData(uiName):
    """'+Language.G_Language[1215]+'"""
    global G_UIElementUserDataArray
    global G_UIElementLayerDictionary
    global G_ResourcesFileList
    global G_UIRootSizeDictionary
    global G_UIRootStateDictionary
    global G_RootSize
    global G_UIScale
    global G_WindowDraggable
    if uiName in G_UIElementUserDataArray:
        for elementName in G_UIElementUserDataArray[uiName].keys():
            for EBData in G_UIElementUserDataArray[uiName][elementName]:
                if EBData[3] == 1:
                    SetText(uiName,elementName,EBData[2],False)
        
    if  HasCanvas == True:
        UIScale = G_UIScale
        if uiName in G_UIRootSizeDictionary.keys():
            if "scale" in G_UIRootSizeDictionary[uiName].keys():
                UIScale = G_UIRootSizeDictionary[uiName]["scale"]
        LoadCanvasRecord(uiName,UIScale)
    if  UseDataBase == True:
        for elementName in G_UIElementDictionary[uiName]:
            if elementName.find("ListView_") >= 0 and elementName.find("Scroll") < 0:
                 LoadDynamicColumn(uiName,elementName)
        
    uiClass = GetElement(uiName,"UIClass")
    if uiClass:
        Form_1 = GetElement(uiName,"Form_1")
        if Form_1:
            Form_1_Width = Form_1.winfo_width()
            Form_1_Pack = Form_1.pack_info()
            if Form_1_Width == 1 or len(Form_1_Pack) > 0:
                if uiName in G_UIRootSizeDictionary.keys() and "width" in G_UIRootSizeDictionary[uiName].keys():
                    Form_1_Width = G_UIRootSizeDictionary[uiName]["width"]
                elif G_RootSize:
                    Form_1_Width = G_RootSize[0]
            Form_1_Height = Form_1.winfo_height()
            if Form_1_Height == 1 or len(Form_1_Pack) > 0:
                if uiName in G_UIRootSizeDictionary.keys() and "height" in G_UIRootSizeDictionary[uiName].keys():
                    Form_1_Height = G_UIRootSizeDictionary[uiName]["height"]
                elif G_RootSize:
                    Form_1_Height = G_RootSize[1]
            event = ChartEvent(Form_1_Width,Form_1_Height,Form_1)
            if hasattr(uiClass,"Configure") == True:
                uiClass.Configure(event)
        if G_WindowDraggable:
            uiRoot = GetElement(uiName,"root")
            if uiRoot is G_WindowDraggable.GetWidget():
                for formName in uiRoot.children.keys():
                    formwidget = uiRoot.children[formName]
                    formwidget.bind('<ButtonPress-1>',G_WindowDraggable.StartDrag)
                    formwidget.bind('<ButtonRelease-1>',G_WindowDraggable.StopDrag)
                    formwidget.bind('<B1-Motion>',G_WindowDraggable.MoveDragPos)
                    for childName in formwidget.children.keys():
                        childwidget = formwidget.children[childName]
                        if childwidget.winfo_class() == "Label" or childwidget.winfo_class() == "Labelframe" or childwidget.winfo_class() == "Frame":
                            childUiName,childElementName = GetElementName(childwidget,False)
                            if childElementName == None or childElementName.find("LabelButton_") >= 0:
                                continue
                            bindingFunc = childwidget.bind('<ButtonPress-1>')
                            if bindingFunc:                       
                                continue
                            childwidget.bind('<ButtonPress-1>',G_WindowDraggable.StartDrag)
                            childwidget.bind('<ButtonRelease-1>',G_WindowDraggable.StopDrag)
                            childwidget.bind('<B1-Motion>',G_WindowDraggable.MoveDragPos)
    for elementName in G_UIElementLayerDictionary[uiName]:
        Control = GetElement(uiName,elementName)
        direction = G_UIElementLayerDictionary[uiName][elementName]
        if direction == 'lift':
            Control.lift()
        else:
            Control.lower()
    ResizeAllChart(uiName,True)
    #显示界面
    if uiName in G_UIRootStateDictionary.keys() and G_UIRootStateDictionary[uiName] == 'deiconify':
        return
    else:
        RestoreUI(uiName)
    #f.write(Language.G_Language[1216]+'
def InitElementStyle(uiName,Style):
    """'+Language.G_Language[1216]+'"""
    StyleArray = ReadStyleFile(Style+".py")
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        Root = GetElement(uiName,\'root\')
        TFormKey = \'.TForm\'
        if TFormKey in StyleArray:
            if \'background\' in StyleArray[TFormKey]:
                Root[\'background\'] = StyleArray[TFormKey][\'background\']
        for elementName in G_UIElementDictionary[uiName].keys():
            Widget = G_UIElementDictionary[uiName][elementName]
            if elementName != "UIClass" and elementName != "root":
                try:
                    OldWidget = Widget
                    if hasattr(Widget,"GetWidget") == True:
                        Widget = Widget.GetWidget()
                    if  Widget.winfo_exists() == 1:
                        WinClass = Widget.winfo_class()
                        StyleName = ".T"+WinClass
                        if StyleName in StyleArray.keys():
                            for attribute in StyleArray[StyleName].keys():
                                if attribute == "relief":
                                    continue
                                if attribute == "highlightthickness":
                                    continue
                                if attribute == "bd":
                                    continue
                                if attribute == "background" and elementName != "Form_1":
                                    if hasattr(OldWidget,"SetBGColor") == True:
                                        OldWidget.SetBGColor(StyleArray[StyleName][attribute])
                                    if Widget["background"] == "#EFEFEF":
                                        Widget[attribute] = StyleArray[StyleName][attribute]
                                    else:
                                        continue
                                else:
                                    if elementName.find("_LabelButton_") > 0:
                                        continue
                                    Widget[attribute] = StyleArray[StyleName][attribute]
                                    if attribute == "foreground" :
                                        if hasattr(OldWidget,"SetFGColor") == True:
                                            OldWidget.SetFGColor(StyleArray[StyleName][attribute])
                except Exception as ex:
                    errorText = str(ex)
                    if errorText.find("no attribute \'winfo_exists\'") < 0:
                        print(ex)
'''
    f.write(code)
#写入更新到文字
def WriteInitFunction_Mobile(f,HasCanvas,UseDataBase):
    code='''
    #f.write(Language.G_Language[1215]+'
def InitElementData(uiName):
    """'+Language.G_Language[1215]+'"""
    
    global G_UIElementUserDataArray
    if uiName in G_UIElementUserDataArray:
        for elementName in G_UIElementUserDataArray[uiName].keys():
            for EBData in G_UIElementUserDataArray[uiName][elementName]:
                if EBData[3] == 1:
                    SetText(uiName,elementName,EBData[2],False)
    if  HasCanvas == True:
        LoadCanvasRecord(uiName)
    if  UseDataBase == True:
        for elementName in G_UIElementDictionary[uiName]:
            if elementName.find("ListView_") >= 0:
                 LoadDynamicColumn(uiName,elementName)
''' 
    f.write(code)
def WriteCallUIDialog_Mobile(f):
    code='''
def GoToUIDialog(uiName,targetUIName,params=None):
    """'+Language.G_Language[1343]+'"""
    root = GetElement(uiName,\'root\')
    Form1 = GetElement(uiName,\'Form_1\')
    layer = root.GetSceneInstance().GetLayer("UI")
    import importlib
    from   importlib import import_module
    try:
        importModule = importlib.import_module(targetUIName)
        importModule = importlib.reload(importModule)
        if hasattr(importModule,"Fun") == True:
            importModule.Fun.G_ExeDir = G_ExeDir
            importModule.Fun.G_ResDir = G_ResDir
            if hasattr(importModule,"EXUIControl") == True:
                importModule.EXUIControl.G_ExeDir = G_ExeDir
                importModule.EXUIControl.G_ResDir = G_ResDir
        if hasattr(importModule,targetUIName) == True:
            uiClass = getattr(importModule,targetUIName)
            newUI = uiClass()
            layer.AddGameNode(newUI)
            layer.DelGameNode(Form1.GetInstanceID())
    except Exception as ex:
        MessageBox(str(ex))
def CallUIDialog(targetUIName,topmost = 1,toolwindow = 1,grab_set = 1,wait_window = 1,animation='',params=None):
    """'+Language.G_Language[1297]+'"""
    GameLib.PopupUI(targetUIName)

def LoadUIDialog(uiName,elementName,targetUIName,params=None,ignoreSameUI=True):
    """'+Language.G_Language[1345]+'"""
    targetUI = GetElement(uiName,elementName)
    if targetUI:
        currUIDialog = GetUserData(uiName,elementName,"CurrUI")
        lastLoadTime = GetUserData(uiName,elementName,"LoadTime")
        if currUIDialog:
            targetUI.RemoveChild(currUIDialog)
        import importlib
        from   importlib import import_module
        try:
            targetUIName = targetUIName.replace(".py","")
            importModule = importlib.import_module(targetUIName)
            importModule = importlib.reload(importModule)
            if hasattr(importModule,"Fun") == True:
                importModule.Fun.G_ExeDir = G_ExeDir
                importModule.Fun.G_ResDir = G_ResDir
                if hasattr(importModule,"EXUIControl") == True:
                    importModule.EXUIControl.G_ExeDir = G_ExeDir
                    importModule.EXUIControl.G_ResDir = G_ResDir
            if hasattr(importModule,targetUIName) == True:
                uiClass = getattr(importModule,targetUIName)
                newUI = uiClass()
                newUI.OnLoad(targetUI.GetSceneInstance())
                x,y = targetUI.GetWXY()
                width = targetUI.GetWidth()
                height = targetUI.GetHeight()
                newUI.SetXY(x,y)  
                newUI.SetWidth(width)  
                newUI.SetHeight(height)  
                targetUI.AddChild(newUI)
        except Exception as ex:
            MessageBox(str(ex))

''' 
    f.write(code)


def WriteCallUIDialog_HTML(f):
    code='''
def GoToUIDialog(uiName,targetUIName,params=None):
    """'+Language.G_Language[1343]+'"""
    global G_TargetUIName
    G_TargetUIName = targetUIName
    
def CallUIDialog(targetUIName,topmost = 1,toolwindow = 1,grab_set = 1,wait_window = 1,animation='',params=None):
    """'+Language.G_Language[1297]+'"""

def LoadUIDialog(uiName,elementName,targetUIName,params=None,ignoreSameUI=True):
    """'+Language.G_Language[1345]+'"""

''' 
    f.write(code)
#取得当前界面的所有数据字典
def WriteGetUIDataDictionaryFunction(f):
    code='''
    #f.write(Language.G_Language[1217]+'
def GetUIDataDictionary(uiName):
    """'+Language.G_Language[1217]+'"""
    global G_UIElementDictionary
    global G_UIInputDataArray
    global G_UIElementVariableArray
    if uiName not in G_UIElementDictionary:
        if "UIClass" in G_UIInputDataArray.keys():
            if uiName == G_UIInputDataArray["UIClass"]:
                return G_UIInputDataArray
    else:
        G_UIInputDataArray.clear()
        for elementName in G_UIElementDictionary[uiName].keys():
            Widget = G_UIElementDictionary[uiName][elementName]
            widgetAliasName = elementName
            if uiName in G_UIElementAliasDictionary.keys():
                for aliasName in  G_UIElementAliasDictionary[uiName].keys():
                    if G_UIElementAliasDictionary[uiName][aliasName] == elementName:
                        widgetAliasName = aliasName
                        break
            if elementName == "UIClass":
                G_UIInputDataArray[elementName] = uiName
            else:
                G_UIInputDataArray[widgetAliasName] = ''
            Widget = G_UIElementDictionary[uiName][elementName]
            if elementName.find(\'Label_\') >= 0:
                text = Widget.cget(\'text\')
                G_UIInputDataArray[widgetAliasName] = text  
            elif elementName.find(\'Text_\') >= 0:
                if elementName.find(\'Scroll\') >= 0:
                    continue
                if hasattr(Widget,"GetEntry") == True:
                    Widget = Widget.GetEntry()
                text = Widget.get(\'0.0\', tkinter.END)
                G_UIInputDataArray[widgetAliasName] = text  
            elif elementName.find(\'Entry_\') >= 0:  
                if elementName in  G_UIElementVariableArray[uiName]:  
                    text = G_UIElementVariableArray[uiName][elementName].get()  
                else:  
                    text = Widget.GetText()  
                G_UIInputDataArray[widgetAliasName] = text  
            elif elementName.find(\'RadioButton_\') >= 0 : 
                value = GetTKVariable(uiName,elementName)  
                G_UIInputDataArray[widgetAliasName] = value  
            elif elementName.find(\'CheckButton_\') >= 0 : 
                value = GetTKVariable(uiName,elementName)  
                G_UIInputDataArray[widgetAliasName] = value  
            elif elementName.find(\'Spinbox_\') >= 0:
                text = Widget.get()  
                G_UIInputDataArray[widgetAliasName] = text  
            elif elementName.find(\'ComboBox_\') >= 0:
                text = Widget.get()  
                G_UIInputDataArray[widgetAliasName] = text  
            elif elementName.find(\'Scale_\') >= 0:
                value = Widget.get()  
                G_UIInputDataArray[widgetAliasName] = value  
            elif elementName.find(\'Progress_\') >= 0 : 
                value = Widget["value"]  
                G_UIInputDataArray[widgetAliasName] = value  
            elif elementName.find(\'ListBox_\') >= 0:
                if elementName.find(\'Scroll\') >= 0:
                    continue
                currIndex = Widget.curselection()
                if len(currIndex) > 0 and currIndex[0] >= 0:
                    text = Widget.get(currIndex[0])
                    G_UIInputDataArray[widgetAliasName] = text  
    if uiName in G_UIElementVariableArray:
        for elementName in G_UIElementVariableArray[uiName].keys():  
            if elementName.find(\'Group_\') >= 0:  
                widgetAliasName = elementName
                if uiName in G_UIElementAliasDictionary.keys():
                    for aliasName in  G_UIElementAliasDictionary[uiName].keys():
                        if G_UIElementAliasDictionary[uiName][aliasName] == elementName:
                            widgetAliasName = aliasName
                            break
                ElementIntValue = G_UIElementVariableArray[uiName][elementName].get()  
                G_UIInputDataArray[widgetAliasName] = ElementIntValue  
    return G_UIInputDataArray  
''' 
    f.write(code)
#设置全屏
def WriteCallUIDialog(f):
    code='''
def DestoryChild(frame,destroy=True):
    global G_UIRootIDDictionary
    global G_UIRootSizeDictionary
    if frame:
        for child in frame.winfo_children():
            DestoryChild(child)
    # f.write('            for className in G_UIRootIDDictionary.keys():
    # f.write('                if G_UIRootIDDictionary[className] is child:
    # f.write('                    DestroyUI(className,-1)
    # f.write('                    G_UIRootIDDictionary.pop(className)
    # f.write('                    break
            uiName,elementName = GetElementName(child,False)
            if uiName in G_UIElementDictionary.keys():
                if elementName in G_UIElementDictionary[uiName]:
                    G_UIElementDictionary[uiName].pop(elementName)
            if uiName in G_UIElementPlaceDictionary.keys():
                if elementName in G_UIElementPlaceDictionary[uiName]:
                    G_UIElementPlaceDictionary[uiName].pop(elementName)
            if uiName in G_UIElementAliasDictionary.keys():
                for aliasName in  G_UIElementAliasDictionary[uiName].keys():
                    if G_UIElementAliasDictionary[uiName][aliasName] == elementName:
                        G_UIElementAliasDictionary[uiName].pop(aliasName)
                        break
            if uiName in G_UIElementRoundRectangleDictionary.keys():
                if elementName in G_UIElementRoundRectangleDictionary[uiName]:
                    G_UIElementRoundRectangleDictionary[uiName].pop(elementName)
            if destroy:
                child.destroy()
        for className in G_UIRootIDDictionary.keys():
            if G_UIRootIDDictionary[className] is frame:
                G_UIRootIDDictionary.pop(className)
                G_UIRootSizeDictionary.pop(className)
                G_UIElementDictionary.pop(className)
                G_UICommandDictionary.pop(className)
                G_UIElementAliasDictionary.pop(className)
                G_UIElementPlaceDictionary.pop(className)
                G_UIElementRoundRectangleDictionary.pop(className)
                G_UIGroupDictionary.pop(className)
                G_UIStyleDictionary.pop(className)
                G_CanvasSizeDictionary.pop(className)
                G_CanvasShapeDictionary.pop(className)
                G_CanvasParamDictionary.pop(className)
                G_CanvasFontDictionary.pop(className)
                G_CanvasImageDictionary.pop(className)
                G_CanvasEventDictionary.pop(className)
                G_CanvasPointDictionary.pop(className)
                G_UIElementIconDictionary.pop(className)
                break
def GoToUIDialog(uiName,targetUIName,params=None):
    """'+Language.G_Language[1343]+'"""
    global G_ExeDir
    global G_ResDir
    # f.write("    import tkinter.messagebox
    # f.write("    tkinter.messagebox.showinfo(G_ExeDir,G_ResDir)
    root = GetElement(uiName,\'root\')
    try:
        parentinfo = root.winfo_parent()
        while parentinfo:
            root = root._nametowidget(parentinfo)
            parentinfo = root.winfo_parent()
        for childName in root.children.keys():
            child = root.children[childName]
            DestoryChild(child,False)
            child.pack_forget()
    except:
        try:
            Form1 = GetElement(uiName,\'Form_1\')
            if Form1:
                Form1.pack_forget()
        except:
            pass
    import importlib
    from   importlib import import_module
    try:
        importModule = importlib.import_module("Compile_"+targetUIName)
        importModule = importlib.reload(importModule)
        if hasattr(importModule,"Fun") == True:
            importModule.Fun.G_ExeDir = G_ExeDir
            importModule.Fun.G_ResDir = G_ResDir
            if hasattr(importModule,"EXUIControl") == True:
                importModule.EXUIControl.G_ExeDir = G_ExeDir
                importModule.EXUIControl.G_ResDir = G_ResDir
        if hasattr(importModule,targetUIName) == True:
            uiClass = getattr(importModule,targetUIName)
            if params is None:
                MyDlg = uiClass(root)
            else:
                try:
                    MyDlg = uiClass(root,True,params)
                except Exception as ex:
                    MyDlg = uiClass(root,True)
            if hasattr(importModule,"Fun") == True:
                try :
                    user32 = ctypes.windll.user32
                    sw = user32.GetSystemMetrics(0)
                    sh = user32.GetSystemMetrics(1)
                    zw,zh = MyDlg.GetRootSize()
                    zx = int((sw-zw)/2) 
                    zy = int((sh-zh)/2)
                    root.geometry('%dx%d+%d+%d'%(zw,zh,zx,zy))
                except ImportError:
                    pass
    except ModuleNotFoundError:
        try:
            importModule = importlib.import_module(targetUIName)
            importModule = importlib.reload(importModule)
            if hasattr(importModule,"Fun") == True:
                importModule.Fun.G_ExeDir = G_ExeDir
                importModule.Fun.G_ResDir = G_ResDir
                if hasattr(importModule,"EXUIControl") == True:
                    importModule.EXUIControl.G_ExeDir = G_ExeDir
                    importModule.EXUIControl.G_ResDir = G_ResDir
            if hasattr(importModule,targetUIName) == True:
                uiClass = getattr(importModule,targetUIName)
                if params is None:
                    MyDlg = uiClass(root)
                else:
                    try:
                        MyDlg = uiClass(root,True,params)
                    except Exception as ex:
                        MyDlg = uiClass(root,True)
                if hasattr(importModule,"Fun") == True:
                    try :
                        user32 = ctypes.windll.user32
                        sw = user32.GetSystemMetrics(0)
                        sh = user32.GetSystemMetrics(1)
                        zw,zh = MyDlg.GetRootSize()
                        zx = int((sw-zw)/2) 
                        zy = int((sh-zh)/2)
                        root.geometry('%dx%d+%d+%d'%(zw,zh,zx,zy))
                    except ImportError:
                        pass
        except Exception as ex:
            MessageBox(str(ex))
    except Exception as ex:
        MessageBox(str(ex))
def PlayCallUIDialogAction(topLevel,uiInstance,animation='zoomin'):
    def FadeIn(topLevel,uiInstance,alpha):
        try :
            hwnd = windll.user32.GetParent(topLevel.winfo_id())
            _winlib = ctypes.windll.user32
            style = _winlib.GetWindowLongA( hwnd, 0xffffffec ) | 0x00080000
            _winlib.SetWindowLongA( hwnd, 0xffffffec, style )
            _winlib.SetLayeredWindowAttributes( hwnd, 0, alpha+1, 2 )
            alpha = alpha + 1
        except ImportError:
            pass
        if alpha < 255:
            topLevel.after(1,lambda:FadeIn(topLevel = topLevel,uiInstance = uiInstance,alpha = alpha))
        else:
            print("结束")
    def ZoomIn(topLevel,uiInstance,zoom,width,height):
        try :
            user32 = ctypes.windll.user32
            sw = user32.GetSystemMetrics(0)
            sh = user32.GetSystemMetrics(1)
            zw = int(width * zoom)
            zh = int(height * zoom)
            zx = int((sw-zw)/2) 
            zy = int((sh-zh)/2)
            topLevel.geometry('%dx%d+%d+%d'%(zw,zh,zx,zy))
            zoom = zoom + 0.01
        except ImportError:
            pass
        if zoom < 1.0:
            topLevel.after(1,lambda:ZoomIn(topLevel = topLevel,uiInstance = uiInstance,zoom = zoom ,width=width,height=height))
        else:
            print("结束")
    animation = animation.lower()
    if animation == "fadein":
        try :
            hwnd = windll.user32.GetParent(topLevel.winfo_id())
            _winlib = ctypes.windll.user32
            style = _winlib.GetWindowLongA( hwnd, 0xffffffec ) | 0x00080000
            _winlib.SetWindowLongA( hwnd, 0xffffffec, style )
            _winlib.SetLayeredWindowAttributes( hwnd, 0, 0, 2 )
            topLevel.deiconify()
            topLevel.after(1,lambda:FadeIn(topLevel = topLevel,uiInstance = uiInstance,alpha = 0))
        except ImportError:
            pass
    elif animation == "zoomin":
        try :
            sw = windll.user32.GetSystemMetrics(0)
            sh = windll.user32.GetSystemMetrics(1)
            topLevel.geometry('%dx%d+%d+%d'%(0,0,int(sw/2),int(sh/2)))
            form1_width,form1_height = uiInstance.GetRootSize()
            topLevel.deiconify()
            topLevel.after(1,lambda:ZoomIn(topLevel = topLevel,uiInstance = uiInstance,zoom = 0.0,width=form1_width,height=form1_height))
        except ImportError:
            pass
def CallUIDialog(uiName,topmost = 1,toolwindow = 1,grab_set = 1,wait_window = 1,animation='',params=None):
    """'+Language.G_Language[1297]+'"""
    global G_ExeDir
    global G_ResDir
    global G_TopDialog
    """'+Language.G_Language[9365]+'"""
    if isinstance(wait_window,str) == True and params is None:
        params = animation
        animation = wait_window
        wait_window = 1
    import importlib
    from   importlib import import_module
    try:
        importModule = importlib.import_module("Compile_"+uiName)
        importModule = importlib.reload(importModule)
        if hasattr(importModule,"Fun") == True:
            importModule.Fun.G_ExeDir = G_ExeDir
            importModule.Fun.G_ResDir = G_ResDir
            if hasattr(importModule,"EXUIControl") == True:
                importModule.EXUIControl.G_ExeDir = G_ExeDir
                importModule.EXUIControl.G_ResDir = G_ResDir
        if hasattr(importModule,uiName) == True and hasattr(importModule,"Fun") == True :
            uiClass = getattr(importModule,uiName)
            funClass = getattr(importModule,"Fun")
            topLevel = tkinter.Toplevel()
            topLevel.withdraw()
            topLevel.attributes("-toolwindow", toolwindow)
            topLevel.wm_attributes("-topmost", topmost)
            G_TopDialog = topLevel
            if grab_set == 1:
                topLevel.grab_set()
            if params is None:
                uiInstance = uiClass(topLevel,True)
            else:
                try:
                    uiInstance = uiClass(topLevel,True,params)
                except Exception as ex:
                    uiInstance = uiClass(topLevel,True)
            if topLevel.winfo_exists() == False:
                return funClass.G_UIInputDataArray
            try:
                if topmost == 0:
                    topLevel.wm_attributes("-topmost", 0)
                if hasattr(uiInstance,"uiName") == True:
                    uiName = uiInstance.uiName
                def CloseWindow():
                    funClass.GetUIDataDictionary(uiName)
                    DestroyUI(uiName)
                    topLevel.destroy()
                topLevel.protocol('WM_DELETE_WINDOW', CloseWindow)
                if animation !='':
                    PlayCallUIDialogAction(topLevel,uiInstance,animation)
                else:
                    topLevel.deiconify()
                dialog_w,dialog_h = uiInstance.GetRootSize()
                CenterDlg(uiName,topLevel,dialog_w,dialog_h)
                if wait_window == 1:
                    tkinter.Tk.wait_window(topLevel)
                    G_TopDialog = None
            except Exception as ex:
                print(uiName+"被销毁，不再弹出窗口")
            return funClass.G_UIInputDataArray
    except ModuleNotFoundError:
        try:
            importModule = importlib.import_module(uiName)
            importModule = importlib.reload(importModule)
            if hasattr(importModule,"Fun") == True:
                importModule.Fun.G_ExeDir = G_ExeDir
                importModule.Fun.G_ResDir = G_ResDir
                if hasattr(importModule,"EXUIControl") == True:
                    importModule.EXUIControl.G_ExeDir = G_ExeDir
                    importModule.EXUIControl.G_ResDir = G_ResDir
            if hasattr(importModule,uiName) == True and hasattr(importModule,"Fun") == True :
                uiClass = getattr(importModule,uiName)
                funClass = getattr(importModule,"Fun")
                topLevel = tkinter.Toplevel()
                topLevel.withdraw()
                topLevel.attributes("-toolwindow", toolwindow)
                topLevel.wm_attributes("-topmost", topmost)
                G_TopDialog = topLevel
                if grab_set == 1:
                    topLevel.grab_set()
                if params is None:
                    uiInstance = uiClass(topLevel,True)
                else:
                    try:
                       uiInstance = uiClass(topLevel,True,params)
                    except Exception as ex:
                       uiInstance = uiClass(topLevel,True)
                if hasattr(uiInstance,"uiName") == True:
                    uiName = uiInstance.uiName
                if topLevel.winfo_exists() == False:
                    return funClass.G_UIInputDataArray
                try:
                    if topmost == 0:
                        topLevel.wm_attributes("-topmost", 0)
                    def CloseWindow():
                        funClass.GetUIDataDictionary(uiName)
                        DestroyUI(uiName)
                        topLevel.destroy()
                    topLevel.protocol('WM_DELETE_WINDOW',CloseWindow)
                    if animation !='':
                        PlayCallUIDialogAction(topLevel,uiInstance,animation)
                    else:
                        topLevel.deiconify()
                    dialog_w,dialog_h = uiInstance.GetRootSize()
                    CenterDlg(uiName,topLevel,dialog_w,dialog_h)
                    if wait_window == 1:
                        tkinter.Tk.wait_window(topLevel)
                        G_TopDialog = None
                except Exception as ex:
                    print(uiName+"被销毁，不再弹出窗口")
                return funClass.G_UIInputDataArray
        except Exception as ex:
            ErrorText = str(ex)
            if ErrorText.find("application has been destroyed") != -1:
                return None
            MessageBox(ErrorText)
    except Exception as ex:
        ErrorText = str(ex)
        if ErrorText.find("application has been destroyed") != -1:
            return None
        MessageBox(ErrorText)
    return None
def LoadUIDialog(uiName,elementName,targetUIName,params=None,ignoreSameUI=True):
    """'+Language.G_Language[1345]+'"""
    global G_ExeDir
    global G_UIElementAliasDictionary
    def OnFrameConfigure(event,targetUIName):
        ReDrawCanvasRecord(targetUIName,True)
    currUIDialog = GetUserData(uiName,elementName,"CurrUI")
    lastLoadTime = GetUserData(uiName,elementName,"LoadTime")
    if currUIDialog is None:
        AddUserData(uiName,elementName,"CurrUI","string",targetUIName,0)
        AddUserData(uiName,elementName,"LoadTime","long",time.time())
    else:
        if currUIDialog == targetUIName and ignoreSameUI == True:
            print("'+Language.G_Language[3109]+'"+":"+targetUIName)
            return 
    # f.write('            currLoadTime = time.time()
    # f.write('            if  (currLoadTime - lastLoadTime) < 1:
    # f.write('                print("'+Language.G_Language[3109]+'"+":"+targetUIName)
    # f.write('                return 
        SetUserData(uiName,elementName,"CurrUI",targetUIName)
        SetUserData(uiName,elementName,"LoadTime",time.time())
    print("LoadUIDialog %s,%s => %s"%(uiName,elementName,targetUIName))
    Root = GetElement(uiName,\'root\')
    ParentFrame = GetElement(uiName,elementName)
    if uiName in G_UIElementAliasDictionary.keys() and elementName in  G_UIElementAliasDictionary[uiName].keys():
        realName = G_UIElementAliasDictionary[uiName][elementName]
        ParentFrame_Child = GetElement(uiName,realName+"_Child")
    else:
        ParentFrame_Child = GetElement(uiName,elementName+"_Child")
    if ParentFrame_Child:
        ParentFrame = ParentFrame_Child
    DestoryChild(ParentFrame)
    import importlib
    from   importlib import import_module
    try:
        UIPath, UIFile = os.path.split(targetUIName)
        if UIPath.find(":") < 0:
            UIPath = os.path.join(G_ExeDir,UIPath)
        UIName, extension = os.path.splitext(UIFile)
        import sys
        sys.path.append(UIPath)
        importModule = importlib.import_module(UIName)
        importModule = importlib.reload(importModule)
        if hasattr(importModule,"Fun") == True:
            importModule.Fun.G_ExeDir = G_ExeDir
            importModule.Fun.G_ResDir = G_ResDir
            if hasattr(importModule,"EXUIControl") == True:
                importModule.EXUIControl.G_ExeDir = G_ExeDir
                importModule.EXUIControl.G_ResDir = G_ResDir
        if hasattr(importModule,UIName) == True:
            uiClass = getattr(importModule,UIName)
            if params is None:
                uiDialog = uiClass(ParentFrame,False)
            else:
                try:
                    uiDialog = uiClass(ParentFrame,False,params)
                except Exception as ex:
                    uiDialog = uiClass(ParentFrame,False)
            UIName = uiDialog.uiName
            if ParentFrame_Child:
                uiDialogWidth = uiDialog.root.winfo_width()
                uiDialogHeight = uiDialog.root.winfo_height()
                uiDialogForm1 = None
                ChildWidgetList = uiDialog.root.children
                for widgetName in ChildWidgetList.keys():
                    uiDialogForm1  = ChildWidgetList[widgetName]
                    ChildHandle = ParentFrame.create_window(0,0, window=uiDialogForm1, anchor=tkinter.NW,tag="Form_1")
                    ParentFrame.itemconfig(ChildHandle,width=uiDialogWidth,height=uiDialogHeight)
            uiDialog.root = Root
    # f.write('            FunLib = getattr(importModule,"Fun")
    # f.write('            if FunLib:
    # f.write('                FunLib.G_UIElementDictionary[UIName][\'root\'] = Root
            G_UIElementDictionary[UIName][\'root\'] = Root
            OnFrameConfigure(None,UIName)
            ParentFrame.bind('<Configure>',EventFunction_Adaptor(OnFrameConfigure,targetUIName = UIName))
            return uiDialog
    except ModuleNotFoundError:
        try:
            UIPath, UIFile = os.path.split(targetUIName)
            if UIPath.find(":") < 0:
                UIPath = os.path.join(G_ExeDir,UIPath)
            UIName, extension = os.path.splitext(UIFile)
            import sys
            sys.path.append(UIPath)
            importModule = importlib.import_module("Compile_"+UIName)
            importModule = importlib.reload(importModule)
            if hasattr(importModule,"Fun") == True:
                importModule.Fun.G_ExeDir = G_ExeDir
                importModule.Fun.G_ResDir = G_ResDir
                if hasattr(importModule,"EXUIControl") == True:
                    importModule.EXUIControl.G_ExeDir = G_ExeDir
                    importModule.EXUIControl.G_ResDir = G_ResDir
            if hasattr(importModule,UIName) == True:
                uiClass = getattr(importModule,UIName)
                if params is None:
                    uiDialog = uiClass(ParentFrame,False)
                else:
                    try:
                        uiDialog = uiClass(ParentFrame,False,params)
                    except Exception as ex:
                        uiDialog = uiClass(ParentFrame,False)
                UIName = uiDialog.uiName
                if ParentFrame_Child:
                    uiDialogWidth = uiDialog.root.winfo_width()
                    uiDialogHeight = uiDialog.root.winfo_height()
                    uiDialogForm1 = None
                    ChildWidgetList = uiDialog.root.children
                    for widgetName in ChildWidgetList.keys():
                        uiDialogForm1  = ChildWidgetList[widgetName]
                        ChildHandle = ParentFrame.create_window(0,0, window=uiDialogForm1, anchor=tkinter.NW,tag="Form_1")
                        ParentFrame.itemconfig(ChildHandle,width=uiDialogWidth,height=uiDialogHeight)
                uiDialog.root = Root
    # f.write('                FunLib = getattr(importModule,"Fun")
    # f.write('                if FunLib:
    # f.write('                    FunLib.G_UIElementDictionary[UIName][\'root\'] = Root
                G_UIElementDictionary[UIName][\'root\'] = Root
                OnFrameConfigure(None,UIName)
                ParentFrame.bind('<Configure>',EventFunction_Adaptor(OnFrameConfigure,targetUIName = UIName))
                return uiDialog
    # f.write('        except Exception as ex:
    # f.write('            MessageBox(str(ex))
        except Exception as ex:
            except_type, except_value, except_traceback = sys.exc_info()
            except_value_str = str(except_value)
            except_stack_end = except_traceback.tb_frame
            except_stack_next = except_traceback.tb_next
            except_stack_lineno = except_traceback.tb_lineno
            while except_stack_next:
                except_stack_end = except_stack_next.tb_frame
                except_stack_lineno = except_stack_next.tb_lineno
                except_stack_next = except_stack_next.tb_next
            except_file = os.path.split(except_stack_end.f_code.co_filename)[1]
            MessageBox("'+Language.G_Language[9517]+'：%s\\n'+Language.G_Language[51]+'：%s\\n'+Language.G_Language[3322]+'：%s" % (except_value_str, except_file, except_stack_lineno),"'+Language.G_Language[9518]+'")
    #f.write('            MessageBox(str(ex))
    except Exception as ex:
        except_type, except_value, except_traceback = sys.exc_info()
        except_value_str = str(except_value)
        except_stack_end = except_traceback.tb_frame
        except_stack_next = except_traceback.tb_next
        except_stack_lineno = except_traceback.tb_lineno
        while except_stack_next:
            except_stack_end = except_stack_next.tb_frame
            except_stack_lineno = except_stack_next.tb_lineno
            except_stack_next = except_stack_next.tb_next
        except_file = os.path.split(except_stack_end.f_code.co_filename)[1]
        MessageBox("'+Language.G_Language[9517]+'：%s\\n'+Language.G_Language[51]+'：%s\\n'+Language.G_Language[3322]+'：%s" % (except_value_str, except_file, except_stack_lineno),"'+Language.G_Language[9518]+'")
        MessageBox(str(ex))
def SetChildFrameScrollRegion(uiName,elementName,width,height):
    """'+Language.G_Language[9335]+'"""
    Frame_ChildName = elementName + "_Child"
    Frame_Child = GetElement(uiName,Frame_ChildName)
    UIChildren = Frame_Child.winfo_children()
    if len(UIChildren) > 0:
        Form_1 = UIChildren[0]
        Frame_ChildHandle = Frame_Child.create_window(0,0, window=Form_1, anchor=tkinter.NW,tag="Form_1")
        Frame_Child.itemconfig(Frame_ChildHandle,width=width,height=height)
        Frame_Child.config(scrollregion=(0,0,width,height))
    # f.write('        def  Resize_Frame(event):
    # f.write('            realWidth = width
    # f.write('            if isinstance(realWidth,float) == True:
    # f.write('                realWidth = int(width*event.width)
    # f.write('            realHeight = height
    # f.write('            if isinstance(realHeight,float) == True:
    # f.write('                realHeight = int(height*event.height)
    # f.write('            event.widget.config(scrollregion=(0,0,event,event))
    # f.write('        Frame_Child.bind(\'<Configure>\',Resize_Frame)
def AddUIDialog(uiName,elementName,targetUIName,x,y,params=None):
    """在指定控件上加载一个界面"""
    global G_ExeDir
    global G_UIElementAliasDictionary
    def OnFrameConfigure(event,targetUIName):
        ReDrawCanvasRecord(targetUIName,True)
    print("AddUIDialog %s,%s => %s"%(uiName,elementName,targetUIName))
    Root = GetElement(uiName,'root')
    ParentFrame = GetElement(uiName,elementName)
    ChildName = elementName+"_Child"
    HScrollName = elementName+"_HScrollbar"
    VScrollName = elementName+"_VScrollbar"
    if uiName in G_UIElementAliasDictionary.keys() and elementName in  G_UIElementAliasDictionary[uiName].keys():
        ChildName = G_UIElementAliasDictionary[uiName][elementName]+"_Child"
        HScrollName = G_UIElementAliasDictionary[uiName][elementName]+"_HScrollbar"
        VScrollName = G_UIElementAliasDictionary[uiName][elementName]+"_VScrollbar"
        ParentFrame_Child = GetElement(uiName,ChildName)
    else:
        ParentFrame_Child = GetElement(uiName,elementName+"_Child")
    if ParentFrame_Child:
        ParentFrame = ParentFrame_Child
    else:
        ParentFrame_Child = tkinter.Canvas(ParentFrame,bg=ParentFrame.cget('bg'))
        ParentFrame_Child.place(x=x,y=y,width=ParentFrame.winfo_width()-30,height=ParentFrame.winfo_height())
        Register(uiName,ChildName,ParentFrame_Child)
        AddUserData(uiName,ChildName,"scrollregion","list",[0,0,0,0],0)
        ParentFrame = ParentFrame_Child
        HScrollbar = GetElement(uiName,HScrollName)
        if HScrollbar:
            HScrollbar.config(command = ParentFrame.xview)
            ParentFrame.config(yscrollcommand=HScrollbar.set)
        VScrollbar = GetElement(uiName,VScrollName)
        if VScrollbar:
            VScrollbar.config(command = ParentFrame.yview)
            ParentFrame.config(yscrollcommand=VScrollbar.set)
    import importlib
    from   importlib import import_module
    try:
        UIPath, UIFile = os.path.split(targetUIName)
        if UIPath.find(":") < 0:
            UIPath = os.path.join(G_ExeDir,UIPath)
        UIName, extension = os.path.splitext(UIFile)
        import sys
        sys.path.append(UIPath)
        importModule = importlib.import_module(UIName)
        importModule = importlib.reload(importModule)
        if hasattr(importModule,"Fun") == True:
            importModule.Fun.G_ExeDir = G_ExeDir
            importModule.Fun.G_ResDir = G_ResDir
            if hasattr(importModule,"EXUIControl") == True:
                importModule.EXUIControl.G_ExeDir = G_ExeDir
                importModule.EXUIControl.G_ResDir = G_ResDir
        if hasattr(importModule,UIName) == True:
            uiClass = getattr(importModule,UIName)
            if params is None:
                uiDialog = uiClass(ParentFrame,False)
            else:
                try:
                    uiDialog = uiClass(ParentFrame,False,params)
                except Exception as ex:
                    uiDialog = uiClass(ParentFrame,False)
            UIName = uiDialog.uiName
            scrollregion_info = GetUserData(uiName,ChildName,"scrollregion")
            scrollregion_width = scrollregion_info[2]
            scrollregion_height = scrollregion_info[3]
            if ParentFrame_Child:
                if hasattr(uiDialog,"GetRootSize") == True:
                    uiDialogWidth,uiDialogHeight = uiDialog.GetRootSize()
                    ChildWidgetList = uiDialog.GetAllElement()
                    if 'Form_1' in ChildWidgetList.keys():
                        uiDialogForm1  = ChildWidgetList['Form_1']
                        ChildHandle = ParentFrame.create_window(x,y, window=uiDialogForm1, anchor=tkinter.NW,tag="Form_1")
                        ParentFrame.itemconfig(ChildHandle,width=uiDialogWidth,height=uiDialogHeight)
                if (x + uiDialogWidth) > scrollregion_width:
                    scrollregion_width = (x + uiDialogWidth) 
                if (y + uiDialogHeight) > scrollregion_height:
                    scrollregion_height = (y + uiDialogHeight) 
            uiDialog.root = Root
            G_UIElementDictionary[UIName]['root'] = Root
            OnFrameConfigure(None,UIName)
            ParentFrame.bind('<Configure>',EventFunction_Adaptor(OnFrameConfigure,targetUIName = UIName))
            ParentFrame.config(scrollregion=(0,0,scrollregion_width,scrollregion_height))
            SetUserData(uiName,ChildName,"scrollregion",[0,0,scrollregion_width,scrollregion_height])
            ParentFrame.update()
            return uiDialog
    except ModuleNotFoundError:
        try:
            UIPath, UIFile = os.path.split(targetUIName)
            if UIPath.find(":") < 0:
                UIPath = os.path.join(G_ExeDir,UIPath)
            UIName, extension = os.path.splitext(UIFile)
            import sys
            sys.path.append(UIPath)
            importModule = importlib.import_module("Compile_"+UIName)
            importModule = importlib.reload(importModule)
            if hasattr(importModule,"Fun") == True:
                importModule.Fun.G_ExeDir = G_ExeDir
                importModule.Fun.G_ResDir = G_ResDir
                if hasattr(importModule,"EXUIControl") == True:
                    importModule.EXUIControl.G_ExeDir = G_ExeDir
                    importModule.EXUIControl.G_ResDir = G_ResDir
            if hasattr(importModule,UIName) == True:
                uiClass = getattr(importModule,UIName)
                if params is None:
                    uiDialog = uiClass(ParentFrame,False)
                else:
                    try:
                        uiDialog = uiClass(ParentFrame,False,params)
                    except Exception as ex:
                        uiDialog = uiClass(ParentFrame,False)
                UIName = uiDialog.uiName
                scrollregion_info = GetUserData(uiName,ChildName,"scrollregion")
                scrollregion_width = scrollregion_info[2]
                scrollregion_height = scrollregion_info[3]
                if ParentFrame_Child:
                    if hasattr(uiDialog,"GetRootSize") == True:
                        uiDialogWidth,uiDialogHeight = uiDialog.GetRootSize()
                        ChildWidgetList = uiDialog.GetAllElement()
                        if 'Form_1' in ChildWidgetList.keys():
                            uiDialogForm1  = ChildWidgetList['Form_1']
                            ChildHandle = ParentFrame.create_window(x,y, window=uiDialogForm1, anchor=tkinter.NW,tag="Form_1")
                            ParentFrame.itemconfig(ChildHandle,width=uiDialogWidth,height=uiDialogHeight)
                    if (x + uiDialogWidth) > scrollregion_width:
                        scrollregion_width = (x + uiDialogWidth) 
                    if (y + uiDialogHeight) > scrollregion_height:
                        scrollregion_height = (y + uiDialogHeight) 
                uiDialog.root = Root
                G_UIElementDictionary[UIName]['root'] = Root
                OnFrameConfigure(None,UIName)
                ParentFrame.bind('<Configure>',EventFunction_Adaptor(OnFrameConfigure,targetUIName = UIName))
                ParentFrame.config(scrollregion=(0,0,scrollregion_width,scrollregion_height))
                SetUserData(uiName,ChildName,"scrollregion",[0,0,scrollregion_width,scrollregion_height])
                ParentFrame.update()
                return uiDialog
        except Exception as ex:
            except_type, except_value, except_traceback = sys.exc_info()
            except_value_str = str(except_value)
            except_stack_end = except_traceback.tb_frame
            except_stack_next = except_traceback.tb_next
            except_stack_lineno = except_traceback.tb_lineno
            while except_stack_next:
                except_stack_end = except_stack_next.tb_frame
                except_stack_lineno = except_stack_next.tb_lineno
                except_stack_next = except_stack_next.tb_next
            except_file = os.path.split(except_stack_end.f_code.co_filename)[1]
            MessageBox("错误信息：：%s\\n文件：%s\\n行号：%s" % (except_value_str, except_file, except_stack_lineno),"运行错误")
    #f.write('            MessageBox(ex)
    except Exception as ex:
        except_type, except_value, except_traceback = sys.exc_info()
        except_value_str = str(except_value)
        except_stack_end = except_traceback.tb_frame
        except_stack_next = except_traceback.tb_next
        except_stack_lineno = except_traceback.tb_lineno
        while except_stack_next:
            except_stack_end = except_stack_next.tb_frame
            except_stack_lineno = except_stack_next.tb_lineno
            except_stack_next = except_stack_next.tb_next
        except_file = os.path.split(except_stack_end.f_code.co_filename)[1]
        MessageBox("错误信息：：%s\\n文件：%s\\n行号：%s" % (except_value_str, except_file, except_stack_lineno),"运行错误")
    #f.write('        MessageBox(ex)


''' 
    f.write(code)
#设置全屏
def WriteShowWindowFunction(f):
    code='''
def ShowWindow(uiName,WindowState):
    """'+Language.G_Language[1294]+'"""
    root = GetElement(uiName,'root')
    hwnd = windll.user32.GetParent(root.winfo_id())  
    win32gui.ShowWindow(hwnd,WindowState)
def SetWindowTitle(uiName,title=""):
    """'+Language.G_Language[1488]+'"""
    root = GetElement(uiName,'root')
    root.title(title)
def SetWindowIco(uiName,imageFile=""):
    """'+Language.G_Language[1489]+'"""
    imageFile_noExt,extension = os.path.splitext(imageFile)
    root = GetElement(uiName,'root')
    if extension == '.ico':
        root.iconbitmap(imageFile)
    else:
        import base64
        open_icon = open(imageFile,"rb")
        open_icon_base64 = base64.b64encode(open_icon.read())
        icoFileName = imageFile_noExt+".ico"
        tmp = open(icoFileName,"wb+")
        tmp.write(open_icon_base64)
        tmp.close()
        img = Image.open(icoFileName)
        img.save(icoFileName)
        root.iconbitmap(icoFileName)
        os.remove(icoFileName)
g_ToolBar_lastX = 0
g_ToolBar_lastY = 0
def SetToolBar(root,uiFileName):
    """'+Language.G_Language[1109]+'"""
    try:
        if uiFileName.find(".py") >= 0:
            pathName,fileName = os.path.split(uiFileName)
            sys.path.insert(0,pathName)
            importSplitArray = fileName.partition('.py')
            uiClass = importSplitArray[0]
        else:
            uiClass = uiFileName
        import importlib
        from   importlib import import_module
        importModule = importlib.import_module(uiClass)
        importModule = importlib.reload(importModule)
        newClass = getattr(importModule, uiClass)
        if newClass:
            def ButtonDown_ToolBar(event):
                global g_ToolBar_lastX
                global g_ToolBar_lastY
                g_ToolBar_lastX = event.x_root
                g_ToolBar_lastY = event.y_root
            def ButtonMotion_ToolBar(event):
                global g_ToolBar_lastX
                global g_ToolBar_lastY
                offsetX = event.x_root - g_ToolBar_lastX
                offsetY = event.y_root - g_ToolBar_lastY
                root_x = root.winfo_x()
                root_y = root.winfo_y()
                root_w = root.winfo_width()
                root_h = root.winfo_height()
                if offsetX != 0 or offsetY != 0:
                    root.geometry('%dx%d+%d+%d'%(root_w,root_h,root_x+offsetX,root_y+offsetY))
                g_ToolBar_lastX = event.x_root
                g_ToolBar_lastY = event.y_root
            def ButtonUp_ToolBar(event):
                pass
            newClassInstance = newClass(root,False)
            ChildWidgetList = newClassInstance.GetAllElement()
            for widgetName in ChildWidgetList.keys():
                if widgetName == 'UIClass':
                    continue
                if widgetName == 'root':
                    continue
                ChildWidget = ChildWidgetList[widgetName]
                if widgetName == 'Form_1':
                    ChildWidget.pack(side=tkinter.TOP,fill=tkinter.X)
                if hasattr(ChildWidget,'GetWidget') == True:
                    ChildWidget = ChildWidget.GetWidget()
                bindList = ChildWidget.bind()
                if widgetName.find('Entry_') >= 0:
                    continue
                if widgetName.find('Text_') >= 0:
                    continue
                if widgetName.find('Button_') >= 0:
                    continue
                if '<Button-1>' not in bindList and '<B1-Motion>' not in bindList and '<ButtonRelease-1>' not in bindList:
                    ChildWidget.bind('<Button-1>',ButtonDown_ToolBar)
                    ChildWidget.bind('<B1-Motion>',ButtonMotion_ToolBar)
                    ChildWidget.bind('<ButtonRelease-1>',ButtonUp_ToolBar)
    except Exception as ex:
        print(ex)

''' 
    f.write(code)
#设置居中
def WriteCenterDlgFunction(f):
    code='''
    #f.write(Language.G_Language[1218]+'
def CenterDlg(uiName,popupDlg,dw=0,dh=0,keepHide=False,popui_xy=\'Center\'):
    """'+Language.G_Language[1218]+'"""
    global g_TKScaling
    global G_LaunchDlg
    global G_UIRootStateDictionary
    if dw == 0:
        dw = popupDlg.winfo_width()
    if dh == 0:
        dh = popupDlg.winfo_height()
    root = GetElement(uiName,\'root\')
    if root != None and popupDlg != root:
        sw = root.winfo_width()
        sh = root.winfo_height()
        sx = root.winfo_x()
        sy = root.winfo_y()
        if popui_xy == \'Center\':
            x = int(sx+(sw-dw)/2)
            if x < 0:
                x = 0
            y = int(sy+(sh-dh)/2)
            if y < 0:
                y = 0
        else:
            x = popui_xy[0]
            y = popui_xy[1]
        popupDlg.geometry(\'%dx%d+%d+%d\'%(dw,dh,x,y))
        popupDlg.update()
        if keepHide == False:
            popupDlg.deiconify()
            G_UIRootStateDictionary[uiName] = 'deiconify'
    else:
        user32 = ctypes.windll.user32
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
    #f.write('            ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
        except:
            ctypes.windll.user32.SetProcessDPIAware()
        sw = user32.GetSystemMetrics(0)
        sh = user32.GetSystemMetrics(1)
        sx = 0
        sy = 0
        if popui_xy == \'Center\':
            x = int(sx+(sw-dw)/2)
            if x < 0:
                x = 0
            y = int(sy+(sh-dh)/2)
            if y < 0:
                y = 0
        else:
            x = popui_xy[0]
            y = popui_xy[1]
        popupDlg.tk.call('tk', 'scaling',g_TKScaling)
        popupDlg.geometry(\'%dx%d+%d+%d\'%(dw,dh,x,y))
        popupDlg.update()
        if keepHide == False:
            popupDlg.deiconify()
            G_UIRootStateDictionary[uiName] = 'deiconify'
        from win32gui import GetParent, SetWindowPos, UpdateWindow, SetWindowLong, GetWindowLong, ReleaseCapture, SendMessage
        from win32con import NULL, SWP_NOSIZE, SWP_NOMOVE, SWP_NOZORDER, SWP_DRAWFRAME, GWL_STYLE, WS_CAPTION, WM_SYSCOMMAND, SC_MOVE, HTCAPTION, WS_THICKFRAME
        WindowHandle = ctypes.windll.user32.GetParent(popupDlg.winfo_id())    
        SetWindowPos(WindowHandle, NULL, x, y, dw, dh, SWP_DRAWFRAME|SWP_NOSIZE|SWP_NOZORDER)
        UpdateWindow(WindowHandle)
        if G_LaunchDlg is None:
            popupDlg.attributes(\'-topmost\', 1)
            popupDlg.attributes(\'-topmost\', 0)
            G_LaunchDlg = popupDlg
def SetUIDialogXYWH(uiName,x,y,width,height):
    """'+Language.G_Language[9504]+'"""
    root = GetElement(uiName,'root')
    if 'root' not in G_UIElementPlaceDictionary[uiName]:
        G_UIElementPlaceDictionary[uiName]['root'] = {}
    G_UIElementPlaceDictionary[uiName]['root']['x'] = x
    G_UIElementPlaceDictionary[uiName]['root']['y'] = y
    G_UIElementPlaceDictionary[uiName]['root']['width'] = width
    G_UIElementPlaceDictionary[uiName]['root']['height'] = height
    while root.master:
        root = root._nametowidget(root.winfo_parent())
    root.geometry('%dx%d+%d+%d'%(width,height,x,y))
    root.update()
def SetUIDialogXY(uiName,x,y):
    """'+Language.G_Language[9505]+'"""
    root = GetElement(uiName,'root')
    if 'root' not in G_UIElementPlaceDictionary[uiName]:
        G_UIElementPlaceDictionary[uiName]['root'] = {}
    G_UIElementPlaceDictionary[uiName]['root']['x'] = x
    G_UIElementPlaceDictionary[uiName]['root']['y'] = y
    while root.master:
        root = root._nametowidget(root.winfo_parent())
    root.geometry('%d+%d'%(x,y))
def SetUIDialogWH(uiName,width,height):
    """'+Language.G_Language[9506]+'"""
    root = GetElement(uiName,'root')
    if 'root' not in G_UIElementPlaceDictionary[uiName]:
        G_UIElementPlaceDictionary[uiName]['root'] = {}
    G_UIElementPlaceDictionary[uiName]['root']['width'] = width
    G_UIElementPlaceDictionary[uiName]['root']['height'] = height
    while root.master:
        root = root._nametowidget(root.winfo_parent())
    root.geometry('%dx%d'%(width,height))
    root.update()
def MaximizeUI(uiName):
    """'+Language.G_Language[1319]+'"""
    root = GetElement(uiName,'root')
    if 'root' not in G_UIElementPlaceDictionary[uiName]:
        G_UIElementPlaceDictionary[uiName]['root'] = {}
    G_UIElementPlaceDictionary[uiName]['root']['x'] = root.winfo_x()
    G_UIElementPlaceDictionary[uiName]['root']['y'] = root.winfo_y()
    G_UIElementPlaceDictionary[uiName]['root']['width'] = root.winfo_width()
    G_UIElementPlaceDictionary[uiName]['root']['height'] = root.winfo_height()
    user32 = ctypes.windll.user32
    sw = user32.GetSystemMetrics(0)
    sh = user32.GetSystemMetrics(1)
    while root.master:
        root = root._nametowidget(root.winfo_parent())
    root.geometry('%dx%d+%d+%d'%(sw,sh,0,0))
    root.update()
    ReDrawCanvasRecord(uiName,True)
def MinimizeUI(uiName):
    """'+Language.G_Language[1321]+'"""
    
    root = GetElement(uiName,'root')
    hwnd = windll.user32.GetParent(root.winfo_id())  
    win32gui.ShowWindow(hwnd,2)
def RestoreUI(uiName):
    """'+Language.G_Language[1320]+'"""
    global G_TKRoot
    global G_UIRootStateDictionary
    root = GetElement(uiName,'root')
    if 'root' in G_UIElementPlaceDictionary[uiName]:
        hwnd = windll.user32.GetParent(root.winfo_id())
        win32gui.ShowWindow(hwnd,1)
        root.geometry('%dx%d+%d+%d'%(G_UIElementPlaceDictionary[uiName]['root']['width'],G_UIElementPlaceDictionary[uiName]['root']['height'],G_UIElementPlaceDictionary[uiName]['root']['x'],G_UIElementPlaceDictionary[uiName]['root']['y']))
    else:
        hwnd = windll.user32.GetParent(root.winfo_id())
        state = 'normal'
        if uiName in G_UIRootStateDictionary.keys():
            state = G_UIRootStateDictionary[uiName]
        if state == \"iconic\":
            win32gui.ShowWindow(hwnd,2)
        elif state == \"zoomed\":
            win32gui.ShowWindow(hwnd,3)
        else:
            win32gui.ShowWindow(hwnd,1)
        root.update()

def HideUI(uiName):
    """'+Language.G_Language[1322]+'"""
    
    root = GetElement(uiName,'root')
    hwnd = windll.user32.GetParent(root.winfo_id())  
    win32gui.ShowWindow(hwnd,0)

def SetUIState(uiName,state):
    """'+Language.G_Language[1319]+'"""
    global G_UIRootStateDictionary
    G_UIRootStateDictionary[uiName] = state
    
''' 
    f.write(code)
#设置居中
def WriteCenterDlgFunction_Mobile(f):
    code='''
def CenterDlg(uiName,popupDlg,dw=0,dh=0):
    """'+Language.G_Language[1218]+'"""
    pass
def MaximizeUI(uiName):
    """'+Language.G_Language[1319]+'"""
    pass
def MinimizeUI(uiName):
    """'+Language.G_Language[1321]+'"""
    pass
def RestoreUI(uiName):
    """'+Language.G_Language[1320]+'"""
    pass
def HideUI(uiName):
    """'+Language.G_Language[1322]+'"""
    pass

''' 
    f.write(code)
#设置窗口圆角
def WriteSetRoundedRectangleFunction(f):
    code='''
def SetRoundedRectangle(uiName,elementName,WidthEllipse=20,HeightEllipse=20):
    """'+Language.G_Language[1219]+'"""
    global G_UIElementRoundRectangleDictionary
    if isinstance(elementName,int) == True:
        WidthEllipse = elementName
        HeightEllipse = WidthEllipse
        uiName,elementName = GetElementName(uiName)
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
        elementName = G_UIElementAliasDictionary[uiName][elementName] 
    G_UIElementRoundRectangleDictionary[uiName][elementName] = [WidthEllipse,HeightEllipse]
    
def ShowRoundedRectangle(Control,WidthEllipse,HeightEllipse):
    """'+Language.G_Language[1220]+'"""
    if Control != None:
        if hasattr(Control,"GetWidget") == True:
            Control = Control.GetWidget()
        import win32gui
        control_width = Control.winfo_width()
        control_height = Control.winfo_height()
        if control_width > 1 and control_height > 1:
            HRGN = win32gui.CreateRoundRectRgn(0,0,control_width,control_height,WidthEllipse,HeightEllipse)
            win32gui.SetWindowRgn(Control.winfo_id(), HRGN,1)
        else:
            Control.after(10, lambda: ShowRoundedRectangle(Control,WidthEllipse,HeightEllipse))

''' 
    f.write(code)
#设置窗口透明度
def WriteSetTransparencyFunction(f):
    code='''
    #f.write(Language.G_Language[1238]+'
def SetTransparencyFunction(root,alpha):
    """'+Language.G_Language[1238]+'"""
    if root != None:
        try :
            hwnd = windll.user32.GetParent(root.winfo_id())
            _winlib = ctypes.windll.user32
            style = _winlib.GetWindowLongA( hwnd, 0xffffffec ) | 0x00080000
            _winlib.SetWindowLongA( hwnd, 0xffffffec, style )
            _winlib.SetLayeredWindowAttributes( hwnd, 0, alpha, 2 )
        except ImportError:   
            pass 

''' 
    f.write(code)
#写入设置光标的函数
def WriteSetCursorFunction(f):
    code='''
def SetCursor(uiName,elementName,cursor='hand2'):
    """'+Language.G_Language[1490]+'"""
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        Control = GetElement(uiName,elementName)
        if Control is not None:
            if hasattr(Control,"GetEntry") == True:
                Control = Control.GetEntry()
            elif hasattr(Control,"GetWidget") == True:
                Control = Control.GetWidget()
            try:
                Control.config(cursor=cursor)
            except:
                pass
def HideCursor(uiName):
    """'+Language.G_Language[1491]+'"""
    global G_UIElementDictionary
    if uiName in G_UIElementDictionary:
        root = GetElement(uiName,"root")
        if root is not None:
            root.config(cursor="none")
def GetCursorPosition(uiName=\'\',elementName=\'root\'):
    """'+Language.G_Language[9805]+'"""
    global G_UIElementDictionary
    global G_TKRoot
    if uiName in G_UIElementDictionary:
        Control = GetElement(uiName,elementName)
        if Control:
            return Control.winfo_pointerxy()
        else:
            Form_1 = GetElement(uiName,"Form_1")
            if Form_1 is not None:
                return Form_1.winfo_pointerxy()
    return G_TKRoot.winfo_pointerxy()

''' 
    f.write(code)
#展开或关闭树型的所有节点
def WriteOpenOrCloseTreeView(f):
    code='''
    #f.write(Language.G_Language[1237]+'
def ExpandAllTreeItem(targetTree,isOpen,parentItem = None):
    """'+Language.G_Language[1237]+'"""
    ParentItemArray = [parentItem]
    if parentItem == None:
        ParentItemArray = targetTree.get_children()
    for Item in ParentItemArray:
        targetTree.item(Item,open=isOpen)
        for childItem in targetTree.get_children(Item):
            targetTree.item(childItem,open=isOpen)
            ExpandAllTreeItem(targetTree,isOpen,childItem)
''' 
    f.write(code)
#弹出对话框
def WriteMessageBoxFunction(f):
    code='''
    #f.write(Language.G_Language[1221]+'
def MessageBox(text="",title="info",type="info",parent=None):
    """'+Language.G_Language[1221]+'"""
    global G_TopDialog
    global G_TKRoot
    if G_TopDialog:
        parent = G_TopDialog
    winhandle = None
    try:
        if parent:
            winhandle = parent.winfo_id()
        elif G_TKRoot:
            winhandle = G_TKRoot.winfo_id()
    except:
        pass
    if type == "error":
    #f.write('        tkinter.messagebox.showerror(title,text)
        import win32api
        import win32con
        ICONERROR=16 #错误图标
        win32api.MessageBox(winhandle,text,title,win32con.MB_OK|ICONERROR)
    else:
        import win32api
        import win32con
        ICONQUESTION=32 #警告图标
        win32api.MessageBox(winhandle,text,title,win32con.MB_OK|ICONQUESTION) 

def RunApplication(uiClass,deiconify=False,projName='',InitCheckFunc=None):
    """'+Language.G_Language[9519]+'"""
    try:
        global G_TKRoot
        G_TKRoot = tkinter.Tk()
        G_TKRoot.withdraw()
        if deiconify == True:
            if RunForm1_CallBack(projName,"InitCheck",InitCheckFunc) == False:
                sys.exit()
                return
            MyDlg = uiClass(G_TKRoot)
        else:
            MyDlg = uiClass(G_TKRoot)
        G_TKRoot.attributes('-topmost',1)   
        G_TKRoot.attributes('-topmost',0)  
        G_TKRoot.mainloop()
        sys.exit()
    except Exception as Ex:
        except_type, except_value, except_traceback = sys.exc_info()
        except_value_str = str(except_value)
        except_stack_end = except_traceback.tb_frame
        except_stack_next = except_traceback.tb_next
        except_stack_lineno = except_traceback.tb_lineno
        while except_stack_next:
            except_stack_end = except_stack_next.tb_frame
            except_stack_lineno = except_stack_next.tb_lineno
            except_stack_next = except_stack_next.tb_next
        except_file = os.path.split(except_stack_end.f_code.co_filename)[1]
        MessageBox("'+Language.G_Language[9517]+'：%s\\n'+Language.G_Language[51]+'：%s\\n'+Language.G_Language[3322]+'：%s" % (except_value_str, except_file, except_stack_lineno),"'+Language.G_Language[9518]+'")
''' 
    f.write(code)
#弹出对话框
def WriteInputBoxFunction(f):
    code='''
    #f.write(Language.G_Language[1222]+'
def InputBox(title='',prompt='',initialvalue='',parent=None):
    """'+Language.G_Language[1222]+'"""
    res = tkinter.simpledialog.askstring(title,prompt=prompt,initialvalue=initialvalue)
    return res

def InputDialog(width,lines=1,bgColor='#EFEFEF',titleText='',promptText='',defaultText='',callBackFunction=None):
    """'+Language.G_Language[9349]+'"""
    theInputDialog = tkinter.Toplevel()
    theInputDialog.attributes("-toolwindow", 1)
    theInputDialog.resizable(1,1)
    theInputDialog.wm_attributes("-topmost", 1)
    theInputDialog.title(titleText)
    height = 140
    if lines > 1:
       height = 110 + lines * 20
    user32 = ctypes.windll.user32
    sw = user32.GetSystemMetrics(0)
    sh = user32.GetSystemMetrics(1)
    zx = int((sw-width)/2) 
    zy = int((sh-height)/2)
    geoinfo = str('%dx%d+%d+%d'%(width,height,zx,zy))
    theInputDialog.geometry(geoinfo)
    theForm = tkinter.Canvas(theInputDialog,bg = bgColor,width = width,height=height,highlightthickness=0,bd=0)
    theForm.pack(expand=1, fill='both')
    theDataLabel = tkinter.Label(theForm,anchor = tkinter.W,text=promptText,width = width,bg = bgColor,fg = '#000000',font = ('宋体',12),justify = tkinter.LEFT,height = 1)
    theDataLabel.place(x = 20,y = 10,width = width-40,height = 30)
    theYPos = 75
    if lines == 1:
        theEntryText = StringVar()
        theEntryText.set('')
        theEntry= tkinter.Entry(theForm,textvariable=theEntryText,bg='#FFFFFF',relief=tkinter.FLAT)
        theEntry.place(x = 20,y = 45,width = width-40,height = 30)
    else:
        theEntry= tkinter.Text(theForm,bg="#FFFFFF",relief=tkinter.FLAT)
        theEntry.place(x = 20,y = 45,width = width-40,height = lines * 20)
        theYPos = 45 + lines * 20
    def submitDialog():
        if lines == 1:
            inputText = theEntryText.get()
        else:
            inputText = theEntry.get('1.0',tkinter.END)
        if callBackFunction:
            callBackFunction(inputText)
        theInputDialog.destroy()
    def closeDialog():
        theInputDialog.destroy()
    
    centerX = int(width/2)
    theOKButton = tkinter.Button(theForm,anchor = tkinter.CENTER,text='"+Language.G_Language[69]+"',width = 100,height = 1,command=submitDialog)
    theOKButton.place(x = centerX - 110 ,y = theYPos + 10,width = 100,height = 30)
    theCancelButton = tkinter.Button(theForm,anchor = tkinter.CENTER,text='"+Language.G_Language[70]+"',width = 100,height = 1,command=closeDialog)
    theCancelButton.place(x = centerX + 10,y = theYPos + 10,width = 100,height = 30)
    tkinter.Tk.wait_window(theInputDialog)
        

''' 
    f.write(code)
#弹出对话框
def WriteAskBoxFunction(f):
    code='''
    #f.write(Language.G_Language[1223]+'
def AskBox(title,text,parent=None):
    """'+Language.G_Language[1223]+'"""
    global G_TopDialog
    global G_TKRoot
    if G_TopDialog:
        parent = G_TopDialog
    #f.write('    res = tkinter.messagebox.askyesno(title,text,parent=parent)
    winhandle = None
    try:
        if parent:
            if isinstance(parent,str) == True:
                parent = GetElement(parent,'root')
                if parent :
                    winhandle = parent.winfo_id()
            else:
                winhandle = parent.winfo_id()
        elif G_TKRoot:
            winhandle = G_TKRoot.winfo_id()
    except:
        pass
    import win32api
    import win32con
    ICONQUESTION=32 #警告图标
    res =  win32api.MessageBox(winhandle,text,title,win32con.MB_YESNO|ICONQUESTION)
    if res == 6:
        return True
    return False
def AskCancelBox(title,text,parent=None):
    """'+Language.G_Language[9988]+'"""
    global G_TopDialog
    global G_TKRoot
    if G_TopDialog:
        parent = G_TopDialog
    #f.write('    res = tkinter.messagebox.askyesno(title,text,parent=parent)
    winhandle = None
    try:
        if parent:
            if isinstance(parent,str) == True:
                parent = GetElement(parent,'root')
                if parent :
                    winhandle = parent.winfo_id()
            else:
                winhandle = parent.winfo_id()
        elif G_TKRoot:
            winhandle = G_TKRoot.winfo_id()
    except:
        pass
    import win32api
    import win32con
    ICONQUESTION=32 #警告图标
    res =  win32api.MessageBox(winhandle,text,title,win32con.MB_YESNOCANCEL|ICONQUESTION)
    if res == 6:
        return "Yes"
    elif res == 7:
        return "No"
    return "Cancel"
''' 
    f.write(code)
#弹出对话框
def WriteWalkAllResFilesFunction(f):
    code='''
    #f.write(Language.G_Language[1224]+'
def WalkAllResFiles(parentPath,alldirs=True,extName=None):
    """'+Language.G_Language[1224]+'"""
    ResultFilesArray = []
    if os.path.exists(parentPath) == True:
        for fileName in os.listdir(parentPath):
            if '__pycache__' not in fileName:
                if '.git' not in fileName:
                    newPath = os.path.join(parentPath,fileName)
                    newPath = newPath.replace("/","\\\\")
                    if os.path.isdir(newPath):
                        if extName == None:
                           ResultFilesArray.append(newPath)
                        if alldirs == True:
                            ResultFilesArray.extend(WalkAllResFiles(newPath,alldirs,extName))
                    else:
                        if extName == None:
                            ResultFilesArray.append(newPath)
                        else:
                            file_extension = os.path.splitext(fileName)[1].replace('.','')
                            file_extension_lower = file_extension.lower().strip()
                            if isinstance(extName,list) == True:
                                extName_lower = [s.lower() for s in extName]
                                if file_extension_lower in extName_lower:
                                    ResultFilesArray.append(newPath)
                            else:
                                file_extName_lower = extName.lower().strip()
                                if file_extension_lower == file_extName_lower:
                                    ResultFilesArray.append(newPath)
    return ResultFilesArray

''' 
    f.write(code)
#文件操作处理
def WriteFileOperateFunction(f):
    code='''
def ImportResources(srcFile,coverMode=True):
    """'+Language.G_Language[2020]+'"""
    try: 
        srcPathName,srcFileName = os.path.split(srcFile) 
        dstFile = os.path.join(G_ResDir,srcFileName) 
        if os.path.normcase(srcFile) != os.path.normcase(dstFile): 
            if os.path.exists(dstFile) == True and coverMode == True: 
                os.remove(dstFile) 
            shutil.copyfile(srcFile,dstFile)
        return True 
    except Exception as ex: 
        print(ex) 
    return False 
def CopyFile(srcFile,dstFile,coverMode=True):
    """'+Language.G_Language[2002]+'"""
    try: 
        if os.path.exists(dstFile) == True and coverMode == True: 
            os.remove(dstFile) 
        def CreateParentDir(PathName):
            ParentPath,DirName = os.path.split(PathName)
            if os.path.exists(ParentPath) == False:
                CreateParentDir(ParentPath)
            os.mkdir(PathName)
        dstPathName,dstFileName = os.path.split(dstFile)
        if os.path.exists(dstPathName) == False:
            CreateParentDir(dstPathName)
        shutil.copyfile(srcFile,dstFile)
        return True 
    except Exception as ex: 
        print(ex) 
    return False 
def MoveFile(srcFile,dstFile,coverMode=True):
    """'+Language.G_Language[2003]+'"""
    try: 
        if os.path.exists(dstFile) == True and coverMode == True: 
            os.remove(dstFile) 
        shutil.move(srcFile,dstFile)
        return True 
    except Exception as ex: 
        print(ex) 
    return False 
def DeleteFile(dstFile):
    """'+Language.G_Language[2004]+'"""
    if os.path.exists(dstFile) == True: 
        os.remove(dstFile)
def GetFileMD5(srcFile):
    """'+Language.G_Language[2005]+'"""
    import hashlib
    try:
        if os.path.exists(srcFile) == True: 
            with open(srcFile, 'rb') as file:
                data = file.read()
                md5_hash = hashlib.md5(data).hexdigest()
                return md5_hash
    except Exception as ex: 
        print(ex) 
    return None
def CompareFileMD5(srcFile,dstFile):
    """'+Language.G_Language[2014]+'"""
    MD51 = GetFileMD5(srcFile)
    MD52 = GetFileMD5(dstFile) 
    return MD51 != None and MD51 == MD52
def CreateDir(dstDir,coverMode=True):
    """'+Language.G_Language[2011]+'"""
    try: 
        if os.path.exists(dstDir) == True: 
            if coverMode == True: 
                shutil.rmtree(dstDir) 
            else: 
                return True 
        def CreateParentDir(PathName):
            ParentPath,DirName = os.path.split(PathName)
            if ParentPath and os.path.exists(ParentPath) == False:
                CreateParentDir(ParentPath)
            os.mkdir(PathName)
        CreateParentDir(dstDir)
        return True 
    except Exception as ex: 
        print(ex) 
    return False 
def CopyDir(srcDir,dstDir,coverMode=True):
    """'+Language.G_Language[2008]+'"""
    try: 
        if os.path.exists(dstDir) == True and coverMode == True: 
            shutil.rmtree(dstDir) 
        shutil.copytree(srcDir, dstDir)
        return True 
    except Exception as ex: 
        print(ex) 
    return False 
def MoveDir(srcDir,dstDir,coverMode=True):
    """'+Language.G_Language[2009]+'"""
    try: 
        if os.path.exists(dstDir) == True and coverMode == True: 
            shutil.rmtree(dstDir) 
        shutil.copytree(srcDir, dstDir) 
        shutil.rmtree(srcDir) 
        return True 
    except Exception as ex: 
        print(ex) 
    return False 
def DeleteDir(srcDir):
    """'+Language.G_Language[2010]+'"""
    return shutil.rmtree(srcDir)
def CheckIsDir(srcDir):
    """'+Language.G_Language[2012]+'"""
    return os.path.isdir(srcDir)
def CheckExist(srcDir):
    """'+Language.G_Language[2013]+'"""
    return os.path.exists(srcDir)
def GetFileExtension(srcFile):
    """'+Language.G_Language[2503]+'"""
    pathName,fileName = os.path.split(srcFile)
    shotname,extension = os.path.splitext(fileName)
    return extension

''' 
    f.write(code)
#写入修改参数的函数
def WriteAddParamsFunction(f):
    code='''
    #f.write(Language.G_Language[1225]+'
def EventFunction_Adaptor(fun,  **params):
    """'+Language.G_Language[1225]+'"""
    return lambda event, fun=fun, params=params: fun(event, **params)
def EventTwoFunction_Adaptor(fun1,fun2, **params):
    """'+Language.G_Language[1225]+'"""
    return lambda event, fun1=fun1,fun2=fun2, params=params: (fun1(event, **params),fun2(event, **params))
def CommandFunction_Adaptor(fun,uiName,widgetName):
    """'+Language.G_Language[1225]+'"""
    button = GetElement(uiName,widgetName)
    if button:
        button.focus_set()
    fun(uiName=uiName,widgetName=widgetName)
def SetValueChangedFunction(fun, uiName,widgetName):
    """'+Language.G_Language[1225]+'"""
    return lambda value,fun=fun: fun(uiName=uiName,widgetName=widgetName,value=value)

def ListViewHeadingFunction_Adaptor(fun,uiName,widgetName,columnname):
    """'+Language.G_Language[1225]+'"""
    # f.write('    button = GetElement(uiName,widgetName)
    # f.write('    if button:
    # f.write('        button.focus_set()
    fun(uiName = uiName , widgetName = widgetName,columnname = columnname)
def MenuFunction_Adaptor(fun,  **params):
    """'+Language.G_Language[1225]+'"""
    return lambda event, fun=fun, params=params: fun(**params)
class   PyMeEvent():
    def __init__(self,x,y,tag=None):
        self.x = x
        self.y = y
        self.tag = tag
class   ChartEvent():
    def __init__(self,width,height,widget):
        self.width = width
        self.height = height
        self.widget = widget
class   ResetPrintClass():
    """'+Language.G_Language[8645]+'"""
    def __init__(self):
        self.str = ""
    def write(self,s):
        self.str += s
    def clear(self):
        self.str = ""
    def getString(self):
        return self.str
def GetParentCallFunc():
    """'+Language.G_Language[9400]+'"""
    stackFunctionInfo = inspect.currentframe().f_back
    while stackFunctionInfo is not None and '__name__' in stackFunctionInfo.f_globals:
        if stackFunctionInfo.f_code.co_filename != __file__: 
            parent_func = stackFunctionInfo.f_globals['__name__'] + \".\" + stackFunctionInfo.f_code.co_name
            return [parent_func,list(stackFunctionInfo.f_locals.values())]
        stackFunctionInfo = stackFunctionInfo.f_back
    return [None,None]
''' 
    f.write(code)
#写入拖放文件函数
def WriteDropFileFunction(f):
    code='''
def DropFileFunction_Callback(fun,files, **params):
    fileList = []
    for fileName in files:
        fileList.append(fileName.decode('gbk'))
    threading.Thread(target=fun,args=(fileList,params['uiName'],params['widgetName'])).start()
    #f.write("    fun(**params,files=fileList)
def DropFileFunction_Adaptor(fun,  **params):
    return lambda files, fun=fun, params=params: DropFileFunction_Callback(fun,files, **params)
def SetControlAcceptDrop(uiName,elementName,functionCallback):
    """'+Language.G_Language[9201]+'"""
    Control = GetElement(uiName,elementName)
    if Control is None:
        return 
    if hasattr(Control,"GetEntry") == True:
        Control = Control.GetEntry()
    elif hasattr(Control,"GetWidget") == True:
        Control = Control.GetWidget()
    import windnd
    windnd.hook_dropfiles(Control,func=DropFileFunction_Adaptor(functionCallback,uiName=uiName,widgetName=elementName))

''' 
    f.write(code)
#写入修改参数的函数
def WriteSetControlPackFunction(f):
    code='''
    #f.write(Language.G_Language[1241]+'
def SetControlPack(uiName,elementName,fill,side,padx,pady,expand,width=0,height=0):
    """'+Language.G_Language[1241]+'"""
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if hasattr(Control,"GetWidget") == True:
            Control = Control.GetWidget()
        Control.pack(fill = fill,side = side,padx = padx,pady = pady,expand = expand)
        if expand == 0:
            Control.pack_propagate(0)
            try:
               Control.configure(width=width)
               Control.configure(height=height)
            except:
               pass
        PackDictionary = {}
        PackDictionary["type"] = "pack"
        PackDictionary["fill"] = fill
        PackDictionary["side"] = side
        PackDictionary["padx"] = padx
        PackDictionary["pady"] = pady
        PackDictionary["expand"] = expand
        PackDictionary["visible"] = True
        G_UIElementPlaceDictionary[uiName][elementName]=PackDictionary
''' 
    f.write(code)
#写入修改参数的函数
def WriteSetControlGridFunction(f):
    code='''
    #f.write(Language.G_Language[1242]+'
def SetControlGrid(uiName,elementName,row,column,rowspan,columnspan):
    """'+Language.G_Language[1242]+'"""
    
    Control = GetElement(uiName,elementName) 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if hasattr(Control,"GetWidget") == True:
            Control = Control.GetWidget()
        Control.grid(row = row,column = column,rowspan = rowspan,columnspan = columnspan)
        GridDictionary = {}
        GridDictionary["type"] = "grid"
        GridDictionary["row"] = row
        GridDictionary["column"] = column
        GridDictionary["rowspan"] = rowspan
        GridDictionary["columnspan"] = columnspan
        GridDictionary["visible"] = True
        G_UIElementPlaceDictionary[uiName][elementName]=GridDictionary
''' 
    f.write(code)
#写入设置位置
def WriteSetControlPlaceFunction(f):
    code='''
    #f.write(Language.G_Language[1226]+'
def SetControlPlace(uiName,elementName,x,y,w,h,anchorpoint=\'nw\',visible=True,modify=True):
    """'+Language.G_Language[1226]+'"""
    Control = GetElement(uiName,elementName) 
    OldControl = Control 
    if Control: 
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
            elementName = G_UIElementAliasDictionary[uiName][elementName] 
        if hasattr(Control,"GetWidget") == True:
            Control = Control.GetWidget()
    def getXW(value):
        return value
    def getYH(value):
        return value
    if Control != None:
        ParentWidth,ParentHeight = GetUIRootSize(uiName)
        try:
            PlaceInfo = Control.place_info()
            if len(PlaceInfo) > 0:
                #避免拖动窗体时闪烁
                if ("relx" in PlaceInfo and float(PlaceInfo["relx"]) > 0) or ("rely" in PlaceInfo and float(PlaceInfo["rely"]) > 0) :
                    Control.place_forget()
        except Exception as ex:
    #对于某些非界面组件也调用了，就直接返回
    #f.write('           print(ex)
           return
        if type(x) == type(1.0):
            if type(y) == type(1.0):
                if type(w) == type(1.0):
                    if type(h) == type(1.0):
                        if visible == True:
                            Control.place(relx=x,rely=y,relwidth=w,relheight=h)
                        if modify == True:
                            PlaceDictionary = {}
                            PlaceDictionary["type"] = "place"
                            PlaceDictionary["relx"] = x
                            PlaceDictionary["rely"] = y
                            PlaceDictionary["relwidth"] = w
                            PlaceDictionary["relheight"] = h
                            PlaceDictionary["visible"] = visible
                            PlaceDictionary["anchorpoint"] = anchorpoint
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                    else:
                        if visible == True:
                            Control.place(relx=x,rely=y,relwidth=w,height=getYH(h))
                        if modify == True:
                            PlaceDictionary = {}
                            PlaceDictionary["type"] = "place"
                            PlaceDictionary["relx"] = x
                            PlaceDictionary["rely"] = y
                            PlaceDictionary["relwidth"] = w
                            PlaceDictionary["height"] = getYH(h)
                            PlaceDictionary["visible"] = visible
                            PlaceDictionary["anchorpoint"] = anchorpoint
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                else:
                    if type(h) == type(1.0):
                        if visible == True:
                            Control.place(relx=x,rely=y,width=getXW(w),relheight=h)
                        if modify == True:
                            PlaceDictionary = {}
                            PlaceDictionary["type"] = "place"
                            PlaceDictionary["relx"] = x
                            PlaceDictionary["rely"] = y
                            PlaceDictionary["width"] = getXW(w)
                            PlaceDictionary["relheight"] = h
                            PlaceDictionary["visible"] = visible
                            PlaceDictionary["anchorpoint"] = anchorpoint
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                    else:
                        if visible == True:
                            Control.place(relx=x,rely=y,width=getXW(w),height=getYH(h))
                        if modify == True:
                            PlaceDictionary = {}
                            PlaceDictionary["type"] = "place"
                            PlaceDictionary["relx"] = x
                            PlaceDictionary["rely"] = y
                            PlaceDictionary["width"] = getXW(w)
                            PlaceDictionary["height"] = getYH(h)
                            PlaceDictionary["visible"] = visible
                            PlaceDictionary["anchorpoint"] = anchorpoint
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
            else:
                if type(w) == type(1.0):
                    if type(h) == type(1.0):
                        if visible == True:
                            Control.place(relx=x,y=getYH(y),relwidth=w,relheight=h)
                        if modify == True:
                            PlaceDictionary = {}
                            PlaceDictionary["type"] = "place"
                            PlaceDictionary["relx"] = x
                            PlaceDictionary["y"] = getYH(y)
                            PlaceDictionary["relwidth"] = w
                            PlaceDictionary["relheight"] = h
                            PlaceDictionary["visible"] = visible
                            PlaceDictionary["anchorpoint"] = anchorpoint
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                    else:
                        if visible == True:
                            Control.place(relx=x,y=getYH(y),relwidth=w,height=getYH(h))
                        if modify == True:
                            PlaceDictionary = {}
                            PlaceDictionary["type"] = "place"
                            PlaceDictionary["relx"] = x
                            PlaceDictionary["y"] = getYH(y)
                            PlaceDictionary["relwidth"] = w
                            PlaceDictionary["height"] = getYH(h)
                            PlaceDictionary["visible"] = visible
                            PlaceDictionary["anchorpoint"] = anchorpoint
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                else:
                    if type(h) == type(1.0):
                        if visible == True:
                            Control.place(relx=x,y=getYH(y),width=w,relheight=h)
                        if modify == True:
                            PlaceDictionary = {}
                            PlaceDictionary["type"] = "place"
                            PlaceDictionary["relx"] = x
                            PlaceDictionary["y"] = getYH(y)
                            PlaceDictionary["relwidth"] = w
                            PlaceDictionary["relheight"] = h
                            PlaceDictionary["visible"] = visible
                            PlaceDictionary["anchorpoint"] = anchorpoint
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                    else:
                        if visible == True:
                            Control.place(relx=x,y=getYH(y),width=w,height=getYH(h))
                        if modify == True:
                            PlaceDictionary = {}
                            PlaceDictionary["type"] = "place"
                            PlaceDictionary["relx"] = x
                            PlaceDictionary["y"] = getYH(y)
                            PlaceDictionary["relwidth"] = w
                            PlaceDictionary["height"] = getYH(h)
                            PlaceDictionary["visible"] = visible
                            PlaceDictionary["anchorpoint"] = anchorpoint
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
        else:
            if type(y) == type(1.0):
                if type(w) == type(1.0):
                    if type(h) == type(1.0):
                        if visible == True:
                            Control.place(x=getXW(x),rely=y,relwidth=w,relheight=h)
                        if modify == True:
                            PlaceDictionary = {}
                            PlaceDictionary["type"] = "place"
                            PlaceDictionary["x"] = getXW(x)
                            PlaceDictionary["rely"] = y
                            PlaceDictionary["relwidth"] = w
                            PlaceDictionary["relheight"] = h
                            PlaceDictionary["visible"] = visible
                            PlaceDictionary["anchorpoint"] = anchorpoint
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                    else:
                        if visible == True:
                            Control.place(x=getXW(x),rely=y,relwidth=w,height=getYH(h))
                        if modify == True:
                            PlaceDictionary = {}
                            PlaceDictionary["type"] = "place"
                            PlaceDictionary["x"] = getXW(x)
                            PlaceDictionary["rely"] = y
                            PlaceDictionary["relwidth"] = w
                            PlaceDictionary["height"] = getYH(h)
                            PlaceDictionary["visible"] = visible
                            PlaceDictionary["anchorpoint"] = anchorpoint
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                else:
                    if type(h) == type(1.0):
                        if visible == True:
                            Control.place(x=getXW(x),rely=y,width=getXW(w),relheight=h)
                        if modify == True:
                            PlaceDictionary = {}
                            PlaceDictionary["type"] = "place"
                            PlaceDictionary["x"] = getXW(x)
                            PlaceDictionary["rely"] = y
                            PlaceDictionary["width"] = getXW(w)
                            PlaceDictionary["relheight"] = h
                            PlaceDictionary["visible"] = visible
                            PlaceDictionary["anchorpoint"] = anchorpoint
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                    else:
                        if visible == True:
                            Control.place(x=getXW(x),rely=y,width=getXW(w),height=getYH(h))
                        if modify == True:
                            PlaceDictionary = {}
                            PlaceDictionary["type"] = "place"
                            PlaceDictionary["x"] = getXW(x)
                            PlaceDictionary["rely"] = y
                            PlaceDictionary["width"] = getXW(w)
                            PlaceDictionary["height"] = getYH(h)
                            PlaceDictionary["visible"] = visible
                            PlaceDictionary["anchorpoint"] = anchorpoint
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
            else:
                if type(w) == type(1.0):
                    if type(h) == type(1.0):
                        if visible == True:
                            Control.place(x=getXW(x),y=getYH(y),relwidth=w,relheight=h)
                        if modify == True:
                            PlaceDictionary = {}
                            PlaceDictionary["type"] = "place"
                            PlaceDictionary["x"] = getXW(x)
                            PlaceDictionary["y"] = getYH(y)
                            PlaceDictionary["relwidth"] = w
                            PlaceDictionary["relheight"] = h
                            PlaceDictionary["visible"] = visible
                            PlaceDictionary["anchorpoint"] = anchorpoint
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                    else:
                        if visible == True:
                            Control.place(x=getXW(x),y=getYH(y),relwidth=w,height=getYH(h))
                        if modify == True:
                            PlaceDictionary = {}
                            PlaceDictionary["type"] = "place"
                            PlaceDictionary["x"] = getXW(x)
                            PlaceDictionary["y"] = getYH(y)
                            PlaceDictionary["relwidth"] = w
                            PlaceDictionary["height"] = getYH(h)
                            PlaceDictionary["visible"] = visible
                            PlaceDictionary["anchorpoint"] = anchorpoint
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                else:
                    if type(h) == type(1.0):
                        if visible == True:
                            Control.place(x=getXW(x),y=getYH(y),width=getXW(w),relheight=h)
                        if modify == True:
                            PlaceDictionary = {}
                            PlaceDictionary["type"] = "place"
                            PlaceDictionary["x"] = getXW(x)
                            PlaceDictionary["y"] = getYH(y)
                            PlaceDictionary["width"] = getXW(w)
                            PlaceDictionary["relheight"] = h
                            PlaceDictionary["visible"] = visible
                            PlaceDictionary["anchorpoint"] = anchorpoint
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
                    else:
    # f.write('                        Control.place(x=getXW(x),y=getYH(y),width=getXW(w),height=getYH(h))
                        PlaceDictionary = {}
                        if h == '' and w == '':
                            if visible == True:
                                Control.place(x=getXW(x),y=getYH(y))
                            if modify == True:
                                PlaceDictionary[\"width\"] = ''
                                PlaceDictionary[\"height\"] = ''
                        elif h == '':
                            if visible == True:
                                Control.place(x=getXW(x),y=getYH(y),width=getXW(w))
                            if modify == True:
                                PlaceDictionary[\"width\"] = getXW(w)
                                PlaceDictionary[\"height\"] = ''
                        elif w == '':
                            if visible == True:
                                Control.place(x=getXW(x),y=getYH(y),height=getYH(h))
                            if modify == True:
                                PlaceDictionary[\"width\"] = ''
                                PlaceDictionary[\"height\"] = getYH(h)
                        else:
                            if visible == True:
                                Control.place(x=getXW(x),y=getYH(y),width=getXW(w),height=getYH(h))
                            if modify == True:
                                PlaceDictionary[\"width\"] =  getXW(w)
                                PlaceDictionary[\"height\"] = getYH(h)
                        if modify == True:
                            PlaceDictionary["type"] = "place"
                            PlaceDictionary["x"] = getXW(x)
                            PlaceDictionary["y"] = getYH(y)
                            PlaceDictionary["visible"] = True
                            PlaceDictionary["anchorpoint"] = anchorpoint
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary
    if Control != None and visible == True:
        Control.update()
        if elementName.find("Frame_") >= 0 or elementName.find("LabelFrame_") >= 0 or elementName.find("PanedWindow_") >= 0:
            for childWidgetName in Control.children.keys():
                frameCanvas = Control.children[childWidgetName]
                for uiName in G_UIElementDictionary.keys():
                    if G_UIElementDictionary[uiName]["root"] is frameCanvas:
                        if "UIClass" in  G_UIElementDictionary[uiName].keys():
                            uiClass = GetElement(uiName,"UIClass")
                            if uiClass:
                                Form_1 = GetElement(uiName,"Form_1")
                                if Form_1:
                                    Form_1_Width = frameCanvas.winfo_width()
                                    Form_1_Height = frameCanvas.winfo_height()
                                    event = ChartEvent(Form_1_Width,Form_1_Height,Form_1)
                                    if hasattr(uiClass,"Configure") == True:
                                        uiClass.Configure(event)
    if elementName.find("LabelButton_") >= 0 or elementName.find("Entry") >= 0 or elementName.find("Text") >= 0:
        if hasattr(OldControl,"Configure") == True:
            event = ChartEvent(w,h,OldControl)
            OldControl.Configure(event)
    if elementName.find("Calendar_") >= 0 or elementName.find("DatePicker_") >= 0 or elementName.find("Navigation_") >= 0 or elementName.find("ListMenu_") >= 0 or elementName.find("SwitchPage_") >= 0 or elementName.find("ShowCase_") >= 0:
        if visible == False:
            if hasattr(OldControl,"Hide") == True:
                OldControl.Hide()
    # f.write("def ResizeControlImage(uiName,elementName):
    # f.write('    """'+Language.G_Language[1213]+'"""
    # f.write('    global G_UIElementAliasDictionary
    # f.write('    global G_UIElementDictionary
    # f.write('    global G_UIElementVariableArray
    # f.write('    global G_ResourcesFileList
    # f.write('    Control = GetElement(uiName,elementName) 
    # f.write('    if Control: 
    # f.write('        Control_Width = Control.winfo_width() 
    # f.write('        Control_Height = Control.winfo_height() 
    # f.write('        realElementName = elementName 
    # f.write('        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():
    # f.write('            realElementName = G_UIElementAliasDictionary[uiName][elementName] 
    # f.write('        if realElementName:
    # f.write('            if uiName in G_UIElementUserDataArray:
    # f.write('                if realElementName in G_UIElementUserDataArray[uiName]:
    # f.write('                    for EBData in G_UIElementUserDataArray[uiName][realElementName]:   
    # f.write('                        if EBData[0] == \'image\' and EBData[1] == \'imageInfo\':
    # f.write('                            imagePath = EBData[2][1]
    # f.write('                            autoSize = EBData[2][2]
    # f.write('                            from   PIL import Image,ImageTk
    # f.write('                            imagePath_Lower = imagePath.lower()
    # f.write('                            if os.path.exists(imagePath) == False:
    # f.write('                                if imagePath_Lower in G_ResourcesFileList:
    # f.write('                                   imagePath = G_ResourcesFileList[imagePath_Lower]
    # f.write('                                if os.path.exists(imagePath) == False:
    # f.write('                                    return
    # f.write('                            image=Image.open(imagePath).convert(\'RGBA\')
    # f.write('                            if autoSize == True:
    # f.write('                                image_Resize = image.resize((Control_Width, Control_Height),Image.LANCZOS)
    # f.write('                            else:
    # f.write('                                image_Resize = image
    # f.write('                            EBData[2][0] = ImageTk.PhotoImage(image_Resize)
    # f.write('                            if realElementName.find(\'Label_\') >= 0 or realElementName.find(\'Button_\') >= 0 :
    # f.write('                                Control.configure(image = EBData[2][0])
    # f.write('                            elif realElementName.find(\'Text_\') >= 0: 
    # f.write('                                Control.delete(\'0.0\',tkinter.END)
    # f.write('                                Control.image_create(tkinter.END, image=newPTImage)

def GetControlPlace_AnchorPoint(uiName,elementName):
    if uiName not in G_UIElementPlaceDictionary:
        return
    RealElementName = elementName
    if uiName in G_UIElementAliasDictionary.keys() and RealElementName in G_UIElementAliasDictionary[uiName].keys():
        RealElementName = G_UIElementAliasDictionary[uiName][RealElementName] 
    anchorPoint = \'nw\'
    if RealElementName in  G_UIElementPlaceDictionary[uiName].keys():
        if "anchorpoint" in G_UIElementPlaceDictionary[uiName][RealElementName]:
            anchorPoint = G_UIElementPlaceDictionary[uiName][RealElementName]["anchorpoint"]
    return anchorPoint

def UpdateAllElementPlace(uiName,HScrollBarOffsetY=0,VScrollBarOffsetX=0):
    """'+Language.G_Language[1722]+'"""
    if uiName not in G_UIElementPlaceDictionary:
        return
    for elementName in G_UIElementPlaceDictionary[uiName]:
        if elementName == "Form_1":
            continue
        UpdateElementPlace(uiName,elementName,HScrollBarOffsetY,VScrollBarOffsetX)
def UpdateElementPlace(uiName,elementName,HScrollBarOffsetY=0,VScrollBarOffsetX=0):
    """'+Language.G_Language[1722]+'"""
    def getPercentXY(x,y,width,height,parentWidth,parentHeight,anchorpoint):
        if width =='' or height == '':
            return x,y
        if isinstance(x,float) == True:
            x = x * parentWidth
        if isinstance(y,float) == True:
            y = y * parentHeight
        anchorX = x / parentWidth
        anchorY = y / parentHeight
        return anchorX,anchorY
    if uiName not in G_UIElementPlaceDictionary:
        return
    if elementName in G_UIElementPlaceDictionary[uiName]:
        Control = G_UIElementDictionary[uiName][elementName]
        if hasattr(Control,"GetEntry") == True:
            Control = Control.GetEntry()
        elif hasattr(Control,"GetWidget") == True:
            Control = Control.GetWidget()
        ControlParentInfo = Control.winfo_parent()
        ControlParentWidget = Control._nametowidget(ControlParentInfo)
        ParentWidth = ControlParentWidget.winfo_width()
        ParentHeight = ControlParentWidget.winfo_height()
        if ParentWidth == 1 and ParentHeight == 1:
            return
        Visible = True
        if "visible" in G_UIElementPlaceDictionary[uiName][elementName]:
            Visible = G_UIElementPlaceDictionary[uiName][elementName]["visible"]
        PlaceType = "pack"
        if "type" in G_UIElementPlaceDictionary[uiName][elementName]:
            PlaceType = G_UIElementPlaceDictionary[uiName][elementName]["type"]
        if Visible == True:
            if PlaceType == "place":
                x = 0
                if "x" in G_UIElementPlaceDictionary[uiName][elementName]:
                    x = G_UIElementPlaceDictionary[uiName][elementName]["x"]
                elif "relx" in G_UIElementPlaceDictionary[uiName][elementName]:
                    x = G_UIElementPlaceDictionary[uiName][elementName]["relx"]
                y = 0
                if "y" in G_UIElementPlaceDictionary[uiName][elementName]:
                    y = G_UIElementPlaceDictionary[uiName][elementName]["y"]
                elif "rely" in G_UIElementPlaceDictionary[uiName][elementName]:
                    y = G_UIElementPlaceDictionary[uiName][elementName]["rely"]
                w = 0
                if "width" in G_UIElementPlaceDictionary[uiName][elementName]:
                    w = G_UIElementPlaceDictionary[uiName][elementName]["width"]
                elif "relwidth" in G_UIElementPlaceDictionary[uiName][elementName]:
                    w = G_UIElementPlaceDictionary[uiName][elementName]["relwidth"]
                h = 0
                if "height" in G_UIElementPlaceDictionary[uiName][elementName]:
                    h = G_UIElementPlaceDictionary[uiName][elementName]["height"]
                elif "relheight" in G_UIElementPlaceDictionary[uiName][elementName]:
                    h = G_UIElementPlaceDictionary[uiName][elementName]["relheight"]
                if "anchorpoint" in G_UIElementPlaceDictionary[uiName][elementName]:
                    anchorpoint = G_UIElementPlaceDictionary[uiName][elementName]["anchorpoint"]
                    ax,ay = getPercentXY(x,y,w,h,ParentWidth,ParentHeight,anchorpoint)
                    if anchorpoint == "n":
                        if isinstance(x,float) == True:
                            if isinstance(w,float) == True:
                                x = (ax * ParentWidth - w * ParentWidth * 0.5)/ParentWidth
                            else:
                                x = (ax * ParentWidth - w * 0.5)/ParentWidth
                        else:
                            if isinstance(w,float) == True:
                                x = int(ax * ParentWidth - w * ParentWidth * 0.5)
                            else:
                                x = int(ax * ParentWidth - w * 0.5)
                        #x = int(ax * ParentWidth - w * 0.5)
                    elif anchorpoint == "ne":
                        if isinstance(x,float) == True:
                            if isinstance(w,float) == True:
                                x = (ax * ParentWidth - w * ParentWidth)/ParentWidth
                            else:
                                x = (ax * ParentWidth - w)/ParentWidth
                        else:
                            if isinstance(w,float) == True:
                                x = int(ax * ParentWidth  - w * ParentWidth)
                            else:
                                x = int(ax * ParentWidth  - w)
                        #x = int(ax * ParentWidth - w)
                    elif anchorpoint == "w":
                        if isinstance(y,float) == True:
                            if isinstance(h,float) == True:
                                y = (ay * ParentHeight - h * ParentHeight * 0.5)/ParentHeight
                            else:
                                y = (ay * ParentHeight - h * 0.5)/ParentHeight
                        else:
                            if isinstance(h,float) == True:
                                y = int(ay * ParentHeight - h * ParentHeight * 0.5)
                            else:
                                y = int(ay * ParentHeight - h * 0.5)
                        #y = int(ay * ParentHeight - h * 0.5)
                    elif anchorpoint == "center":
                        if isinstance(x,float) == True:
                            if isinstance(w,float) == True:
                                x = (ax * ParentWidth - w * ParentWidth * 0.5)/ParentWidth
                            else:
                                x = (ax * ParentWidth - w * 0.5)/ParentWidth
                        else:
                            if isinstance(w,float) == True:
                                x = int(ax * ParentWidth - w * ParentWidth * 0.5)
                            else:
                                x = int(ax * ParentWidth - w * 0.5)
                        if isinstance(y,float) == True:    
                            if isinstance(h,float) == True:
                                y = (ay * ParentHeight - h * ParentHeight * 0.5)/ParentHeight
                            else:
                                y = (ay * ParentHeight - h * 0.5)/ParentHeight
                        else:
                            if isinstance(h,float) == True:
                                y = int(ay * ParentHeight - h * ParentHeight * 0.5)
                            else:
                                y = int(ay * ParentHeight - h * 0.5)
                        #x = int(ax * ParentWidth - w * 0.5)
                        #y = int(ay * ParentHeight - h * 0.5)
                    elif anchorpoint == "e":
                        if isinstance(x,float) == True:
                            if isinstance(w,float) == True:
                                x = (ax * ParentWidth - w * ParentWidth)/ParentWidth
                            else:
                                x = (ax * ParentWidth - w)/ParentWidth
                        else:
                            if isinstance(w,float) == True:
                                x = int(ax * ParentWidth - w * ParentWidth)
                            else:
                                x = int(ax * ParentWidth - w)
                        if isinstance(y,float) == True:
                            if isinstance(h,float) == True:
                                y = (ay * ParentHeight - h * ParentHeight * 0.5)/ParentHeight
                            else:
                                y = (ay * ParentHeight - h * 0.5)/ParentHeight
                        else:
                            if isinstance(h,float) == True:
                                y = int(ay * ParentHeight - h * ParentHeight * 0.5)
                            else:
                                y = int(ay * ParentHeight - h * 0.5)
                        #x = int(ax * ParentWidth - w)
                        #y = int(ay * ParentHeight - h * 0.5)
                    elif anchorpoint == "sw":
                        if isinstance(y,float) == True:
                            if isinstance(h,float) == True:
                                y = (ay * ParentHeight - h * ParentHeight )/ParentHeight
                            else:
                                y = (ay * ParentHeight - h )/ParentHeight
                        else:
                            if isinstance(h,float) == True:
                                y = int(ay * ParentHeight - h * ParentHeight )
                            else:
                                y = int(ay * ParentHeight - h )
                        #y = int(ay * ParentHeight - h)
                    elif anchorpoint == "s":
                        if isinstance(x,float) == True:
                            if isinstance(w,float) == True:
                                x = (ax * ParentWidth - w * ParentWidth * 0.5)/ParentWidth
                            else:
                                x = (ax * ParentWidth - w * 0.5)/ParentWidth
                        else:
                            if isinstance(w,float) == True:
                                x = int(ax * ParentWidth - w * ParentWidth * 0.5)
                            else:
                                x = int(ax * ParentWidth - w * 0.5)
                        if isinstance(y,float) == True:
                            if isinstance(h,float) == True:
                                y = int(ay * ParentHeight - h * ParentHeight )/ParentHeight
                            else:
                                y = int(ay * ParentHeight - h )
                        else:
                            if isinstance(h,float) == True:
                                y = int(ay * ParentHeight - h * ParentHeight )
                            else:
                                y = int(ay * ParentHeight - h )
                        # x = int(ax * ParentWidth - w * 0.5)
                        # y = int(ay * ParentHeight - h)
                    elif anchorpoint == "se":
                        if isinstance(x,float) == True:
                            if isinstance(w,float) == True:
                                x = (ax * ParentWidth - w * ParentWidth)/ParentWidth
                            else:
                                x = (ax * ParentWidth - w)/ParentWidth
                        else:
                            if isinstance(w,float) == True:
                                x = int(ax * ParentWidth - w * ParentWidth)
                            else:
                                x = int(ax * ParentWidth - w)
                        if isinstance(y,float) == True:
                            if isinstance(h,float) == True:
                                y = (ay * ParentHeight - h * ParentHeight )/ParentHeight
                            else:
                                y = (ay * ParentHeight - h )/ParentHeight
                        else:
                            if isinstance(h,float) == True:
                                y = int(ay * ParentHeight - h * ParentHeight )
                            else:
                                y = int(ay * ParentHeight - h )
                        #x = int(ax * ParentWidth - w)
                        #y = int(ay * ParentHeight - h)
                for aliasName in  G_UIElementAliasDictionary[uiName].keys():
                    if G_UIElementAliasDictionary[uiName][aliasName] == elementName:
                        SetControlPlace(uiName,aliasName,x,y,w,h,'nw',True,False)
                        break
            else:
                x = Control.winfo_x()
                y = Control.winfo_y()
                w = Control.winfo_width()
                h = Control.winfo_height()
            Width_PX = w
            if isinstance(w,float) == True:
               Width_PX = int(w * ParentWidth)
            Height_PX = h
            if isinstance(h,float) == True:
               Height_PX = int(h * ParentHeight)
            HScrollbarName = elementName + "_HScrollbar"
            HScrollbar= GetElement(uiName,HScrollbarName)
            if HScrollbar:
                HScrollbar.place(x = 0,y = Height_PX-20+HScrollBarOffsetY,width = Width_PX,height = 20)
            VScrollbarName = elementName + "_VScrollbar"
            VScrollbar= GetElement(uiName,VScrollbarName)
            if VScrollbar:
                VScrollbar.place(x = Width_PX-20+VScrollBarOffsetX,y = 0,width = 20,height = Height_PX)
            VScrollbarName = elementName + "_Scrollbar"
            VScrollbar= GetElement(uiName,VScrollbarName)
            if VScrollbar:
                VScrollbar.place(x = Width_PX-20+VScrollBarOffsetX,y = 0,width = 20,height = Height_PX)
            ChildCanvasName = elementName + "_Child"
            ChildCanvas = GetElement(uiName,ChildCanvasName)
            if ChildCanvas:
                ChildHandleName = elementName + "_ChildHandle"
                ChildHandle = GetElement(uiName,ChildHandleName)
                if ChildHandle:   
                    ChildCanvas.itemconfig(ChildHandle,width=ParentWidth,height=ParentHeight)       
                    ChildCanvas.config(scrollregion=(0,0,ParentWidth,ParentHeight))          
            if uiName in G_UIElementUserDataArray:
                if elementName in G_UIElementUserDataArray[uiName]:
                    for EBData in G_UIElementUserDataArray[uiName][elementName]:   
                        if EBData[0] == \'image\' and EBData[1] == \'imageInfo\':
                            oldImagePT = EBData[2][0]
                            if oldImagePT.width() == 1 and oldImagePT.height() == 1:
                                imagePath = EBData[2][1]
                                autoSize = EBData[2][2]
                                from   PIL import Image,ImageTk
                                imagePath_Lower = imagePath.lower()
                                if os.path.exists(imagePath) == False:
                                    if imagePath_Lower in G_ResourcesFileList:
                                        imagePath = G_ResourcesFileList[imagePath_Lower]
                                    if os.path.exists(imagePath) == False:
                                        continue
                                image=Image.open(imagePath).convert(\'RGBA\')
                                if autoSize == True:
                                    image_Resize = image.resize((Width_PX, Height_PX),Image.LANCZOS)
                                else:
                                    image_Resize = image
                                EBData[2][0] = ImageTk.PhotoImage(image_Resize)
                                if elementName.find(\'Label_\') >= 0 or elementName.find(\'Button_\') >= 0 :
                                    Control.configure(image = EBData[2][0])
                                elif elementName.find(\'Text_\') >= 0: 
                                    Control.delete(\'0.0\',tkinter.END)
                                    Control.image_create(tkinter.END, image=EBData[2][0])
def SetUIRootSize(uiName,width,height,scale=1.0):
    global G_UIRootSizeDictionary
    global G_RootSize
    global G_UIScale
    if uiName in G_UIRootSizeDictionary:
        G_UIRootSizeDictionary[uiName]["width"] = width
        G_UIRootSizeDictionary[uiName]["height"] = height
        G_UIRootSizeDictionary[uiName]["scale"] = scale
        if "init" not in G_UIRootSizeDictionary[uiName].keys():
            G_UIRootSizeDictionary[uiName]["init"] = [width,height]
    else:
       G_RootSize = [width,height]
       G_UIScale = scale
def GetUIRootSize(uiName,init=False):
    global G_UIRootSizeDictionary
    global G_RootSize
    if uiName in G_UIRootSizeDictionary:
        if init == True and "init" in G_UIRootSizeDictionary[uiName]:
            return G_UIRootSizeDictionary[uiName]["init"][0],G_UIRootSizeDictionary[uiName]["init"][1]
        if "width" in G_UIRootSizeDictionary[uiName].keys() and "height" in G_UIRootSizeDictionary[uiName].keys():
            return G_UIRootSizeDictionary[uiName]["width"],G_UIRootSizeDictionary[uiName]["height"]
    return G_RootSize

def ResizeRoot(uiName,root,event):
    if isinstance(root,tkinter.Frame) == True or isinstance(root,tkinter.LabelFrame) == True or isinstance(root,tkinter.ttk.Frame) == True:
        oldWidth  = root.winfo_width()
        oldHeight = root.winfo_height()
        if oldWidth== event.width and oldHeight== event.height:
            return 
        event.width = oldWidth
        event.height = oldHeight
        Form_1 = GetElement(uiName,\'Form_1\')
        if Form_1:
            Form_1.configure(width = event.width)
            Form_1.configure(height = event.height)
        HScrollBarOffsetY = 0
        VScrollBarOffsetX = 0
        if isinstance(root,tkinter.LabelFrame) == True:
            HScrollBarOffsetY = -30
        UpdateAllElementPlace(uiName,HScrollBarOffsetY,VScrollBarOffsetX)
    # f.write('    for elementName in G_UIElementPlaceDictionary[uiName]:
    # f.write('        PlaceDictionary = G_UIElementPlaceDictionary[uiName][elementName]
    # f.write('        if "anchorpoint" in PlaceDictionary:
    # f.write('            anchorpoint = PlaceDictionary["anchorpoint"]
    # f.write('            if anchorpoint != "nw":
    # f.write('                x = 0
    # f.write('                if "relx" in PlaceDictionary:
    # f.write('                    x = PlaceDictionary["relx"]
    # f.write('                else:
    # f.write('                    x = PlaceDictionary["x"]
    # f.write('                y = 0
    # f.write('                if "rely" in PlaceDictionary:
    # f.write('                    y = PlaceDictionary["rely"]
    # f.write('                else:
    # f.write('                    y = PlaceDictionary["y"]
    # f.write('                w = 0
    # f.write('                if "relwidth" in PlaceDictionary:
    # f.write('                    w = PlaceDictionary["relwidth"]
    # f.write('                else:
    # f.write('                    w = PlaceDictionary["width"]
    # f.write('                h = 0
    # f.write('                if "relheight" in PlaceDictionary:
    # f.write('                    h = PlaceDictionary["relheight"]
    # f.write('                else:
    # f.write('                    h = PlaceDictionary["height"]
    # f.write('                SetControlPlace(uiName,elementName,x,y,w,h,anchorpoint)
    SetUIRootSize(uiName,event.width,event.height)
''' 
    f.write(code)
#写入修改参数的函数
def WriteSetElementLayerFunction(f):
    code='''
    #f.write(Language.G_Language[1241]+'
def SetElementLayer(uiName,elementName,direction='lift'):
    """'+Language.G_Language[1869]+'"""
    global G_UIElementLayerDictionary
    if uiName in G_UIElementDictionary.keys():
        G_UIElementLayerDictionary[uiName][elementName] = direction
''' 
    f.write(code)
#SIN函数图表
def WriteBuildChartFunction(f):
    code='''
    #f.write('#'+Language.G_Language[711]+'
def BuildChart(chartName,uiName,parentWidget,elementName):
    """'+Language.G_Language[710]+'"""
    f = Figure(figsize=(5, 4), dpi=100)
    theChart = FigureCanvasTkAgg(f, master=parentWidget)
    theChart.draw()
    AddUserData(uiName,elementName,\'ChartName\',\'string\',chartName,0)
    AddUserData(uiName,elementName,\'ChartFigure\',\'figure\',f,0)
    AddUserData(uiName,elementName,\'ChartReady\',\'int\',0,0)
    AddUserData(uiName,elementName,\'ChartCanvas\',\'canvas\',theChart,0)
    return theChart.get_tk_widget()
def UpdateChart(uiName,elementName,width = 0,height = 0):
    """'+Language.G_Language[759]+'"""
    theChart = GetUserData(uiName,elementName,\'ChartCanvas\')
    if theChart:
        theChartCanvas = theCharwt.get_tk_widget()
        w = width
        if w == 0:
            w = theChartCanvas.winfo_width()
        h = height
        if h == 0:
            h = theChartCanvas.winfo_height()
        event = ChartEvent(w,h,theChartCanvas)
        theChart.resize(event)
        theChartCanvas.update()
        SetUserData(uiName,elementName,'ChartReady',1)
    # f.write('    canvas = GetUserData(uiName,elementName,\'ChartCanvas\').get_tk_widget()
    # f.write('    def refresh():
    # f.write('        canvas.place(x = 0,y=0,width=1,height=1)
    # f.write('        canvas.update()
    # f.write('        canvas.place(x = G_UIElementPlaceDictionary[uiName][elementName]["x"],y=G_UIElementPlaceDictionary[uiName][elementName]["y"],width=G_UIElementPlaceDictionary[uiName][elementName]["width"],height=G_UIElementPlaceDictionary[uiName][elementName]["height"])
    # f.write('        canvas.update()
    # f.write('    if elementName in G_UIElementPlaceDictionary[uiName]:
    # f.write('        canvas.after(10,refresh)
def UpdateChartData(uiName,elementName,x,y,subplotName='subplot111'):
    """'+Language.G_Language[762]+'"""
    theChart = GetUserData(uiName,elementName,\'ChartCanvas\')
    if theChart:
        a = GetUserData(uiName,elementName,subplotName)
        a.cla()
        a.plot(x, y)
        theChartCanvas = theChart.get_tk_widget()
        w = theChartCanvas.winfo_width()
        h = theChartCanvas.winfo_height()
        event = ChartEvent(w,h,theChartCanvas)
        theChart.resize(event)
def SetClickXYFunction(uiName,elementName,callBackFunction):
    """'+Language.G_Language[764]+'"""
    theChart = GetUserData(uiName,elementName,\'ChartCanvas\')
    if theChart:
        def mouse_event(event):
            a = GetUserData(uiName,elementName,'subplot111')
            if a:
    #f.write("            a.axhline(event.ydata)
    #f.write("            a.axvline(event.xdata)
    #f.write("            print('ClickXY:%d,%d'%(event.xdata,event.ydata))
               callBackFunction(event,uiName,elementName,event.xdata,event.ydata)
    theChart.mpl_connect('button_press_event', mouse_event)
''' 
    f.write(code)
#SIN函数图表
def WriteBuildChartFunctions_Mobile(f):
    code='''
    #f.write('#'+Language.G_Language[711]+'
def BuildChart(chartName,uiName,parentWidget,elementName):
    """'+Language.G_Language[711]+'"""
    
    chart = GameLib.GUI_Label(parentWidget)
    chart.SetBGColor(255,255,255)
    chart.SetStyle("flat")
    f = Figure(figsize=(5, 4), dpi=100)
    chartCanvas = FigureCanvasAgg(f)
    AddUserData(uiName,elementName,\'ChartName\',\'string\',chartName,0)
    AddUserData(uiName,elementName,\'ChartFigure\',\'figure\',f,0)
    AddUserData(uiName,elementName,\'ChartCanvas\',\'canvas\',chartCanvas,0)
    return chart
def UpdateChart(uiName,elementName):
    """'+Language.G_Language[759]+'"""
    pass
def UpdateChartData(uiName,elementName,x,y,subplotName='subplot111'):
    """'+Language.G_Language[762]+'"""
    pass
def SetClickXYFunction(uiName,elementName,callBackFunction):
    """'+Language.G_Language[764]+'"""
    pass
'''
    f.write(code)
    
#写入画板动作
def WriteDoCanvasRecordFunction(f,useAggdraw = True):
    code='''f.write(code)
    #f.write(Language.G_Language[1234]+'
def DoCanvasRecord(drawCanvas,shapeType,x,y,x2,y2,fillcolor,outlinecolor,fillwidth,dash1=0,dash2=0,newImage=None,text='',textFont = None,textColor='',shapeTag=''):
    """'+Language.G_Language[1234]+'"""
    if  drawCanvas != None:
        if shapeType == 'line' or shapeType == 'pen'  :
    if useAggdraw == True:

                if  dash1 > 0 :
                    drawCanvas.create_line(x, y, x2, y2, fill=fillcolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                else:
                    uiName,drawCanvasName = GetElementName(drawCanvas)
                    if shapeTag in G_CanvasParamDictionary[uiName][drawCanvasName].keys():
                        if G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][5]:
                            left = x
                            right = x2
                            if x2 < x:
                                left = x2
                                right = x
                            top = y
                            bottom = y2        
                            if y2 < y:
                                top = y2
                                bottom = y
                            width = right - left + 2 * fillwidth
                            height = bottom - top + 2 * fillwidth
                            startx = x-left+fillwidth
                            starty =  y-top+fillwidth
                            endx = x2-left+fillwidth
                            endy = y2-top+fillwidth
                            img = Image.new('RGBA', (width, height), '#00000000')
                            draw = aggdraw.Draw(img)
                            p = aggdraw.Pen(fillcolor,fillwidth)
                            draw.line((x-left+fillwidth,y-top+fillwidth,x2-left+fillwidth,y2-top+fillwidth), p)
                            draw.flush()
                            newImage = ImageTk.PhotoImage(img)
                            G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][5] = newImage
                            drawCanvas.create_image(left-fillwidth, top-fillwidth,image=newImage,anchor='nw',tag=shapeTag)
                        else:
                            drawCanvas.create_line(x, y, x2, y2, fill=fillcolor,width = fillwidth,tag=shapeTag)
                    else:
                        drawCanvas.create_line(x, y, x2, y2, fill=fillcolor,width = fillwidth,tag=shapeTag)
    else:
                if  dash1 > 0 :
                    drawCanvas.create_line(x, y, x2, y2, fill=fillcolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                else:
                    drawCanvas.create_line(x, y, x2, y2,fill=fillcolor, width = fillwidth,tag=shapeTag)

        elif shapeType == 'arrow':
            if  dash1 > 0 :
                drawCanvas.create_line(x, y, x2, y2, arrow=tkinter.LAST,fill=fillcolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
            else:
                drawCanvas.create_line(x, y, x2, y2,arrow=tkinter.LAST,fill=fillcolor, width = fillwidth,tag=shapeTag)
        elif shapeType.find('triangle') == 0:
            width = x2 - x
            height = y2 - y
            direction = 'up'
            if shapeType.find('_left')>0:
                direction = 'left'
            elif shapeType.find('_right')>0:
                direction = 'right'
            elif shapeType.find('_down')>0:
                direction = 'down'
            if direction == 'left':
                points = [
                    x,
                    y + int(height/2),
                    x + width,
                    y ,
                    x + width,
                    y + height,
                    x,
                    y + int(height/2),]
            elif direction == 'right':
                points = [
                    x,
                    y,
                    x + width,
                    y + int(height/2) ,
                    x,
                    y + height,
                    x,
                    y,]
            elif direction == 'down':
                points = [
                    x,
                    y,
                    x + width,
                    y,
                    x + int(width/2),
                    y + height,
                    x,
                    y,]
            else:
                points = [
                    x,
                    y + height,
                    x + int(width/2),
                    y ,
                    x + width,
                    y + height,
                    x,
                    y + height,]
            if  fillcolor == \'None\':
                if  dash1 > 0 :
                    drawCanvas.create_polygon(
                        points,
                        outline=outlinecolor, 
                        width= fillwidth,
                        dash=(dash1,dash2),
                        tag=shapeTag)
                else :
                    drawCanvas.create_polygon(
                        points,
                        outline=outlinecolor, 
                        width= fillwidth,
                        tag=shapeTag)
            else:
                if  dash1 > 0 :
                    drawCanvas.create_polygon(
                        points,
                        fill=fillcolor,
                        outline=outlinecolor, 
                        width= fillwidth,
                        dash=(dash1,dash2),
                        tag=shapeTag)
                else :
                    drawCanvas.create_polygon(
                        points,
                        fill=fillcolor,
                        outline=outlinecolor, 
                        width= fillwidth,
                        tag=shapeTag)
        elif shapeType == 'diamond':
            width = x2 - x
            height = y2 - y
            points = [
                x,
                y + int(height/2),
                x + int(width/2),
                y ,
                x + width,
                y + int(height/2),
                x + int(width/2),
                y + height,]
            if  fillcolor == \'None\':
                if  dash1 > 0 :
                    drawCanvas.create_polygon(
                        points,
                        outline=outlinecolor, 
                        width= fillwidth,
                        dash=(dash1,dash2),
                        tag=shapeTag)
                else :
                    drawCanvas.create_polygon(
                        points,
                        outline=outlinecolor, 
                        width= fillwidth,
                        tag=shapeTag)
            else:
                if  dash1 > 0 :
                    drawCanvas.create_polygon(
                        points,
                        fill=fillcolor,
                        outline=outlinecolor, 
                        width= fillwidth,
                        dash=(dash1,dash2),
                        tag=shapeTag)
                else :
                    drawCanvas.create_polygon(
                        points,
                        fill=fillcolor,
                        outline=outlinecolor, 
                        width= fillwidth,
                        tag=shapeTag)
        elif shapeType == 'rect':
            if  fillcolor == \'None\':
                if  dash1 > 0 :
                    drawCanvas.create_rectangle(x, y, x2, y2, outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                else:
                    drawCanvas.create_rectangle(x, y, x2, y2,outline=outlinecolor, width = fillwidth,tag=shapeTag)
            else:
                if  dash1 > 0 :
                    drawCanvas.create_rectangle(x, y, x2, y2, fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                else:
                    drawCanvas.create_rectangle(x, y, x2, y2,fill=fillcolor,outline=outlinecolor, width = fillwidth,tag=shapeTag)
        elif shapeType == 'roundrect':
            width = x2 - x
            height = y2 - y
            if newImage:
                roundRadius = int(newImage)
            else:
                roundRadius = int(0.2 * height)
            if roundRadius == 0:
                if  dash1 > 0 :
                    drawCanvas.create_rectangle(x, y, x2, y2, fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                else:
                    drawCanvas.create_rectangle(x, y, x + width,y + height,fill=fillcolor, outline=outlinecolor,width = fillwidth,tag=shapeTag)
            else:
                drawCanvas.create_rectangle(x+roundRadius,y+roundRadius,x+width-roundRadius, y+height-roundRadius,fill=fillcolor, width = 0,tag=shapeTag)
                drawCanvas.create_rectangle(x+roundRadius,y,x+width-roundRadius,y+roundRadius,fill=fillcolor, width=0,tag=shapeTag)
                drawCanvas.create_rectangle(x+roundRadius,y+height-roundRadius,x+width-roundRadius,y+height,fill=fillcolor, width=0,tag=shapeTag)
                drawCanvas.create_rectangle(x,y+roundRadius,x+roundRadius,y+height-roundRadius,fill=fillcolor,width=0,tag=shapeTag)
                drawCanvas.create_rectangle(x+width-roundRadius,y+roundRadius,x+width,y+height-roundRadius,fill=fillcolor,width=0,tag=shapeTag)
            OutLineTag = shapeTag+"_outline"
            if fillwidth > 0:
                if  dash1 > 0:
                    drawCanvas.create_line(x+roundRadius,y,x+width-roundRadius,y,fill=outlinecolor,dash=(dash1,dash2),tag=OutLineTag,width=fillwidth)
                    drawCanvas.create_line(x+roundRadius,y+height,x+width-roundRadius,y+height,fill=outlinecolor,dash=(dash1,dash2),tag=OutLineTag,width=fillwidth)
                    drawCanvas.create_line(x,y+roundRadius,x,y+height-roundRadius,fill=outlinecolor,tag=OutLineTag,dash=(dash1,dash2),width=fillwidth)
                    drawCanvas.create_line(x+width,y+roundRadius,x+width,y+height-roundRadius,fill=outlinecolor,dash=(dash1,dash2),tag=OutLineTag,width=fillwidth)
                else:
                    drawCanvas.create_line(x+roundRadius,y,x+width-roundRadius,y,fill=outlinecolor,tag=OutLineTag,width=fillwidth)
                    drawCanvas.create_line(x+roundRadius,y+height,x+width-roundRadius,y+height,fill=outlinecolor,tag=OutLineTag,width=fillwidth)
                    drawCanvas.create_line(x,y+roundRadius,x,y+height-roundRadius,fill=outlinecolor,tag=OutLineTag,width=fillwidth)
                    drawCanvas.create_line(x+width,y+roundRadius,x+width,y+height-roundRadius,fill=outlinecolor,tag=OutLineTag,width=fillwidth)
            drawCanvas.create_arc(x,y,x+2*roundRadius,y+2*roundRadius,start=180,extent=-90,fill=fillcolor,outline=fillcolor,width=0,tag=shapeTag)
            drawCanvas.create_arc(x+width-2*roundRadius,y,x+width,y+2*roundRadius,extent=90,fill=fillcolor,outline=fillcolor,width=0,tag=shapeTag)
            drawCanvas.create_arc(x+width-2*roundRadius,y+height-2*roundRadius,x+width,y+height,extent=-90,fill=fillcolor,outline=fillcolor,width=0,tag=shapeTag)
            drawCanvas.create_arc(x,y+height-2*roundRadius,x+2*roundRadius,y+height,start=180,extent=90,fill=fillcolor,outline=fillcolor,width=0,tag=shapeTag)
            OutArcTag = shapeTag+"_arc"
            if fillwidth > 0:
                if  dash1 > 0:
                    drawCanvas.create_arc(x,y,x+2*roundRadius,y+2*roundRadius,start=180,extent=-90,outline=outlinecolor,dash=(dash1,dash2),width=fillwidth, style=\'arc\',tag=OutArcTag)
                    drawCanvas.create_arc(x+width-2*roundRadius,y,x+width,y+2*roundRadius,extent=90,outline=outlinecolor,dash=(dash1,dash2),width=fillwidth, style=\'arc\',tag=OutArcTag)
                    drawCanvas.create_arc(x+width-2*roundRadius,y+height-2*roundRadius,x+width,y+height,extent=-90,outline=outlinecolor,dash=(dash1,dash2),width=fillwidth, style=\'arc\',tag=OutArcTag)
                    drawCanvas.create_arc(x,y+height-2*roundRadius,x+2*roundRadius,y+height,start=180,extent=90,outline=outlinecolor,dash=(dash1,dash2),width=fillwidth, style=\'arc\',tag=OutArcTag)
                else:
                    drawCanvas.create_arc(x,y,x+2*roundRadius,y+2*roundRadius,start=180,extent=-90,outline=outlinecolor,width=fillwidth, style=\'arc\',tag=OutArcTag)
                    drawCanvas.create_arc(x+width-2*roundRadius,y,x+width,y+2*roundRadius,extent=90,outline=outlinecolor,width=fillwidth, style=\'arc\',tag=OutArcTag)
                    drawCanvas.create_arc(x+width-2*roundRadius,y+height-2*roundRadius,x+width,y+height,extent=-90,outline=outlinecolor,width=fillwidth, style=\'arc\',tag=OutArcTag)
                    drawCanvas.create_arc(x,y+height-2*roundRadius,x+2*roundRadius,y+height,start=180,extent=90,outline=outlinecolor,width=fillwidth, style=\'arc\',tag=OutArcTag)
        elif shapeType == 'circle':
    if useAggdraw == True:
                if  fillcolor == \'None\':
                    if  dash1 > 0 :
                        drawCanvas.create_oval(x, y, x2, y2, outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                    else:
                        width = x2 - x + 2 * fillwidth
                        height = y2 - y + 2 * fillwidth
                        img = Image.new('RGBA', (width, height), '#00000000')
                        draw = aggdraw.Draw(img)
                        p = aggdraw.Pen(outlinecolor,fillwidth)
                        draw.ellipse((fillwidth,fillwidth,width-fillwidth,height-fillwidth), p)
                        draw.flush()
                        newImage = ImageTk.PhotoImage(img)
                        uiName,drawCanvasName = GetElementName(drawCanvas)
                        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][5] = newImage
                        drawCanvas.create_image(x-fillwidth, y-fillwidth,image=newImage,anchor='nw',tag=shapeTag)
                else:
                    if  dash1 > 0 :
                        width = x2 - x + 2 * fillwidth
                        height = y2 - y + 2 * fillwidth
                        img = Image.new('RGBA', (width, height), '#00000000')
                        draw = aggdraw.Draw(img)
                        p = aggdraw.Pen(outlinecolor,0)
                        b = aggdraw.Brush(fillcolor)
                        draw.ellipse((fillwidth,fillwidth,width-fillwidth,height-fillwidth), p, b)
                        draw.flush()
                        newImage = ImageTk.PhotoImage(img)
                        uiName,drawCanvasName = GetElementName(drawCanvas)
                        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][5] = newImage
                        drawCanvas.create_image(x-fillwidth, y-fillwidth,image=newImage,anchor='nw',tag=shapeTag)
                        drawCanvas.create_oval(x, y, x2, y2, outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                    else:
                        width = x2 - x + 2 * fillwidth
                        height = y2 - y + 2 * fillwidth
                        img = Image.new('RGBA', (width, height), '#00000000')
                        draw = aggdraw.Draw(img)
                        p = aggdraw.Pen(outlinecolor,fillwidth)
                        b = aggdraw.Brush(fillcolor)
                        draw.ellipse((fillwidth,fillwidth,width-fillwidth,height-fillwidth), p, b)
                        draw.flush()
                        newImage = ImageTk.PhotoImage(img)
                        uiName,drawCanvasName = GetElementName(drawCanvas)
                        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][5] = newImage
                        drawCanvas.create_image(x-fillwidth, y-fillwidth,image=newImage,anchor='nw',tag=shapeTag)
    else:
                if  fillcolor == \'None\':
                    if  dash1 > 0 :
                        drawCanvas.create_oval(x, y, x2, y2, outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                    else:
                        drawCanvas.create_oval(x, y, x2, y2,outline=outlinecolor, width = fillwidth,tag=shapeTag)
                else:
                    if  dash1 > 0 :
                        drawCanvas.create_oval(x, y, x2, y2, fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                    else:
                        drawCanvas.create_oval(x, y, x2, y2,fill=fillcolor,outline=outlinecolor, width = fillwidth,tag=shapeTag)


        elif shapeType == 'cylinder':  
            width = x2 - x
            height = y2 - y
            OvalHeight = height * 0.2
            OvalHeight_Half = height * 0.1
            OutLineTag = shapeTag+"_outline"
            if  dash1 > 0 :
                drawCanvas.create_oval(x,y2-OvalHeight,x2,y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                drawCanvas.create_rectangle(x,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill=fillcolor,width=0,tag=shapeTag)
                drawCanvas.create_oval(x,y,x2,y+OvalHeight,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                drawCanvas.create_line(x,y+OvalHeight_Half,x,y2-OvalHeight_Half,fill=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=OutLineTag)
                drawCanvas.create_line(x2,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=OutLineTag)
            else:
                drawCanvas.create_oval(x,y2-OvalHeight,x2,y2,fill=fillcolor,outline=outlinecolor,width = fillwidth,tag=shapeTag)
                drawCanvas.create_rectangle(x,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill=fillcolor,width=0,tag=shapeTag)
                drawCanvas.create_oval(x,y,x2,y+OvalHeight,fill=fillcolor,outline=outlinecolor,width = fillwidth,tag=shapeTag)
                drawCanvas.create_line(x,y+OvalHeight_Half,x,y2-OvalHeight_Half,fill=outlinecolor,width = fillwidth,tag=OutLineTag)
                drawCanvas.create_line(x2,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill=outlinecolor,width = fillwidth,tag=OutLineTag)
        elif shapeType == 'star':
            center_x = (x + x2)/2
            center_y = (y + y2)/2
            rx = (x2 - x)/2
            ry = (y2 - y)/2
            points = [
                center_x - int(rx * math.sin(2 * math.pi / 5)),
                center_y - int(ry * math.cos(2 * math.pi / 5)),
                center_x + int(rx * math.sin(2 * math.pi / 5)),
                center_y - int(ry * math.cos(2 * math.pi / 5)),
                center_x - int(rx * math.sin(math.pi / 5)),
                center_y + int(ry * math.cos(math.pi / 5)),
                center_x,
                center_y - ry,
                center_x + int(rx * math.sin(math.pi / 5)),
                center_y + int(ry * math.cos(math.pi / 5)),
                ]
            if  dash1 > 0 :
                drawCanvas.create_polygon(
                    points,
                    fill=fillcolor,
                    outline=outlinecolor, 
                    width= fillwidth,
                    dash=(dash1,dash2),
                    tag=shapeTag)
            else :
                drawCanvas.create_polygon(
                    points,
                    fill=fillcolor,
                    outline=outlinecolor, 
                    width= fillwidth,
                    tag=shapeTag)
        elif shapeType == 'eraser':
            drawCanvas.create_rectangle(x, y, x2, y2,fill=fillcolor, width = 0,tag=shapeTag) 
        elif shapeType == 'grid':
            rows = int((y2 - y)/dash2)+1
            cows = int((x2 - x)/dash1)+1
            for i in range(rows):
                for j in range(cows):
                    if (i+j)%2 == 0:
                        tx = x + j*dash1
                        ty = y + i*dash2
                        drawCanvas.create_rectangle(tx, ty, tx+dash1, ty+dash2,fill=fillcolor, width = 0,tag=shapeTag) 
        elif shapeType == 'text':
            drawCanvas.create_text(x, y,fill=fillcolor,text=text,font = textFont,anchor='nw',tag=shapeTag)
        elif shapeType == 'button':
            center_x = (x + x2)/2
            center_y = (y + y2)/2
            if newImage:
                drawCanvas.create_image(x, y,image=newImage,anchor='nw',tag=shapeTag)
            else:
                oval_rx = 20
                OutLineTag = shapeTag+"_outline"
                half_width = int((fillwidth+1)/2)
                if  dash1 > 0 :
                    drawCanvas.create_oval(x,y,x+2*oval_rx,y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                    drawCanvas.create_oval(x2-2*oval_rx,y,x2,y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                    drawCanvas.create_rectangle(x+oval_rx, y, x2-oval_rx, y2+1,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2), width = fillwidth,tag=shapeTag)
                    drawCanvas.create_line(x+oval_rx, y+half_width, x+oval_rx, y2-half_width,fill=fillcolor,width = fillwidth,tag=shapeTag)
                    drawCanvas.create_line(x2-oval_rx, y+half_width, x2-oval_rx, y2-half_width,fill=fillcolor,width = fillwidth,tag=shapeTag)
                else:
                    drawCanvas.create_oval(x,y,x+2*oval_rx,y2,fill=fillcolor,outline=outlinecolor,width = fillwidth,tag=shapeTag)
                    drawCanvas.create_oval(x2-2*oval_rx,y,x2,y2,fill=fillcolor,outline=outlinecolor,width = fillwidth,tag=shapeTag)
    #f.write("                    drawCanvas.create_rectangle(x+oval_rx, y, x2-oval_rx, y2+1,fill=fillcolor,outline=outlinecolor, width = fillwidth,tag=shapeTag)
    #f.write("                    drawCanvas.create_line(x+oval_rx, y+half_width, x+oval_rx, y2-half_width,fill=fillcolor,width = fillwidth,tag=OutLineTag)
    #f.write("                    drawCanvas.create_line(x2-oval_rx, y+half_width, x2-oval_rx, y2-half_width,fill=fillcolor,width = fillwidth,tag=OutLineTag)

                    drawCanvas.create_rectangle(x+oval_rx+1, y + half_width, x2-oval_rx-1, y2+1-half_width,fill=fillcolor,outline=outlinecolor, width = 0,tag=shapeTag)
                    drawCanvas.create_line(x+oval_rx, y, x2-oval_rx, y,fill=outlinecolor,width = fillwidth,tag=OutLineTag)
                    drawCanvas.create_line(x+oval_rx, y2, x2-oval_rx, y2,fill=outlinecolor,width = fillwidth,tag=OutLineTag)    

            if len(text) > 0:
                drawCanvas.create_text(center_x, center_y,fill=textColor,text=text,font = textFont,anchor='center',tag=shapeTag+\"_text\")
        elif shapeType == 'image':
            if type(newImage) == type([]):
                drawCanvas.create_image(x, y,image=newImage[0][0],anchor='nw',tag=shapeTag)
            else:
                drawCanvas.create_image(x, y,image=newImage,anchor='nw',tag=shapeTag)
        elif shapeType == 'switch':
            SwitchWidth = x2 - x
            SwitchHeight = y2 - y
            Switch_radius = int(SwitchHeight/2)
            fillcolor = '#777777'
            drawCanvas.create_oval(x, y, x+SwitchHeight, y+SwitchHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
            drawCanvas.create_oval(x+(SwitchWidth-SwitchHeight), y, x+SwitchWidth,y+ SwitchHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
            drawCanvas.create_rectangle(x+Switch_radius,y,x+(SwitchWidth-Switch_radius),y+SwitchHeight,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
            drawCanvas.create_oval(x+2, y+2, x+(SwitchHeight-3), y+(SwitchHeight-3),fill=outlinecolor,width=0,tag=shapeTag)
            drawCanvas.create_text(x+(SwitchWidth-int(1.0*SwitchHeight)), y+int(SwitchHeight/2), text="Off",font = ("System",int(SwitchHeight/2)),anchor=\'center\',fill=outlinecolor,width=0,tag=shapeTag) 
        elif shapeType == 'listmenu':
            if  dash1 > 0 :
                drawCanvas.create_rectangle(x, y, x2, y2,fill='#FFFFFF', outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
            else:
                drawCanvas.create_rectangle(x, y, x2, y2,fill='#FFFFFF', outline=outlinecolor,width = fillwidth,tag=shapeTag)
            MenuInfo = newImage
            SubMenus = MenuInfo['SubMenus']
            ListMenuWidth = x2 - x
            ListMenuHeight = y2 - y
            SubMenuTitleHeight = 24
            SubMenuTitleSpacingX = 2
            SubMenuTitleSpacingY = 5
            SubMenuItemHeight = 22
            SubMenuItemSpacingX = 2
            SubMenuItemSpacingY = 4
            centerX = x + int(ListMenuWidth/2)
            SubMeshX = x + SubMenuTitleSpacingX
            SubMenuTitleHeight_Half = int(SubMenuTitleHeight/2)
            IconX = x+int(0.25 * ListMenuWidth)
            ListMenuTop = y + SubMenuTitleSpacingY
            for subMenu in SubMenus:
                titleText = subMenu[0]
                bgImgFile = subMenu[1]
                itemList = subMenu[2]
                subMeshTag = shapeTag + "_"+titleText
                drawCanvas.create_oval(SubMeshX, ListMenuTop, SubMeshX + SubMenuTitleHeight, ListMenuTop+SubMenuTitleHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=subMeshTag)
                drawCanvas.create_oval(x2-SubMenuTitleHeight, ListMenuTop, x2,ListMenuTop+ SubMenuTitleHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=subMeshTag)
                drawCanvas.create_rectangle(x+SubMenuTitleHeight_Half,ListMenuTop,x2-SubMenuTitleHeight_Half,ListMenuTop+SubMenuTitleHeight,fill=fillcolor,outline=outlinecolor,width=0, tag=subMeshTag)
                centerY = ListMenuTop + int(SubMenuTitleHeight/2)
                drawCanvas.create_text(centerX ,centerY,text=titleText,anchor=tkinter.CENTER,font=('Arial',14,'bold'),fill = outlinecolor,tag=subMeshTag) 
                ListMenuTop = ListMenuTop + (SubMenuTitleHeight + SubMenuTitleSpacingY)
                if subMenu[3] == True:
                    for itemInfo in itemList:
                        titleText = itemInfo[0]
                        centerY = ListMenuTop + int(SubMenuItemHeight/2)
                        drawCanvas.create_oval(IconX-5, centerY-5, IconX+5, centerY+5,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
                        drawCanvas.create_text(centerX ,centerY,text=titleText,anchor=tkinter.CENTER,font=('Arial',10,'bold'),fill = outlinecolor,tag=shapeTag) 
                        ListMenuTop = ListMenuTop + (SubMenuItemHeight + SubMenuItemSpacingY)
        elif shapeType == 'table':
            if  dash1 > 0 :
                drawCanvas.create_rectangle(x, y, x2, y2,fill='#FFFFFF', outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
            else:
                drawCanvas.create_rectangle(x, y, x2, y2,fill='#FFFFFF', outline=outlinecolor,width = fillwidth,tag=shapeTag)
            TableWidth = x2 - x
            TableHeight = y2 - y
            if TableHeight > 0:
                TableTopY = y
                TableInfo = newImage
                RowCount = len(TableInfo['rows'])
                CowInfo = TableInfo['cows']
                TableRowHeight = TableHeight
                if RowCount > 0:
                    TableRowHeight = TableHeight / RowCount
                RowTopY = TableTopY
                RowIndex = 0
                for rowInfoLine in TableInfo['rows']:
                    left = 0
                    CowIndex = 0
                    for rowInfo in rowInfoLine:
                        x1 = x + int(left * TableWidth) 
                        y1 = int(RowTopY)
                        x2 = x + int((left + CowInfo[CowIndex])* TableWidth) 
                        y2 = int(RowTopY + TableRowHeight)
                        CellText = rowInfo[0]
                        StyleIndex = rowInfo[1]
                        StyleInfo = TableInfo['style'][StyleIndex]
                        FillColor = StyleInfo[0]
                        if FillColor == '':
                            FillColor = '#FFFFFF'
                        FontIndex = StyleInfo[1]
                        TextAnchor = StyleInfo[2]
                        TextColor = StyleInfo[3]
                        if TextColor == '':
                            TextColor = '#000000'
                        BorderWidth = StyleInfo[4]
                        OutLineColor = StyleInfo[5]
                        if OutLineColor == '':
                            OutLineColor = '#000000'
                        drawCanvas.create_rectangle(x1,y1,x2,y2,fill = FillColor,outline = OutLineColor,width = BorderWidth,tag = 'drawing_shape')
                        #显示文字
                        if CellText != '':
                            if CellText.find("┇") >= 0:
                                drawCanvas.create_line(x1,y1,x2,y2,fill = OutLineColor,width = BorderWidth,tag = 'drawing_shape')
                                TextSplitArray = CellText.split('┇')
                                Text1 = TextSplitArray[0]
                                Text2 = TextSplitArray[1]
                                CellWidth  = x2 - x1
                                CellHeight = y2 - y1
                                cell_cx1 = x1 + int(CellWidth * 0.67)
                                cell_cy1 = y1 + int(CellHeight * 0.33)
                                TextAnchor1 = 'center'
                                cell_cx2 = x2 - int(CellWidth * 0.67)
                                cell_cy2 = y2 - int(CellHeight * 0.33)
                                TextAnchor2 = 'center'
                                if FontIndex >= 0:
                                    FontInfo = TableInfo['font'][FontIndex]
                                    fontName = FontInfo[0]
                                    fontSize = FontInfo[1]
                                    drawCanvas.create_text(cell_cx1,cell_cy1,fill=TextColor,text=Text1, font=(fontName,fontSize),anchor=TextAnchor1,tag='drawing_shape')
                                    drawCanvas.create_text(cell_cx2,cell_cy2,fill=TextColor,text=Text2, font=(fontName,fontSize),anchor=TextAnchor2,tag='drawing_shape')
                                else:
                                    drawCanvas.create_text(cell_cx1,cell_cy1,fill=TextColor,text=Text1, anchor=TextAnchor1,tag='drawing_shape')
                                    drawCanvas.create_text(cell_cx2,cell_cy2,fill=TextColor,text=Text2, anchor=TextAnchor2,tag='drawing_shape')
                            else:
                                cell_cx = int((x1 + x2)/2)
                                cell_cy = int((y1 + y2)/2)
                                #['WN','N','EN','W','CENTER','E','WS','S','ES','XY']
                                TextAnchor = TextAnchor.lower()
                                if TextAnchor == 'n' or TextAnchor == 'wn' or TextAnchor == 'en'  or TextAnchor == 'nw' or TextAnchor == 'ne':
                                    cell_cy = int(y1)
                                elif TextAnchor == 's' or TextAnchor == 'ws' or TextAnchor == 'es' or TextAnchor == 'sw' or TextAnchor == 'se':
                                    cell_cy = int(y2)
                                if TextAnchor == 'w' or TextAnchor == 'wn' or TextAnchor == 'ws' or TextAnchor == 'nw' or TextAnchor == 'sw':
                                    cell_cx = int(x1)
                                elif TextAnchor == 'e' or TextAnchor == 'en' or TextAnchor == 'es' or TextAnchor == 'ne' or TextAnchor == 'se':
                                    cell_cx = int(x2)
                                if FontIndex >= 0:
                                    FontInfo = TableInfo['font'][FontIndex]
                                    fontName = FontInfo[0]
                                    fontSize = FontInfo[1]
                                    drawCanvas.create_text(cell_cx,cell_cy,fill=TextColor,text=CellText, font=(fontName,fontSize),anchor=TextAnchor,tag='drawing_shape')
                                else:
                                    drawCanvas.create_text(cell_cx,cell_cy,fill=TextColor,text=CellText, anchor=TextAnchor,tag='drawing_shape')
                        left = left + CowInfo[CowIndex]
                        CowIndex = CowIndex + 1
                    RowTopY = RowTopY + TableRowHeight
                    RowIndex = RowIndex + 1
                for mergeCell in TableInfo['merge']:
                    BeginRow = mergeCell[0][0]
                    BeginCow = mergeCell[0][1]
                    EndRow = mergeCell[1][0]
                    EndCow = mergeCell[1][1]
                    CellText = mergeCell[2]
                    StyleIndex = mergeCell[3]
                    StyleInfo = TableInfo['style'][StyleIndex]
                    FillColor = StyleInfo[0]
                    if FillColor == '':
                        FillColor = '#FFFFFF'
                    FontIndex = StyleInfo[1]
                    TextAnchor = StyleInfo[2]
                    TextColor = StyleInfo[3]
                    if TextColor == '':
                        TextColor = '#000000'
                    BorderWidth = StyleInfo[4]
                    BorderColor = StyleInfo[5]
                    if BorderColor == '':
                        BorderColor = '#000000'
                    Left = x + TableWidth
                    Right = x 
                    Top = TableTopY + TableHeight
                    Bottom = TableTopY
                    RowTopY = TableTopY
                    RowIndex = 0
                    for rowInfoLine in TableInfo['rows']:
                        left = 0
                        CowIndex = 0
                        for rowInfo in rowInfoLine:
                            x1 = x + int(left * TableWidth)
                            y1 = int(RowTopY)
                            x2 = x + int((left + CowInfo[CowIndex])* TableWidth)
                            y2 = int(RowTopY + TableRowHeight)
                            if checkPtInRect(CowIndex,RowIndex,BeginCow,EndCow,BeginRow,EndRow) == True:
                                if x1 < Left:
                                    Left = x1
                                if y1 < Top:
                                    Top = y1
                                if x2 > Right:
                                    Right = x2
                                if y2 > Bottom:
                                    Bottom = y2
                            left = left + CowInfo[CowIndex]
                            CowIndex = CowIndex + 1
                        RowTopY = RowTopY + TableRowHeight
                        RowIndex = RowIndex + 1
                    if Right >= Left and Bottom >= Top:
                        drawCanvas.create_rectangle(Left,Top,Right,Bottom,fill = FillColor,outline = BorderColor,width = BorderWidth,tag = 'drawing_shape')
                        #显示文字
                        if CellText != '':
                            if CellText.find('┇') >= 0:
                                drawCanvas.create_line(Left,Top,Right,Bottom,fill = BorderColor,width = BorderWidth,tag = 'drawing_shape')
                                TextSplitArray = CellText.split('┇')
                                Text1 = TextSplitArray[0]
                                Text2 = TextSplitArray[1]
                                CellWidth  = Right - Left
                                CellHeight = Bottom - Top
                                cell_cx1 = Left + int(CellWidth * 0.67)
                                cell_cy1 = Top + int(CellHeight * 0.33)
                                TextAnchor1 = 'center'
                                cell_cx2 = Left + int(CellWidth * 0.33)
                                cell_cy2 = Top + int(CellHeight * 0.67)
                                TextAnchor2 = 'center'
                                if FontIndex >= 0:
                                    FontInfo = TableInfo['font'][FontIndex]
                                    fontName = FontInfo[0]
                                    fontSize = FontInfo[1]
                                    drawCanvas.create_text(cell_cx1,cell_cy1,fill=TextColor,text=Text1, font=(fontName,fontSize),anchor=TextAnchor1,tag='drawing_shape')
                                    drawCanvas.create_text(cell_cx2,cell_cy2,fill=TextColor,text=Text2, font=(fontName,fontSize),anchor=TextAnchor2,tag='drawing_shape')
                                else:
                                    drawCanvas.create_text(cell_cx1,cell_cy1,fill=TextColor,text=Text1, anchor=TextAnchor1,tag='drawing_shape')
                                    drawCanvas.create_text(cell_cx2,cell_cy2,fill=TextColor,text=Text2, anchor=TextAnchor2,tag='drawing_shape')
                            else:
                                cell_cx = int((Left + Right)/2)
                                cell_cy = int((Top + Bottom)/2)
                                #['WN','N','EN','W','CENTER','E','WS','S','ES','XY']
                                if TextAnchor == 'n' or TextAnchor == 'wn' or TextAnchor == 'en'  or TextAnchor == 'nw' or TextAnchor == 'ne':
                                    cell_cy = int(Top)
                                elif TextAnchor == 's' or TextAnchor == 'ws' or TextAnchor == 'es' or TextAnchor == 'sw' or TextAnchor == 'se':
                                    cell_cy = int(Bottom)
                                if TextAnchor == 'w' or TextAnchor == 'wn' or TextAnchor == 'ws' or TextAnchor == 'nw' or TextAnchor == 'sw':
                                    cell_cx = int(Left)
                                elif TextAnchor == 'e' or TextAnchor == 'en' or TextAnchor == 'es' or TextAnchor == 'ne' or TextAnchor == 'se':
                                    cell_cx = int(Right)
                                if FontIndex >= 0:
                                    FontInfo = TableInfo['font'][FontIndex]
                                    fontName = FontInfo[0]
                                    fontSize = FontInfo[1]
                                    drawCanvas.create_text(cell_cx,cell_cy,fill=TextColor,text=CellText, font=(fontName,fontSize),anchor=TextAnchor,tag='drawing_shape')
                                else:
                                    drawCanvas.create_text(cell_cx,cell_cy,fill=TextColor,text=CellText, anchor=TextAnchor,tag='drawing_shape')



def DrawLine(uiName,drawCanvasName,x1,y1,x2,y2,color,width=1,dash=(0,0),shapeTag=''):
    """'+Language.G_Language[1450]+'"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('line_') == 0:
                NameSplitArray = ShepTagName.partition('line_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("line_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[\'line\',x1,y1,x2,y2,color,color,width,dash[0],dash[1]]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,color,width,dash[0],dash[1],None,'',None,'']
    DoCanvasRecord(drawCanvas,'line',x1,y1,x2,y2,color,color,width,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag
def DrawArrow(uiName,drawCanvasName,x1,y1,x2,y2,color,width=1,dash=(0,0),shapeTag=''):
    """'+Language.G_Language[1451]+'"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('arrow_') == 0:
                NameSplitArray = ShepTagName.partition('arrow_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("arrow_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[\'arrow\',x1,y1,x2,y2,color,color,width,dash[0],dash[1]]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,color,width,dash[0],dash[1],None,'',None,'']
    DoCanvasRecord(drawCanvas,'arrow',x1,y1,x2,y2,color,color,width,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag

def DrawTriangle(uiName,drawCanvasName,direction,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):
    """'+Language.G_Language[1453]+'"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    TriangleType = "triangle_up"
    if direction == "down":
        TriangleType = "triangle_down"
    if direction == "left":
        TriangleType = "triangle_left"
    if direction == "right":
        TriangleType = "triangle_right"
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('triangle_') == 0:
                NameSplitArray = ShepTagName.partition('triangle_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("triangle_%d"%Index)
    G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[TriangleType,x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,outlinecolor,outlinewidth,dash[0],dash[1],None,'',None,'']
    DoCanvasRecord(drawCanvas,TriangleType,x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag
def DrawRectangle(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):
    """'+Language.G_Language[1452]+'"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('rect_') == 0:
                NameSplitArray = ShepTagName.partition('rect_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("rect_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[\'rect\',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,outlinecolor,outlinewidth,dash[0],dash[1],None,'',None,'']
    DoCanvasRecord(drawCanvas,'rect',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag

def DrawRoundedRectangle(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),roundRadius=10,shapeTag=''):
    """'+Language.G_Language[1462]+'"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('roundrect_') == 0:
                NameSplitArray = ShepTagName.partition('roundrect_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("roundrect_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[\'roundrect\',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,outlinecolor,outlinewidth,dash[0],dash[1],None,'',None,'']
    DoCanvasRecord(drawCanvas,'roundrect',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash1=dash[0],dash2=dash[1],newImage=roundRadius,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag

def DrawCircle(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):
    """'+Language.G_Language[1454]+'"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('circle_') == 0:
                NameSplitArray = ShepTagName.partition('circle_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("circle_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[\'circle\',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,outlinecolor,outlinewidth,dash[0],dash[1],None,'',None,'']
    DoCanvasRecord(drawCanvas,'circle',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag
def DrawDiamond(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):
    """'+Language.G_Language[1455]+'"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('diamond_') == 0:
                NameSplitArray = ShepTagName.partition('diamond_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("diamond_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[\'diamond\',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,outlinecolor,outlinewidth,dash[0],dash[1],None,'',None,'']
    DoCanvasRecord(drawCanvas,'diamond',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag
def DrawCylinder(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):
    """'+Language.G_Language[1456]+'"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('cylinder_') == 0:
                NameSplitArray = ShepTagName.partition('cylinder_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("cylinder_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[\'cylinder\',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,outlinecolor,outlinewidth,dash[0],dash[1],None,'',None,'']
    DoCanvasRecord(drawCanvas,'cylinder',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag
def DrawStar(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):
    """'+Language.G_Language[1457]+'"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('star_') == 0:
                NameSplitArray = ShepTagName.partition('star_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("star_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[\'star\',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,outlinecolor,outlinewidth,dash[0],dash[1],None,'',None,'']
    DoCanvasRecord(drawCanvas,'star',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag
def DrawText(uiName,drawCanvasName,x,y,text,textFont=None,color='#FFFFFF',anchor='nw',shapeTag=''):
    """'+Language.G_Language[1458]+'"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('text_') == 0:
                NameSplitArray = ShepTagName.partition('text_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("text_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[\'text\',x,y,x,y,text,textFont,color]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,color,0,0,0,None,text,textFont,color]
    drawCanvas.create_text(x, y,fill=color,text=text,font = textFont,anchor=anchor,tag=shapeTag)
    return shapeTag
def DrawImage(uiName,drawCanvasName,x1,y1,x2,y2,imagefile,shapeTag=''):
    """'+Language.G_Language[1459]+'"""
    global G_ResDir
    global G_ResourcesFileList
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    newImage = None
    hasGIFAnimation = False
    w = x2 - x1
    h = y2 - y1
    if uiName and uiName in G_CanvasImageDictionary:
        if drawCanvasName and drawCanvasName in G_CanvasImageDictionary[uiName]:
            for ImageInfo in G_CanvasImageDictionary[uiName][drawCanvasName]:
                if ImageInfo[0] == imagefile and ImageInfo[2] == w and ImageInfo[3] == h :
                    newImage = ImageInfo[1]
                    break
    else:
        return
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('image_') == 0:
                NameSplitArray = ShepTagName.partition('image_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("image_%d"%Index)
    if newImage == None:
        resourPath = imagefile
        imagefile_Lower = imagefile.lower()
        if imagefile_Lower in G_ResourcesFileList:
            resourPath = G_ResourcesFileList[imagefile_Lower]
        if type(resourPath) == type(""):
            if os.path.exists(resourPath) == True:
                try:
                    if imagefile.find('.gif') >= 0:
                        GifData = Image.open(resourPath)
                        seq = []
                        try:
                            while 1:
                                imageRGBA = GifData.copy().convert('RGBA')
                                resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                newImage = ImageTk.PhotoImage(resizeImage)
                                seq.append(newImage)
                                GifData.seek(len(seq))
                        except EOFError:
                            pass
                        delay = 100
                        try:
                            delay = GifData.info['duration']
                        except KeyError:
                            delay = 100
                        if delay == 0:
                            delay = 100
                        newImage = [seq,delay,0]
                        hasGIFAnimation = True
                    else:
                        imageRGBA = Image.open(resourPath).convert('RGBA')
                        resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                        newImage = ImageTk.PhotoImage(resizeImage)
                    if drawCanvasName not in G_CanvasImageDictionary[uiName]:
                        G_CanvasImageDictionary[uiName][drawCanvasName] = []
                    G_CanvasImageDictionary[uiName][drawCanvasName].append([imagefile,newImage,w,h])
                except:
                    return 
        elif type(imagefile) == type(Image):
            imageRGBA = imagefile
            resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
            newImage = ImageTk.PhotoImage(resizeImage)
            if drawCanvasName not in G_CanvasImageDictionary[uiName]:
                G_CanvasImageDictionary[uiName][drawCanvasName] = []
            G_CanvasImageDictionary[uiName][drawCanvasName].append([imagefile,newImage,w,h])
    if newImage:
        if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[\'image\',x1,y1,x2,y2,newImage,imagefile]
        if drawCanvasName not in G_CanvasParamDictionary[uiName]:
            G_CanvasParamDictionary[uiName][drawCanvasName] = {}
        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=['#FFFFFF','#FFFFFF',0,0,0,newImage,'',None,'#FFFFFF']
        DoCanvasRecord(drawCanvas,'image',x1,y1,x2,y2,\'#FFFFFF\',\'#FFFFFF\',0,dash1=0,dash2=0,newImage=newImage,text='',textFont = None,textColor='',shapeTag=shapeTag)
        if hasGIFAnimation == True:
            drawCanvas.after(100,lambda: updateGIFFrame(uiName,drawCanvasName))
def DrawButton(uiName,drawCanvasName,x1,y1,x2,y2,text='',textcolor='#000000',textFont = None,fillcolor='#FFFFFF',outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):
    """'+Language.G_Language[1461]+'"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    center_x = (x1 + x2)/2
    center_y = (y1 + y2)/2
    oval_rx = 20
    dash1=dash[0],dash2=dash[1]
    OutLineTag = shapeTag+"_outline"
    half_width = int((outlinewidth+1)/2)
    if shapeTag == '':
        Index = 0
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            if ShepTagName.find('button_') == 0:
                NameSplitArray = ShepTagName.partition('button_')
                if NameSplitArray[2].isdigit() == True:
                    Number = int(NameSplitArray[2])
                    if Number > Index:
                        Index = Number
        Index = Index + 1
        shapeTag = str("button_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[\'button\',x1,y1,x2,y2,text,textcolor,textFont,fillcolor,outlinecolor,outlinewidth,dash[0],dash[1],None]
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fillcolor,outlinecolor,outlinewidth,dash[0],dash[1],None,text,textFont,textcolor]
    if  dash1 > 0 :
        drawCanvas.create_oval(x1,y1,x1+2*oval_rx,y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = outlinewidth,tag=shapeTag)
        drawCanvas.create_oval(x2-2*oval_rx,y1,x2,y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = outlinewidth,tag=shapeTag)
        drawCanvas.create_rectangle(x1+oval_rx, y1, x2-oval_rx, y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2), width = outlinewidth,tag=shapeTag)
        drawCanvas.create_line(x1+oval_rx, y1+half_width, x1+oval_rx, y2-half_width,fill=fillcolor,width = outlinewidth,tag=OutLineTag)
        drawCanvas.create_line(x2-oval_rx, y1+half_width, x2-oval_rx, y2-half_width,fill=fillcolor,width = outlinewidth,tag=OutLineTag)
    else:
        drawCanvas.create_oval(x1,y1,x1+2*oval_rx,y2,fill=fillcolor,outline=outlinecolor,width = outlinewidth,tag=shapeTag)
        drawCanvas.create_oval(x2-2*oval_rx,y1,x2,y2,fill=fillcolor,outline=outlinecolor,width = outlinewidth,tag=shapeTag)
        drawCanvas.create_rectangle(x1+oval_rx, y1, x2-oval_rx, y2,fill=fillcolor,outline=outlinecolor, width = outlinewidth,tag=shapeTag)
        drawCanvas.create_line(x1+oval_rx, y1+half_width, x1+oval_rx, y2-half_width,fill=fillcolor,width = outlinewidth,tag=OutLineTag)
        drawCanvas.create_line(x2-oval_rx, y1+half_width, x2-oval_rx, y2-half_width,fill=fillcolor,width = outlinewidth,tag=OutLineTag)
    if len(text) > 0:
        drawCanvas.create_text(center_x, center_y,text=text,fill=textcolor,anchor='center',tag=shapeTag+\"_text\")
def EraserCanvas(uiName,drawCanvasName,x1,y1,x2,y2):
    """'+Language.G_Language[1460]+'"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    bgcolor = drawCanvas.cget('bg')
    DoCanvasRecord(drawCanvas,'eraser',x1,y1,x2,y2,bgcolor,bgcolor,0,dash1=0,dash2=0,newImage=None,text='',textFont = None,textColor='',shapeTag='')
def SetCanvasGridBG(uiName,drawCanvasName,bgcolor='#888888',tile_width=20,tile_height=20):
    """'+Language.G_Language[9202]+'"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    canvasWidth = drawCanvas.winfo_width()
    canvasHeight = drawCanvas.winfo_height()
    DoCanvasRecord(drawCanvas,'grid',0,0,canvasWidth,canvasHeight,bgcolor,bgcolor,0,dash1=tile_width,dash2=tile_height,newImage=None,text='',textFont = None,textColor='',shapeTag='grid_bg')

''' 
    f.write(code)
#写入画板动作
def WriteLoadCanvasRecordFunction(f):
    code='''
    #f.write(Language.G_Language[1235]+'
def checkPtInRect(x,y,left,right,top,bottom):
    if x < left:return 0
    if x > right:return 0
    if y < top:return 0
    if y > bottom:return 0
    return 1
def Shape_MouseEvent(event,uiName,canvasName,shapeTag,eventName):
    if eventName == 'MouseLeave':
        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]
        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]
        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]
        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]
        if type(x1) == type(1.0):
            x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
        if type(y1) == type(1.0):
            y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
        if type(x2) == type(1.0):
            if x2 <= 1.0:
                x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
            else:
                x2 = x1 + int(x2)
        if type(y2) == type(1.0):
            if y2 <= 1.0:
                y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
            else:
                y2 = y1 + int(y2)
        borderwidth = 0
        if G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'button':
            borderwidth = 1 + G_CanvasShapeDictionary[uiName][canvasName][shapeTag][10]
        if checkPtInRect(event.x,event.y,x1+borderwidth,x2-borderwidth,y1+borderwidth,y2-borderwidth) == 1:
            return 
    if shapeTag not in G_CanvasEventDictionary[uiName][canvasName]:
        return
    if eventName not in G_CanvasEventDictionary[uiName][canvasName][shapeTag]:
        return
    for actionInfo in G_CanvasEventDictionary[uiName][canvasName][shapeTag][eventName]:
        if actionInfo[0] == "SetShapeRect":
            SetShapeRect(uiName ,canvasName,actionInfo[1],actionInfo[2],actionInfo[3],actionInfo[4],actionInfo[5])
        elif actionInfo[0] == "SetFillColor":
            SetShapeFillColor(uiName ,canvasName,actionInfo[1],actionInfo[2])
        elif actionInfo[0] == "SetOutlineColor":
            SetShapeOutlineColor(uiName ,canvasName,actionInfo[1],actionInfo[2])
        elif actionInfo[0] == "ChangeImage":
            SetShapeImage(uiName ,canvasName,actionInfo[1],actionInfo[2])
        elif actionInfo[0] == "ChangeText":
            SetShapeText(uiName ,canvasName,actionInfo[1],actionInfo[2],actionInfo[3])
        elif actionInfo[0] == "JumpToUI":
            UIPath, UIFile = os.path.split(actionInfo[2])
            UIName, extension = os.path.splitext(UIFile)
            if len(UIPath) > 0:
                import sys
                sys.path.append(UIPath)
            GoToUIDialog(uiName,UIName)
        elif actionInfo[0] == "LoadUI":
            WidgetName = actionInfo[2]
            UIPath, UIFile = os.path.split(actionInfo[3])
            UIName, extension = os.path.splitext(UIFile)
            if len(UIPath) > 0:
                import sys
                sys.path.append(UIPath)
            if WidgetName == "Form_1":
                WidgetName == "root"
            LoadUIDialog(uiName,WidgetName,UIName)
        elif actionInfo[0] == "DeleteShape":
            DeleteShape(uiName ,canvasName,actionInfo[1])
        elif actionInfo[0] == "OnSwitch":
            OnSwitch(uiName ,canvasName,actionInfo[1],actionInfo)
        elif actionInfo[0] == "OnExpandOrShrink":
            OnExpandOrShrink(uiName ,canvasName,actionInfo[1],actionInfo)
        elif actionInfo[0] == "CallFunction":
            if actionInfo[1]:
                if actionInfo[2]:
                   actionInfo[1](event,uiName,canvasName,actionInfo[2])
                else:
                   actionInfo[1](event,uiName,canvasName)
def updateGIFFrame(uiName,elementName):
    """'+Language.G_Language[1470]+'"""
    global G_CanvasShapeDictionary
    global G_CanvasImageDictionary
    Control = GetElement(uiName,elementName)
    if elementName in G_CanvasShapeDictionary[uiName].keys():
        for shapeTag in G_CanvasShapeDictionary[uiName][elementName]:
            ShapeInfo = G_CanvasShapeDictionary[uiName][elementName][shapeTag]
            if ShapeInfo[0] == 'image':
                if type(ShapeInfo[5]) == type([]):
                    FrameIndex = ShapeInfo[5][2]
                    FrameImages = ShapeInfo[5][0]
                    x = ShapeInfo[1]
                    y = ShapeInfo[2]
                    newImage = FrameImages[FrameIndex]
                    Control.delete(shapeTag)
                    Control.create_image(x, y,image=newImage,anchor='nw',tag=shapeTag)
                    FrameIndex = FrameIndex + 1
                    if FrameIndex == len(FrameImages):
                         FrameIndex = 0
                    ShapeInfo[5][2] = FrameIndex
    if uiName in G_CanvasImageDictionary:
        if elementName in G_CanvasImageDictionary[uiName].keys():
            if hasattr(Control,"GetEntry") == True:
                Control = Control.GetEntry()
            if Control != None:     
                for imageInfo in G_CanvasImageDictionary[uiName][elementName]:
                    if type(imageInfo) == type([]):
                        GifData = imageInfo[1]
                        FrameSequ = GifData[0]
                        FrameIndex = GifData[2]
                        if elementName.find('Text_') >= 0:
                            if GifData[3]:
                                Control.delete(GifData[3])
                                GifData[3] = Control.image_create(tkinter.END, image=FrameSequ[FrameIndex])
                            else:
                                GifData[3] = Control.image_create(tkinter.END, image=FrameSequ[FrameIndex])
                        elif elementName.find('Label_') >= 0 or elementName.find('Button_') >= 0 or elementName.find('RadioButton_') >= 0 or elementName.find('CheckButton_') >= 0:
                            Control.configure(image = FrameSequ[FrameIndex])
                        FrameIndex = FrameIndex + 1
                        if FrameIndex == len(FrameSequ):
                            FrameIndex = 0
                        GifData[2] = FrameIndex
    if Control:
        Control.after(100,lambda: updateGIFFrame(uiName,elementName)) 
def LoadCanvasRecord(uiName,UIScale=1.0):
    """'+Language.G_Language[1235]+'"""
    global G_ExeDir
    global G_ResDir
    global G_ResourcesFileList
    drawCanvasName = None
    drawCanvas = None
    drawCanvas_width = 0
    drawCanvas_height = 0
    canvasFile = os.path.join(G_ResDir,uiName + ".cav")
    if os.path.exists(canvasFile) == False:
        file_path = os.path.abspath(__file__)  
        checkExeDir = os.path.dirname(file_path)  
        checkResDir = os.path.join(checkExeDir,"Resources")  
        canvasFile = os.path.join(G_ResDir,uiName + ".cav")  
        if os.path.exists(canvasFile) == False:  
            if uiName.find("_") > 0:  
                endIndex = uiName.rfind("_")  
                originalName = uiName[0:endIndex]  
                canvasFile = os.path.join(G_ResDir,originalName + ".cav")  
                if os.path.exists(canvasFile) == False:  
                    file_path = os.getcwd()  
                    checkExeDir = os.path.dirname(file_path)  
                    checkResDir = os.path.join(checkExeDir,"Resources")  
                    if os.path.exists(canvasFile) == False:  
                        return
                    else:  
                        G_ExeDir = checkExeDir
                        G_ResDir = checkResDir
                else:  
                    G_ExeDir = checkExeDir
                    G_ResDir = checkResDir
        else:  
            G_ExeDir = checkExeDir
            G_ResDir = checkResDir
    if os.path.exists(canvasFile) == True:
        f = open(canvasFile,encoding='utf-8')
        line ="" 
        while True:
            line = f.readline()
            if not line:
                break
            text = line.strip()
            if not text:
                continue
            if text.find('Canvas:') >= 0:
                splitArray = text.split(':')
                drawCanvasName = splitArray[1].strip()
                drawCanvas = GetElement(uiName,drawCanvasName)
                drawCanvas_width = drawCanvas.winfo_width()
                drawCanvas_height = drawCanvas.winfo_height()
                if drawCanvasName == "Form_1":
                    root = GetElement(uiName,"root")
                    drawCanvas_width = root.winfo_width()
                    drawCanvas_height = root.winfo_height()
                G_CanvasSizeDictionary[uiName][drawCanvasName] = [drawCanvas_width,drawCanvas_height]
                G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
                G_CanvasParamDictionary[uiName][drawCanvasName] = {}
                G_CanvasFontDictionary[uiName][drawCanvasName] = []
                G_CanvasImageDictionary[uiName][drawCanvasName] = []
                G_CanvasPointDictionary[uiName][drawCanvasName] = {}
                G_CanvasEventDictionary[uiName][drawCanvasName] = {}
                continue
            elif text.find(',') >= 0:
                if drawCanvas != None:
                    splitArray = text.split(',')
                    splitCount = len(splitArray)
                    ShapeType = splitArray[0]
                    if ShapeType == 'image':
                        if splitArray[1].find('.') > 0:
                            x1 = float(splitArray[1])
                        else:
                            x1 = int(splitArray[1])
                            x1 = int(x1 * UIScale)
                        if splitArray[2].find('.') > 0:
                            y1 = float(splitArray[2])
                        else:
                            y1 = int(splitArray[2])
                            y1 = int(y1 * UIScale)
                        if splitArray[3].find('.') > 0:
                            x2 = float(splitArray[3])
                        else:
                            x2 = int(splitArray[3])
                            x2 = int(x2 * UIScale)
                        if splitArray[4].find('.') > 0:
                            y2 = float(splitArray[4])
                        else:
                            y2 = int(splitArray[4])
                            y2 = int(y2 * UIScale)
                        w = x2 - x1
                        if isinstance(w,float) == True:
                            w = w * drawCanvas_width
                        h = y2 - y1
                        if isinstance(h,float) == True:
                            h = h * drawCanvas_height
                        fill = splitArray[5]
                        outline = splitArray[6]
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        imagefile = splitArray[10]
                        newImage = None
                        newtext = ''
                        textFont = None
                        textColor=''
                        shapeTag = ''
                        if len(splitArray) > 12:
                            shapeTag = splitArray[11]
                        for ImageInfo in G_CanvasImageDictionary[uiName][drawCanvasName]:
                            if ImageInfo[0] == imagefile and ImageInfo[2] == w and ImageInfo[3] == h :
                                newImage = ImageInfo[1]
                                continue
                        if newImage == None:
                            imagefile_Lower = imagefile.lower()
                            if imagefile_Lower in G_ResourcesFileList:
                                resourPath = G_ResourcesFileList[imagefile_Lower]
                                if os.path.exists(resourPath) == True:
                                    try:
                                        imageRGBA = Image.open(resourPath).convert('RGBA')
                                        resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                        newImage = ImageTk.PhotoImage(resizeImage)
                                    except:
                                        pass 
                            G_CanvasImageDictionary[uiName][drawCanvasName].append([imagefile,newImage,w,h])
                        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,newImage,imagefile]
                        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                    elif ShapeType == 'text':
                        if splitArray[1].find('.') > 0:
                            x1 = float(splitArray[1])
                        else:
                            x1 = int(splitArray[1])
                            x1 = int(x1 * UIScale)
                        if splitArray[2].find('.') > 0:
                            y1 = float(splitArray[2])
                        else:
                            y1 = int(splitArray[2])
                            y1 = int(y1 * UIScale)
                        if splitArray[3].find('.') > 0:
                            x2 = float(splitArray[3])
                        else:
                            x2 = int(splitArray[3])
                            x2 = int(x2 * UIScale)
                        if splitArray[4].find('.') > 0:
                            y2 = float(splitArray[4])
                        else:
                            y2 = int(splitArray[4])
                            y2 = int(y2 * UIScale)
                        w = x2 - x1
                        if isinstance(w,float) == True:
                            w = w * drawCanvas_width
                        h = y2 - y1
                        if isinstance(h,float) == True:
                            h = h * drawCanvas_height
                        fill = splitArray[5]
                        outline = splitArray[6]
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        imagefile = ''
                        newImage = None
                        shapeTag = ''
                        newtext = splitArray[10]
                        for i in range(11,splitCount-8):
                            newtext = newtext + ","+splitArray[i]                
                        familytext = splitArray[-8]
                        sizetext = int(int(splitArray[-7]) * UIScale)
                        sizetext = str(sizetext)
                        weighttext = splitArray[-6]
                        slanttext = splitArray[-5]
                        underlinetext = splitArray[-4]
                        overstriketext = splitArray[-3]
                        textColor=''
                        textFont = tkinter.font.Font(family=familytext, size=sizetext,weight=weighttext,slant=slanttext,underline=underlinetext,overstrike=overstriketext)
                        shapeTag = splitArray[-2]
                        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,newtext,textFont,fill]
                        #字体
                        fontFind = False
                        for fontInfo in G_CanvasFontDictionary[uiName][drawCanvasName]:
                            if fontInfo[1] == familytext and fontInfo[2] == sizetext and fontInfo[3] == weighttext and fontInfo[4] == slanttext and fontInfo[5] == underlinetext and fontInfo[6] == overstriketext:
                                fontFind = True
                                continue
                        if fontFind == False:
                            G_CanvasFontDictionary[uiName][drawCanvasName].append([textFont,familytext,sizetext,weighttext,slanttext,underlinetext,overstriketext])
                        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                    elif ShapeType == 'button':
                        if splitArray[1].find('.') > 0:
                            x1 = float(splitArray[1])
                        else:
                            x1 = int(splitArray[1])
                            x1 = int(x1 * UIScale)
                        if splitArray[2].find('.') > 0:
                            y1 = float(splitArray[2])
                        else:
                            y1 = int(splitArray[2])
                            y1 = int(y1 * UIScale)
                        if splitArray[3].find('.') > 0:
                            x2 = float(splitArray[3])
                        else:
                            x2 = int(splitArray[3])
                            x2 = int(x2 * UIScale)
                        if splitArray[4].find('.') > 0:
                            y2 = float(splitArray[4])
                        else:
                            y2 = int(splitArray[4])
                            y2 = int(y2 * UIScale)
                        w = x2 - x1
                        if isinstance(w,float) == True:
                            w = w * drawCanvas_width
                        h = y2 - y1
                        if isinstance(h,float) == True:
                            h = h * drawCanvas_height
                        fill = splitArray[5]
                        outline = splitArray[6]
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        shapeTag = ''
                        newtext = splitArray[10]
                        for i in range(11,splitCount-11):
                            newtext = newtext + ","+splitArray[i]         
                        familytext = splitArray[-11]
                        sizetext = int(int(splitArray[-10]) * UIScale)
                        sizetext = str(sizetext)
                        weighttext = splitArray[-9]
                        slanttext = splitArray[-8]
                        underlinetext = splitArray[-7]
                        overstriketext = splitArray[-6]
                        textColor = splitArray[-5]
                        textFont = None
                        if len(familytext) > 0:
                            textFont = tkinter.font.Font(family=familytext, size=sizetext,weight=weighttext,slant=slanttext,underline=underlinetext,overstrike=overstriketext)
                            #字体
                            fontFind = False
                            for fontInfo in G_CanvasFontDictionary[uiName][drawCanvasName]:
                                if fontInfo[1] == familytext and fontInfo[2] == sizetext and fontInfo[3] == weighttext and fontInfo[4] == slanttext and fontInfo[5] == underlinetext and fontInfo[6] == overstriketext:
                                    fontFind = True
                                    continue
                            if fontFind == False:
                                G_CanvasFontDictionary[uiName][drawCanvasName].append([textFont,familytext,sizetext,weighttext,slanttext,underlinetext,overstriketext])
                        imagefile = splitArray[-4]
                        newImage = None
                        if imagefile != "":
                            for ImageInfo in G_CanvasImageDictionary[uiName][drawCanvasName]:
                                if ImageInfo[0] == imagefile and ImageInfo[2] == w and ImageInfo[3] == h :
                                    newImage = ImageInfo[1]
                                    continue
                            if newImage == None:
                                imagefile_Lower = imagefile.lower()
                                if imagefile_Lower in G_ResourcesFileList:
                                    resourPath = G_ResourcesFileList[imagefile_Lower]
                                    if os.path.exists(resourPath) == True:
                                        try:
                                            imageRGBA = Image.open(resourPath).convert('RGBA')
                                            resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                            newImage = ImageTk.PhotoImage(resizeImage)
                                        except:
                                            return 
                                G_CanvasImageDictionary[uiName][drawCanvasName].append([imagefile,newImage,w,h])
                        shapeTag = splitArray[-2]
                        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,newtext,textColor,textFont,fill,outline,width,dashx,dashy,newImage]
                        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                    elif ShapeType == 'roundrect':
                        if len(splitArray) > 11:
                            if splitArray[1].find('.') > 0:
                                x1 = float(splitArray[1])
                            else:
                                x1 = int(splitArray[1])
                                x1 = int(x1 * UIScale)
                            if splitArray[2].find('.') > 0:
                                y1 = float(splitArray[2])
                            else:
                                y1 = int(splitArray[2])
                                y1 = int(y1 * UIScale)
                            if splitArray[3].find('.') > 0:
                                x2 = float(splitArray[3])
                            else:
                                x2 = int(splitArray[3])
                                x2 = int(x2 * UIScale)
                            if splitArray[4].find('.') > 0:
                                y2 = float(splitArray[4])
                            else:
                                y2 = int(splitArray[4])
                                y2 = int(y2 * UIScale)
                            w = x2 - x1
                            if isinstance(w,float) == True:
                                w = w * drawCanvas_width
                            h = y2 - y1
                            if isinstance(h,float) == True:
                                h = h * drawCanvas_height
                            fill = splitArray[5]
                            outline = splitArray[6]
                            width = int(splitArray[7])
                            dashx = int(splitArray[8])
                            dashy = int(splitArray[9])
                            imagefile = int(splitArray[10])
                            newImage = imagefile
                            newtext = ''
                            textFont = None
                            textColor = ''
                            shapeTag = splitArray[11]
                            G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy]
                            G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]
                            DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                    elif ShapeType == 'point':
                        if splitArray[1].find('.') > 0:
                            x1 = float(splitArray[1])
                        else:
                            x1 = int(splitArray[1])
                            x1 = int(x1 * UIScale)
                        if splitArray[2].find('.') > 0:
                            y1 = float(splitArray[2])
                        else:
                            y1 = int(splitArray[2])
                            y1 = int(y1 * UIScale)
                        if splitArray[3].find('.') > 0:
                            x2 = float(splitArray[3])
                        else:
                            x2 = int(splitArray[3])
                            x2 = int(x2 * UIScale)
                        if splitArray[4].find('.') > 0:
                            y2 = float(splitArray[4])
                        else:
                            y2 = int(splitArray[4])
                            y2 = int(y2 * UIScale)
                        w = x2 - x1
                        if isinstance(w,float) == True:
                            w = w * drawCanvas_width
                        h = y2 - y1
                        if isinstance(h,float) == True:
                            h = h * drawCanvas_height
                        fill = splitArray[5]
                        outline = splitArray[6]
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        parentShapeTag = splitArray[10]
                        imagefile = ''
                        newImage = None
                        newtext = ''
                        textFont = None
                        textColor = ''
                        shapeTag = ''
                        centerX = (x1 + x2)*0.5
                        if centerX  > 1.0:
                            centerX = int(centerX)                 
                        centerY = (y1 + y2)*0.5
                        if centerY  > 1.0:
                            centerY = int(centerY)      
                        if len(splitArray) > 12:
                            shapeTag = splitArray[11]
                            G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=(ShapeType,x1,y1,x2,y2)
                        if parentShapeTag not in G_CanvasPointDictionary[uiName][drawCanvasName]:
                            G_CanvasPointDictionary[uiName][drawCanvasName][parentShapeTag] = {}
                        G_CanvasPointDictionary[uiName][drawCanvasName][parentShapeTag][shapeTag] = [centerX,centerY]
                        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
    # f.write("                    elif ShapeType == 'listmenu':
    # f.write('                        shapeTag = splitArray[-2]
    # f.write('                        LockFlag = splitArray[-1]
    # f.write("                        if splitArray[1].find('.') > 0:
    # f.write('                            x1 = float(splitArray[1])
    # f.write('                        else:
    # f.write('                            x1 = int(splitArray[1])
    # f.write("                        if splitArray[2].find('.') > 0:
    # f.write('                            y1 = float(splitArray[2])
    # f.write('                        else:
    # f.write('                            y1 = int(splitArray[2])
    # f.write("                        if splitArray[3].find('.') > 0:
    # f.write('                            x2 = float(splitArray[3])
    # f.write('                        else:
    # f.write('                            x2 = int(splitArray[3])
    # f.write("                        if splitArray[4].find('.') > 0:
    # f.write('                            y2 = float(splitArray[4])
    # f.write('                        else:
    # f.write('                            y2 = int(splitArray[4])
    # f.write('                        w  = x2 - x1
    # f.write('                        h  = y2 - y1
    # f.write('                        fill = splitArray[5]
    # f.write('                        outline = splitArray[6]
    # f.write('                        width = int(splitArray[7])
    # f.write('                        dashx = int(splitArray[8])
    # f.write('                        dashy = int(splitArray[9])
    # f.write("                        menuInfo_Begin = text.find('{')
    # f.write("                        menuInfo_End = text.rfind('}')
    # f.write("                        menuInfo = text[menuInfo_Begin :menuInfo_End+1]
    # f.write("                        menuInfo = menuInfo.replace(\"'\",'\"')
    # f.write("                        menu_dict = json.loads(menuInfo)
    # f.write("                        imagefile = ''
    # f.write('                        newImage = menu_dict
    # f.write("                        newtext = ''
    # f.write('                        textFont = None
    # f.write("                        textColor = ''
    # f.write("                        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,menu_dict]
    # f.write("                        for subMesh in menu_dict['SubMenus']:
    # f.write('                            subMeshTag = shapeTag + "_" + subMesh[0]
    # f.write('                            if subMeshTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:                     
    # f.write('                                G_CanvasEventDictionary[uiName][drawCanvasName][subMeshTag] = {}   
    # f.write('                            EventName = "ButtonDown" 
    # f.write('                            if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][subMeshTag]:             
    # f.write('                                G_CanvasEventDictionary[uiName][drawCanvasName][subMeshTag][EventName] = []   
    # f.write('                            actionInfo = ["OnExpandOrShrink",subMeshTag,True]                      
    # f.write('                            G_CanvasEventDictionary[uiName][drawCanvasName][subMeshTag][EventName].append(actionInfo) 
    # f.write('                        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]
    # f.write('                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                    elif ShapeType == 'table':
                        shapeTag = splitArray[-2]
                        LockFlag = splitArray[-1]
                        if splitArray[1].find('.') > 0:
                            x1 = float(splitArray[1])
                        else:
                            x1 = int(splitArray[1])
                            x1 = int(x1 * UIScale)
                        if splitArray[2].find('.') > 0:
                            y1 = float(splitArray[2])
                        else:
                            y1 = int(splitArray[2])
                            y1 = int(y1 * UIScale)
                        if splitArray[3].find('.') > 0:
                            x2 = float(splitArray[3])
                        else:
                            x2 = int(splitArray[3])
                            x2 = int(x2 * UIScale)
                        if splitArray[4].find('.') > 0:
                            y2 = float(splitArray[4])
                        else:
                            y2 = int(splitArray[4])
                            y2 = int(y2 * UIScale)
                        w  = x2 - x1
                        h  = y2 - y1
                        fill = splitArray[5]
                        outline = splitArray[6]
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        tableInfo_Begin = text.find('{')
                        tableInfo_End = text.rfind('}')
                        tableInfo_Text = text[tableInfo_Begin :tableInfo_End+1]
                        table_dict = {}
                        table_dict['font'] = []
                        table_dict['font'].append(['System','12'])
                        table_dict['style'] = []
                        table_dict['style'].append(['',0,'center','',0,''])
                        table_dict['style'].append(['',0,'center','',1,''])
                        table_dict['style'].append(['#EEEEEE',0,'center','',1,''])
                        table_dict['cows'] = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
                        table_dict['rows'] = []
                        table_dict['merge'] = []
                        try:
                            table_dict = eval(tableInfo_Text)
                        except Exception as ex:
                            PyMeFuns.MessageBox('"+Language.G_Language[1686]+"'+':'+str(ex))
                        imagefile = ''
                        newImage = table_dict
                        if UIScale < 1.0:
                            for FontInfo in table_dict['font']:
                                FontInfo[1] = int(int(FontInfo[1]) * UIScale)
                                FontInfo[1] = str(FontInfo[1])
                        newtext = ''
                        textFont = None
                        textColor = ''
                        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,table_dict]
                        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                    elif ShapeType == 'SetShapeRect':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        if splitArray[4].find('.') > 0:
                            x = float(splitArray[4])
                        else:
                            x = int(splitArray[4])
                            x = int(x * UIScale)
                        if splitArray[5].find('.') > 0:
                            y = float(splitArray[5])
                        else:
                            y = int(splitArray[5])
                            y = int(y * UIScale)
                        if splitArray[6].find('.') > 0:
                            w = float(splitArray[6])
                        else:
                            w = int(splitArray[6])
                            w = int(w * UIScale)
                        if splitArray[7].find('.') > 0:
                            h = float(splitArray[7])
                        else:
                            h = int(splitArray[7])
                            h = int(h * UIScale)
                        actionInfo = ["SetShapeRect",TargetShapeTag,x,y,w,h]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'SetFillColor':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        Color = splitArray[4]   
                        actionInfo = ["SetFillColor",TargetShapeTag,Color]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'SetOutlineColor':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        Color = splitArray[4]   
                        actionInfo = ["SetOutlineColor",TargetShapeTag,Color]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'ChangeImage':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        ImageFile = splitArray[4]
                        actionInfo = ["ChangeImage",TargetShapeTag,ImageFile]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'ChangeText':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        Text = splitArray[4]
                        TextColor = splitArray[5]
                        actionInfo = ["ChangeText",TargetShapeTag,Text,TextColor]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'JumpToUI':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetUIName = splitArray[3]
                        actionInfo = ["JumpToUI",shapeTag,TargetUIName]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'LoadUI':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        WidgetName = splitArray[3]
                        TargetUIName = splitArray[4]
                        actionInfo = ["LoadUI",shapeTag,WidgetName,TargetUIName]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'DeleteShape':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        actionInfo = ["DeleteShape",TargetShapeTag]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'OnSwitch':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = shapeTag
                        actionInfo = ["OnSwitch",TargetShapeTag,True]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'CallFunction':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        FunctionName = drawCanvasName+"_"+shapeTag+"_on"+EventName
                        CallBackFunc = None
                        if hasattr(G_UICommandDictionary[uiName],FunctionName) == True:
                            CallBackFunc = getattr(G_UICommandDictionary[uiName],FunctionName)
                        actionInfo = ["CallFunction",CallBackFunc,None]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    else:
                        if len(splitArray) > 11:
                            if splitArray[1].find('.') > 0:
                                x1 = float(splitArray[1])
                            else:
                                x1 = int(splitArray[1])
                                x1 = int(x1 * UIScale)
                            if splitArray[2].find('.') > 0:
                                y1 = float(splitArray[2])
                            else:
                                y1 = int(splitArray[2])
                                y1 = int(y1 * UIScale)
                            if splitArray[3].find('.') > 0:
                                x2 = float(splitArray[3])
                            else:
                                x2 = int(splitArray[3])
                                x2 = int(x2 * UIScale)
                            if splitArray[4].find('.') > 0:
                                y2 = float(splitArray[4])
                            else:
                                y2 = int(splitArray[4])
                                y2 = int(y2 * UIScale)
                            w = x2 - x1
                            if isinstance(w,float) == True:
                                w = w * drawCanvas_width
                            h = y2 - y1
                            if isinstance(h,float) == True:
                                h = h * drawCanvas_height
                            fill = splitArray[5]
                            outline = splitArray[6]
                            width = int(splitArray[7])
                            dashx = int(splitArray[8])
                            dashy = int(splitArray[9])
                            imagefile = ''
                            newImage = None
                            newtext = ''
                            textFont = None
                            textColor = ''
                            shapeTag = splitArray[10]
                            G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy]
                            G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]
                            DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                continue
        f.close()   
        if uiName in G_CanvasEventDictionary: 
            for drawCanvasName in G_CanvasEventDictionary[uiName].keys():
                drawCanvas = GetElement(uiName,drawCanvasName)
                for shapeTag in G_CanvasEventDictionary[uiName][drawCanvasName].keys():
                    for EventName in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                        if EventName == "MouseEnter":
                            drawCanvas.tag_bind(shapeTag, "<Any-Enter>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseEnter"))
                            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName] and G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                                TextTag = shapeTag+"_text"
                                drawCanvas.tag_bind(TextTag, "<Any-Enter>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseEnter"))
                        elif EventName == "MouseLeave":
                            drawCanvas.tag_bind(shapeTag, "<Any-Leave>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseLeave"))
                            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName] and G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                                TextTag = shapeTag+"_text"
                                drawCanvas.tag_bind(TextTag, "<Any-Leave>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseLeave"))
                        elif EventName == "ButtonDown":
                            drawCanvas.tag_bind(shapeTag, "<Button-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonDown"))
                            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName] and G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                                TextTag = shapeTag+"_text"
                                drawCanvas.tag_bind(TextTag, "<Button-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonDown"))
                        elif EventName == "ButtonMotion":
                            drawCanvas.tag_bind(shapeTag, "<B1-Motion>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonMotion"))
                            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName] and G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                                TextTag = shapeTag+"_text"
                                drawCanvas.tag_bind(TextTag, "<B1-Motion>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonMotion"))
                        elif EventName == "ButtonUp":
                            drawCanvas.tag_bind(shapeTag, "<ButtonRelease-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonUp"))
                            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName] and G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                                TextTag = shapeTag+"_text"
                                drawCanvas.tag_bind(TextTag, "<ButtonRelease-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonUp"))
                        elif EventName == "DoubleClick":
                            drawCanvas.tag_bind(shapeTag, "<Double-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="DoubleClick"))
                            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName] and G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                                TextTag = shapeTag+"_text"
                                drawCanvas.tag_bind(TextTag, "<Double-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="DoubleClick"))

''' 
    f.write(code)
#写入设置图形矩形
def WriteReDrawCanvasRecordFunction(f):
    code='''
def ReDrawCanvasShape(uiName,canvasName):
    """'+Language.G_Language[1816]+'"""
    global G_ResourcesFileList
    global G_CanvasSizeDictionary
    global G_CanvasShapeDictionary
    global G_UIElementAliasDictionary
    hasGIFAnimation = False   
    drawCanvas = GetElement(uiName,canvasName)
    if uiName in G_UIElementAliasDictionary.keys() and canvasName in G_UIElementAliasDictionary[uiName].keys():
        canvasName = G_UIElementAliasDictionary[uiName][canvasName]
    if drawCanvas:
        if uiName in G_CanvasSizeDictionary:
            if  canvasName in G_CanvasSizeDictionary[uiName]:
                for shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:
                    ShapeType = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0]
                    if ShapeType == 'image':
                        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]
                        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]
                        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]
                        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]
                        image_handle = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][5]
                        image_filename = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][6]
                        if type(x1) == type(1.0):
                            x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                        if type(y1) == type(1.0):
                            y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                        if type(x2) == type(1.0):
                            if x2 <= 1.0:
                                x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                            else:
                                x2 = x1 + int(x2)
                        if type(y2) == type(1.0):
                            if y2 <= 1.0:
                                y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                            else:
                                y2 = y1 + int(y2)
                        w = x2 - x1
                        if isinstance(w,float) == True:
                            w = w * G_CanvasSizeDictionary[uiName][canvasName][0]
                        h = y2 - y1
                        if isinstance(h,float) == True:
                            h = h * G_CanvasSizeDictionary[uiName][canvasName][1]
                        if w == 1 and h == 1:
                            continue
                        newImage = None
                        if newImage == None:
                            image_filename_Lower = image_filename.lower()
                            if image_filename_Lower in G_ResourcesFileList:
                                resourPath = G_ResourcesFileList[image_filename_Lower]
                                if os.path.exists(resourPath) == True:
                                    try:
                                        if image_filename.find('.gif') >= 0:
                                            GifData = Image.open(resourPath)
                                            seq = []
                                            try:
                                                while 1:
                                                    imageRGBA = GifData.copy().convert('RGBA')
                                                    resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                                    newImage = ImageTk.PhotoImage(resizeImage)
                                                    seq.append(newImage)
                                                    GifData.seek(len(seq))
                                            except EOFError:
                                                pass
                                            delay = 100
                                            try:
                                                delay = GifData.info['duration']
                                            except KeyError:
                                                delay = 100
                                            if delay == 0:
                                                delay = 100
                                            newImage = [seq,delay,0]
                                            hasGIFAnimation = True
                                        else:
                                            imageRGBA = Image.open(resourPath).convert('RGBA')
                                            resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                            newImage = ImageTk.PhotoImage(resizeImage)
                                    except Exception as Ex:
                                        OutputText = resourPath + ":"+str(Ex)
                                        print(OutputText)
                                        return 
                                else:
                                    print("找不到"+resourPath)
                            else:
                                print("Resources目录找不到"+image_filename)
                            #G_CanvasImageDictionary[uiName][canvasName].append([imagefile,newImage,w,h])
                            #G_CanvasShapeDictionary[uiName][canvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,newImage,image_filename]
                            G_CanvasShapeDictionary[uiName][canvasName][shapeTag][5] = newImage
                            G_CanvasParamDictionary[uiName][canvasName][shapeTag][5] = newImage
    #f.write('                            print("Delete:"+shapeTag +" and Build:"+str("%d,%d,%d,%d"%(x1,y1,x2,y2)))
                            drawCanvas.delete(shapeTag)
    # f.write("                            drawCanvas.create_image(x1, y1,image=newImage,anchor='nw',tag=shapeTag)
                            Params = G_CanvasParamDictionary[uiName][canvasName][shapeTag]
    #        [fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]
                            DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                    elif ShapeType == 'text':
                        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]
                        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]
                        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]
                        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]
                        if type(x1) == type(1.0):
                            x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                        if type(y1) == type(1.0):
                            y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                        if type(x2) == type(1.0):
                            if x2 <= 1.0:
                                x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                            else:
                                x2 = x1 + int(x2)
                        if type(y2) == type(1.0):
                            if y2 <= 1.0:
                                y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                            else:
                                y2 = y1 + int(y2)
                        w = x2 - x1
                        if isinstance(w,float) == True:
                            w = w * G_CanvasSizeDictionary[uiName][canvasName][0]
                        h = y2 - y1
                        if isinstance(h,float) == True:
                            h = h * G_CanvasSizeDictionary[uiName][canvasName][1]
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][canvasName][shapeTag]
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                    elif ShapeType == 'button':
                        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]
                        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]
                        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]
                        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]
                        if type(x1) == type(1.0):
                            x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                        if type(y1) == type(1.0):
                            y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                        if type(x2) == type(1.0):
                            if x2 <= 1.0:
                                x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                            else:
                                x2 = x1 + int(x2)
                        if type(y2) == type(1.0):
                            if y2 <= 1.0:
                                y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                            else:
                                y2 = y1 + int(y2)
                        w = x2 - x1
                        if isinstance(w,float) == True:
                            w = w * G_CanvasSizeDictionary[uiName][canvasName][0]
                        h = y2 - y1
                        if isinstance(h,float) == True:
                            h = h * G_CanvasSizeDictionary[uiName][canvasName][1]
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][canvasName][shapeTag]
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                    elif ShapeType == 'point':
                        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]
                        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]
                        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]
                        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]
                        if type(x1) == type(1.0):
                            x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                        if type(y1) == type(1.0):
                            y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                        if type(x2) == type(1.0):
                            if x2 <= 1.0:
                                x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                            else:
                                x2 = x1 + int(x2)
                        if type(y2) == type(1.0):
                            if y2 <= 1.0:
                                y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                            else:
                                y2 = y1 + int(y2)
                        w = x2 - x1
                        if isinstance(w,float) == True:
                            w = w * G_CanvasSizeDictionary[uiName][canvasName][0]
                        h = y2 - y1
                        if isinstance(h,float) == True:
                            h = h * G_CanvasSizeDictionary[uiName][canvasName][1]
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][canvasName][shapeTag]
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                    elif ShapeType == 'table':
                        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]
                        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]
                        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]
                        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]
                        if type(x1) == type(1.0):
                            x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                        if type(y1) == type(1.0):
                            y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                        if type(x2) == type(1.0):
                            if x2 <= 1.0:
                                x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                            else:
                                x2 = x1 + int(x2)
                        if type(y2) == type(1.0):
                            if y2 <= 1.0:
                                y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                            else:
                                y2 = y1 + int(y2)
                        w = x2 - x1
                        if isinstance(w,float) == True:
                            w = w * G_CanvasSizeDictionary[uiName][canvasName][0]
                        h = y2 - y1
                        if isinstance(h,float) == True:
                            h = h * G_CanvasSizeDictionary[uiName][canvasName][1]
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][canvasName][shapeTag]
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
    # f.write("                    elif ShapeType == 'listmenu':
    # f.write('                        shapeTag = splitArray[-2]
    # f.write('                        LockFlag = splitArray[-1]
    # f.write("                        if splitArray[1].find('.') > 0:
    # f.write('                            x1 = float(splitArray[1])
    # f.write('                        else:
    # f.write('                            x1 = int(splitArray[1])
    # f.write("                        if splitArray[2].find('.') > 0:
    # f.write('                            y1 = float(splitArray[2])
    # f.write('                        else:
    # f.write('                            y1 = int(splitArray[2])
    # f.write("                        if splitArray[3].find('.') > 0:
    # f.write('                            x2 = float(splitArray[3])
    # f.write('                        else:
    # f.write('                            x2 = int(splitArray[3])
    # f.write("                        if splitArray[4].find('.') > 0:
    # f.write('                            y2 = float(splitArray[4])
    # f.write('                        else:
    # f.write('                            y2 = int(splitArray[4])
    # f.write('                        w  = x2 - x1
    # f.write('                        h  = y2 - y1
    # f.write('                        fill = splitArray[5]
    # f.write('                        outline = splitArray[6]
    # f.write('                        width = int(splitArray[7])
    # f.write('                        dashx = int(splitArray[8])
    # f.write('                        dashy = int(splitArray[9])
    # f.write("                        menuInfo_Begin = text.find('{')
    # f.write("                        menuInfo_End = text.rfind('}')
    # f.write('                        menuInfo = text[menuInfo_Begin :menuInfo_End+1]
    # f.write("                        menuInfo = menuInfo.replace(\"'\",'\"')
    # f.write('                        menu_dict = json.loads(menuInfo)
    # f.write("                        imagefile = ''
    # f.write('                        newImage = menu_dict
    # f.write("                        newtext = ''
    # f.write('                        textFont = None
    # f.write("                        textColor = ''
    # f.write('                        G_CanvasShapeDictionary[uiName][canvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,menu_dict]
    # f.write("                        for subMesh in menu_dict['SubMenus']:
    # f.write('                            subMeshTag = shapeTag + "_" + subMesh[0]
    # f.write('                            if subMeshTag not in G_CanvasEventDictionary[uiName][canvasName]:
    # f.write('                                G_CanvasEventDictionary[uiName][canvasName][subMeshTag] = {}
    # f.write('                            EventName = "ButtonDown"
    # f.write('                            if EventName not in G_CanvasEventDictionary[uiName][canvasName][subMeshTag]:
    # f.write('                                G_CanvasEventDictionary[uiName][canvasName][subMeshTag][EventName] = []
    # f.write('                            actionInfo = ["OnExpandOrShrink",subMeshTag,True]
    # f.write('                            G_CanvasEventDictionary[uiName][canvasName][subMeshTag][EventName].append(actionInfo)
    # f.write('                        G_CanvasParamDictionary[uiName][canvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]
    # f.write('                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
    # f.write("                    elif ShapeType == 'table':
    # f.write('                        shapeTag = splitArray[-2]
    # f.write('                        LockFlag = splitArray[-1]
    # f.write("                        if splitArray[1].find('.') > 0:
    # f.write('                            x1 = float(splitArray[1])
    # f.write('                        else:
    # f.write('                            x1 = int(splitArray[1])
    # f.write("                        if splitArray[2].find('.') > 0:
    # f.write('                            y1 = float(splitArray[2])
    # f.write('                        else:
    # f.write('                            y1 = int(splitArray[2])
    # f.write("                        if splitArray[3].find('.') > 0:
    # f.write('                            x2 = float(splitArray[3])
    # f.write('                        else:
    # f.write('                            x2 = int(splitArray[3])
    # f.write("                        if splitArray[4].find('.') > 0:
    # f.write('                            y2 = float(splitArray[4])
    # f.write('                        else:
    # f.write('                            y2 = int(splitArray[4])
    # f.write('                        w  = x2 - x1
    # f.write('                        h  = y2 - y1
    # f.write('                        fill = splitArray[5]
    # f.write('                        outline = splitArray[6]
    # f.write('                        width = int(splitArray[7])
    # f.write('                        dashx = int(splitArray[8])
    # f.write('                        dashy = int(splitArray[9])
    # f.write("                        tableInfo_Begin = text.find('{')
    # f.write("                        tableInfo_End = text.rfind('}')
    # f.write('                        tableInfo = text[tableInfo_Begin :tableInfo_End+1]
    # f.write("                        tableInfo = tableInfo.replace(\"'\",'\"')
    # f.write('                        table_dict = json.loads(tableInfo)
    # f.write("                        imagefile = ''
    # f.write('                        newImage = table_dict
    # f.write("                        newtext = ''
    # f.write('                        textFont = None
    # f.write("                        textColor = ''
    # f.write('                        G_CanvasShapeDictionary[uiName][canvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,table_dict]
    # f.write('                        G_CanvasParamDictionary[uiName][canvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]
    # f.write('                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                    elif ShapeType == 'SetShapeRect':
                        pass
                    elif ShapeType == 'SetFillColor':
                        pass
                    elif ShapeType == 'SetOutlineColor':
                        pass
                    elif ShapeType == 'ChangeImage':
                        pass
                    elif ShapeType == 'ChangeText':
                        pass
                    elif ShapeType == 'JumpToUI':
                        pass
                    elif ShapeType == 'LoadUI':
                        pass
                    elif ShapeType == 'DeleteShape':
                        pass
                    elif ShapeType == 'OnSwitch':
                        pass
                    elif ShapeType == 'CallFunction':
                        pass
                    else:
                        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]
                        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]
                        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]
                        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]
                        if type(x1) == type(1.0):
                            x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                        if type(y1) == type(1.0):
                            y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                        if type(x2) == type(1.0):
                            if x2 <= 1.0:
                                x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                            else:
                                x2 = x1 + int(x2)
                        if type(y2) == type(1.0):
                            if y2 <= 1.0:
                                y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                            else:
                                y2 = y1 + int(y2)
                        w = x2 - x1
                        if isinstance(w,float) == True:
                            w = w * G_CanvasSizeDictionary[uiName][canvasName][0]
                        h = y2 - y1
                        if isinstance(h,float) == True:
                            h = h * G_CanvasSizeDictionary[uiName][canvasName][1]
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][canvasName][shapeTag]
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
        drawCanvas.update()
        if hasGIFAnimation == True:
            drawCanvas.after(100,updateGIFFrame(uiName,canvasName))
def ReDrawCanvasRecord(uiName,ForceReDraw=False):
    """'+Language.G_Language[1817]+'"""
    global G_ResourcesFileList
    global G_UIElementDictionary
    global G_CanvasSizeDictionary
    global G_UIElementRoundRectangleDictionary
    global G_UIElementUserDataArray
    ReDraw = False
    if uiName in G_CanvasSizeDictionary:
        for canvasName in G_CanvasSizeDictionary[uiName]:
            drawCanvas =  G_UIElementDictionary[uiName][canvasName]
            drawCanvas_width = drawCanvas.winfo_width()
            drawCanvas_height = drawCanvas.winfo_height()
            if canvasName == "Form_1":
                root = GetElement(uiName,"root")
                drawCanvas_width = root.winfo_width()
                drawCanvas_height = root.winfo_height()
            if ForceReDraw == True or G_CanvasSizeDictionary[uiName][canvasName][0] != drawCanvas_width or G_CanvasSizeDictionary[uiName][canvasName][1] != drawCanvas_height:
                ReDraw = True
            G_CanvasSizeDictionary[uiName][canvasName] = [drawCanvas_width,drawCanvas_height]
    if ReDraw == True:
        if G_CanvasSizeDictionary[uiName][canvasName][0] == 1 and G_CanvasSizeDictionary[uiName][canvasName][1] == 1:
            return 
        print("ReDrawCanvasRecord")
        if uiName in G_CanvasShapeDictionary:
            for canvasName in G_CanvasSizeDictionary[uiName]:
                ReDrawCanvasShape(uiName,canvasName)
    if uiName in G_UIElementRoundRectangleDictionary:
        for elementName in G_UIElementRoundRectangleDictionary[uiName]:
            Control = G_UIElementDictionary[uiName][elementName]
            if Control:
                RRInfo = G_UIElementRoundRectangleDictionary[uiName][elementName]
                ShowRoundedRectangle(Control,RRInfo[0],RRInfo[1])
def ResizeAllChart(uiName,forceRedraw=False):
    """'+Language.G_Language[759]+'"""
    global G_UIElementUserDataArray
    if uiName in G_UIElementUserDataArray.keys():
        for elementName in G_UIElementUserDataArray[uiName]:
            ChartReady = 0
            for EBData in G_UIElementUserDataArray[uiName][elementName]:
                if EBData[0] == 'ChartReady':
                    ChartReady = EBData[2]
                if EBData[0] == 'ChartCanvas' and (ChartReady == 1 or forceRedraw == True):
                    theChart = EBData[2]
                    theChartCanvas = theChart.get_tk_widget()
                    w = theChartCanvas.winfo_width()
                    h = theChartCanvas.winfo_height()
                    if w == 1 and h == 1:
                        parentWidget = theChartCanvas._nametowidget(theChartCanvas.winfo_parent())
                        if "relwidth" in G_UIElementPlaceDictionary[uiName][elementName]:
                            w = G_UIElementPlaceDictionary[uiName][elementName]["relwidth"]
                            w = int(w * parentWidget.winfo_width())
                        else:
                            w = G_UIElementPlaceDictionary[uiName][elementName]["width"]
                        if "relheight" in G_UIElementPlaceDictionary[uiName][elementName]:
                            h = G_UIElementPlaceDictionary[uiName][elementName]["relheight"]
                            h = int(h * parentWidget.winfo_width())
                        else:
                            h = G_UIElementPlaceDictionary[uiName][elementName]["height"]
                    else:
                        oldw = W
                        oldh = h
                        parentWidget = theChartCanvas._nametowidget(theChartCanvas.winfo_parent())
                        if "relwidth" in G_UIElementPlaceDictionary[uiName][elementName]:
                            oldw = G_UIElementPlaceDictionary[uiName][elementName]["relwidth"]
                            oldw = int(oldw * parentWidget.winfo_width())
                        else:
                            oldw = G_UIElementPlaceDictionary[uiName][elementName]["width"]
                        if "relheight" in G_UIElementPlaceDictionary[uiName][elementName]:
                            oldh = G_UIElementPlaceDictionary[uiName][elementName]["relheight"]
                            oldh = int(oldh * parentWidget.winfo_height())
                        else:
                            oldh = G_UIElementPlaceDictionary[uiName][elementName]["height"]
                        if forceRedraw == False and w == oldw and h == oldh:
                            continue
                    event = ChartEvent(w,h,theChartCanvas)
                    theChart.resize(event)
                    theChartCanvas.update()
''' 
    f.write(code)
#写入设置图形矩形
def WriteSetShapeRectFunction(f):
    code='''
def SetShapeRect(uiName,canvasName,shapeTag,x1,y1,x2,y2):
    """'+Language.G_Language[856]+'"""
    if uiName in G_CanvasShapeDictionary:
        drawCanvas = GetElement(uiName,canvasName)
        if canvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:
                if shapeTag.find('text_') >= 0:
                    drawCanvas.coords(shapeTag, x1,y1) 
                else:
                    try:
                        drawCanvas.coords(shapeTag, x1,y1,x2,y2) 
                    except:
                        drawCanvas.coords(shapeTag, x1,y1) 
    #f.write('            drawCanvas.itemconfig(shapeTag,width=x2-x1,height=y2-y1) 
                G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1] = x1
                G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2] = y1
                G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3] = x2
                G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4] = y2
def GetShapeRect(uiName,canvasName,shapeTag):
    """'+Language.G_Language[866]+'"""
    if uiName in G_CanvasShapeDictionary:
        drawCanvas = GetElement(uiName,canvasName)
        if canvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:
                x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]
                if type(x1) == type(1.0):
                    x1 = round(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]
                if type(y1) == type(1.0):
                    y1 = round(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]
                if type(x2) == type(1.0):
                    x2 = round(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]
                if type(y2) == type(1.0):
                    y2 = round(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                return (x1,y1,x2,y2)
    return None
''' 
    f.write(code)
#写入设置线条宽度
def WriteSetShapeWidthFunction(f):
    code='''
def SetShapeLineWidth(uiName,canvasName,shapeTag,width):
    """'+Language.G_Language[1464]+'"""
    
    if uiName in G_CanvasShapeDictionary:
        if canvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:
                if G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'button':
                    if G_CanvasShapeDictionary[uiName][canvasName][shapeTag][-1] == None:
                        drawCanvas = GetElement(uiName,canvasName)
                        drawCanvas.itemconfig(shapeTag, width=width)
                        G_CanvasParamDictionary[uiName][canvasName][shapeTag][2]=width
                elif G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'roundrect':
                    OutlineTag = shapeTag+\"_outline\"
                    ArcTag = shapeTag+\"_arc\"
                    drawCanvas = GetElement(uiName,canvasName)
                    drawCanvas.itemconfig(OutlineTag, width=width)
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][2]=width
                else:
                    drawCanvas = GetElement(uiName,canvasName)
                    drawCanvas.itemconfig(shapeTag, width=width)
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][2]=width
''' 
    f.write(code)
#写入设置填充颜色
def WriteSetShapeFillColorFunction(f):
    code='''
def SetShapeFillColor(uiName,canvasName,shapeTag,color):
    """'+Language.G_Language[844]+'"""
    if uiName in G_CanvasShapeDictionary:
        if canvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:
                if G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'button':
                    if G_CanvasShapeDictionary[uiName][canvasName][shapeTag][-1] == None:
                        drawCanvas = GetElement(uiName,canvasName)
                        drawCanvas.itemconfig(shapeTag, fill=color)
    # f.write("                        OutlineTag = shapeTag+\"_outline\"
    # f.write('                        drawCanvas.itemconfig(OutlineTag, fill=color)
                        G_CanvasParamDictionary[uiName][canvasName][shapeTag][0]=color
                elif G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'text':
                    drawCanvas = GetElement(uiName,canvasName)
                    drawCanvas.itemconfig(shapeTag, fill=color)
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][0]=color
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][8]=color
                else:
                    drawCanvas = GetElement(uiName,canvasName)
                    drawCanvas.itemconfig(shapeTag, fill=color)
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][0]=color
def GetShapeFillColor(uiName,canvasName,shapeTag):
    """'+Language.G_Language[867]+'"""
    if uiName in G_CanvasShapeDictionary:
        if canvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:
                return G_CanvasShapeDictionary[uiName][canvasName][shapeTag][5]
    return None
''' 
    f.write(code)
#写入设置边框颜色
def WriteSetShapeOutlineColorFunction(f):
    code='''
def SetShapeOutlineColor(uiName,canvasName,shapeTag,color):
    """'+Language.G_Language[845]+'"""
    if uiName in G_CanvasShapeDictionary:
        if canvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:
                if G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'cylinder':
                    drawCanvas = GetElement(uiName,canvasName)
                    drawCanvas.itemconfig(shapeTag, outline=color)
                    OutlineTag = shapeTag+\"_outline\"
                    drawCanvas.itemconfig(OutlineTag, fill=color)
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][1]=color
                elif G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'roundrect':
                    OutlineTag = shapeTag+\"_outline\"
                    ArcTag = shapeTag+\"_arc\"
                    drawCanvas = GetElement(uiName,canvasName)
                    drawCanvas.itemconfig(OutlineTag, fill=color)
                    drawCanvas.itemconfig(ArcTag, outline=color)
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][1]=color
                else:
                    drawCanvas = GetElement(uiName,canvasName)
                    drawCanvas.itemconfig(shapeTag, outline=color)
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][1]=color

def GetShapeOutlineColor(uiName,canvasName,shapeTag):
    """'+Language.G_Language[868]+'"""
    if uiName in G_CanvasShapeDictionary:
        if canvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:
                return G_CanvasShapeDictionary[uiName][canvasName][shapeTag][6]
        return None
''' 
    f.write(code)
#写入设置图形图片
def WriteSetShapeImageFunction(f):
    code='''
def SetShapeImage(uiName,canvasName,shapeTag,imageFile,angle=0):
    """'+Language.G_Language[846]+'"""
    global G_ResourcesFileList
    if uiName in G_CanvasShapeDictionary:
        drawCanvas = GetElement(uiName,canvasName)
        if canvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]: 
                x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]
                y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]
                x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]
                y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]
                if type(x1) == type(1.0):
                    x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                if type(y1) == type(1.0):
                    y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                if type(x2) == type(1.0):
                    if x2 <= 1.0:
                        x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                    else:
                        x2 = x1 + int(x2)
                if type(y2) == type(1.0):
                    if y2 <= 1.0:
                        y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                    else:
                        y2 = y1 + int(y2)
                w = x2 - x1
                h = y2 - y1
                newImage = None
                if isinstance(imageFile,str) == True:
                    for ImageInfo in G_CanvasImageDictionary[uiName][canvasName]:
                        if ImageInfo[0] == imageFile and ImageInfo[2] == w and ImageInfo[3] == h :
                            newImage = ImageInfo[1]
                            continue
                    if newImage == None:
                        imageFile_Lower = imageFile.lower()
                        if imageFile_Lower in G_ResourcesFileList:
                            resourPath = G_ResourcesFileList[imageFile_Lower]
                            if os.path.exists(resourPath) == True:
                                try:
                                    imageRGBA = Image.open(resourPath).convert('RGBA')
                                    resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                    newImage = ImageTk.PhotoImage(resizeImage.rotate(angle))
                                except:
                                    return 
                        G_CanvasImageDictionary[uiName][canvasName].append([imageFile,newImage,w,h])
                elif imageFile:
                    resizeImage = imageFile.resize((w, h),Image.LANCZOS)
                    newImage = ImageTk.PhotoImage(resizeImage.rotate(angle))
                    imageFile = ''
                G_CanvasShapeDictionary[uiName][canvasName][shapeTag][5] = newImage
                G_CanvasShapeDictionary[uiName][canvasName][shapeTag][6] = imageFile
                drawCanvas.itemconfig(shapeTag, image=newImage)
def GetShapeImage(uiName,canvasName,shapeTag):
    """'+Language.G_Language[869]+'"""
    if uiName in G_CanvasShapeDictionary:
        if canvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]: 
                return G_CanvasShapeDictionary[uiName][canvasName][shapeTag][5]
    return None
def PasteImageToShapeImage(uiName,canvasName,shapeTag,imageFileName,x1,x2,y1,y2,angle):
    """'+Language.G_Language[9334]+'"""
    if uiName in G_CanvasShapeDictionary:
        if canvasName in G_CanvasShapeDictionary[uiName]:
            drawCanvas = GetElement(uiName,canvasName)
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]: 
                if G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'image':
                    image_x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]
                    image_y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]
                    image_x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]
                    image_y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]
                    if type(image_x1) == type(1.0):
                        image_x1 = int(image_x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                    if type(image_y1) == type(1.0):
                        image_y1 = int(image_y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                    if type(image_x2) == type(1.0):
                        if image_x2 <= 1.0:
                            image_x2 = int(image_x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                        else:
                            image_x2 = image_x1 + int(image_x2)
                    if type(image_y2) == type(1.0):
                        if image_y2 <= 1.0:
                            image_y2 = int(image_y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                        else:
                            image_y2 = image_y1 + int(image_y2)
                    image_w = image_x2 - image_x1
                    image_h = image_y2 - image_y1
                    imageFile = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][6]
                    imageFile_Lower = imageFile.lower()
                    if imageFile_Lower in G_ResourcesFileList:
                        resourPath = G_ResourcesFileList[imageFile_Lower]
                        if os.path.exists(resourPath) == True:
                            try:
                                imageRGBA = Image.open(resourPath).convert('RGBA')
                                bigImage = imageRGBA.resize((image_w, image_h),Image.LANCZOS)
                                imageFileName_Lower = imageFileName.lower()
                                if imageFileName_Lower in G_ResourcesFileList:
                                    resourPath = G_ResourcesFileList[imageFileName_Lower]
                                else:
                                    resourPath = imageFileName
                                    if os.path.exists(resourPath) == True:
                                        try:
                                            imageRGBA = Image.open(resourPath).convert('RGBA')
                                            w = x2 - x1
                                            h = y2 - y1
                                            smallImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                            smallImage = smallImage.rotate(angle)
                                            bigImage.paste(smallImage, (x1,y1), mask=smallImage)
                                            newImage = ImageTk.PhotoImage(bigImage)
                                            G_CanvasShapeDictionary[uiName][canvasName][shapeTag][5] = newImage
                                            G_CanvasShapeDictionary[uiName][canvasName][shapeTag][6] = imageFile
                                            drawCanvas.itemconfig(shapeTag, image=newImage) 
                                        except:
                                            return 
                            except:
                                return 


''' 
    f.write(code)
#写入获取绑定点位置
def WriteSetShapeTextFunction(f):
    code='''
def SetShapeText(uiName,drawCanvasName,shapeTag,text,color = None):
    """'+Language.G_Language[836]+'"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]: 
                drawCanvas = GetElement(uiName,drawCanvasName)
                G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][5] = text 
    #f.write('                textFont = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][6]
                shapeTextTag = shapeTag 
                textcolor = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][7] 
                if G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                    shapeTextTag = shapeTag+"_text" 
                    textcolor = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][6] 
                if color: 
                    textcolor = color 
    # f.write("                if anchor == 'center':
    # f.write("                    drawCanvas.create_text((x1+x2)//2, (y1+y2)//2,fill=fillcolor,text=text,font = textFont,anchor=anchor,tag=shapeTag)
    # f.write("                elif anchor == 'n' or anchor == tkinter.N:
    # f.write("                    drawCanvas.create_text((x1+x2)//2, y1,fill=fillcolor,text=text,font = textFont,anchor=anchor,tag=shapeTag)
    # f.write("                elif anchor == 'w' or anchor == tkinter.W:
    # f.write("                    drawCanvas.create_text(x1, (y1+y2)//2,fill=fillcolor,text=text,font = textFont,anchor=anchor,tag=shapeTag)
    # f.write("                elif anchor == 's' or anchor == tkinter.S:
    # f.write("                    drawCanvas.create_text((x1+x2)//2, y2,fill=fillcolor,text=text,font = textFont,anchor=anchor,tag=shapeTag)
    # f.write("                elif anchor == 'e' or anchor == tkinter.E:
    # f.write("                    drawCanvas.create_text(x2, (y1+y2)//2,fill=fillcolor,text=text,font = textFont,anchor=anchor,tag=shapeTag)
    # f.write("                elif anchor == 'se' or anchor == tkinter.SE:
    # f.write("                    drawCanvas.create_text(x2, y2,fill=fillcolor,text=text,font = textFont,anchor=anchor,tag=shapeTag)
    # f.write("                elif anchor == 'ne' or anchor == tkinter.NE:
    # f.write("                    drawCanvas.create_text(x2, y1,fill=fillcolor,text=text,font = textFont,anchor=anchor,tag=shapeTag)
    # f.write("                elif anchor == 'sw' or anchor == tkinter.SW:
    # f.write("                    drawCanvas.create_text(x1, y2,fill=fillcolor,text=text,font = textFont,anchor=anchor,tag=shapeTag)
    # f.write("                else:
                G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][6] = text
                G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][8] = textcolor
                drawCanvas.itemconfigure(shapeTextTag,text=text)
                drawCanvas.itemconfigure(shapeTextTag,fill=textcolor)
def GetShapeText(uiName,drawCanvasName,shapeTag):
    """'+Language.G_Language[870]+'"""
    if uiName not in G_CanvasShapeDictionary:
        return None
    if drawCanvasName in G_CanvasParamDictionary[uiName]:
        if shapeTag in G_CanvasParamDictionary[uiName][drawCanvasName]: 
            text = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][6]
            textColor = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][8]
            return (text,textColor)
    return None

def SetCanvasTableCellBGColor(uiName,drawCanvasName,shapeTag,row=0,col=0,bgColor='#FFFFFF'):
    """'+Language.G_Language[2102]+'"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]: 
                drawCanvas = GetElement(uiName,drawCanvasName)
                x1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][1]
                y1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][2]
                x2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][3]
                y2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][4]
                if type(x1) == type(1.0):
                    x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                if type(y1) == type(1.0):
                    y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                if type(x2) == type(1.0):
                    if x2 <= 1.0:
                        x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                    else:
                        x2 = x1 + int(x2)
                if type(y2) == type(1.0):
                    if y2 <= 1.0:
                        y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                    else:
                        y2 = y1 + int(y2)
                TableInfo = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][10]
                for mergeInfo in TableInfo['merge']:
                    MergeBeginRow = mergeInfo[0][0]
                    MergeBeginCow = mergeInfo[0][1]
                    MergeEndRow = mergeInfo[1][0]
                    MergeEndCow = mergeInfo[1][1]
                    if checkPtInRect(col,row,MergeBeginCow,MergeEndCow,MergeBeginRow,MergeEndRow) == True:
                        styleIndex = mergeInfo[3]
                        StyleList = TableInfo['style']
                        StyleInfo = StyleList[styleIndex]
                        NewStyleInfo = copy.deepcopy(StyleInfo)
                        NewStyleInfo[0] = bgColor
                        if NewStyleInfo in TableInfo['style']:
                            mergeInfo[3] = TableInfo['style'].index(NewStyleInfo)
                        else:
                            TableInfo['style'].append(NewStyleInfo)
                            mergeInfo[3] = TableInfo['style'].index(NewStyleInfo)
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]
                        Params[5] = TableInfo
                        DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                        return
                RowIndex = 0
                for rowInfoLine in TableInfo['rows']:
                    CowIndex = 0
                    for rowInfo in rowInfoLine:
                        if CowIndex == col and RowIndex == row:
                            styleIndex = rowInfo[1]
                            StyleList = TableInfo['style']
                            StyleInfo = StyleList[styleIndex]
                            NewStyleInfo = copy.deepcopy(StyleInfo)
                            NewStyleInfo[0] = bgColor
                            if NewStyleInfo in TableInfo['style']:
                                rowInfo[1] = TableInfo['style'].index(NewStyleInfo)
                            else:
                                TableInfo['style'].append(NewStyleInfo)
                                rowInfo[1] = TableInfo['style'].index(NewStyleInfo)
                            drawCanvas.delete(shapeTag)
                            Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]
                            Params[5] = TableInfo
                            DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                            return
                        CowIndex = CowIndex + 1
                    RowIndex = RowIndex + 1
def SetCanvasTableCellText(uiName,drawCanvasName,shapeTag,row=0,col=0,cellText=''):
    """'+Language.G_Language[2103]+'"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]: 
                drawCanvas = GetElement(uiName,drawCanvasName)
                x1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][1]
                y1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][2]
                x2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][3]
                y2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][4]
                if type(x1) == type(1.0):
                    x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                if type(y1) == type(1.0):
                    y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                if type(x2) == type(1.0):
                    if x2 <= 1.0:
                        x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                    else:
                        x2 = x1 + int(x2)
                if type(y2) == type(1.0):
                    if y2 <= 1.0:
                        y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                    else:
                        y2 = y1 + int(y2)
                TableInfo = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][10]
                for mergeInfo in TableInfo['merge']:
                    MergeBeginRow = mergeInfo[0][0]
                    MergeBeginCow = mergeInfo[0][1]
                    MergeEndRow = mergeInfo[1][0]
                    MergeEndCow = mergeInfo[1][1]
                    if checkPtInRect(col,row,MergeBeginCow,MergeEndCow,MergeBeginRow,MergeEndRow) == True:
                        mergeInfo[2] = str(cellText)
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]
                        Params[5] = TableInfo
                        DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                        return
                RowIndex = 0
                for rowInfoLine in TableInfo['rows']:
                    CowIndex = 0
                    for rowInfo in rowInfoLine:
                        if CowIndex == col and RowIndex == row:
                            rowInfo[0] = str(cellText)
                            drawCanvas.delete(shapeTag)
                            Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]
                            Params[5] = TableInfo
                            DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                            return
                        CowIndex = CowIndex + 1
                    RowIndex = RowIndex + 1
def SetCanvasTableCellTextColor(uiName,drawCanvasName,shapeTag,row=0,col=0,textColor='#000000'):
    """'+Language.G_Language[2106]+'"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]: 
                drawCanvas = GetElement(uiName,drawCanvasName)
                x1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][1]
                y1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][2]
                x2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][3]
                y2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][4]
                if type(x1) == type(1.0):
                    x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                if type(y1) == type(1.0):
                    y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                if type(x2) == type(1.0):
                    if x2 <= 1.0:
                        x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                    else:
                        x2 = x1 + int(x2)
                if type(y2) == type(1.0):
                    if y2 <= 1.0:
                        y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                    else:
                        y2 = y1 + int(y2)
                TableInfo = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][10]
                for mergeInfo in TableInfo['merge']:
                    MergeBeginRow = mergeInfo[0][0]
                    MergeBeginCow = mergeInfo[0][1]
                    MergeEndRow = mergeInfo[1][0]
                    MergeEndCow = mergeInfo[1][1]
                    if checkPtInRect(col,row,MergeBeginCow,MergeEndCow,MergeBeginRow,MergeEndRow) == True:
                        styleIndex = mergeInfo[3]
                        StyleList = TableInfo['style']
                        StyleInfo = StyleList[styleIndex]
                        NewStyleInfo = copy.deepcopy(StyleInfo)
                        NewStyleInfo[3] = textColor
                        if NewStyleInfo in TableInfo['style']:
                            mergeInfo[3] = TableInfo['style'].index(NewStyleInfo)
                        else:
                            TableInfo['style'].append(NewStyleInfo)
                            mergeInfo[3] = TableInfo['style'].index(NewStyleInfo)
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]
                        Params[5] = TableInfo
                        DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                        return
                RowIndex = 0
                for rowInfoLine in TableInfo['rows']:
                    CowIndex = 0
                    for rowInfo in rowInfoLine:
                        if CowIndex == col and RowIndex == row:
                            styleIndex = rowInfo[1]
                            StyleList = TableInfo['style']
                            StyleInfo = StyleList[styleIndex]
                            NewStyleInfo = copy.deepcopy(StyleInfo)
                            NewStyleInfo[3] = textColor
                            if NewStyleInfo in TableInfo['style']:
                                rowInfo[1] = TableInfo['style'].index(NewStyleInfo)
                            else:
                                TableInfo['style'].append(NewStyleInfo)
                                rowInfo[1] = TableInfo['style'].index(NewStyleInfo)
                            drawCanvas.delete(shapeTag)
                            Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]
                            Params[5] = TableInfo
                            DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                            return
                        CowIndex = CowIndex + 1
                    RowIndex = RowIndex + 1
def SetCanvasTableCellTextFont(uiName,drawCanvasName,shapeTag,row=0,col=0,font='TkDefaultFont'):
    """'+Language.G_Language[2099]+'"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]: 
                drawCanvas = GetElement(uiName,drawCanvasName)
                x1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][1]
                y1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][2]
                x2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][3]
                y2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][4]
                if type(x1) == type(1.0):
                    x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                if type(y1) == type(1.0):
                    y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                if type(x2) == type(1.0):
                    if x2 <= 1.0:
                        x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                    else:
                        x2 = x1 + int(x2)
                if type(y2) == type(1.0):
                    if y2 <= 1.0:
                        y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                    else:
                        y2 = y1 + int(y2)
                TableInfo = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][10]
                #字体信息
                familytext = font.actual('family')
                sizetext = font.actual('size')
                weighttext = font.actual('weight')
                slanttext = font.actual('slant')
                underlinetext = font.actual('underline')
                overstriketext = font.actual('overstrike')
                CellTextFontIndex = -1
                FontIndex = 0
                for FontInfo in TableInfo['font']:
                    if FontInfo[0] == familytext and FontInfo[1] == sizetext and FontInfo[2] == weighttext and FontInfo[3] == slanttext and FontInfo[4] == underlinetext and FontInfo[5] == overstriketext:
                        CellTextFontIndex = FontIndex
                        break
                    FontIndex = FontIndex + 1
                if CellTextFontIndex < 0:
                    CellTextFontIndex = len(TableInfo['font'])
                    TableInfo['font'].append([familytext,sizetext,weighttext,slanttext,underlinetext,overstriketext])
                for mergeInfo in TableInfo['merge']:
                    MergeBeginRow = mergeInfo[0][0]
                    MergeBeginCow = mergeInfo[0][1]
                    MergeEndRow = mergeInfo[1][0]
                    MergeEndCow = mergeInfo[1][1]
                    if checkPtInRect(col,row,MergeBeginCow,MergeEndCow,MergeBeginRow,MergeEndRow) == True:
                        styleIndex = mergeInfo[3]
                        StyleList = TableInfo['style']
                        StyleInfo = StyleList[styleIndex]
                        NewStyleInfo = copy.deepcopy(StyleInfo)
                        NewStyleInfo[1] = CellTextFontIndex
                        if NewStyleInfo in TableInfo['style']:
                            mergeInfo[1] = TableInfo['style'].index(NewStyleInfo)
                        else:
                            TableInfo['style'].append(NewStyleInfo)
                            mergeInfo[1] = TableInfo['style'].index(NewStyleInfo)
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]
                        Params[5] = TableInfo
                        DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                        return
                RowIndex = 0
                for rowInfoLine in TableInfo['rows']:
                    CowIndex = 0
                    for rowInfo in rowInfoLine:
                        if CowIndex == col and RowIndex == row:
                            styleIndex = rowInfo[1]
                            StyleList = TableInfo['style']
                            StyleInfo = StyleList[styleIndex]
                            NewStyleInfo = copy.deepcopy(StyleInfo)
                            NewStyleInfo[1] = CellTextFontIndex
                            if NewStyleInfo in TableInfo['style']:
                                rowInfo[1] = TableInfo['style'].index(NewStyleInfo)
                            else:
                                TableInfo['style'].append(NewStyleInfo)
                                rowInfo[1] = TableInfo['style'].index(NewStyleInfo)
                            drawCanvas.delete(shapeTag)
                            Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]
                            Params[5] = TableInfo
                            DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                            return
                        CowIndex = CowIndex + 1
                    RowIndex = RowIndex + 1
def SetCanvasTableCellTextAnchor(uiName,drawCanvasName,shapeTag,row=0,col=0,anchor='center'):
    """'+Language.G_Language[2105]+'"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]: 
                drawCanvas = GetElement(uiName,drawCanvasName)
                x1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][1]
                y1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][2]
                x2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][3]
                y2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][4]
                if type(x1) == type(1.0):
                    x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                if type(y1) == type(1.0):
                    y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                if type(x2) == type(1.0):
                    if x2 <= 1.0:
                        x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                    else:
                        x2 = x1 + int(x2)
                if type(y2) == type(1.0):
                    if y2 <= 1.0:
                        y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                    else:
                        y2 = y1 + int(y2)
                TableInfo = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][10]
                for mergeInfo in TableInfo['merge']:
                    MergeBeginRow = mergeInfo[0][0]
                    MergeBeginCow = mergeInfo[0][1]
                    MergeEndRow = mergeInfo[1][0]
                    MergeEndCow = mergeInfo[1][1]
                    if checkPtInRect(col,row,MergeBeginCow,MergeEndCow,MergeBeginRow,MergeEndRow) == True:
                        styleIndex = mergeInfo[3]
                        StyleList = TableInfo['style']
                        StyleInfo = StyleList[styleIndex]
                        NewStyleInfo = copy.deepcopy(StyleInfo)
                        NewStyleInfo[2] = anchor
                        if NewStyleInfo in TableInfo['style']:
                            mergeInfo[3] = TableInfo['style'].index(NewStyleInfo)
                        else:
                            TableInfo['style'].append(NewStyleInfo)
                            mergeInfo[3] = TableInfo['style'].index(NewStyleInfo)
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]
                        Params[5] = TableInfo
                        DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                        return
                RowIndex = 0
                for rowInfoLine in TableInfo['rows']:
                    CowIndex = 0
                    for rowInfo in rowInfoLine:
                        if CowIndex == col and RowIndex == row:
                            styleIndex = rowInfo[1]
                            StyleList = TableInfo['style']
                            StyleInfo = StyleList[styleIndex]
                            NewStyleInfo = copy.deepcopy(StyleInfo)
                            NewStyleInfo[2] = anchor
                            if NewStyleInfo in TableInfo['style']:
                                rowInfo[1] = TableInfo['style'].index(NewStyleInfo)
                            else:
                                TableInfo['style'].append(NewStyleInfo)
                                rowInfo[1] = TableInfo['style'].index(NewStyleInfo)
                            drawCanvas.delete(shapeTag)
                            Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]
                            Params[5] = TableInfo
                            DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                            return
                        CowIndex = CowIndex + 1
                    RowIndex = RowIndex + 1
def SetCanvasTableCellMerge(uiName,drawCanvasName,shapeTag,BeginRow=0,BeginCow=0,EndRow=0,EndCow=0):
    """'+Language.G_Language[2100]+'"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]: 
                drawCanvas = GetElement(uiName,drawCanvasName)
                x1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][1]
                y1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][2]
                x2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][3]
                y2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][4]
                if type(x1) == type(1.0):
                    x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                if type(y1) == type(1.0):
                    y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                if type(x2) == type(1.0):
                    if x2 <= 1.0:
                        x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                    else:
                        x2 = x1 + int(x2)
                if type(y2) == type(1.0):
                    if y2 <= 1.0:
                        y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                    else:
                        y2 = y1 + int(y2)
                TableInfo = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][10]
                RowIndex = 0
                for rowInfoLine in TableInfo['rows']:
                    CowIndex = 0
                    for rowInfo in rowInfoLine:
                        if checkPtInRect(CowIndex,RowIndex,BeginCow,EndCow,BeginRow,EndRow) == True:
                            rowInfo[1] = 0
                        CowIndex = CowIndex + 1
                    RowIndex = RowIndex + 1
                TableInfo['merge'].append([(BeginRow,BeginCow),(EndRow,EndCow),'',1])
                drawCanvas.delete(shapeTag)
                Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]
                Params[5] = TableInfo
                DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
def SetCanvasTableCellSplit(uiName,drawCanvasName,shapeTag,row=0,col=0):
    """'+Language.G_Language[2101]+'"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]: 
                drawCanvas = GetElement(uiName,drawCanvasName)
                x1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][1]
                y1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][2]
                x2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][3]
                y2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][4]
                if type(x1) == type(1.0):
                    x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                if type(y1) == type(1.0):
                    y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                if type(x2) == type(1.0):
                    if x2 <= 1.0:
                        x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                    else:
                        x2 = x1 + int(x2)
                if type(y2) == type(1.0):
                    if y2 <= 1.0:
                        y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                    else:
                        y2 = y1 + int(y2)
                TableInfo = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][10]
                for mergeInfo in TableInfo['merge']:
                    MergeBeginRow = mergeInfo[0][0]
                    MergeBeginCow = mergeInfo[0][1]
                    MergeEndRow = mergeInfo[1][0]
                    MergeEndCow = mergeInfo[1][1]
                    if checkPtInRect(col,row,MergeBeginCow,MergeEndCow,MergeBeginRow,MergeEndRow) == True:
                        TableInfo['merge'].remove(mergeInfo)
                    RowIndex = 0
                    for rowInfoLine in TableInfo['rows']:
                        CowIndex = 0
                        for rowInfo in rowInfoLine:
                            if checkPtInRect(CowIndex,RowIndex,MergeBeginCow,MergeEndCow,MergeBeginRow,MergeEndRow) == True:
                                rowInfo[1] = 1
                        CowIndex = CowIndex + 1
                    RowIndex = RowIndex + 1
                drawCanvas.delete(shapeTag)
                Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]
                Params[5] = TableInfo
                DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
def SetCanvasTableRowTextList(uiName,drawCanvasName,shapeTag,row=0,textList=[]):
    """'+Language.G_Language[2098]+'"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]: 
                drawCanvas = GetElement(uiName,drawCanvasName)
                x1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][1]
                y1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][2]
                x2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][3]
                y2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][4]
                if type(x1) == type(1.0):
                    x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                if type(y1) == type(1.0):
                    y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                if type(x2) == type(1.0):
                    if x2 <= 1.0:
                        x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                    else:
                        x2 = x1 + int(x2)
                if type(y2) == type(1.0):
                    if y2 <= 1.0:
                        y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                    else:
                        y2 = y1 + int(y2)
                TableInfo = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][10]
                if row < len(TableInfo['rows']):
                    col = 0
                    for cellText in textList:
                        CellInfo = TableInfo['rows'][row][col]
                        CellInfo[0] = str(cellText)
                        for mergeInfo in TableInfo['merge']:
                            MergeBeginRow = mergeInfo[0][0]
                            MergeBeginCow = mergeInfo[0][1]
                            MergeEndRow = mergeInfo[1][0]
                            MergeEndCow = mergeInfo[1][1]
                            if checkPtInRect(col,row,MergeBeginCow,MergeEndCow,MergeBeginRow,MergeEndRow) == True:
                                mergeInfo[2] = str(cellText)
                        col = col + 1
                    drawCanvas.delete(shapeTag)
                    Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]
                    Params[5] = TableInfo
                    DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
''' 
    f.write(code)
#写入切换按钮事件
def WriteOnSwitchFunction(f):
    code='''
def OnSwitch(uiName,drawCanvasName,shapeTag,actionInfo):
    """'+Language.G_Language[3333]+'"""
    if uiName not in G_CanvasShapeDictionary:
        return None
    if drawCanvasName in G_CanvasShapeDictionary[uiName]:
        if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            drawCanvas = GetElement(uiName,drawCanvasName)
            drawCanvas.delete(shapeTag)
            x1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][1]
            y1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][2]
            x2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][3]
            y2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][4]
            SwitchWidth = x2 - x1
            SwitchHeight = y2 - y1
            Switch_radius = int(SwitchHeight/2)
            fillcolor = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][5]
            outlinecolor = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][6]
            if actionInfo[2] == False:
                fillcolor = '#777777'
                drawCanvas.create_oval(x1, y1, x1+SwitchHeight, y1+SwitchHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
                drawCanvas.create_oval(x1+(SwitchWidth-SwitchHeight), y1, x1+SwitchWidth,y1+ SwitchHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
                drawCanvas.create_rectangle(x1+Switch_radius,y1,x1+(SwitchWidth-Switch_radius),y1+SwitchHeight,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
                drawCanvas.create_oval(x1+2, y1+2, x1+(SwitchHeight-3), y1+(SwitchHeight-3),fill=outlinecolor,width=0,tag=shapeTag)
                drawCanvas.create_text(x1+(SwitchWidth-int(1.0*SwitchHeight)), y1+int(SwitchHeight/2), text="Off",font = ("System",int(SwitchHeight/2)),anchor=\'center\',fill=outlinecolor,width=0,tag=shapeTag)
                actionInfo[2] = True
            else:
                drawCanvas.create_oval(x1, y1, x1+SwitchHeight, y1+SwitchHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
                drawCanvas.create_oval(x1+(SwitchWidth-SwitchHeight), y1, x1+SwitchWidth,y1+ SwitchHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
                drawCanvas.create_rectangle(x1+Switch_radius,y1,x1+(SwitchWidth-Switch_radius),y1+SwitchHeight,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
                drawCanvas.create_oval(x1+(SwitchWidth-SwitchHeight)-2, y1+2, x1+SwitchWidth-3, y1+(SwitchHeight-3),fill=outlinecolor,width=0,tag=shapeTag)
                drawCanvas.create_text(x1+int(0.8*SwitchHeight), y1+int(SwitchHeight/2), text="On",font = ("System",int(SwitchHeight/2)),anchor=\'center\',fill=outlinecolor,width=0,tag=shapeTag)
                actionInfo[2] = False

''' 
    f.write(code)
#写入切换按钮事件
def WriteOnExpandOrShrinkFunction(f):
    code='''
def OnExpandOrShrink(uiName,drawCanvasName,shapeTag,actionInfo):
    """'+Language.G_Language[3334]+'"""
    if uiName not in G_CanvasShapeDictionary:
        return None
    if drawCanvasName in G_CanvasShapeDictionary[uiName]:
        listmenuNameIndex = shapeTag.rfind(\'_\')
        listmenuName = shapeTag[0:listmenuNameIndex]
        if listmenuName in G_CanvasShapeDictionary[uiName][drawCanvasName]:
            drawCanvas = GetElement(uiName,drawCanvasName)
            drawCanvas.delete('drawing_shape')
            drawInfo = G_CanvasShapeDictionary[uiName][drawCanvasName][listmenuName]
            MenuInfo = drawInfo[10]
            SubMenus = MenuInfo['SubMenus']
            x1 = drawInfo[1]
            y1 = drawInfo[2]
            x2 = drawInfo[3]
            y2 = drawInfo[4]
            fillcolor = drawInfo[5]
            outlinecolor = drawInfo[6]
            fillwidth = int(drawInfo[7])
            dashx = int(drawInfo[8])
            dashy = int(drawInfo[9])
            for subMenu in SubMenus:
                titleText = subMenu[0]
                bgImgFile = subMenu[1]
                itemList = subMenu[2]
                subMenuTag = listmenuName +"_"+titleText
                drawCanvas.delete(subMenuTag)
                if shapeTag == subMenuTag:
                    if subMenu[3] == True:
                        subMenu[3] = False
                    else:
                        subMenu[3] = True
            DoCanvasRecord(drawCanvas,\"listmenu\",x1,y1,x2,y2,fillcolor,outlinecolor,fillwidth,dash1=0,dash2=0,newImage=MenuInfo,text='',textFont = None,textColor='',shapeTag=listmenuName)
            for subMenu in SubMenus:
                titleText = subMenu[0]
                subMenuTag = listmenuName +"_"+titleText
                drawCanvas.tag_bind(subMenuTag, "<Button-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=subMenuTag,eventName="ButtonDown"))


''' 
    f.write(code)
#写入删除图形
def WriteDeleteShapeFunction(f):
    code='''
def DeleteShape(uiName,drawCanvasName,shapeTag):
    """'+Language.G_Language[1295]+'"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
                drawCanvas = GetElement(uiName,drawCanvasName)
                drawCanvas.delete(shapeTag)
                OutLineTag = shapeTag+"_outline"
                drawCanvas.delete(OutLineTag)
                G_CanvasShapeDictionary[uiName][drawCanvasName].pop(shapeTag)
                if drawCanvasName in G_CanvasEventDictionary[uiName]:
                    if shapeTag in G_CanvasEventDictionary[uiName][drawCanvasName]:
                        G_CanvasEventDictionary[uiName][drawCanvasName].pop(shapeTag)
                if drawCanvasName in G_CanvasParamDictionary[uiName]:
                    if shapeTag in G_CanvasParamDictionary[uiName][drawCanvasName]:
                        G_CanvasParamDictionary[uiName][drawCanvasName].pop(shapeTag)
'''
    f.write(code)
def WriteSetShapeEventFunction(f,runMode):
    code='''
def BindShapeEvent_SetShapeRect(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,x,y,w,h):
    """'+Language.G_Language[858]+'"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
    #f.write('                drawCanvas = GetElement(uiName,drawCanvasName)
                actionInfo = ["SetShapeRect",targetShapeTag,x,y,w,h]
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_SetFillColor(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,color):
    """'+Language.G_Language[859]+'"""
    
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
    #f.write('                drawCanvas = GetElement(uiName,drawCanvasName)
                actionInfo = ["SetFillColor",targetShapeTag,color]
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_SetOutlineColor(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,color):
    """'+Language.G_Language[860]+'"""
    
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
    #f.write('                drawCanvas = GetElement(uiName,drawCanvasName)
                actionInfo = ["SetOutlineColor",targetShapeTag,color]
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_ChangeImage(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,ImageFile):
    """'+Language.G_Language[861]+'"""
    
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
    #f.write('                drawCanvas = GetElement(uiName,drawCanvasName)
                actionInfo = ["ChangeImage",targetShapeTag,ImageFile]
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_ChangeText(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,Text,TextColor):
    """'+Language.G_Language[862]+'"""
    
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
    #f.write('                drawCanvas = GetElement(uiName,drawCanvasName)
                actionInfo = ["ChangeText",targetShapeTag,Text,TextColor]
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_JumpToUI(uiName,drawCanvasName,shapeTag,bindEvent,targetUIName):
    """'+Language.G_Language[876]+'"""
    
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
    #f.write('                drawCanvas = GetElement(uiName,drawCanvasName)
                actionInfo = ["JumpToUI",shapeTag,targetUIName]
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_LoadUI(uiName,drawCanvasName,shapeTag,bindEvent,widgetName,targetUIName):
    """'+Language.G_Language[1567]+'"""
    
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
    #f.write('                drawCanvas = GetElement(uiName,drawCanvasName)
                actionInfo = ["LoadUI",shapeTag,widgetName,targetUIName]
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_DeleteShape(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag):
    """'+Language.G_Language[877]+'"""
    
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
    #f.write('                drawCanvas = GetElement(uiName,drawCanvasName)
                actionInfo = ["DeleteShape",targetShapeTag]
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_CallFunction(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,callBackFuncton,param = None):
    """'+Language.G_Language[863]+'"""
    if uiName in G_CanvasShapeDictionary:
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:
    #f.write('                drawCanvas = GetElement(uiName,drawCanvasName)
    #f.write('                actionInfo = ["CallFunction",targetShapeTag,callBackFuncton]
                actionInfo = ["CallFunction",callBackFuncton,param]
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo):
    """'+Language.G_Language[864]+'"""
    
    if uiName in G_CanvasShapeDictionary:
        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
        if bindEvent not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][bindEvent] = []
        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][bindEvent].append(actionInfo)
        drawCanvas = GetElement(uiName,drawCanvasName)
        if bindEvent == "MouseEnter":
    if runMode == 'android':
                drawCanvas.tag_bind(uiName,drawCanvasName,shapeTag, "MouseEnter",Shape_MouseEvent)
    else:
                drawCanvas.tag_bind(shapeTag, "<Any-Enter>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseEnter"))
            if G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                TextTag = shapeTag+"_text"
    if runMode == 'android':
                    drawCanvas.tag_bind(uiName,drawCanvasName,TextTag, "MouseEnter",Shape_MouseEvent)
    else:
                    drawCanvas.tag_bind(TextTag, "<Any-Enter>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseEnter"))
        elif bindEvent == "MouseLeave":
    if runMode == 'android':
                drawCanvas.tag_bind(uiName,drawCanvasName,shapeTag, "MouseLeave",Shape_MouseEvent)
    else:
                drawCanvas.tag_bind(shapeTag, "<Any-Leave>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseLeave"))
            if G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                TextTag = shapeTag+"_text"
    if runMode == 'android':
                    drawCanvas.tag_bind(uiName,drawCanvasName,TextTag, "MouseLeave",Shape_MouseEvent)
    else:
                    drawCanvas.tag_bind(TextTag, "<Any-Leave>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseLeave"))
        elif bindEvent == "ButtonDown":
    if runMode == 'android':
                drawCanvas.tag_bind(uiName,drawCanvasName,shapeTag, "ButtonDown",Shape_MouseEvent)
    else:
                drawCanvas.tag_bind(shapeTag, "<Button-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonDown"))
            if G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                TextTag = shapeTag+"_text"
    if runMode == 'android':
                    drawCanvas.tag_bind(uiName,drawCanvasName,TextTag, "ButtonDown",Shape_MouseEvent)
    else:
                    drawCanvas.tag_bind(TextTag, "<Button-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonDown"))
        elif bindEvent == "ButtonMotion":
    if runMode == 'android':
                drawCanvas.tag_bind(uiName,drawCanvasName,shapeTag, "ButtonMotion",Shape_MouseEvent)
    else:
                drawCanvas.tag_bind(shapeTag, "<B1-Motion>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonMotion"))
            if G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                TextTag = shapeTag+"_text"
    if runMode == 'android':
                    drawCanvas.tag_bind(uiName,drawCanvasName,TextTag, "ButtonMotion",Shape_MouseEvent)
    else:
                    drawCanvas.tag_bind(TextTag, "<B1-Motion>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonMotion"))
        elif bindEvent == "ButtonUp":
    if runMode == 'android':
                drawCanvas.tag_bind(uiName,drawCanvasName,shapeTag, "ButtonUp",Shape_MouseEvent)
    else:
                drawCanvas.tag_bind(shapeTag, "<ButtonRelease-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonUp"))
            if G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                TextTag = shapeTag+"_text"
    if runMode == 'android':
                    drawCanvas.tag_bind(uiName,drawCanvasName,TextTag, "ButtonUp",Shape_MouseEvent)
    else:
                    drawCanvas.tag_bind(TextTag, "<ButtonRelease-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonUp"))
        elif bindEvent == "DoubleClick":
    if runMode == 'android':
                drawCanvas.tag_bind(uiName,drawCanvasName,shapeTag, "DoubleClick",Shape_MouseEvent)
    else:
                drawCanvas.tag_bind(shapeTag, "<Double-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="DoubleClick"))
            if G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':
                TextTag = shapeTag+"_text"
    if runMode == 'android':
                    drawCanvas.tag_bind(uiName,drawCanvasName,TextTag, "DoubleClick",Shape_MouseEvent)
    else:
                    drawCanvas.tag_bind(TextTag, "<Double-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="DoubleClick"))

''' 
    f.write(code)
#写入画板动作
def WriteDoCanvasRecordFunctions_Mobile(f):
    code='''
    #f.write(Language.G_Language[1234]+'
def DoCanvasRecord(drawCanvas,ShapeType,x,y,x2,y2,fillcolor,outlinecolor,fillwidth,roundRadius,shapeTag):
    """'+Language.G_Language[1234]+'"""
    center_x = (x + x2)/2
    center_y = (y + y2)/2
    width = x2 - x
    height = y2 - y
    if  drawCanvas != None:
        if ShapeType == 'line' or ShapeType == 'pen'  :
            drawCanvas.create_line(x, y, x2, y2,fill=fillcolor, width = fillwidth,tag = shapeTag)
        elif ShapeType == 'arrow':
            drawCanvas.create_line(x, y, x2, y2,arrow=tkinter.LAST,fill=fillcolor, width = fillwidth,tag = shapeTag)
        elif ShapeType == 'rect':
            drawCanvas.create_rectangle(x, y, x2, y2,fill=fillcolor,outline=outlinecolor, width = fillwidth,tag = shapeTag)
        elif ShapeType == 'roundrect':
            width = x2 - x
            height = y2 - y
            if roundRadius == 0:
               roundRadius = int(0.2 * height)
            if roundRadius == 0:
                drawCanvas.create_rectangle(x, y, x + width,y + height,fill=fillcolor, outline=outlinecolor,width = fillwidth,tag=shapeTag)
            else:
                drawCanvas.create_rectangle(x+roundRadius,y+roundRadius,x+width-roundRadius, y+height-roundRadius,fill=fillcolor, width = 0,tag=shapeTag)
                drawCanvas.create_rectangle(x+roundRadius,y,x+width-roundRadius,y+roundRadius,fill=fillcolor, width=0,tag=shapeTag)
                drawCanvas.create_rectangle(x+roundRadius,y+height-roundRadius,x+width-roundRadius,y+height,fill=fillcolor, width=0,tag=shapeTag)
                drawCanvas.create_rectangle(x,y+roundRadius,x+roundRadius,y+height-roundRadius,fill=fillcolor,width=0,tag=shapeTag)
                drawCanvas.create_rectangle(x+width-roundRadius,y+roundRadius,x+width,y+height-roundRadius,fill=fillcolor,width=0,tag=shapeTag)
            OutLineTag = shapeTag+"_outline"
            if fillwidth > 0:
                drawCanvas.create_line(x+roundRadius,y,x+width-roundRadius,y,fill=outlinecolor,tag=OutLineTag,width=fillwidth)
                drawCanvas.create_line(x+roundRadius,y+height,x+width-roundRadius,y+height,fill=outlinecolor,tag=OutLineTag,width=fillwidth)
                drawCanvas.create_line(x,y+roundRadius,x,y+height-roundRadius,fill=outlinecolor,tag=OutLineTag,width=fillwidth)
                drawCanvas.create_line(x+width,y+roundRadius,x+width,y+height-roundRadius,fill=outlinecolor,tag=OutLineTag,width=fillwidth)
            drawCanvas.create_oval(x,y,x+2*roundRadius,y+2*roundRadius,fill=fillcolor,outline=fillcolor,width=0,tag=shapeTag)
            drawCanvas.create_oval(x+width-2*roundRadius,y,x+width,y+2*roundRadius,fill=fillcolor,outline=fillcolor,width=0,tag=shapeTag)
            drawCanvas.create_oval(x+width-2*roundRadius,y+height-2*roundRadius,x+width,y+height,fill=fillcolor,outline=fillcolor,width=0,tag=shapeTag)
            drawCanvas.create_oval(x,y+height-2*roundRadius,x+2*roundRadius,y+height,fill=fillcolor,outline=fillcolor,width=0,tag=shapeTag)
            OutArcTag = shapeTag+"_arc"
            if fillwidth > 0:
                drawCanvas.create_arc(x,y,x+2*roundRadius,y+2*roundRadius,startAngle=90,endAngle=180,outline=outlinecolor,width=fillwidth, tag=OutArcTag)
                drawCanvas.create_arc(x+width-2*roundRadius,y,x+width,y+2*roundRadius,startAngle=0,endAngle=90,outline=outlinecolor,width=fillwidth, tag=OutArcTag)
                drawCanvas.create_arc(x+width-2*roundRadius,y+height-2*roundRadius,x+width,y+height,startAngle=-90,endAngle=0,outline=outlinecolor,width=fillwidth, tag=OutArcTag)
                drawCanvas.create_arc(x,y+height-2*roundRadius,x+2*roundRadius,y+height,startAngle=180,endAngle=270,outline=outlinecolor,width=fillwidth, tag=OutArcTag)
        elif ShapeType == 'triangle':
            points = [
                #顶点
                x,
                y + height,
                #右上点
                x + int(width/2),
                y,
                #左下点
                x + width,
                y + height,
                #顶点
                x,
                y + height,
                ]
            # 根据点来连线
            lastDraw = drawCanvas.create_polygon(
                    points,
                    fill=fillcolor,
                    outline=outlinecolor, 
                    width= fillwidth,
                    tag = shapeTag)
        elif ShapeType == 'diamond':
            points = [
                #左上点
                x,
                y + int(height/2),
                #右上点
                x + int(width/2),
                y,
                #左下点
                x + width,
                y + int(height/2),
                #顶点
                x + int(width/2),
                y + height,
                ]
            # 根据点来连线
            lastDraw = drawCanvas.create_polygon(
                    points,
                    fill=fillcolor,
                    outline=outlinecolor, 
                    width= fillwidth,
                    tag = shapeTag)
        elif ShapeType == 'circle':
            drawCanvas.create_oval(x, y, x2, y2,fill=fillcolor,outline=outlinecolor, width = fillwidth,tag = shapeTag)
        elif ShapeType == 'cylinder':
            OvalHeight = int(height * 0.2)
            OvalHeight_Half = int(height * 0.1)
            drawCanvas.create_oval(x,y2-OvalHeight,x2,y2,fill=fillcolor,outline=outlinecolor,width = fillwidth,tag=shapeTag)
            drawCanvas.create_rectangle(x,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill=fillcolor,width=0,tag=shapeTag) 
            drawCanvas.create_oval(x,y,x2,y+OvalHeight,fill=fillcolor,outline=outlinecolor,width = fillwidth,tag=shapeTag)
    #f.write('            drawCanvas.create_line(x,y+OvalHeight_Half,x,y2-OvalHeight_Half,fill=outlinecolor,width = fillwidth,tag=shapeTag)
    #f.write('            drawCanvas.create_line(x2,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill=outlinecolor,width = fillwidth,tag=shapeTag)
            drawCanvas.create_rectangle(x-fillwidth-1,y+OvalHeight_Half,x,y2-OvalHeight_Half,fill=outlinecolor,width=0,tag=shapeTag)
            drawCanvas.create_rectangle(x2,y+OvalHeight_Half,x2+fillwidth,y2-OvalHeight_Half,fill=outlinecolor,width=0,tag=shapeTag)
        elif ShapeType == 'star':
            center_x = (x + x2)/2
            center_y = (y + y2)/2
            rx = (x2 - x)/2
            ry = (y2 - y)/2
            points = [
                center_x - int(rx * math.sin(2 * math.pi / 5)),
                center_y - int(ry * math.cos(2 * math.pi / 5)),
                center_x + int(rx * math.sin(2 * math.pi / 5)),
                center_y - int(ry * math.cos(2 * math.pi / 5)),
                center_x - int(rx * math.sin(math.pi / 5)),
                center_y + int(ry * math.cos(math.pi / 5)),
                center_x,
                center_y - ry,
                center_x + int(rx * math.sin(math.pi / 5)),
                center_y + int(ry * math.cos(math.pi / 5)),
                ]
            lastDraw = drawCanvas.create_polygon(
                    points,
                    fill=fillcolor,
                    outline=outlinecolor, 
                    width= fillwidth,
                    tag = shapeTag)
def DrawLine(uiName,drawCanvasName,x1,y1,x2,y2,color,width=1,dash=(0,0),shapeTag=''):
    """'+Language.G_Language[1450]+'"""
    
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[\'line\',x1,y1,x2,y2,color,color,width,dash[0],dash[1]]
    DoCanvasRecord(drawCanvas,'line',x1,y1,x2,y2,color,color,width,0,shapeTag=shapeTag)

def DrawArrow(uiName,drawCanvasName,x1,y1,x2,y2,color,width=1,dash=(0,0),shapeTag=''):
    """'+Language.G_Language[1451]+'"""
    
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[\'arrow\',x1,y1,x2,y2,color,color,width,dash[0],dash[1]]
    DoCanvasRecord(drawCanvas,'arrow',x1,y1,x2,y2,color,color,width,0,shapeTag=shapeTag)
def DrawTriangle(uiName,drawCanvasName,direction,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):
    """'+Language.G_Language[1452]+'"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    TriangleType = "triangle_up"
    if direction == "down":
        TriangleType = "triangle_down"
    if direction == "left":
        TriangleType = "triangle_left"
    if direction == "right":
        TriangleType = "triangle_right"
    G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[TriangleType,x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]
    DoCanvasRecord(drawCanvas,TriangleType,x1,y1,x2,y2,color,outlinecolor,outlinewidth,0,shapeTag=shapeTag)
def DrawRectangle(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):
    """'+Language.G_Language[1453]+'"""
    
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[\'rect\',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]
    DoCanvasRecord(drawCanvas,'rect',x1,y1,x2,y2,color,outlinecolor,outlinewidth,0,shapeTag=shapeTag)
def DrawRoundedRectangle(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),roundRadius=10,shapeTag=''):
    """'+Language.G_Language[1462]+'"""
    
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[\'roundrect\',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]
    DoCanvasRecord(drawCanvas,'roundrect',x1,y1,x2,y2,color,outlinecolor,outlinewidth,roundRadius,shapeTag=shapeTag)
def DrawCircle(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):
    """'+Language.G_Language[1454]+'"""
    
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[\'circle\',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]
    DoCanvasRecord(drawCanvas,'circle',x1,y1,x2,y2,color,outlinecolor,outlinewidth,0,shapeTag=shapeTag)
def DrawDiamond(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):
    """'+Language.G_Language[1455]+'"""
    
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[\'diamond\',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]
    DoCanvasRecord(drawCanvas,'diamond',x1,y1,x2,y2,color,outlinecolor,outlinewidth,0,shapeTag=shapeTag)
def DrawCylinder(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):
    """'+Language.G_Language[1456]+'"""
    
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[\'cylinder\',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]
    DoCanvasRecord(drawCanvas,'cylinder',x1,y1,x2,y2,color,outlinecolor,outlinewidth,0,shapeTag=shapeTag)
def DrawStar(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):
    """'+Language.G_Language[1457]+'"""
    
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[\'star\',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]
    DoCanvasRecord(drawCanvas,'star',x1,y1,x2,y2,color,outlinecolor,outlinewidth,0,shapeTag=shapeTag)
def DrawText(uiName,drawCanvasName,x,y,text,textFont=None,color='#FFFFFF',anchor='nw',shapeTag=''):
    """'+Language.G_Language[1458]+'"""
    
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[\'text\',x,y,x,y,text,textFont,color]
    drawCanvas.create_text(x, y,fill=color,text=text,font = textFont,anchor=anchor,tag=shapeTag)
    # if androidTTFFile and (androidTTFFile.find('.ttf') > 0 or androidTTFFile.find('.otf') > 0):
    #     androidFont = GameLib.Res.GetFont("'+androidTTFFile+'",sizetext)
    #     drawCanvas.create_text_simple(x,y,x,y,text=text,font = androidFont,anchor=anchor,tag = shapeTag)
    # else:
    #     drawCanvas.create_text(x,y,x,y,text=text,font = textFont,anchor=anchor,tag = shapeTag)
def DrawImage(uiName,drawCanvasName,x1,y1,x2,y2,imagefile,shapeTag=''):
    """'+Language.G_Language[1459]+'"""
    
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[\'image\',x1,y1,x2,y2,imagefile]
    drawCanvas.create_image(x1,y1,x2,y2,imagefile=imagefile,tag=shapeTag)
def DrawButton(uiName,drawCanvasName,x1,y1,x2,y2,text='',textcolor='#000000',textFont = None,fillcolor='#FFFFFF',outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):
    """'+Language.G_Language[1461]+'"""
    
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    center_x = (x1 + x2)/2
    center_y = (y1 + y2)/2
    oval_rx = 20
    dash1=dash[0],dash2=dash[1]
    if  dash1 > 0 :
        drawCanvas.create_oval(x1,y1,x1+2*oval_rx,y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = outlinewidth,tag=shapeTag)
        drawCanvas.create_oval(x2-2*oval_rx,y1,x2,y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = outlinewidth,tag=shapeTag)
        drawCanvas.create_rectangle(x1+oval_rx, y1, x2-oval_rx, y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2), width = outlinewidth,tag=shapeTag)
        drawCanvas.create_rectangle(x1+oval_rx, y1+outlinewidth, x2-oval_rx, y2-outlinewidth+1,fill=fillcolor, width = 0,tag=shapeTag)
        drawCanvas.create_line(x1+oval_rx, y1+outlinewidth-1, x1+oval_rx, y2-outlinewidth+1,fill=fillcolor,width = outlinewidth,tag=shapeTag)
        drawCanvas.create_line(x2-oval_rx, y1+outlinewidth-1, x2-oval_rx, y2-outlinewidth+1,fill=fillcolor,width = outlinewidth,tag=shapeTag)
    else:
        drawCanvas.create_oval(x1,y1,x1+2*oval_rx,y2,fill=fillcolor,outline=outlinecolor,width = outlinewidth,tag=shapeTag)
        drawCanvas.create_oval(x2-2*oval_rx,y1,x2,y2,fill=fillcolor,outline=outlinecolor,width = outlinewidth,tag=shapeTag)
        drawCanvas.create_rectangle(x1+oval_rx, y1, x2-oval_rx, y2,fill=fillcolor,outline=outlinecolor, width = outlinewidth,tag=shapeTag)
        drawCanvas.create_rectangle(x1+oval_rx, y1+outlinewidth, x2-oval_rx, y2-outlinewidth+1,fill=fillcolor, width = 0,tag=shapeTag)
        drawCanvas.create_line(x1+oval_rx, y1+outlinewidth-1, x1+oval_rx, y2-outlinewidth+1,fill=fillcolor,width = outlinewidth,tag=shapeTag)
        drawCanvas.create_line(x2-oval_rx, y1+outlinewidth-1, x2-oval_rx, y2-outlinewidth+1,fill=fillcolor,width = outlinewidth,tag=shapeTag)
    if len(text) > 0:
        drawCanvas.create_text(center_x, center_y,text=text,fill=textcolor,anchor='center',tag=shapeTag+\"_text\")
def EraserCanvas(uiName,drawCanvasName,x1,y1,x2,y2):
    """'+Language.G_Language[1460]+'"""
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:
        return
    bgcolor = drawCanvas.cget('bg')
    DoCanvasRecord(drawCanvas,'eraser',x1,y1,x2,y2,bgcolor,bgcolor,0,0,shapeTag=shapeTag)
''' 
    f.write(code)
#写入设置图形矩形
def WriteReDrawCanvasRecordFunction_Mobile(f):
    code='''
def ReDrawCanvasRecord(uiName,ForceReDraw=False):
    pass
def ResizeAllChart(uiName):
    """'+Language.G_Language[759]+'"""
    pass'''
    f.write(code)

#写入画板动作
def WriteLoadCanvasRecordFunctions_Mobile(f,exportMode,androidTTFFile):
    code='''
def checkPtInRect(x,y,left,right,top,bottom):
    if x < left:return 0
    if x > right:return 0
    if y < top:return 0
    if y > bottom:return 0
    return 1
def Shape_MouseEvent(x,y,uiName,canvasName,shapeTag,eventName):
    
    if eventName == 'MouseLeave':
        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]
        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]
        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]
        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]
        borderwidth = 0
        if G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'button':
            borderwidth = 1 + G_CanvasShapeDictionary[uiName][canvasName][shapeTag][10]
        if checkPtInRect(x,y,x1+borderwidth,x2-borderwidth,y1+borderwidth,y2-borderwidth) == 1:
            return 
    if shapeTag not in G_CanvasEventDictionary[uiName][canvasName]:
        return
    if eventName not in G_CanvasEventDictionary[uiName][canvasName][shapeTag]:
        return
    for actionInfo in G_CanvasEventDictionary[uiName][canvasName][shapeTag][eventName]:
        if actionInfo[0] == "SetShapeRect":
            SetShapeRect(uiName ,canvasName,actionInfo[1],actionInfo[2],actionInfo[3],actionInfo[4],actionInfo[5])
        elif actionInfo[0] == "SetFillColor":
            SetShapeFillColor(uiName ,canvasName,actionInfo[1],actionInfo[2])
        elif actionInfo[0] == "SetOutlineColor":
            SetShapeOutlineColor(uiName ,canvasName,actionInfo[1],actionInfo[2])
        elif actionInfo[0] == "ChangeImage":
            SetShapeImage(uiName ,canvasName,actionInfo[1],actionInfo[2])
        elif actionInfo[0] == "ChangeText":
            SetShapeText(uiName ,canvasName,actionInfo[1],actionInfo[2],actionInfo[3])
        elif actionInfo[0] == "DeleteShape":
            SetShapeText(uiName ,canvasName,actionInfo[1])
        elif actionInfo[0] == "JumpToUI":
            UIPath, UIFile = os.path.split(actionInfo[2])
            UIName, extension = os.path.splitext(UIFile)
            if len(UIPath) > 0:
                import sys
                sys.path.append(UIPath)
            GoToUIDialog(uiName,UIName)
        elif actionInfo[0] == "LoadUI":
            WidgetName = actionInfo[2]
            UIPath, UIFile = os.path.split(actionInfo[3])
            UIName, extension = os.path.splitext(UIFile)
            if len(UIPath) > 0:
                import sys
                sys.path.append(UIPath)
            if WidgetName == "Form_1":
                WidgetName == "root"
            LoadUIDialog(uiName,WidgetName,UIName)
        elif actionInfo[0] == "DeleteShape":
            DeleteShape(uiName ,canvasName,actionInfo[1])
        elif actionInfo[0] == "OnSwitch":
            OnSwitch(uiName ,canvasName,actionInfo[1],actionInfo)
        elif actionInfo[0] == "OnExpandOrShrink":
            OnExpandOrShrink(uiName ,canvasName,actionInfo[1],actionInfo)
        elif actionInfo[0] == "CallFunction":
            if actionInfo[1]:
                Event = PyMeEvent(x,y,shapeTag)
                if actionInfo[2]:
                   actionInfo[1](Event,uiName,canvasName,actionInfo[2])
                else:
                   actionInfo[1](Event,uiName,canvasName)
    #f.write(Language.G_Language[1235]+'
def LoadCanvasRecord(uiName):
    """'+Language.G_Language[1235]+'"""
    drawCanvasName = None
    drawCanvas = None
    
    def Hex_to_RGB(hex):
        r = int(hex[1:3],16)
        g = int(hex[3:5],16)
        b = int(hex[5:7], 16)
        return (r,g,b)
'''
    f.write(code)

    if exportMode == False:
        code='''
        canvasFile = GameLib.APKResDir + "\\\\res\\\\" + uiName + ".cav"
'''
        f.write(code)
    else:
        code='''
        resdir = os.path.join(GameLib.APKResDir,"res")
        canvasFile = os.path.join(resdir,uiName + ".cav")
        canvasFile = canvasFile.replace("\\\\","//")
    if os.path.exists(canvasFile) == True:
        f = open(canvasFile,encoding='utf-8')
        line ="" 
        while True:
            line = f.readline()
            if not line:
                break
            text = line.strip()
            if not text:
                continue
            if text.find('Canvas:') >= 0:
                splitArray = text.split(':')
                drawCanvasName = splitArray[1].strip()
                drawCanvas = GetElement(uiName,drawCanvasName)
                G_CanvasShapeDictionary[uiName][drawCanvasName] = {}
                G_CanvasFontDictionary[uiName][drawCanvasName] = []
                G_CanvasImageDictionary[uiName][drawCanvasName] = []
                G_CanvasPointDictionary[uiName][drawCanvasName] = {}
                G_CanvasEventDictionary[uiName][drawCanvasName] = {}
                continue
            elif text.find(',') >= 0:
                if drawCanvas != None:
                    splitArray = text.split(',')
                    ShapeType = splitArray[0]
                    if ShapeType == \'image\':
                        if splitArray[1].find('.') > 0:
                            x1 = float(splitArray[1])
                        else:
                            x1 = int(splitArray[1])
                        if splitArray[2].find('.') > 0:
                            y1 = float(splitArray[2])
                        else:
                            y1 = int(splitArray[2])
                        if splitArray[3].find('.') > 0:
                            x2 = float(splitArray[3])
                        else:
                            x2 = int(splitArray[3])
                        if splitArray[4].find('.') > 0:
                            y2 = float(splitArray[4])
                        else:
                            y2 = int(splitArray[4])
                        w = x2 - x1
                        h = y2 - y1
                        fill = splitArray[5]
                        outline = splitArray[6]
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        imagefile = splitArray[10]
                        newImage = None
                        newtext = ''
                        textFont = None
                        shapeTag = ''
                        imagefile = splitArray[10]
                        if len(splitArray) > 12:
                            shapeTag = splitArray[11]
                            G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,imagefile]
                        drawCanvas.create_image(x1,y1,x2,y2,imagefile=imagefile,tag=shapeTag)
                    elif ShapeType == \'roundrect\':
                        if splitArray[1].find('.') > 0:
                            x1 = float(splitArray[1])
                        else:
                            x1 = int(splitArray[1])
                        if splitArray[2].find('.') > 0:
                            y1 = float(splitArray[2])
                        else:
                            y1 = int(splitArray[2])
                        if splitArray[3].find('.') > 0:
                            x2 = float(splitArray[3])
                        else:
                            x2 = int(splitArray[3])
                        if splitArray[4].find('.') > 0:
                            y2 = float(splitArray[4])
                        else:
                            y2 = int(splitArray[4])
                        w = x2 - x1
                        h = y2 - y1
                        fill = splitArray[5]
                        outline = splitArray[6]
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        roundradius = int(splitArray[10])
                        shapeTag = splitArray[11]
                        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,roundradius]
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,roundradius,shapeTag)
                    elif ShapeType == \'text\':
                        if splitArray[1].find('.') > 0:
                            x1 = float(splitArray[1])
                        else:
                            x1 = int(splitArray[1])
                        if splitArray[2].find('.') > 0:
                            y1 = float(splitArray[2])
                        else:
                            y1 = int(splitArray[2])
                        if splitArray[3].find('.') > 0:
                            x2 = float(splitArray[3])
                        else:
                            x2 = int(splitArray[3])
                        if splitArray[4].find('.') > 0:
                            y2 = float(splitArray[4])
                        else:
                            y2 = int(splitArray[4])
                        w = x2 - x1
                        h = y2 - y1
                        fill = splitArray[5]
                        outline = splitArray[6]
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        imagefile = ""
                        newImage = None
                        shapeTag = ''
                        newtext = splitArray[10]
                        familytext = splitArray[11]
                        sizetext = int(splitArray[12])
                        weighttext = splitArray[13]
                        slanttext = splitArray[14]
                        underline = int(splitArray[15])
                        overstrike = int(splitArray[16])
                        if len(splitArray) > 18:
                            shapeTag = splitArray[17]
'''
        f.write(code)
    if androidTTFFile and (androidTTFFile.find('.ttf') > 0 or androidTTFFile.find('.otf') > 0):
        code='''
                            androidFont = GameLib.Res.GetFont("'+androidTTFFile+'",sizetext)
                            drawCanvas.create_text_simple(x1,y1,x2,y2,text=newtext,anchor='nw',fill=fill,font = androidFont,tag = shapeTag)
                            G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,newtext,androidFont,fill]
'''
        f.write(code)
    else:
        code='''
                            drawCanvas.create_text(x1,y1,x2,y2,text=newtext,anchor='nw',fill=fill,familytext = familytext,sizetext = sizetext,weighttext = weighttext,slanttext = slanttext,underline = underline,overstrike = overstrike,tag = shapeTag)
                            G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,newtext,None,fill]
'''
        f.write(code)
    code='''
                    elif ShapeType == 'button':
                        if splitArray[1].find('.') > 0:
                            x1 = float(splitArray[1])
                        else:
                            x1 = int(splitArray[1])
                        if splitArray[2].find('.') > 0:
                            y1 = float(splitArray[2])
                        else:
                            y1 = int(splitArray[2])
                        if splitArray[3].find('.') > 0:
                            x2 = float(splitArray[3])
                        else:
                            x2 = int(splitArray[3])
                        if splitArray[4].find('.') > 0:
                            y2 = float(splitArray[4])
                        else:
                            y2 = int(splitArray[4])
                        w = x2 - x1
                        h = y2 - y1
                        fill = splitArray[5]
                        outline = splitArray[6]
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        imagefile = ""
                        newImage = None
                        shapeTag = ''
                        newtext = splitArray[10]
                        familytext = splitArray[11]
                        sizetext = int(splitArray[12])
                        weighttext = splitArray[13]
                        slanttext = splitArray[14]
                        underline = int(splitArray[15])
                        overstrike = int(splitArray[16])
                        textcolor = splitArray[17]
                        imagefile = splitArray[18]
                        shapeTag = splitArray[20]
                        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,fill,familytext,sizetext,weighttext,slanttext,underline,overstrike,textcolor]
'''
        f.write(code)

    if androidTTFFile and (androidTTFFile.find('.ttf') > 0 or androidTTFFile.find('.otf') > 0):
        code='''
                            androidFont = GameLib.Res.GetFont("'+androidTTFFile+'",sizetext)
                            drawCanvas.create_button_simple(x1,y1,x2,y2,text=newtext,anchor='nw',fill=fill,outline=outline,width=width,font = androidFont,textcolor=textcolor,imagefile=imagefile,tag = shapeTag)
    '''
        f.write(code)
    else:
        code='''
                            drawCanvas.create_button(x1,y1,x2,y2,text=newtext,anchor='nw',fill=fill,outline=outline,width=width,familytext = familytext,sizetext = sizetext,weighttext = weighttext,slanttext = slanttext,underline = underline,overstrike = overstrike,textcolor=textcolor,imagefile=imagefile,tag = shapeTag)
                    elif ShapeType == \'point\':
                        if splitArray[1].find('.') > 0:
                            x1 = float(splitArray[1])
                        else:
                            x1 = int(splitArray[1])
                        if splitArray[2].find('.') > 0:
                            y1 = float(splitArray[2])
                        else:
                            y1 = int(splitArray[2])
                        if splitArray[3].find('.') > 0:
                            x2 = float(splitArray[3])
                        else:
                            x2 = int(splitArray[3])
                        if splitArray[4].find('.') > 0:
                            y2 = float(splitArray[4])
                        else:
                            y2 = int(splitArray[4])
                        w = x2 - x1
                        h = y2 - y1
                        fill = splitArray[5]
                        outline = splitArray[6]
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        imagefile = ""
                        newImage = None
                        shapeTag = ''
                        parentShapeID = splitArray[10]
                        centerX = (x1 + x2)//2
                        centerY = (y1 + y2)//2
                        if len(splitArray) > 12:
                            shapeTag = splitArray[11]
                            G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2]
                        if parentShapeID not in G_CanvasPointDictionary[uiName][drawCanvasName]:
                            G_CanvasPointDictionary[uiName][drawCanvasName][parentShapeID] = {}
                        G_CanvasPointDictionary[uiName][drawCanvasName][parentShapeID][shapeTag] = (centerX,centerY)
                    elif ShapeType == 'SetShapeRect':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        x = round(float(splitArray[4]))
                        y = round(float(splitArray[5]))
                        w = round(float(splitArray[6]))
                        h = round(float(splitArray[7]))    
                        actionInfo = ["SetShapeRect",TargetShapeTag,x,y,w,h]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'SetFillColor':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        Color = splitArray[4]    
                        actionInfo = ["SetFillColor",TargetShapeTag,Color]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'SetOutlineColor':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        Color = splitArray[4]  
                        actionInfo = ["SetOutlineColor",TargetShapeTag,Color]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'ChangeImage':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        ImageFile = splitArray[4]    
                        actionInfo = ["ChangeImage",TargetShapeTag,ImageFile]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'ChangeText':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        Text = splitArray[4]
                        TextColor = splitArray[5]
                        actionInfo = ["ChangeText",TargetShapeTag,Text,TextColor]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'JumpToUI':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        targetUIName = splitArray[3]
                        actionInfo = ["JumpToUI",shapeTag,targetUIName]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'LoadUI':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        widgetName = splitArray[3]
                        targetUIName = splitArray[4]
                        actionInfo = ["LoadUI",shapeTag,widgetName,targetUIName]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'DeleteShape':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = splitArray[3]
                        actionInfo = ["DeleteShape",TargetShapeTag]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'OnSwitch':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        TargetShapeTag = shapeTag
                        actionInfo = ["OnSwitch",TargetShapeTag,True]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'CallFunction':
                        shapeTag = splitArray[1]
                        EventName = splitArray[2]
                        FunctionName = drawCanvasName+"_"+shapeTag+"_on"+EventName
                        CallBackFunc = None
                        if hasattr(drawCanvas,FunctionName) == True:
                            CallBackFunc = getattr(drawCanvas,FunctionName)
                        actionInfo = ["CallFunction",CallBackFunc,None]
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    else:
                        if splitArray[1].find('.') > 0:
                            x1 = float(splitArray[1])
                        else:
                            x1 = int(splitArray[1])
                        if splitArray[2].find('.') > 0:
                            y1 = float(splitArray[2])
                        else:
                            y1 = int(splitArray[2])
                        if splitArray[3].find('.') > 0:
                            x2 = float(splitArray[3])
                        else:
                            x2 = int(splitArray[3])
                        if splitArray[4].find('.') > 0:
                            y2 = float(splitArray[4])
                        else:
                            y2 = int(splitArray[4])
                        fillcolor = splitArray[5]
                        outlinecolor = splitArray[6]
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        if len(splitArray) > 11:
                            shapeTag = splitArray[10]
                            G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2]
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fillcolor,outlinecolor,width,0,shapeTag)
                continue
        f.close()  
        if uiName in G_CanvasEventDictionary: 
            if drawCanvasName in G_CanvasEventDictionary[uiName]:
                for shapeTag in G_CanvasEventDictionary[uiName][drawCanvasName]:
                    for EventName in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:
                        drawCanvas.tag_bind(uiName,drawCanvasName,shapeTag, EventName,Shape_MouseEvent)  
''' 
        f.write(code)
#写入设置图形矩形
def WriteSetShapeRectFunction_Mobile(f):
    code='''
def SetShapeRect(uiName,canvasName,shapeTag,x1,y1,x2,y2):
    """'+Language.G_Language[856]+'"""
    drawCanvas = GetElement(uiName,canvasName)
    drawCanvas.coords(shapeTag, x1,y1,x2,y2) 
    G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1] = x1
    G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2] = y1
    G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3] = x2
    G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4] = y2
def GetShapeRect(uiName,canvasName,shapeTag):
    """'+Language.G_Language[866]+'"""
    drawCanvas = GetElement(uiName,canvasName)
    if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:
        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]
        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]
        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]
        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]
        return (x1,y1,x2,y2)
    return None
''' 
    f.write(code)
#写入设置填充颜色
def WriteSetShapeFillColorFunction_Mobile(f):
    code='''
def SetShapeFillColor(uiName,canvasName,shapeTag,color):
    """'+Language.G_Language[844]+'"""
    drawCanvas = GetElement(uiName,canvasName)
    drawCanvas.itemconfig(shapeTag, "fill",color)
''' 
    f.write(code)
#写入设置边框颜色
def WriteSetShapeOutlineColorFunction_Mobile(f):
    code='''
def SetShapeOutlineColor(uiName,canvasName,shapeTag,color):
    """'+Language.G_Language[845]+'"""
    drawCanvas = GetElement(uiName,canvasName)
    drawCanvas.itemconfig(shapeTag, "outline",color)
''' 
    f.write(code)
#写入设置线条宽度
def WriteSetShapeWidthFunction_Mobile(f):
    code='''
def SetShapeLineWidth(uiName,canvasName,shapeTag,width):
    """'+Language.G_Language[1464]+'"""
    drawCanvas = GetElement(uiName,canvasName)
    drawCanvas.itemconfig(shapeTag, "width",width)
''' 
    f.write(code)
#写入设置图形图片
def WriteSetShapeImageFunction_Mobile(f):
    code='''
def SetShapeImage(uiName,canvasName,shapeTag,imageFile):
    """'+Language.G_Language[846]+'"""
    drawCanvas = GetElement(uiName,canvasName)
    drawCanvas.itemconfig(shapeTag, "image",imageFile) 
''' 
    f.write(code)
#写入设置图形文字
def WriteSetShapeTextFunction_Mobile(f):
    code='''
def SetShapeText(uiName,canvasName,shapeTag,text,color = None):
    """'+Language.G_Language[836]+'"""
    global G_CanvasShapeDictionary
    drawCanvas = GetElement(uiName,canvasName)
    if color is None:
        if canvasName in G_CanvasShapeDictionary[uiName]:
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:  
                color = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][7]
    drawCanvas.itemconfig(shapeTag, "text",text,color) 
    G_CanvasShapeDictionary[uiName][canvasName][shapeTag][5] = text
    G_CanvasShapeDictionary[uiName][canvasName][shapeTag][7] = color
def GetShapeText(uiName,drawCanvasName,shapeTag):
    """'+Language.G_Language[870]+'"""
    if uiName not in G_CanvasShapeDictionary:
        return None
    if drawCanvasName in G_CanvasShapeDictionary[uiName]:
        if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]: 
            text = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][5]
            textColor = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][7]
            return (text,textColor)
    return None

''' 
    f.write(code)
#写入获取绑定点位置
def WriteGetShapePointFunction(f):
    code='''
def GetShapePoint(uiName,drawCanvasName,shapeTag,pointTag,absoluteMode=True):
    """'+Language.G_Language[835]+'"""
    if uiName not in G_CanvasShapeDictionary:
        return None
    if drawCanvasName in G_CanvasShapeDictionary[uiName]:
        if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]: 
            if shapeTag in G_CanvasPointDictionary[uiName][drawCanvasName]:  
                parentX1,parentY1,parentX2,parentY2 = GetShapeRect(uiName,drawCanvasName,shapeTag) 
                if pointTag in G_CanvasPointDictionary[uiName][drawCanvasName][shapeTag]: 
                    shapeX = G_CanvasPointDictionary[uiName][drawCanvasName][shapeTag][pointTag][0] 
                    shapeY = G_CanvasPointDictionary[uiName][drawCanvasName][shapeTag][pointTag][1] 
                    if type(shapeX) == type(1.0): 
                        shapeX = int(shapeX * (parentX2-parentX1)) 
                    if type(shapeY) == type(1.0): 
                        shapeY = int(shapeY * (parentX2-parentX1)) 
                    if absoluteMode == True: 
                        shapeX = shapeX + parentX1 
                        shapeY = shapeY + parentY1 
                    return (shapeX,shapeY) 
    return None 
''' 
    f.write(code)
#写入获取绑定点位置
# def WriteSetShapePositionFunction(f):
#code='''
# def SetShapePosition(uiName,drawCanvasName,shapeTag,x1,y1,x2,y2):
#     """'+Language.G_Language[837]+'"""
#     if drawCanvasName in G_CanvasPointDictionary[uiName]:
#        if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]: 
#            drawCanvas = GetElement(uiName,drawCanvasName)  
#            drawCanvas.delete(shapeTag) 
#            ShapeType = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] 
#            G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][1] = x1 
#            G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][2] = y1 
#            G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][3] = x2 
#            G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][4] = y2 
#            if ShapeType == 'text': 
#                text = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][5] 
#                textFont = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][6] 
#                textcolor = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][7] 
#                drawCanvas.create_text(x1, y1,fill=textcolor,text=text,font = textFont,anchor='nw',tag=shapeTag) 
#            elif ShapeType == 'image': 
#                theImage = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][5] 
#                drawCanvas.create_image(x1, y1,image=theImage,anchor='nw',tag=shapeTag) 
#            else: 
#                fill = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][5] 
#                outline = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][6]
#                width = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][7]
#                dashx = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][8]
#                dashy = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][9]
#                DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,None,'','#FFFFFF',shapeTag)
#     return None 
# def GetShapePosition(uiName,drawCanvasName,shapeTag):
#     """'+Language.G_Language[857]+'"""
#     if drawCanvasName in G_CanvasPointDictionary[uiName]:
#        if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]: 
#            return [G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][1],G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][2],G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][3],G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][4]] 
#     return None 
''' 
    f.write(code)
#写入获取绑定点位置
# def WriteSetShapeTextFunction_Mobile(f):
    code='''
# def SetShapeText(uiName,drawCanvasName,shapeTag,text,fillcolor = None):
#     """'+Language.G_Language[835]+'"""
#     if drawCanvasName in G_CanvasPointDictionary[uiName]:
#         if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:  
#             drawCanvas = GetElement(uiName,drawCanvasName)
#             drawCanvas.delete(shapeTag) 
#             shapeInfo = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag] 
#             shapeInfo[5] = text 
#             textcolor = shapeInfo[4] 
#             if fillcolor: 
#                 textcolor = fillcolor 
#             drawCanvas.create_text(shapeInfo[1],shapeInfo[2],shapeInfo[3],shapeInfo[4],text=text,anchor='nw',fill=textcolor,familytext = shapeInfo[5],sizetext = shapeInfo[6],weighttext = shapeInfo[7],slanttext = shapeInfo[8],underline = shapeInfo[9],overstrike = shapeInfo[10],tag=shapeTag)


#设置RadioButton的样式
def SetWidgetUsePyMeStyle(f):
    code='''
PyMeStyleRadioGroup = {}
def OnRadioButtonClick(groupid,radio_value):
    global PyMeStyleRadioGroup
    if groupid in PyMeStyleRadioGroup.keys():
        for RadioInfo in PyMeStyleRadioGroup[groupid]:
            if RadioInfo["var"] == radio_value:
                RadioInfo["radio"].select()
                RadioInfo["icon"].itemconfig("icon_image", image=RadioInfo["tkimage_yes"])
            else:
                RadioInfo["icon"].itemconfig("icon_image", image=RadioInfo["tkimage_no"])
def OnRadioButtonConfigure(event):
    global PyMeStyleRadioGroup
    for groupid in PyMeStyleRadioGroup.keys():
        for RadioInfo in PyMeStyleRadioGroup[groupid]:
            if RadioInfo["radio"] is event.widget:
                radio_x = event.widget.winfo_x()
                radio_y = event.widget.winfo_y()
                font_height = event.widget.winfo_reqheight()
                RadioInfo["icon"].place(x=radio_x - 10 ,y = radio_y+font_height//4,width=font_height, height=font_height)
def SetRadioButtonPyMeStyle(uiName,elementName,groupid,radiovalue,oval_color,over_select_color):
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global PyMeStyleRadioGroup
    Control = GetElement(uiName,elementName)
    if Control :
        parentinfo = Control.winfo_parent()
        parentwidget = Control._nametowidget(parentinfo)
        Control.bind("<Button-1>", lambda event: OnRadioButtonClick(groupid,radiovalue))
        Control.bind("<Configure>", OnRadioButtonConfigure)
        radio_x = Control.winfo_x()
        radio_y = Control.winfo_y()
        radio_bg = Control.cget(\'bg\')
        radio_height = Control.winfo_height()
        radio_req_height = Control.winfo_reqheight()
        radio_circle_size = int(radio_req_height*0.8)
        if radio_circle_size < 26:
            radio_circle_size = 26
        small_radio_icon = tkinter.Canvas(parentwidget,bg=radio_bg,highlightthickness=0,bd=0)
        image_no = Image.new(\'RGBA\', (radio_circle_size, radio_circle_size), \'#00000000\')
        draw = aggdraw.Draw(image_no)
        border_p = aggdraw.Pen(oval_color,2)
        draw.ellipse((4,4,radio_circle_size-4,radio_circle_size-4), border_p)
        draw.flush()
        tkimage_no = ImageTk.PhotoImage(image_no)
        image_yes = Image.new(\'RGBA\', (radio_circle_size, radio_circle_size), \'#00000000\')
        draw = aggdraw.Draw(image_yes)
        border_p = aggdraw.Pen(over_select_color,2)
        draw.ellipse((4,4,radio_circle_size-4,radio_circle_size-4), border_p)
        center_b = aggdraw.Brush(over_select_color)
        draw.ellipse((8,8,radio_circle_size-8,radio_circle_size-8), center_b)
        draw.flush()
        tkimage_yes = ImageTk.PhotoImage(image_yes)
        small_radio_icon.create_image(0, 0,image=tkimage_no,anchor=\'nw\',tag="icon_image")
        small_radio_icon.place(x=radio_x - (radio_circle_size)//2 + 4 ,y = radio_y + radio_height//2 - radio_circle_size//2,width=radio_circle_size, height=radio_circle_size)
        small_radio_icon.bind("<Button-1>", lambda event: OnRadioButtonClick(groupid,radiovalue))
        if groupid not in PyMeStyleRadioGroup:
            PyMeStyleRadioGroup[groupid] = []
        NewRadioInfo = {"radio":Control,"var":radiovalue,"icon":small_radio_icon,"border_color":oval_color,"image_no":image_no,"image_yes":image_yes,"tkimage_no":tkimage_no,"tkimage_yes":tkimage_yes}
        PyMeStyleRadioGroup[groupid].append(NewRadioInfo)
        currvalue = GetCurrentValue(uiName,elementName)
        OnRadioButtonClick(groupid,currvalue)
PyMeStyleCheckButton = {}
def OnCheckButtonClick(event,uiName,elementName):
    global PyMeStyleCheckButton
    print("OnCheckButtonClick")
    if uiName in PyMeStyleCheckButton.keys():
        for RadioInfo in PyMeStyleCheckButton[uiName]:
            if RadioInfo["checkbutton"] is event.widget or RadioInfo["icon"] is event.widget:
                CheckValue = GetCurrentValue(uiName,elementName)
                print("Value:"+str(CheckValue))
                if CheckValue == 0:
                    RadioInfo["icon"].itemconfig("icon_image", image=RadioInfo["tkimage_yes"])
                    if RadioInfo["icon"] is event.widget:
                        SetCurrentValue(uiName,elementName,1)
                else:
                    RadioInfo["icon"].itemconfig("icon_image", image=RadioInfo["tkimage_no"])
                    if RadioInfo["icon"] is event.widget:
                        SetCurrentValue(uiName,elementName,0)
                return
def OnCheckButtonConfigure(event):
    global PyMeStyleCheckButton
    for uiName in PyMeStyleCheckButton.keys():
        for RadioInfo in PyMeStyleCheckButton[uiName]:
            if RadioInfo["checkbutton"] is event.widget:
                radio_x = event.widget.winfo_x()
                radio_y = event.widget.winfo_y()
                font_height = event.widget.winfo_reqheight()
                RadioInfo["icon"].place(x=radio_x - 10 ,y = radio_y+font_height//4,width=font_height, height=font_height)
def SetCheckButtonPyMeStyle(uiName,elementName,checkbutton_value,oval_color,over_select_color):
    global G_UIElementAliasDictionary
    global G_UIElementDictionary
    global PyMeStyleCheckButton
    Control = GetElement(uiName,elementName)
    if Control :
        parentinfo = Control.winfo_parent()
        parentwidget = Control._nametowidget(parentinfo)
        Control.bind("<Button-1>", lambda event: OnCheckButtonClick(event,uiName,elementName))
        Control.bind("<Configure>", OnCheckButtonConfigure)
        radio_x = Control.winfo_x()
        radio_y = Control.winfo_y()
        radio_bg = Control.cget(\'bg\')
        radio_height = Control.winfo_height()
        radio_req_height = Control.winfo_reqheight()
        radio_circle_size = int(radio_req_height*0.8)
        if radio_circle_size < 26:
            radio_circle_size = 26
        small_radio_icon = tkinter.Canvas(parentwidget,bg=radio_bg,highlightthickness=0,bd=0)
        image_no = Image.new(\'RGBA\', (radio_circle_size, radio_circle_size), \'#00000000\')
        draw = aggdraw.Draw(image_no)
        border_p = aggdraw.Pen(oval_color,2)
        draw.rectangle((4,4,radio_circle_size-4,radio_circle_size-4), border_p)
        draw.flush()
        tkimage_no = ImageTk.PhotoImage(image_no)
        image_yes = Image.new(\'RGBA\', (radio_circle_size, radio_circle_size), \'#00000000\')
        draw = aggdraw.Draw(image_yes)
        border_p = aggdraw.Pen(over_select_color,2)
        draw.rectangle((4,4,radio_circle_size-4,radio_circle_size-4), border_p)
        center_b = aggdraw.Brush(over_select_color)
        draw.rectangle((8,8,radio_circle_size-8,radio_circle_size-8), center_b)
        draw.flush()
        tkimage_yes = ImageTk.PhotoImage(image_yes)
        if checkbutton_value == True:
            small_radio_icon.create_image(0, 0,image=tkimage_yes,anchor=\'nw\',tag="icon_image")
        else:
            small_radio_icon.create_image(0, 0,image=tkimage_no,anchor=\'nw\',tag="icon_image")
        small_radio_icon.place(x=radio_x - (radio_circle_size)//2 + 6 ,y = radio_y + radio_height//2 - radio_circle_size//2,width=radio_circle_size, height=radio_circle_size)
        small_radio_icon.bind("<Button-1>", lambda event: OnCheckButtonClick(event,uiName,elementName))
        if uiName not in PyMeStyleCheckButton:
            PyMeStyleCheckButton[uiName] = []
        NewCheckButtonInfo = {"checkbutton":Control,"icon":small_radio_icon,"border_color":oval_color,"image_no":image_no,"image_yes":image_yes,"tkimage_no":tkimage_no,"tkimage_yes":tkimage_yes}
        PyMeStyleCheckButton[uiName].append(NewCheckButtonInfo)
    

''' 
    f.write(code)
#写入拖动设置位置
def WriteCtrlCCopyContentFunction(f):
    code='''
def CtrlCCopy_CallBack(event):
    currIndex = event.widget.curselection()
    currIndexCount = len(currIndex)
    if currIndexCount > 0:
        import pyperclip
        if currIndexCount == 1:
            currText = event.widget.get(currIndex[0])
        else:
            currText = ""
            for i in range(currIndexCount):
                currText = currText + event.widget.get(currIndex[i]) + "\\n"
        pyperclip.copy(currText)
def KeyUpDown_CallBack(event):
    if event.keysym == "Up":
        currIndex = event.widget.curselection()
        if currIndex[0] > 0:
            event.widget.selection_clear(0, "end")
            event.widget.selection_set(currIndex[0]-1)
            event.widget.see(currIndex[0] - 1)
    elif event.keysym == "Down":
        currIndex = event.widget.curselection()
        if currIndex[0] < event.widget.size() - 1:
            event.widget.selection_clear(0, "end")
            event.widget.selection_set(currIndex[0]+1)
            event.widget.see(currIndex[0] + 1)
def EnableCtrlCCopyContent(uiName,elementName):
    """'+Language.G_Language[1722]+'"""
    Control = GetElement(uiName,elementName)
    if Control :
        Control.bind("<Control-c>",CtrlCCopy_CallBack)
        Control.bind("<Up>",KeyUpDown_CallBack)
        Control.bind("<Down>",KeyUpDown_CallBack)
''' 
    f.write(code)
#写入拖动设置位置
def WriteDragWidgetFunction(f):
    code='''
class FrameDraggable():
    """'+Language.G_Language[1723]+'"""
    def __init__(self,widget,hasChildren = True):
        if hasChildren == True:
            self.root = widget.root
            ChildWidgetList = widget.root.children
            for childKey in ChildWidgetList.keys():
                Form_1 = ChildWidgetList[childKey]
                Form_1.bind('<Button-1>',self.BeginDrag)
                Form_1.bind('<ButtonRelease-1>',self.EndDrag)
                Form_1.bind('<B1-Motion>',self.Draging)
        else:
            self.root = widget
            self.root.bind('<Button-1>',self.BeginDrag)
            self.root.bind('<ButtonRelease-1>',self.EndDrag)
            self.root.bind('<B1-Motion>',self.Draging)
    def BeginDrag(self,event):
        self.beginx = event.x_root
        self.beginy = event.y_root
    def Draging(self,event):
        offsetx = event.x_root - self.beginx 
        offsety = event.y_root - self.beginy
        oldX = self.root.winfo_x() 
        oldY = self.root.winfo_y() 
        x = oldX + offsetx
        y = oldY + offsety
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        for uiName in G_UIElementPlaceDictionary:
            for elementName in G_UIElementPlaceDictionary[uiName]:
                Control = G_UIElementDictionary[uiName][elementName]
                if Control == self.root:
                    SetControlPlace(uiName,elementName,x,y,w,h)
                    break
        self.beginx = event.x_root
        self.beginy = event.y_root
    def EndDrag(self,event):
        self.beginx = event.x_root
        self.beginy = event.y_root
class WindowDraggable():
    """'+Language.G_Language[1233]+'"""
    def __init__(self,widget,dragmove=False,bordersize = 6,bordercolor = '#444444'):
        global G_WindowDraggable
        G_WindowDraggable = self
        self.widget = widget
        if dragmove == True:
            if bordersize > 0:
                widget.bind('<Enter>',self.Enter)
                widget.bind('<Motion>',self.Motion)
                widget.bind('<Leave>',self.Leave)
    # 暂时在InitElementData中处理了
    # f.write("            widget.bind('<ButtonPress-1>',self.StartDrag)
    # f.write("            widget.bind('<ButtonRelease-1>',self.StopDrag)
    # f.write("            widget.bind('<B1-Motion>',self.MoveDragPos)
            widget.after(10, lambda: self.ShowWindowIcoToBar(widget))
        self.bordersize = bordersize
        self.bordercolor = bordercolor
        self.x = None
        self.y = None
        self.formw = self.widget.winfo_width()
        self.formh = self.widget.winfo_height()
        self.top_drag = None
        self.left_drag = None
        self.right_drag = None
        self.bottom_drag = None
        self.topleft_drag = None
        self.bottomleft_drag = None
        self.topright_drag = None
        self.bottomright_drag = None
    def GetWidget(self):
        return self.widget
    def ShowWindowIcoToBar(self,widget):
        GWL_EXSTYLE=-20
        WS_EX_APPWINDOW=0x00040000
        WS_EX_TOOLWINDOW=0x00000080
        hwnd = windll.user32.GetParent(widget.winfo_id())
        _winlib = windll.user32
        try :
            style = _winlib.GetWindowLongPtrW(hwnd, GWL_EXSTYLE)
            style = style & ~WS_EX_TOOLWINDOW
            style = style | WS_EX_APPWINDOW
            res =_winlib.SetWindowLongPtrW(hwnd, GWL_EXSTYLE, style)
        except :
            try :
                style = _winlib.GetWindowLongA(hwnd, GWL_EXSTYLE)
                style = style & ~WS_EX_TOOLWINDOW
                style = style | WS_EX_APPWINDOW
                _winlib.SetWindowLongA(hwnd, GWL_EXSTYLE, style)
            except :
                pass
    def Enter(self,event):
        if self.widget == event.widget or event.widget.winfo_class() =="Canvas":
            formx = self.widget.winfo_x() 
            formy = self.widget.winfo_y() 
    # f.write('            self.formw = self.widget.winfo_width() 
    # f.write('            self.formh = self.widget.winfo_height()
    def Motion(self,event):
        if self.widget == event.widget or event.widget.winfo_class() =="Canvas":
            formx = self.widget.winfo_x() 
            formy = self.widget.winfo_y() 
            formw = self.widget.winfo_width() 
            formh = self.widget.winfo_height()
            x = event.x_root - formx
            y = event.y_root - formy
            if ((x >= 0) and (x <= self.bordersize) and (y >= 0) and (y <= self.bordersize)):
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TL)
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_TL)
                self.top_drag.place(x = 0,y = 0,width = formw,height = self.bordersize)
                self.top_drag.configure(bg = self.bordercolor)
                self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = formh)
                self.left_drag.configure(bg = self.bordercolor)
            if ((y >= 0) and (y <= self.bordersize)):
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_V1)
                self.top_drag.bind('<Motion>',self.MotionDragBorder)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder)
                self.top_drag.place(x = 0,y = 0,width = formw,height = self.bordersize)
                self.top_drag.configure(bg = self.bordercolor)
            if ((y >= (formh - self.bordersize)) and (y <= formh)):
                if self.bottom_drag == None:
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_V2)
                self.bottom_drag.bind('<Motion>',self.MotionDragBorder)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder)
                self.bottom_drag.place(x = 0,y = (formh - self.bordersize),width = formw,height = self.bordersize)
                self.bottom_drag.configure(bg = self.bordercolor)
            if ((x >= 0 ) and (x <= self.bordersize)):
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_H1)
                self.left_drag.bind('<Motion>',self.MotionDragBorder)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder)
                self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = formh)
                self.left_drag.configure(bg = self.bordercolor)
            if ((x >= (formw - self.bordersize)) and (x <= formw)):
                if self.right_drag == None:
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_H2)
                self.right_drag.bind('<Motion>',self.MotionDragBorder)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder)
                self.right_drag.place(x = (formw - self.bordersize),y = 0,width = self.bordersize,height = formh)
                self.right_drag.configure(bg = self.bordercolor)
    def Leave(self,event):
        if self.widget == event.widget or event.widget.winfo_class() =="Canvas":
            pass
    def StartDrag(self,event):
        state = self.widget.state()
        if state == "normal":
            self.x = event.x_root
            self.y = event.y_root
            self.formw = self.widget.winfo_width()
            self.formh = self.widget.winfo_height()
    def StopDrag(self,event):
        self.x = None
        self.y = None
        self.widget.configure(cursor='arrow')
    def MoveDragPos(self,event):
        state = self.widget.state()
        if state == "normal":
            if self.widget == event.widget or event.widget.winfo_class() =="Canvas" or event.widget.winfo_class() =="Label" or event.widget.winfo_class() =="Frame"  or event.widget.winfo_class() =="Labelframe":
                formx = self.widget.winfo_x() 
                formy = self.widget.winfo_y() 
                if self.x and self.y:
                    deltaX = event.x_root - self.x
                    deltaY = event.y_root - self.y
                    newX = formx + deltaX
                    newY = formy + deltaY
                    WindowMaster = win32gui.GetParent(self.widget.winfo_id())
                    if self.widget.overrideredirect() == True:
                        win32gui.MoveWindow(WindowMaster,newX,newY,self.formw,self.formh,False)
                    else:
                        geoinfo = str('%dx%d+%d+%d'%(self.formw,self.formh,newX,newY))
                        self.widget.geometry(geoinfo)
                self.x = event.x_root
                self.y = event.y_root
                return "break"
    def MoveDragSize_H1(self,event):
        deltaX = event.x_root - self.x
        newX = self.widget.winfo_x() + deltaX
        newY = self.widget.winfo_y()
        newW = self.formw - deltaX
        WindowMaster = win32gui.GetParent(self.widget.winfo_id())
        if self.widget.overrideredirect() == True:
            win32gui.MoveWindow(WindowMaster,newX,newY,newW,self.formh,False)
        else:
            geoinfo = str('%dx%d+%d+%d'%(newW,self.formh,newX,newY))
            self.widget.geometry(geoinfo)
        self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = self.widget.winfo_height())
        self.x = event.x_root
        self.widget.configure(cursor='plus')
        self.formw = newW
    def MoveDragSize_H2(self,event):
        deltaX = event.x_root - self.x
        newX = self.widget.winfo_x()
        newY = self.widget.winfo_y()
        newW = self.formw + deltaX
        WindowMaster = win32gui.GetParent(self.widget.winfo_id())
        if self.widget.overrideredirect() == True:
            win32gui.MoveWindow(WindowMaster,newX,newY,newW,self.formh,False)
        else:
            geoinfo = str('%dx%d+%d+%d'%(newW,self.formh,newX,newY))
            self.widget.geometry(geoinfo)
        self.right_drag.place(x = newW-self.bordersize,y = 0,width = self.bordersize,height = formh)
        self.x = event.x_root
        self.widget.configure(cursor='plus')
        self.formw = newW
    def MoveDragSize_V1(self,event):
        deltaY = event.y_root - self.y
        newX = self.widget.winfo_x()
        newY = self.widget.winfo_y() + deltaY
        newH = self.formh - deltaY
        WindowMaster = win32gui.GetParent(self.widget.winfo_id())
        if self.widget.overrideredirect() == True:
            win32gui.MoveWindow(WindowMaster,newX,newY,self.formw,newH,False)
        else:
            geoinfo = str('%dx%d+%d+%d'%(self.formw,newH,newX,newY))
            self.widget.geometry(geoinfo)
        self.top_drag.place(x = 0,y = 0,width = self.formw,height = self.bordersize)
        self.y = event.y_root
        self.widget.configure(cursor='plus')
        self.formh = newH
    def MoveDragSize_V2(self,event):
        deltaY = event.y_root - self.y
        newX = self.widget.winfo_x()
        newY = self.widget.winfo_y()
        newH = self.formh + deltaY
        WindowMaster = win32gui.GetParent(self.widget.winfo_id())
        if self.widget.overrideredirect() == True:
            win32gui.MoveWindow(WindowMaster,newX,newY,self.formh,newH,False)
        else:
            geoinfo = str('%dx%d+%d+%d'%(self.formw,newH,newX,newY))
            self.widget.geometry(geoinfo)
        self.bottom_drag.place(x = 0,y = (newH - self.bordersize),width = self.formw,height = self.bordersize)
        self.y = event.y_root
        self.widget.configure(cursor='plus')
        self.formh = newH
    def MotionDragBorder(self,event):
        formx = self.widget.winfo_x() 
        formy = self.widget.winfo_y() 
        formw = self.widget.winfo_width() 
        formh = self.widget.winfo_height() 
        x = event.x_root - formx
        y = event.y_root - formy
        if event.widget == self.left_drag:
            if y >=0 and y <= self.bordersize:
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.place(x = 0,y = 0,width = formw,height = self.bordersize)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TL)
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_TL)
            if y >=(formh-self.bordersize) and y <= formh:
                if self.bottom_drag == None:
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.place(x = 0,y = formh-self.bordersize,width = formw,height = self.bordersize)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_BL)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder_BL)
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_BL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_BL)
        if event.widget == self.right_drag:
            if y >=0 and y <= self.bordersize:
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.place(x = 0,y = 0,width = formw,height = self.bordersize)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TR)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TR)
                if self.right_drag == None:
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_TR)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder_TR)
            if y >=(formh-self.bordersize) and y <= formh:
                if self.bottom_drag == None:
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.place(x = 0,y = formh-self.bordersize,width = formw,height = self.bordersize)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_BR)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder_BR)
                if self.right_drag == None:
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_BR)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder_BR)
        if event.widget == self.top_drag:
            if x >=0 and x <= self.bordersize:
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TL)
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = formh)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_TL)
            if x >=(formw-self.bordersize) and x <= formw:
                if self.top_drag == None:
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TR)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TR)
                if self.right_drag == None:
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.place(x = formw-self.bordersize,y = 0,width = self.bordersize,height = formh)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_TR)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder_TR)
        if event.widget == self.bottom_drag:
            if x >=0 and x <= self.bordersize:
                if self.bottom_drag == None:
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_BL)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder_BL)
                if self.left_drag == None:
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = formh)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_BL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_BL)
            if x >=(formw-self.bordersize) and x <= formw:
                if self.bottom_drag == None:
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_BR)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder_BR)  
                if self.right_drag == None:
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.place(x = formw-self.bordersize,y = 0,width = self.bordersize,height = formh)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_BR)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder_BR)
    def LeaveDragBorder(self,event):
        event.widget.place_forget()
    def MoveDragSize_TL(self,event):
        deltaX = event.x_root - self.x
        deltaY = event.y_root - self.y
        newX = self.widget.winfo_x() + deltaX
        newY = self.widget.winfo_y() + deltaY
        newW = self.formw - deltaX
        newH = self.formh - deltaY
        WindowMaster = win32gui.GetParent(self.widget.winfo_id())
        if self.widget.overrideredirect() == True:
            win32gui.MoveWindow(WindowMaster,newX,newY,newW,newH,False)
        else:
            geoinfo = str('%dx%d+%d+%d'%(newW,newH,newX,newY))
            self.widget.geometry(geoinfo)
        self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = self.newH)
        self.top_drag.place(x = 0,y = 0,width = newW,height = self.bordersize)
        self.x = event.x_root
        self.y = event.y_root
        self.widget.configure(cursor='plus')
        self.formw = newW
        self.formh = newH
    def LeaveDragBorder_TL(self,event):
        self.left_drag.place_forget()
        self.top_drag.place_forget()
        self.widget.configure(cursor='arrow')
    def MoveDragSize_TR(self,event):
        deltaX = event.x_root - self.x
        deltaY = event.y_root - self.y
        newX = self.widget.winfo_x()
        newY = self.widget.winfo_y() + deltaY
        newW = self.widget.winfo_width() + deltaX
        newH = self.widget.winfo_height() - deltaY
        WindowMaster = win32gui.GetParent(self.widget.winfo_id())
        if self.widget.overrideredirect() == True:
            win32gui.MoveWindow(WindowMaster,newX,newY,newW,newH,False)
        else:
            geoinfo = str('%dx%d+%d+%d'%(newW,newH,newX,newY))
            self.widget.geometry(geoinfo)
        self.right_drag.place(x = newW-self.bordersize,y = 0,width = self.bordersize,height = newH)
        self.top_drag.place(x = 0,y = 0,width = newW,height = self.bordersize)
        self.x = event.x_root
        self.y = event.y_root
        self.widget.configure(cursor='plus')
        self.formw = newW
        self.formh = newH
    def LeaveDragBorder_TR(self,event):
        self.right_drag.place_forget()
        self.top_drag.place_forget()
        self.widget.configure(cursor='arrow')
    def MoveDragSize_BL(self,event):
        deltaX = event.x_root - self.x
        deltaY = event.y_root - self.y
        newX = self.widget.winfo_x() + deltaX
        newY = self.widget.winfo_y()
        newW = self.widget.winfo_width() - deltaX
        newH = self.widget.winfo_height() + deltaY
        WindowMaster = win32gui.GetParent(self.widget.winfo_id())
        if self.widget.overrideredirect() == True:
            win32gui.MoveWindow(WindowMaster,newX,newY,newW,newH,False)
        else:
            geoinfo = str('%dx%d+%d+%d'%(newW,newH,newX,newY))
            self.widget.geometry(geoinfo)
        self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = newH)
        self.bottom_drag.place(x = 0,y = newH-self.bordersize,width = newW,height = self.bordersize)
        self.x = event.x_root
        self.y = event.y_root
        self.widget.configure(cursor='plus')
        self.formw = newW
        self.formh = newH
    def LeaveDragBorder_BL(self,event):
        self.left_drag.place_forget()
        self.bottom_drag.place_forget()
        self.widget.configure(cursor='arrow')
    def MoveDragSize_BR(self,event):
        deltaX = event.x_root - self.x
        deltaY = event.y_root - self.y
        newX = self.widget.winfo_x()
        newY = self.widget.winfo_y()
        newW = self.widget.winfo_width() + deltaX
        newH = self.widget.winfo_height() + deltaY
        WindowMaster = win32gui.GetParent(self.widget.winfo_id())
        if self.widget.overrideredirect() == True:
            win32gui.MoveWindow(WindowMaster,newX,newY,newW,newH,False)
        else:
            geoinfo = str('%dx%d+%d+%d'%(newW,newH,newX,newY))
            self.widget.geometry(geoinfo)
        self.right_drag.place(x = newW-self.bordersize,y = 0,width = self.bordersize,height = newH)
        self.bottom_drag.place(x = 0,y = newH-self.bordersize,width = newW,height = self.bordersize)
        self.x = event.x_root
        self.y = event.y_root
        self.widget.configure(cursor='plus')
        self.formw = newW
        self.formh = newH
    def LeaveDragBorder_BR(self,event):
        self.right_drag.place_forget()
        self.bottom_drag.place_forget() 
        self.widget.configure(cursor='arrow')


''' 
    f.write(code)
#提示文字函数
def WriteTipTextFunction(f):
    code='''
ToolTipClick_X = 0
ToolTipClick_Y = 0
#提示类
class ToolTip(object):
    def __init__(self, widget,bgColor = '#CCCCCC',fgColor='#000000'):
        self.widget = widget
        self.tipwindow = None
        self.bgColor = bgColor
        self.fgColor = fgColor
        self.id = None
        self.x = 0
        self.y = 0
        self.font = tkinter.font.Font(family=\"Arial\", size=12,weight='normal',slant='roman',underline=0,overstrike=0)
    #显示提示
    def showtip(self, text ,x ,y):
        global ToolTipClick_X
        global ToolTipClick_Y
        if self.tipwindow or not text:
            return
        if ToolTipClick_X == x  and ToolTipClick_Y == y:
            return 
        self.tipwindow = tkinter.Toplevel(self.widget)
        self.tipwindow.wm_overrideredirect(1)
        self.tipwindow.wm_attributes("-topmost", 1)
        maxwidth = 0
        maxheight = 24
        #label = tkinter.Label(self.tipwindow, text=self.text, justify=tkinter.LEFT,background=g_Scheme_FG2,fg=g_Scheme_BG2, relief=tkinter.SOLID, borderwidth=2,font=("Roman", "12", "normal"))
        if type(text) == type([]):
            self.text = ""
            TextLineArray = text
            for TextLine in TextLineArray:
                maxwidth = max(int(self.font.measure(TextLine)),maxwidth)
                self.text = self.text + TextLine 
                maxheight = maxheight + 24
        else: 
            self.text = text
            maxwidth = max(int(self.font.measure(text)),maxwidth)
        maxwidth = maxwidth + 24
        geoinfo = str('%dx%d+%d+%d'%(maxwidth,maxheight,x-int(maxwidth/2), y-30))
        self.tipwindow.wm_geometry(geoinfo)
        if type(text) == type([]):
            self.Text = tkinter.Text(self.tipwindow, width=maxwidth,background=self.bgColor,fg=self.fgColor, relief=tkinter.SOLID, borderwidth=2,font=self.font)
            self.Text.pack(ipadx=1)
            self.Text.bind('<Button-1>',self.clicktip)
            TextLineArray = text
            for TextLine in TextLineArray:
                self.Text.insert(tkinter.END,TextLine,'tag0')    
        else: 
            maxwidth = max(self.font.measure(text),maxwidth)
            self.label = tkinter.Message(self.tipwindow, text=self.text, anchor=tkinter.W,width=maxwidth,background=self.bgColor,fg=self.fgColor, relief=tkinter.SOLID, borderwidth=2,font=self.font)
            self.label.pack(ipadx=1)
            self.label.bind('<Button-1>',self.clicktip)
    #点击隐藏提示
    def clicktip(self,event):
        global ToolTipClick_X
        global ToolTipClick_Y
        ToolTipClick_X = event.x
        ToolTipClick_Y = event.y
        self.hidetip()
    #隐藏提示
    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
#创建提示
def CreateToolTip(uiName,elementName,tipText,bgColor = '#CCCCCC',fgColor='#000000'):
    Control = GetElement(uiName,elementName)
    if Control is None:
        return
    if hasattr(Control,"GetEntry") == True:
        Control = Control.GetEntry()
    elif hasattr(Control,"GetWidget") == True:
        Control = Control.GetWidget()
    toolTip = ToolTip(Control,bgColor,fgColor)
    def enter(event):
        toolTip.showtip(tipText,event.x_root,event.y_root)
    def leave(event):
        toolTip.hidetip()
    def click(event):
        toolTip.hidetip()
    Control.bind('<Enter>', enter,add=True)
    Control.bind('<Leave>', leave,add=True)
    #f.write("    Control.bind('<Button-1>',click)

''' 
    f.write(code)
#动作函数
def WriteWidgetActionFunction(f):
    code='''
def PlayAction_MoveTo(uiName,elementName,targetX,targetY,duration = 1.0,fps = 50):
    """'+Language.G_Language[6576]+'"""
    Control = GetElement(uiName,elementName)
    if Control is None:
        return
    InitTime = time.time()
    InitX = Control.winfo_x()
    InitY = Control.winfo_y()
    InitW = Control.winfo_width()
    InitH = Control.winfo_height()
    Delay = int(1000 / fps)
    def MovingLoop():
        CurrTime = time.time() - InitTime
        Progress = CurrTime / duration 
        if Progress > 1.0:
            CurrX = targetX
            CurrY = targetY
            Control.place(x=int(CurrX),y=int(CurrY),width=InitW,height=InitH)
        else:
            CurrX = InitX + (targetX - InitX) * Progress 
            CurrY = InitY + (targetY - InitY) * Progress 
            Control.place(x=int(CurrX),y=int(CurrY),width=InitW,height=InitH)
            Control.after(Delay,MovingLoop)
    Control.after(Delay,MovingLoop)
def PlayAction_MoveBy(uiName,elementName,moveX=0,moveY=0,duration = 1.0,fps = 50):
    """'+Language.G_Language[6577]+'"""
    Control = GetElement(uiName,elementName)
    if Control is None:
        return
    InitTime = time.time()
    InitX = Control.winfo_x()
    InitY = Control.winfo_y()
    InitW = Control.winfo_width()
    InitH = Control.winfo_height()
    targetX = InitX + moveX
    targetY = InitY + moveY
    Delay = int(1000 / fps)
    def MovingLoop():
        CurrTime = time.time() - InitTime
        Progress = CurrTime / duration 
        if Progress > 1.0:
            CurrX = targetX
            CurrY = targetY
            Control.place(x=int(CurrX),y=int(CurrY),width=InitW,height=InitH)
        else:
            CurrX = InitX + (targetX - InitX) * Progress 
            CurrY = InitY + (targetY - InitY) * Progress 
            Control.place(x=int(CurrX),y=int(CurrY),width=InitW,height=InitH)
            Control.after(Delay,MovingLoop)
    Control.after(Delay,MovingLoop)
def PlayAction_ScaleTo(uiName,elementName,anchor = "center",scaleW=1.0,scaleH=1.0,duration = 1.0,fps = 50):
    """'+Language.G_Language[6578]+'"""
    Control = GetElement(uiName,elementName)
    if Control is None:
        return
    InitTime = time.time()
    InitX = Control.winfo_x()
    InitY = Control.winfo_y()
    InitW = Control.winfo_width()
    InitH = Control.winfo_height()
    CenterX = InitX + InitW * 0.5
    CenterY = InitY + InitH * 0.5
    targetW = InitW * scaleW
    targetH = InitH * scaleH
    if anchor == "nw":
        targetX = InitX
        targetY = InitY
    elif anchor == "n":
        targetX = int(CenterX-targetW * 0.5)
        targetY = InitY
    elif anchor == "ne":
        targetX = InitX + InitW - targetW
        targetY = InitY
    elif anchor == "w":
        targetX = InitX
        targetY = int(CenterY-targetH * 0.5)
    elif anchor == "e":
        targetX = InitX + InitW - targetW
        targetY = int(CenterY-targetH * 0.5)
    elif anchor == "sw":
        targetX = InitX
        targetY = InitY + InitH - targetH
    elif anchor == "s":
        targetX = int(CenterX-targetW * 0.5)
        targetY = InitY + InitH - targetH
    elif anchor == "se":
        targetX = InitX + InitW - targetW
        targetY = InitY + InitH - targetH
    else:
        targetX = int(CenterX - targetW*0.5)
        targetY = int(CenterY - targetH*0.5)
    Delay = int(1000 / fps)
    def ScalingLoop():
        CurrTime = time.time() - InitTime
        Progress = CurrTime / duration 
        if Progress > 1.0:
            Control.place(x=targetX,y=targetY,width=targetW,height=targetH)
        else:
            CurrX = InitX + (targetX - InitX) * Progress 
            CurrY = InitY + (targetY - InitY) * Progress 
            CurrW = InitW + (targetW - InitW) * Progress 
            CurrH = InitH + (targetH - InitH) * Progress 
            Control.place(x=int(CurrX),y=int(CurrY),width=CurrW,height=CurrH)
            Control.after(Delay,ScalingLoop)
    Control.after(Delay,ScalingLoop)
    # f.write('def PlayAction_FadeIn(uiName,duration = 1.0,fps = 50):
    # f.write('    """'+Language.G_Language[6586]+'"""
    # f.write('def PlayAction_FadeOut(uiName,duration = 1.0,fps = 50):  
    # f.write('    """'+Language.G_Language[6587]+'"""
    # f.write('def PlayAction_Popup(uiName,duration = 1.0,fps = 50):
    # f.write('    """'+Language.G_Language[6586]+'"""
    # f.write('def PlayAction_Shrink(uiName,duration = 1.0,fps = 50):  
    # f.write('    """'+Language.G_Language[6587]+'"""


''' 
    f.write(code)
#写入圆角设置位置
def WriteSetRootRoundRectangleFunction(f):
    code='''
    #f.write(Language.G_Language[1227]+'
def SetRootRoundRectangle(canvas,hastitlebar,x1, y1, x2, y2, radius=25,**kwargs):
    """'+Language.G_Language[1227]+'"""
    rootinfo = canvas.winfo_parent()
    root = canvas._nametowidget(rootinfo)
    DwmApi = ctypes.windll.dwmapi
    DwmSetWindowAttribute = DwmApi.DwmSetWindowAttribute
    WindowMaster = win32gui.GetParent(root.winfo_id())
    RoundValue = ctypes.c_int(4)
    DwmSetWindowAttribute(WindowMaster,33,ctypes.byref(RoundValue),ctypes.sizeof(RoundValue))

    # f.write('    canvas.create_rectangle(x1, y1, x2, y2, fill=kwargs[\'outline\'])
    # f.write('    if hastitlebar == True:
    # f.write('        points = [x1, y1,
    # f.write('              x1, y1,
    # f.write('              x2, y1,
    # f.write('              x2, y1,
    # f.write('              x2, y1,
    # f.write('              x2, y1,
    # f.write('              x2, y1,
    # f.write('              x2, y2-radius,
    # f.write('              x2, y2-radius,
    # f.write('              x2, y2,
    # f.write('              x2-radius, y2,
    # f.write('              x2-radius, y2,
    # f.write('              x1+radius, y2,
    # f.write('              x1+radius, y2,
    # f.write('              x1, y2,
    # f.write('              x1, y2-radius,
    # f.write('              x1, y2-radius,
    # f.write('              x1, y1,
    # f.write('              x1, y1,
    # f.write('              x1, y1]
    # f.write('    else:
    # f.write('        points = [x1+radius, y1,
    # f.write('              x1+radius, y1,
    # f.write('              x2-radius, y1,
    # f.write('              x2-radius, y1,
    # f.write('              x2, y1,
    # f.write('              x2, y1+radius,
    # f.write('              x2, y1+radius,
    # f.write('              x2, y2-radius,
    # f.write('              x2, y2-radius,
    # f.write('              x2, y2,
    # f.write('              x2-radius, y2,
    # f.write('              x2-radius, y2,
    # f.write('              x1+radius, y2,
    # f.write('              x1+radius, y2,
    # f.write('              x1, y2,
    # f.write('              x1, y2-radius,
    # f.write('              x1, y2-radius,
    # f.write('              x1, y1+radius,
    # f.write('              x1, y1+radius,
    # f.write('              x1, y1]
    # f.write('    return canvas.create_polygon(points, smooth=True, **kwargs)

''' 
    f.write(code)
#打开目录
def SelectDirectoryFunction(f):
    code='''
   f.write('def SelectDirectory(title="'+Language.G_Language[167]+'",initDir = os.path.abspath(\'.\'),parent=None):
   f.write('    """'+Language.G_Language[1557]+'"""
   f.write('    """'+Language.G_Language[9022]+'"""
   f.write('    global G_TopDialog
   f.write('    if G_TopDialog:
   f.write('        parent = G_TopDialog
   f.write('    import tkinter.filedialog
   f.write('    openPath = tkinter.filedialog.askdirectory(title=title,initialdir=initDir,parent=parent)
   f.write('    return openPath

''' 
    f.write(code)
#打开目录
def SelectColorFunction(f):
    code='''
   f.write('def SelectColor(title="'+Language.G_Language[456]+'"):
   f.write('    """'+Language.G_Language[1558]+'"""
   f.write('    import tkinter.colorchooser
   f.write('    color = tkinter.colorchooser.askcolor(title=title)
   f.write('    return color
''' 
    f.write(code)
#罗列系统所有字体
def WriteEnumFontNameFunction(f):
    code='''
   f.write('def EnumFontName():
   f.write('    """'+Language.G_Language[1960]+'"""
   f.write('    import tkinter.font
   f.write('    return tkinter.font.families()
''' 
    f.write(code)
#罗列系统所有字体
def WriteEnumFontNameFunction_App(f):
    code='''
   f.write('def EnumFontName():
   f.write('    """'+Language.G_Language[1960]+'"""
   f.write('    import pygame.font
   f.write("    return pygame.font.get_fonts()
''' 
    f.write(code)
#罗列系统所有字体
def WriteSetCursorFunction_App(f):
    code='''
def SetCursor(uiName,elementName,cursor='hand2'):
    """'+Language.G_Language[1490]+'"""
    pass
def HideCursor(uiName):
    """'+Language.G_Language[1491]+'"""
    pass
def GetCursorPosition(uiName=\'\',elementName=\'root\'):
    """'+Language.G_Language[9805]+'"""
    pass
''' 
    f.write(code)
#写入读取样式表数据
def WriteReadWriteFileFunction(f):
    code='''
   #f.write(Language.G_Language[1228]+'
   f.write("def ReadFromFile(filePath,encoding='utf-8',autoEval=False):
   f.write('    """'+Language.G_Language[1228]+'"""
   f.write('    content = None
   f.write('    if filePath != None:
   f.write("        if os.path.exists(filePath) == True: 
   f.write("            f = open(filePath,mode='r',encoding=encoding)
   f.write('            if f != None:
   f.write('                content = f.read()
   f.write('                if autoEval == True:
   f.write('                    content = eval(content)
   f.write('                f.close()
   f.write('    return content
   f.write('def OpenFile(title="Open Python File",filetypes=[(\'Python File\',\'*.py\'),(\'All files\',\'*\')],initDir = \'\'):
   f.write('    """'+Language.G_Language[187]+'"""
   f.write('    import tkinter.filedialog
   f.write('    import inspect
   f.write('    parent = None
   f.write('    calling_frame = inspect.currentframe().f_back
   f.write('    if "uiName" in calling_frame.f_locals:
   f.write('        uiName = calling_frame.f_locals["uiName"]
   f.write('        parent = GetElement(uiName,"Form_1")
   f.write('    openPath = tkinter.filedialog.askopenfilename(initialdir=initDir,title=title,filetypes=filetypes,parent=parent)
   f.write('    return openPath

   #f.write(Language.G_Language[1229]+'
   f.write("def WriteToFile(filePath,content,encoding='utf-8',append=False):
   f.write('    """'+Language.G_Language[1229]+'"""
   f.write('    if filePath != None:
   f.write('        f = None
   f.write('        if append == True:
   f.write("            f = open(filePath,mode='a',encoding=encoding)
   f.write('        else:
   f.write("            f = open(filePath,mode='w',encoding=encoding)
   f.write('        if f != None:
   f.write('            if content != None:
   f.write('                f.write(str(content))
   f.write('            f.close()
   f.write('            return True
   f.write('    return False
   f.write('def SaveFile(title="Save Python File",filetypes=[(\'Python File\',\'*.py\'),(\'All files\',\'*\')],initDir = \'\',defaultextension=\'py\'):
   f.write('    """'+Language.G_Language[188]+'"""
   f.write('    import tkinter.filedialog
   f.write('    import inspect
   f.write('    parent = None
   f.write('    calling_frame = inspect.currentframe().f_back
   f.write('    if "uiName" in calling_frame.f_locals:
   f.write('        uiName = calling_frame.f_locals["uiName"]
   f.write('        parent = GetElement(uiName,"Form_1")
   f.write('    savePath = tkinter.filedialog.asksaveasfilename(initialdir=initDir,title=title,filetypes=filetypes,defaultextension=defaultextension,parent=parent)
   f.write('    return savePath
''' 
    f.write(code)
#写入读取样式表数据
def WriteReadWriteFileFunction_Moblie(f):
    code='''
   #f.write(Language.G_Language[1228]+'
   f.write("def ReadFromFile(filePath,encoding='utf-8',autoEval=False):
   f.write('    """'+Language.G_Language[1228]+'"""
   f.write('    content = None
   f.write('    if filePath != None:
   f.write("        if os.path.exists(filePath) == True: 
   f.write("            f = open(filePath,mode='r',encoding=encoding)
   f.write('            if f != None:
   f.write('                content = f.read()
   f.write('                if autoEval == True:
   f.write('                    content = eval(content)
   f.write('                f.close()
   f.write('    return content
   #f.write(Language.G_Language[1229]+'
   f.write("def WriteToFile(filePath,content,encoding='utf-8'):
   f.write('    """'+Language.G_Language[1229]+'"""
   f.write('    if filePath != None:
   f.write("        f = open(filePath,mode='w',encoding=encoding)
   f.write('        if f != None:
   f.write('            if content != None:
   f.write('                f.write(str(content))
   f.write('            f.close()
   f.write('            return True
   f.write('    return False
''' 
    f.write(code)
#写入读取样式表数据
def WriteNativeCallBackFunction_Mobile(f):
    code='''
   f.write('NativeCallBackDataList = {}
   f.write('def NativeCallBack(eventName,eventdata):
   f.write('    global NativeCallBackDataList
   f.write('    NativeCallBackDataList[eventName] = eventdata
   f.write('def OpenFile(title="Open Python File",filetypes=[(\'Python File\',\'*.py\'),(\'All files\',\'*\')],initDir = os.path.abspath(\'.\')):
   f.write('    """'+Language.G_Language[187]+'"""
   f.write('    global NativeCallBackDataList
   f.write('    NativeCallBackDataList["openPhoto"]=None
   f.write('    GameLib.gameAppInstance.GetCurrentScene().SetNativeCallBackFunction(NativeCallBack)
   f.write('    GameLib.gameAppInstance.GetCurrentScene().CallNativeEvent("openPhoto")
   f.write('    while NativeCallBackDataList["openPhoto"] is None:
   f.write('        time.sleep(100)
   f.write('    openPath = NativeCallBackDataList["openPhoto"]
   f.write('    NativeCallBackDataList["openPhoto"]=None
   f.write('    return openPath
   f.write('def QuitApplication():
   f.write('    GameLib.gameAppInstance.GetCurrentScene().CallNativeEvent("quit")
'''
    f.write(code)
#写入读取样式表数据
def WriteReadStyleFileFunction(f,exportMode=False,StyleArray=None):

    #f.write(Language.G_Language[1230]+'
    if exportMode == True and StyleArray != None:
        code='''
def ReadStyleFile(filePath):
    """'+Language.G_Language[1230]+'"""
    StyleArray = {}
'''
        f.write(code)
        for keyName in StyleArray.keys():
            f.write("    StyleArray['"+keyName+"'] = "+str(StyleArray[keyName])+"\n")
            f.write("    if 'font_family' in StyleArray['"+keyName+"'] and 'font_size' in StyleArray['"+keyName+"']  and 'font_weight' in StyleArray['"+keyName+"'] :\n")
            f.write("        StyleArray['"+keyName+"']['font'] = tkinter.font.Font(family=StyleArray['"+keyName+"']['font_family'], size=int(StyleArray['"+keyName+"']['font_size']),weight=StyleArray['"+keyName+"']['font_weight'])\n")
        f.write("    return StyleArray \n")
    else:
        code='''
def ReadStyleFile(filePath):
    """'+Language.G_Language[1230]+'"""
    global G_ExeDir
    StyleArray = {}
    if len(filePath)==0 :
        return StyleArray
    if os.path.exists(filePath) == False:
        PathName, FileName = os.path.split(filePath)
        filePath = os.path.join(G_ExeDir,FileName)
        if os.path.exists(filePath) == False:
            return StyleArray
    f = open(filePath,encoding='utf-8')
    line =""
    while True:
        line = f.readline()
        if not line:
            break
        text = line.strip()
        if not text:
            continue
        if text.find('style = tkinter.ttk.Style()') >= 0:
            continue
        if text.find('style.configure(') >= 0:
            splitarray1 = text.partition('style.configure(')
            stylename = None
            splitarray2 = None
            if splitarray1[2].find(',') >= 0:
                splitarray2 = splitarray1[2].partition(',')
                stylename = splitarray2[0].replace('\"','')
            else:
                splitarray2 = splitarray1[2].partition(')')
                stylename = splitarray2[0].replace('\"','')
            sytleValueText = splitarray2[2]
            fontindex_begin = sytleValueText.find('font=(')
            fontindex_end = fontindex_begin
            StyleArray[stylename] = {}
            othertext = sytleValueText
            if fontindex_begin >= 0:
                fontindex_end = sytleValueText.find(')')
                fonttext = sytleValueText[fontindex_begin+6:fontindex_end]
                fontsplitarray = fonttext.split(',')
                StyleArray[stylename]['font'] = tkinter.font.Font(family=fontsplitarray[0].replace('\"','').strip(), size=int(fontsplitarray[1].replace('\"','').strip()),weight=fontsplitarray[2].replace('\"','').strip())
                othertext = sytleValueText[0:fontindex_begin] + sytleValueText[fontindex_end+1:-1]
            else:
                splitarray4 = sytleValueText.partition(')')
                othertext = splitarray4[0]
            splitarray3 = othertext.split(',')
            for stylecfgtext in splitarray3:
                if stylecfgtext.find('=') > 0:
                    splitarray4 = stylecfgtext.partition('=')
                    key = splitarray4[0].replace('\"','').strip()
                    value = splitarray4[2].replace('\"','').strip()
                    StyleArray[stylename][key] = value
            continue
        if text.find('style.map(') >= 0:
            continue
    f.close()
    return StyleArray 

''' 
        f.write(code)
#数据源处理
def WriteDataBaseClass(f):
    code='''
    #f.write('#Data DataBase Class
class DataBase:
    """'+Language.G_Language[1781]+'"""
    def __init__(self):
        self.SourceData = None
        self.SourceType = None
        self.Filename = None
        self.SheetName = None
        self.PageIndex = 0
        self.RecordCount = 0
        self.PageCount = 0
        self.RPP = 10
        self.Connect = None
        self.Cursor = None
        self.SQLiteTableColNameList = []
    def __del__(self):
        if self.Cursor:
             self.Cursor.close()
        if self.Connect:
             self.Connect.close()
    def OpenSQLITE(self,filename=None):
        """'+Language.G_Language[2619]+'"""
        Connect = None
        ConnectText = filename
        if filename == None or filename == '':
            ConnectText = ":memory:"
        try:
            import sqlite3
            Connect = sqlite3.connect(ConnectText)
            self.Connect = Connect
            self.Cursor = self.Connect.cursor()
            self.SourceType = 'SQLite'
            return True
        except sqlite3.Error:
            self.SourceData = None
        return False
    def OpenMYSQL(self,ip,port,user,password,database):
        """'+Language.G_Language[2619]+'"""
        try:
            import pymysql
            Connect = pymysql.connect(host=ip,port=int(port),user=user,password=password,database=database,charset='utf8',connect_timeout=3)
            self.Connect = Connect
            self.Cursor = self.Connect.cursor()
            self.SourceType = 'MySql'
            return True
        except Exception as Ex:
            print(Ex)
            self.SourceData = None
        return False
    def OpenSQLSERVER(self,ip,port,user,password,database):
        """'+Language.G_Language[2619]+'"""
        try:
            import pymssql
            Connect = pymssql.connect(host=ip,port=int(port),user=user,password=password,database=database,charset='utf8',timeout=3)
            self.SourceType = 'SQLServer'
            self.Connect = Connect
            self.Cursor = self.Connect.cursor()
            return True
        except Exception as Ex:
            print(Ex)
            self.SourceData = None
        return False
    # f.write('    def ListDataBase(self):
    # f.write('        """'+Language.G_Language[3460]+'"""
    # f.write('        if self.SourceType:n')
    # f.write('            try:
    # f.write('                if self.SourceType == "SQLite":
    # f.write('                    self.Cursor.execute(\'show databases\')
    # f.write('                if self.SourceType == "MYSQL":
    # f.write('                    self.Cursor.execute(\'show databases\')
    # f.write('                if self.SourceType == "SQLSERVER"
    # f.write('                    self.Cursor.execute(\'select Name from master.dbo.sysdatabases\')
    # f.write('                database_array = []
    # f.write('                for database_name in self.Cursor.fetchall():
    # f.write('                    database_array.append(database_name[0])
    # f.write('                return database_array
    # f.write('            except Exception as Ex:
    # f.write('                print(Ex)
    # f.write('        return False
    def ListTables(self):
        """'+Language.G_Language[3461]+'"""
        if self.SourceType:
            try:
                if self.SourceType == "SQLite":
                    self.Cursor.execute("select * from sqlite_master where type=\'table\'")
                    table_array = []
                    for table_name in self.Cursor.fetchall():
                        table_array.append(table_name[0])
                    return table_array
                if self.SourceType == "MYSQL":
                    self.Cursor.execute(\'show tables\')
                    table_array = []
                    for table_name in self.Cursor.fetchall():
                        table_array.append(table_name[0])
                    return table_array
                if self.SourceType == "SQLSERVER":
                    self.Cursor.execute("select name from sysobjects where xType=\'U\'")
                    table_array = []
                    for table_name in self.Cursor.fetchall():
                        table_array.append(table_name[0])
                    return table_array
            except Exception as Ex:
                print(Ex)
        return False
    def CreateTable(self,tablename,fieldlist=[]):
        """'+Language.G_Language[2611]+'"""
        if self.Connect and tablename:
            try:
                CreateCMDText = "CREATE TABLE IF NOT EXISTS "+tablename+"("
                FieldCount = len(fieldlist)
                FieldIndex = 0
                for field in fieldlist:
                    CreateCMDText = CreateCMDText + field 
                    if FieldIndex < (FieldCount-1):
                        CreateCMDText = CreateCMDText + ","
                    FieldIndex = FieldIndex + 1
                CreateCMDText = CreateCMDText + ")"
                self.Cursor.execute(CreateCMDText)
                self.Connect.commit()
                return True
            except Exception as Ex:
                print(Ex)
        return False
    def SQLQuery(self,sqlString=None,params=None):    
        """'+Language.G_Language[2617]+'"""
        if self.Connect is not None and sqlString is not None:
            try:
                ResultArray = []
                if params:
                    self.Cursor.execute(sqlString,params)
                else:
                    self.Cursor.execute(sqlString)
                for row in self.Cursor.fetchall():
                    ResultArray.append(row)
                return ResultArray
            except Exception as Ex:
                print(Ex)
                self.SourceData = None
        return []
    def SQLCMD(self,sqlString=None,params=None):    
        """'+Language.G_Language[2618]+'"""
        if self.Connect is not None and sqlString is not None:
            try:
                if params:
                    self.Cursor.execute(sqlString,params)
                else:
                    self.Cursor.execute(sqlString)
                self.Connect.commit()
                return True
            except Exception as Ex:
                print(Ex)
        return False
    def CallProc(self,procName:"str",inParams:list = [],outParams:list = []):
        """'+Language.G_Language[2635]+'"""
        if self.Connect is not None and procName is not None:
            try:
                inParamsLength = 0
                params_list = []
                if inParams:
                    params_list = params_list + inParams
                    inParamsLength = len(inParams)
                if outParams:
                    params_list = params_list + outParams
                self.Cursor.callproc(procName,params_list)
                resParams = []
                if outParams:
                    out_parm_string = "select "
                    for x in range(len(outParams)):
                        out_parm_string = "{pre} @_{p}_{i},".format(pre=out_parm_string, p=procName, i=inParamsLength)
                        inParamsLength += 1
                    self.Connect.execute(out_parm_string[:-1])
                    resParams = list(self.Connect.fetchall()[0])
                return True,resParams
            except Exception as Ex:
                print(Ex)
        return False,[]
    def DropTable(self,tablename):
        """'+Language.G_Language[2612]+'"""
        if tablename is not None and self.Connect is not None:
            sqlString = "drop table " + tablename
            try:
                self.Cursor.execute(sqlString)
                self.Connect.commit()
                return True
            except Exception as Ex:
                print(Ex)
                self.SourceData = None
        return False
    def CalculatePages(self,recordcount,recordcountprepage):
        """'+Language.G_Language[1977]+'"""
        self.RecordCount = recordcount
        self.RPP = recordcountprepage
        self.PageCount = int(recordcount/self.RPP)
        if self.RecordCount > self.RPP*self.PageCount:
            self.PageCount = self.PageCount + 1
        self.PageIndex = 0
    def GetRecordCount(self):
        """'+Language.G_Language[1979]+'"""
        return self.RecordCount
    def GetPageCount(self):
        """'+Language.G_Language[1978]+'"""
        return self.PageCount
    def GetPageIndex(self):
        """'+Language.G_Language[1975]+'"""
        return self.PageIndex
    def SetPageIndex(self,pageindex):
        """'+Language.G_Language[1976]+'"""
        self.PageIndex = pageindex
    def GetBeginRecordIndex(self):
        """'+Language.G_Language[1980]+'"""
        return self.PageIndex*self.RPP
    def GetEndRecordIndex(self):
        """'+Language.G_Language[1981]+'"""
        EndRecordIndex = self.PageIndex*self.RPP + self.RPP
        if EndRecordIndex >= self.RecordCount:
            EndRecordIndex = self.RecordCount
        return EndRecordIndex-1
def LoadDynamicColumn(uiName,listViewName):   
    """'+Language.G_Language[1988]+'"""
    ListView_4 = GetElement(uiName,listViewName)   
    ColumnNameList = copy.deepcopy(ListView_4.cget('columns'))   
    NewColumnList = []   
    NewColumnNameList = []   
    for ColumnName in ColumnNameList:   
        ColumnAnchor = ListView_4.column(ColumnName,"anchor")  
        ColumnWidth = ListView_4.column(ColumnName,"width")  
        if ColumnName.find('>>') >= 0:  
            ColumnSplitArray = ColumnName.split('>>')  
            if len(ColumnSplitArray) == 3:  
                DataBaseName = ColumnSplitArray[0]  
                TableName = ColumnSplitArray[1]  
                FieldName = ColumnSplitArray[2]  
                DataBase = GetElement(uiName,DataBaseName)  
                RecordsetList = DataBase.SQLQuery("select "+FieldName+" from "+TableName)  
                for Recordset in RecordsetList:  
                    NewColumnList.append([Recordset[0],ColumnAnchor,ColumnWidth])  
                    NewColumnNameList.append(Recordset[0])  
            if len(ColumnSplitArray) == 4:  
                DataBaseName = ColumnSplitArray[0]  
                TableName = ColumnSplitArray[1]  
                FieldName = ColumnSplitArray[2]  
                WhereText = ColumnSplitArray[3]  
                DataBase = GetElement(uiName,DataBaseName)  
                RecordsetList = DataBase.SQLQuery("select "+FieldName+" from "+TableName+" where "+WhereText)  
                for Recordset in RecordsetList:  
                    NewColumnList.append([Recordset[0],ColumnAnchor,ColumnWidth])  
                    NewColumnNameList.append(Recordset[0]) 
        else:  
            NewColumnList.append([ColumnName,ColumnAnchor,ColumnWidth])  
            NewColumnNameList.append(ColumnName)  
    ListView_4.configure(columns = NewColumnNameList)  
    for ColumnInfo in NewColumnList:   
        ListView_4.column(ColumnInfo[0],anchor=ColumnInfo[1],width=ColumnInfo[2])  
        ListView_4.heading(ColumnInfo[0],anchor=ColumnInfo[1],text=ColumnInfo[0])  

''' 
    f.write(code)
#数据表
def WriteDataTableClass(f):
    code='''
    #f.write('#Data Table Class
class DataTable:
    """'+Language.G_Language[1782]+'"""
    def __init__(self):
        self.TableData = None
        self.TableType = None
        self.Filename = None
        self.SheetName = None
        self.host = None
        self.port = None
        self.username = None
        self.password = None
        self.database = None
        self.Connect = None
        self.ListView = None
    def __del__(self):
        if self.Connect:
             self.Connect.close()
    def OpenExcel(self,filename,sheetname):
        if os.path.exists(filename) == True:
            try:
                self.TableData = pd.read_excel(filename,sheet_name=sheetname)
                self.TableType = 'Excel'
                self.Filename = filename
                self.SheetName = sheetname
                if self.SheetName and self.ListView:
                    self.LoadData(sheetname)
                return True
            except Exception as Ex:
                print(Ex)
                self.TableData = None
                return False
        else:
            return False
    def OpenSQLITE(self,fileormemory,sheetname):
        Connect = None
        ConnectText = fileormemory
        if ConnectText == "memory":
            ConnectText = ":memory:"
        try:
            import sqlite3
            Connect = sqlite3.connect(ConnectText)
        except sqlite3.Error:
            self.TableData = None
            return False
        if sheetname is not None and Connect is not None:
            sqlString = "selete * from " + sheetname
            try:
                self.TableData = pd.read_sql(sqlString,Connect)
                self.TableType = 'SQLite'
                self.Connect = Connect
                self.Filename = ConnectText
                self.SheetName = sheetname
                if self.SheetName and self.ListView:
                    self.LoadData(sheetname)
                return True
            except Exception as Ex:
                print(Ex)
                self.TableData = None
        return False
    def OpenMYSQL(self,ip,port,user,password,database,sheetname):
        try:
            import pymysql
            Connect = pymysql.connect(host=ip,port=int(port),user=user,password=password,database=database,charset='utf8')
        except :
            self.TableData = None
            return False
        if sheetname is not None and Connect is not None:
            try:
                sqlString = "selete * from " + sheetname
                self.TableData = pd.read_sql(sqlString,Connect)
                self.TableType = 'Mysql'
                self.Connect = Connect
                self.SheetName = sheetname
                self.host = ip
                self.port = port
                self.username = user
                self.password = password
                self.database = database
                if self.SheetName and self.ListView:
                    self.LoadData(sheetname)
                return True
            except Exception as Ex:
                print(Ex)
                self.TableData = None
        return True
    def OpenSQLSERVER(self,ip,port,user,password,database,sheetname):
        try:
            import pymssql
            Connect = pymssql.connect(host=ip,port=int(port),user=user,password=password,database=database,charset='utf8')
        except :
            self.TableData = None
            return False
        if sheetname is not None and Connect is not None:
            try:
                sqlString = "selete * from " + sheetname
                self.TableData = pd.read_sql(sqlString,Connect)
                self.TableType = 'SQLServer'
                self.Connect = Connect
                self.SheetName = sheetname
                self.host = ip
                self.port = port
                self.username = user
                self.password = password
                self.database = database
                if self.SheetName and self.ListView:
                    self.LoadData(sheetname)
                return True
            except Exception as Ex:
                print(Ex)
                self.TableData = None
        return True
    def getSQLResult(self):
        return self.TableData
    def BindingListView(self,uiName = None,elementName = None):
        if uiName and elementName:
            if GetElementType(uiName,elementName) == "ListView":
                self.ListView = GetElement(uiName,elementName)
                return True
        return False
    def LoadData(self,sheetname):
        if self.ListView is not None:
            self.DeleteAllLines()
            if sheetname is not None:
                try:
                    if sheetname != self.SheetName:
                        if self.TableType == 'Excel':
                            if os.path.exists(self.Filename) == True:
                                self.TableData = pd.read_excel(self.Filename,sheet_name=sheetname)
                            else:
                                return False
                        if self.TableType == 'SQLite' or self.TableType == 'Mysql' or self.TableType == 'SQLServer':
                            sqlString = "selete * from " + sheetname
                            if self.Connect is not None:
                                self.TableData = pd.read_sql(sqlString,self.Connect)   
                            else:
                                return False
                        self.SheetName = sheetname
                    self.ListView.configure(show = "headings")
                    self.ListView.configure(selectmode = "extended")
                    columns_list = self.TableData.columns.tolist()
                    self.ListView.configure(columns = columns_list)
                    placeinfo = self.ListView.place_info()
                    columnWidth = int(placeinfo["width"])
                    if len(columns_list) > 0:
                        columnWidth = int(columnWidth / len(columns_list))
                    for column_name in columns_list:
                        self.ListView.column(column_name,anchor="center",width=columnWidth)
                        self.ListView.heading(column_name,text=column_name)
                    if len(self.TableData.values):
                        i = 0
                        for item in self.TableData.values:
                            self.ListView.insert('',i,values=item.tolist())
                            i = i + 1
                    return True
                except :
                    self.TableData = None
        return False
    def SaveData(self,sheetname = None):
        if self.ListView is not None:
            self.TableData = self.TableData.drop(index = self.TableData.index)
            for item in self.ListView.get_children():
                item_value = self.ListView.item(item,'values')  
                self.TableData.append(item_value) 
            if self.TableType == 'Excel':
                self.TableData.to_excel(self.Filename, sheet_name=sheetname)
            elif self.TableType == 'SQLite':
                con_engine = create_engine("sqlite:///"+self.Filename)
                self.TableData.to_sql(sheetname, con=engine, if_exists='replace', index=False)
            elif self.TableType == 'MySQL':
                from sqlalchemy import create_engine
                con_engine = create_engine('mysql+pymysql://{}:{}@{}/{}'.format(self.username, self.password, self.host, self.database)) 
                self.TableData.to_sql(sheetname, con=engine, if_exists='replace', index=False)
            elif self.TableType == 'MSSQL':
                from sqlalchemy import create_engine
                import urllib
                params = urllib.parse.quote_plus('DRIVER={ODBC Driver 13 for SQL Server};'+'SERVER='+self.host+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
                engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
                reload(sys)
                sys.setdefaultencoding('utf8')
                self.TableData.to_sql(sheetname, con=engine, if_exists='replace', index=False)
    def InsertLine(self,row,values):
        if self.ListView is not None:
            self.ListView.insert('',row,values=values)
    def AppendLine(self,values):
        if self.ListView is not None:
            self.ListView.insert('',-1,values=values)
    def DeleteLine(self,row):
        if self.ListView is not None:
            index = 0
            for item in self.ListView.get_children():
                if index == row:
                    self.ListView.delete(item)
                    return 
                index = index + 1
    def DeleteAllLines(self):
        if self.ListView is not None:
    # f.write('            for item in self.ListView.get_children():
    # f.write('                self.ListView.delete(item)
            if len(self.ListView.get_children()) > 0:
                self.ListView.delete(*self.ListView.get_children())

    def ModifyValue(self,row,column,text):
        if self.ListView is not None:
            self.ListView.item(row,column=column,text=text)
    #Read EXCEL File
    def ReadEXCELFile(self,filename,encoding,sheetname = "Sheet1",uiName = None,elementName = None):
        if self.BindingListView(uiName,elementName) == False:
            return False
        if self.OpenExcel(filename,sheetname) == False:
            return False
        return self.LoadData(sheetname)
    #Read MYSQL 
    def ReadMYSQL(self,ip='localhost',port=3306,user='root',password='123456',database='',sheetname = '',uiName = None,elementName = None):
        if self.BindingListView(uiName,elementName) == False:
            return False
        return self.OpenMYSQL(ip,port,user,password,database,sheetname)
    #Read SQLServer 
    def ReadSQLSERVER(self,ip='localhost',port=1433,user='sa',password='123456',database='',sheetname = '',uiName = None,elementName = None):
        if self.BindingListView(uiName,elementName) == False:
            return False
        return self.OpenSQLSERVER(ip,port,user,password,database,sheetname)
'''
    f.write(code)
#读取TXT            
def WriteFileReader_ReadTXT(f,runMode,exportMode):
    code='''
    #f.write('#Read TXT File
def FileReader_ReadTXTFile(filename = None,encoding="utf-8",uiName = None,elementName = None):
    """Read TXT File"""
    global G_ResDir
    if filename is None:
       return ['TXT','No File']
'''
    f.write(code)
    if exportMode == True:
        code='''
        if runMode == 'android':
            realpath = GameLib.Res.GetResPath(filename)
            if realpath is not None:
        else:
            realpath = os.path.join(G_ResDir,filename)
            if os.path.exists(realpath) == True:
'''
        f.write(code)

    else:
        code='''
        if runMode == 'android':
            realpath = GameLib.Res.GetResPath(filename)
            if realpath is not None:
        else:
            realpath = filename
            if os.path.exists(realpath) == True:
        try:
            with open(realpath,encoding = encoding) as f:
                content = f.read()
                if uiName and elementName:
                    SetText(uiName,elementName,content)
                    return ['TXT',content]
        except FileNotFoundError:
            if uiName and elementName:
                    SetText(uiName,elementName,"FileNotFoundError:"+realpath)
            return ['TXT',\"FileNotFoundError:\"+realpath]
    if uiName and elementName:
            SetText(uiName,elementName,"FileNotFoundError:"+realpath)
    return ['TXT',\"FileNotFoundError:\"+realpath]
'''
        f.write(code)
#读取CSV
def WriteFileReader_ReadCSV(f,runMode,exportMode):
    code='''
    #f.write('#Read CSV File
def FileReader_ReadCSVFile(filename,encoding,uiName = None,elementName = None):
    """Read CSV File"""
    global G_ResDir
    if filename is None:
       return ['CSV','No File']
'''
    f.write(code)
    if exportMode == True:
        code='''
        if runMode == 'android':
            realpath = GameLib.Res.GetResPath(filename)
            if realpath is not None:
        else:
            realpath = os.path.join(G_ResDir,filename)
            if os.path.exists(realpath) == True:
'''
        f.write(code)
    else:
        code='''
        if runMode == 'android':
            realpath = GameLib.Res.GetResPath(filename)
            if realpath is not None:
        else:
            realpath = filename
            if os.path.exists(realpath) == True:
        try:
            with open(realpath,encoding = encoding) as f:
                content = f.read()
                if uiName and elementName:
                    SetText(uiName,elementName,content)
                    return ['CSV',content]
        except FileNotFoundError:
            if uiName and elementName:
                    SetText(uiName,elementName,"FileNotFoundError:"+realpath)
            return ['CSV',\"FileNotFoundError:\"+realpath]
    if uiName and elementName:
            SetText(uiName,elementName,"FileNotFoundError:"+realpath)
    return ['CSV',\"FileNotFoundError:\"+realpath]
'''
        f.write(code)
#读取JSON
def WriteFileReader_ReadJSON(f,runMode,exportMode):
    code='''
    #f.write('#Read JSON File
def FileReader_ReadJSONFile(fileorurl,encoding,uiName = None,elementName = None):
    """Read JSON File"""
    global G_ResDir
    if fileorurl is None:
       return ['JSON','No File']
    if fileorurl.find("http:") >= 0 or fileorurl.find("https:") >= 0 :
        content = requests.get(fileorurl).json()
        if uiName and elementName:
            SetText(uiName,elementName,content)
        return [\'JSON\',content]
'''
    f.write(code)
    if exportMode == True:
        code='''
        if runMode == 'android':
            realpath = GameLib.Res.GetResPath(fileorurl)
            if realpath is not None:
        else:
            realpath = os.path.join(G_ResDir,fileorurl)
            if os.path.exists(realpath) == True:
'''
        f.write(code)
    else:
        code='''
        if runMode == 'android':
            realpath = GameLib.Res.GetResPath(fileorurl)
            if realpath is not None:
        else:
            realpath = fileorurl
            if os.path.exists(realpath) == True:
        try:
            with open(realpath,encoding = encoding) as f:
                content = f.read()
                if uiName and elementName:
                    SetText(uiName,elementName,content)
                    return ['JSON',content]
        except FileNotFoundError:
            if uiName and elementName:
                    SetText(uiName,elementName,"FileNotFoundError:"+realpath)
            return ['JSON',\"FileNotFoundError:\"+realpath]
    if uiName and elementName:
            SetText(uiName,elementName,"FileNotFoundError:"+realpath)
    return ['JSON',\"FileNotFoundError:\"+realpath]
'''
        f.write(code)
#读取JSON
def WriteFileReader_ReadXML(f,runMode,exportMode):
    code='''
    #f.write('#Read XML File
def FileReader_ReadXMLFile(filename,encoding,uiName = None,elementName = None):
    """Read XML File"""
    global G_ResDir
    if filename is None:
       return ['XML','No File']
'''
    f.write(code)
    if exportMode == True:
        code='''
        if runMode == 'android':
            realpath = GameLib.Res.GetResPath(filename)
            if realpath is not None:
        else:
            realpath = os.path.join(G_ResDir,filename)
            if os.path.exists(realpath) == True:
'''
        f.write(code)
    else:
        code='''
        if runMode == 'android':
            realpath = GameLib.Res.GetResPath(filename)
            if realpath is not None:
        else:
            realpath = filename
            if os.path.exists(realpath) == True:
        try:
            with open(realpath,encoding = encoding) as f:
                content = f.read()
                if uiName and elementName:
                    SetText(uiName,elementName,content)
                    return ['XML',content]
        except FileNotFoundError:
            if uiName and elementName:
                SetText(uiName,elementName,"FileNotFoundError:"+realpath)
            return ['XML',\"FileNotFoundError:\"+realpath]
    if uiName and elementName:
            SetText(uiName,elementName,"FileNotFoundError:"+realpath)
    return ['XML',\"FileNotFoundError:\"+realpath]
''' 
        f.write(code)
#读取WEB
def WriteFileReader_ReadWEB(f):
    code='''
    #f.write('#Read WEBFile
def FileReader_ReadWEBFile(fileorurl,encoding,uiName = None,elementName = None):
    """Read WEB File"""
    if fileorurl is None:
       return ['WEB','No File']
    if fileorurl.find("http:") >= 0 or fileorurl.find("https:") >= 0 :
        try:
            response = request.urlopen(fileorurl)
            if response is not None:
                content = response.read()
                if uiName and elementName:
                    SetText(uiName,elementName,content)
                return [\'WEB\',content]
            else:
                return ['WEB','Can\'t visit '+fileorurl]
        except :
            if uiName and elementName:
               SetText(uiName,elementName,"Find visit:"+fileorurl)
            return ['WEB','Can\'t visit '+fileorurl]
    elif os.path.exists(fileorurl) == True:
        f = open(fileorurl,mode=\'r\',encoding=encoding)
        content = f.read()
        f.close()
        if uiName and elementName:
            SetText(uiName,elementName,content)
        return [\'WEB\',content]
    return ['WEB','No File']
''' 
    f.write(code)
#读取SOCKET
def WriteFileReader_ReadSOCKET(f):
    code='''
    #f.write('#Read Socket
def FileReader_ReadSOCKET(IP,port,uiName = None,elementName = None):
    """Read Data From Socket """
    if IP is None:
       return ['SOCKET','No IP']
    if IP.find(".") >= 0:
        socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = socket.connect((IP,port))
        if result == 0:
            content = self.socket.recv(1024)
            if uiName and elementName:
                SetText(uiName,elementName,content)
        return [\'SOCKET\',content]
    return None
''' 
    f.write(code)
#读取SQLITE
def WriteFileReader_ReadSQLITE(f):
    code='''
    #f.write('#Read SQLITE
def FileReader_ReadSQLITE(fileormemory,sqlstring = None,uiName = None,elementName = None):
    """Read Data From SQLITE """
    Connect = None
    ConnectText = fileormemory
    if ConnectText == "memory":
        ConnectText = ":memory:"
    try:
        Connect = sqlite3.connect(ConnectText)
    except sqlite3.Error:
        return None
    if sqlstring is not None and Connect is not None:
        content = pd.read_sql(sqlstring,Connect)
        if uiName and elementName:
            SetText(uiName,elementName,content)
        return [\'SQLITE\',Connect]
    return None
''' 
    f.write(code)
#读取MYSQL
def WriteFileReader_ReadMYSQL(f):
    code='''
    #f.write('#Read MYSQL
def FileReader_ReadMYSQL(host,port,user,password,database,sqlstring,uiName = None,elementName = None):
    """Read Data From MYSQL """
    Connect = pymysql.connect(host=host,port=port,user=user,password=password,database=database,charset=\'utf8\')
    if sqlstring is not None and Connect is not None:
        content = pd.read_sql(sqlstring,Connect)
        if uiName and elementName:
            SetText(uiName,elementName,content)
        return [\'MYSQL\',Connect]
    return None
''' 
    f.write(code)
#读取SQLSERVER
def WriteFileReader_ReadSQLSERVER(f):
    code='''
    #f.write('#Read SQLSERVER
def FileReader_ReadSQLSERVER(host,port,user,password,database,sqlstring,uiName = None,elementName = None):
    """Read Data From SQLSERVER """
    Connect = pymssql.connect(host=host,port=port,user=user,password=password,database=database,charset=\'utf8\')
    if sqlstring is not None and Connect is not None:
        content = pd.read_sql(sqlstring,Connect)
        if uiName and elementName:
            SetText(uiName,elementName,content)
        return [\'SQLSERVER\',Connect]
    return None
''' 
    f.write(code)
#读取MONGODB
def WriteFileReader_ReadMONGODB(f):
    code='''
    #f.write('#Read MONGODB
def FileReader_ReadMONGODB(host,port,user,password,database,sqlstring,uiName = None,elementName = None):
    """Read Data From MONGODB """
    if user and password:
        mongo_uri = \'mongodb://%s:%s@%s:%s/%s\' % (username, password, host, port, database)
        Connect = MongoClient(mongo_uri)
    else:
        Connect = MongoClient(host=host,port=port)
    if sqlstring is not None and Connect is not None:
        dbObj = Connect[database]
        content = self.dbObj[querystring]
        if uiName and elementName:
            SetText(uiName,elementName,content)
        return [\'MONGODB\',dbObj]
    return None
''' 
    f.write(code)
#摄像头
def WriteFileReader(f):
    code='''
#Create A Empty FileReader
def FileReader():
    return None
'''
    f.write(code)
#播放器

def WriteAudioPlayer(f,runMode='windows'):
    code='''
    #f.write('#Create AudioPlayer
class AudioPlayer():
    """'+Language.G_Language[1785]+'"""
    def __init__(self,filename=None):
        self.filename = None
        self.state_flag = 0
        self.time_total = 0
        self.isbgm = True
        self.channel = None
        self.soundID = 0
        if filename:
            self.LoadFile(filename)
    def LoadFile(self,filename,isbgm=True):
        """'+Language.G_Language[1250]+'"""
        global G_ResDir
        try:
    if runMode == 'android':
                audioPath, autioFile = os.path.split(filename)
                realpath = GameLib.Res.GetResPath(autioFile)
                if realpath is not None:
    else:
                realpath = filename
                if os.path.exists(realpath) == False:
                    realpath = os.path.join(G_ResDir,filename)
                if os.path.exists(realpath) == True:
                if isbgm == True:
                    mixer.music.load(realpath)
                else:
                    self.channel = mixer.find_channel()
                    self.soundID = mixer.Sound(realpath)
    if runMode == 'windows':
                    media_info = MediaInfo.parse(realpath)
                    data = media_info.to_json()
                    data2 = json.loads(data)
                    if 'tracks' in data2:
                        track0 = data2['tracks'][0]
                        duration = track0["duration"]
                        self.time_total = duration * 1000
    else:
                        self.time_total = 0
                self.isbgm = isbgm
                self.filename = realpath
                return True
        except Exception as e:
            print(e)
        return False
    #f.write('    '+Language.G_Language[1251]+'
    def Play(self):
        """'+Language.G_Language[1251]+'"""
        try:
            if self.filename is not None:
                if self.isbgm == False:
                    if self.channel: 
                        self.channel.play(self.soundID)
                else:
                    mixer.music.play()
                self.state_flag = 1
                return True
        except Exception as e:
            print(e)
        return False
    #f.write('    '+Language.G_Language[1273]+'
    def Pause(self):
        """'+Language.G_Language[1273]+'"""
        try:
            if self.state_flag == 1:
                if self.isbgm == False:
                    if self.channel:  
                        self.channel.pause()
                else:
                    mixer.music.pause()
                return True
        except Exception as e:
            print(e)
        return False
    #f.write('    '+Language.G_Language[1274]+'
    def Resume(self):
        """'+Language.G_Language[1274]+'"""
        try:
            if self.state_flag == 1:
                if self.isbgm == False:
                    if self.channel:  
                        self.channel.unpause()
                else:
                    mixer.music.unpause()
                return True
        except Exception as e:
            print(e)
        return False
    #f.write('    '+Language.G_Language[1255]+'
    def Stop(self):
        """'+Language.G_Language[1255]+'"""
        try:
            if self.state_flag == 1:
                if self.isbgm == False:
                    if self.channel:  
                        self.channel.stop()
                else:
                    mixer.music.stop()
                self.state_flag = 0
                return True
        except Exception as e:
            print(e)
        return False
    def SetVolume(self,volume):
        """'+Language.G_Language[1275]+'"""
        try:
            if self.isbgm == False:
                if self.channel:  
                    self.channel.set_volume(volume)
            else:
                mixer.music.set_volume(volume)
            return True
        except Exception as e:
            print(e)
        return False
    def GetVolume(self):
        """'+Language.G_Language[1276]+'"""
        try:
            if self.isbgm == False:
                if self.channel:  
                    return  self.channel.get_volume()
            else:
                return mixer.music.get_volume()
        except Exception as e:
            print(e)
        return 0.0
    def GetDuration(self):
        """'+Language.G_Language[1277]+'"""
        return self.time_total
    def SetCurrTime(self,time):
        """'+Language.G_Language[1278]+'"""
        try:
            if self.isbgm == False:
                if self.channel:  
                    self.channel.set_pos(time)
            else:
                mixer.music.set_pos(time)
            return True
        except Exception as e:
            print(e)
        return False
    def GetCurrTime(self):
        """'+Language.G_Language[1279]+'"""
        try:
            if self.isbgm == False:
                if self.channel:  
                    return self.channel.get_pos()
            else:
                return mixer.music.get_pos()
        except Exception as e:
            print(e)
        return 0.0

''' 
    f.write(code)
#播放器
def WriteVideoPlayer(f):
    code='''
class VideoPlayer():
    """'+Language.G_Language[1786]+'"""
    def __init__(self,uiName = None,elementName = None,filename = None,vlcpath = ''):
        super().__init__()
        self.canvas = GetElement(uiName,elementName)
        self.canvas_winfo = None
        self.player = None
        self.metadata = None
        self.fps = 30
        self.state_flag = 0
        self.filename = None
        self.image_frame = None
        self.image_canvas = None
        self.volume = -1.0
        self.loopnumber = 1
        self.duration = 0
        self.current_time = 0 
        self.includeAudio = False
        self.isMute = False
        self.vlcpath = vlcpath
        if self.vlcpath !='':
            os.environ[\'PYTHON_VLC_MODULE_PATH\'] = self.vlcpath
            import vlc
            self.PLAY_STATE = vlc.State.Playing
            self.PAUSE_STATE = vlc.State.Paused
            self.player = vlc.MediaPlayer()
            self.player.set_hwnd(self.canvas.winfo_id())
        self.PlayFile(filename)
    #Thread 
    def thread_playvideo(self):
        try:
            if self.canvas is None:
                return
            if self.state_flag == -1:
                return 
            if self.player is None:
                return
            if self.state_flag == 1:
                autio_frame,val = self.player.get_frame()
                if val != 'eof' and autio_frame is not None:
                    self.image_frame, self.current_time = autio_frame
                    width = self.canvas.winfo_width()
                    height = self.canvas.winfo_height()
                    img_resize = Image.frombytes("RGB", (self.image_frame.get_size()[0], self.image_frame.get_size()[1]), bytes(self.image_frame.to_bytearray()[0])).resize((width, height))
                    self.image_canvas = ImageTk.PhotoImage(img_resize)
                    self.canvas.create_image(0,0,anchor=tkinter.NW,image=self.image_canvas,tag='image')
                    self.canvas.update()
                    self.player.set_volume(self.volume)
            if val == 'eof':
                if self.loopnumber > 1:
                    self.loopnumber -= 1
                    self.SetCurrTime(0)
                    self.canvas.after(self.wait_time,self.thread_playvideo)
                else:
                    self.Stop()
                return 
            self.canvas.after(self.wait_time,self.thread_playvideo)
        except Exception as e:
            self.canvas.after(self.wait_time,self.thread_playvideo)
    def PlayFile(self,filename,loopnumber=1):
        """'+Language.G_Language[1250]+'"""
        global G_ResDir
        global G_ResourcesFileList
        if filename is not None:
            sameFile = False
            oldfilename_lower = self.filename
            if oldfilename_lower:
                oldfilename_lower = oldfilename_lower.lower()
            if os.path.exists(filename) == True:
                filename_lower = filename.lower()
                if oldfilename_lower == filename_lower:
                    sameFile = True
                else:
                    self.filename = filename
            else:
                projpath, resdirname = os.path.split(G_ResDir)
                filepath, filename = os.path.split(filename)
                filepath = os.path.join(projpath,filename)
                if os.path.exists(filepath) == True:
                    filename_lower = filepath.lower()
                    if oldfilename_lower == filename_lower:
                        sameFile = True
                    else:
                        self.filename = filepath
                else:
                    filename_Lower = filename.lower()
                    if filename_Lower in G_ResourcesFileList:
                        filepath = G_ResourcesFileList[filename_Lower]
                        if os.path.exists(filepath) == True:
                            filename_lower = filepath.lower()
                            if oldfilename_lower == filename_lower:
                                sameFile = True
                            else:
                                self.filename = filepath
            if sameFile == True:
                if self.IsPause() == True:
                    self.Resume()
            else:
                if self.player is not None:
                    self.Stop()
                try:
                    self.duration = 0
                    video = VideoFileClip(self.filename)
                    self.includeAudio = (video.audio != None)
                    if self.vlcpath:
                        self.player.set_mrl(self.filename)
                        self.player.play()
                    else:
                        self.player = MediaPlayer(self.filename,paused = True)
                        self.metadata = self.player.get_metadata()
                        if self.isMute == True:
                            self.volume = 0
                        if self.includeAudio == True:
                            if self.volume == -1.0:
                                self.volume = self.player.get_volume()
                    self.fps = 30
                    self.wait_time = int(1000 / self.fps)
                    self.state_flag = 1
                    self.loopnumber = loopnumber
                    self.thread_playvideo()
                except Exception as e:
                    print(e)
    def HasAudio(self):
        """'+Language.G_Language[1273]+'"""
        return self.includeAudio
    def IsPlaying(self):
        """'+Language.G_Language[1330]+'"""
        if self.player is not None:
            if self.state_flag == 1:
                if self.vlcpath:
                    return self.player.is_playing()
                else:
                    if self.player.get_pause() == False:
                        return True
        return False
    def Pause(self):
        """'+Language.G_Language[1273]+'"""
        if self.player is not None:
            if self.state_flag == 1:
                if self.vlcpath:
                    self.player.pause()
                else:
                    self.player.set_pause(True)
    def IsPause(self):
        """'+Language.G_Language[1331]+'"""
        if self.player is not None:
            if self.state_flag == 1:
                if self.vlcpath:
                    if self.player.is_playing() == False:
                        return True
                else:
                    return self.player.get_pause()
        return False
    def Resume(self):
        """'+Language.G_Language[1274]+'"""
        if self.player is not None:
            if self.state_flag == 1:
                if self.vlcpath:
                    self.player.set_pause(0)
                else:
                    self.player.set_pause(False)
    def Toggle_Pause(self):
        """'+Language.G_Language[1332]+'"""
        if self.player is not None:
            if self.state_flag == 1:
                if self.vlcpath:
                    state = self.player.get_state()
                    if state == self.PLAY_STATE:
                        self.player.pause(0)
                    else:
                        self.player.pause(1)
                else:
                    self.player.toggle_pause() 
    def FullScreen(self):
        """'+Language.G_Language[1324]+'"""
        if self.vlcpath:
            self.player.set_fullscreen(True)
        else:
            self.canvas_winfo = [self.canvas.winfo_x(),self.canvas.winfo_y(),self.canvas.winfo_width(),self.canvas.winfo_height()]
            user32 = ctypes.windll.user32
            sw = user32.GetSystemMetrics(0)
            sh = user32.GetSystemMetrics(1)
            self.canvas.place(x=0,y=0,width=sw,height=sh)
            if self.image_frame:
                img_resize = Image.frombytes("RGB", (self.image_frame.get_size()[0], self.image_frame.get_size()[1]), bytes(self.image_frame.to_bytearray()[0])).resize((sw, sh))
                self.image_canvas = ImageTk.PhotoImage(img_resize)
                self.canvas.create_image(0,0,anchor=tkinter.NW,image=self.image_canvas,tag='image')
                self.canvas.update()
    def RecoveryWindow(self):
        """'+Language.G_Language[1325]+'"""
        if self.vlcpath:
            self.player.set_fullscreen(True)
        else:
            if self.canvas_winfo:
                self.canvas.place(x=self.canvas_winfo[0],y=self.canvas_winfo[1],width=self.canvas_winfo[2],height=self.canvas_winfo[3])
                if self.image_frame:
                    img_resize = Image.frombytes("RGB", (self.image_frame.get_size()[0], self.image_frame.get_size()[1]), bytes(self.image_frame.to_bytearray()[0])).resize((self.canvas_winfo[2], self.canvas_winfo[3]))
                    self.image_canvas = ImageTk.PhotoImage(img_resize)
                    self.canvas.create_image(0,0,anchor=tkinter.NW,image=self.image_canvas,tag='image')
                    self.canvas.update()
            self.canvas_winfo = None
    def Stop(self):
        """'+Language.G_Language[1252]+'"""
        if self.state_flag == 1:
            self.state_flag = -1
            if self.vlcpath:
                self.player.stop()
            else:
                self.player.set_pause(True) 
            self.canvas.after_cancel(self.thread_playvideo)
            time.sleep(self.wait_time/1000.0)
            if self.vlcpath:
                pass
            else:
                self.player.close_player() 
            self.player = None
            self.filename = None
    def IsStop(self):
        """'+Language.G_Language[1333]+'"""
        if self.state_flag == -1:
            return True
        return True 
    def SetVolume(self,volume):
        """'+Language.G_Language[1275]+'"""
        if self.includeAudio == True:
            self.volume = volume 
            if self.player is not None:
                if self.vlcpath:
                    self.player.audio_set_volume(volume)
                else:
                    self.player.set_volume(volume)
            self.isMute = False
    def GetVolume(self):
        """'+Language.G_Language[1276]+'"""
        if self.includeAudio == True:
            if self.player is not None:
                if self.vlcpath:
                    return self.player.audio_get_volume()
                else:
                    return self.player.get_volume()
            return self.volume
        return 0.0
    def Mute(self):
        """'+Language.G_Language[1315]+'"""
        if self.player is not None:
            if self.vlcpath:
                self.player.audio_set_volume(0)
            else:
                self.player.set_volume(0)
        self.isMute = True
    def IsMute(self):
        """'+Language.G_Language[1316]+'"""
        return self.isMute
    def Restore(self):
        """'+Language.G_Language[1317]+'"""
        return self.SetVolume(self.volume)
    def GetDuration(self):
        """'+Language.G_Language[1277]+'"""
        if self.duration == 0:
            if self.vlcpath:
                self.duration = self.player.get_length()/1000.0
            else:
                import subprocess
                if 'duration' in self.metadata:
                    self.duration =  self.metadata['duration']
                    if self.duration  is None:
                        ffprobe_cmd = 'ffprobe -i {} -show_entries format=duration -v quiet -of csv=\"p=0\"'
                        p = subprocess.Popen(
                            ffprobe_cmd.format(self.filename),
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True)
                        out, err = p.communicate()
                        self.duration = float(str(out, 'utf-8').strip())
        return self.duration
    def SetCurrTime(self,time):
        """'+Language.G_Language[1278]+'"""
        if self.player is not None:
            if self.vlcpath:
                self.player.set_time(int(time*1000))
            else:
                self.player.seek(pts=time,relative=False,seek_by_bytes=False,accurate=False) 
    def GetCurrTime(self):
        """'+Language.G_Language[1279]+'"""
        if self.player is not None:
            if self.vlcpath:
                self.current_time = self.player.get_time()/1000.0
        return self.current_time


''' 
    f.write(code)
#摄像头
def WriteVideoCapture(f):
    code='''
class VideoCapture():
    """'+Language.G_Language[1787]+'"""
    def __init__(self,uiName = None,elementName = None):
        super().__init__()
        global G_ResDir
        self.uiName = uiName
        self.canvas = GetElement(uiName,elementName)
        self.framefps = 30
        self.framefps_delay = 1000//self.framefps
        self.imageFormat = cv2.COLOR_BGR2RGBA
        self.imageFrame = None
        self.photoImage = None
        self.capture = None
        self.savePath = ""
        self.saveFinishCallBackFunction = None
        self.frameCallBackFunction = None
        self.face_detectionArray = {}
        self.CascadesDir = G_ResDir
    def SetFps(self,fps):
        """'+Language.G_Language[1301]+'"""
        self.framefps = fps
        self.framefps_delay = 1000//fps
    def GetFps(self):
        """'+Language.G_Language[1302]+'"""
        return self.framefps
    def SetImageFormat(self,format):
        """'+Language.G_Language[1304]+'"""
        checkformat = format.lower()
        if checkformat == "rgb":
            format = cv2.COLOR_BGR2RGB
        elif checkformat == "rgba":
            format = cv2.COLOR_BGR2RGBA
        elif checkformat == "gray":
            format = cv2.COLOR_BGR2GRAY
        elif checkformat == "yuv":
            format = cv2.COLOR_BGR2YUV
        elif checkformat == "i420":
            format = cv2.COLOR_BGR2YUV_I420
        self.imageFormat = format
    def GetImageFormat(self):
        """'+Language.G_Language[1305]+'"""
        return self.imageFormat
    def SaveImageToFile(self,filePath,callbackFunction = None):
        """'+Language.G_Language[1303]+'"""
        self.savePath = filePath
        self.saveFinishCallBackFunction = callbackFunction
    def SaveFrameCallBackFunction(self,callbackFunction = None):
        """'+Language.G_Language[9500]+'"""
        self.frameCallBackFunction = callbackFunction
    def SetCascadesDir(self,cascadesDir):
        """'+Language.G_Language[1306]+'"""
        global G_ResDir
        self.CascadesDir = cascadesDir
        if os.path.exists(self.CascadesDir) == False:
           projpath, resdirname = os.path.split(G_ResDir)
           self.CascadesDir = os.path.join(projpath,cascadesDir)
           if os.path.exists(self.CascadesDir) == False:
               self.CascadesDir = os.path.join(G_ResDir,cascadesDir)
    def AddDetector(self,detectorName = 'face',xmlfile = 'haarcascade_frontalface_default.xml',bordercolor='red'):
        """'+Language.G_Language[1307]+'"""
        xmlPath = os.path.join(self.CascadesDir,xmlfile)
        match = zhPattern.search(xmlPath)
        if match:
            MessageBox("检测XML数据文件需要放在英文路径下才能识别!")
        else:
            if os.path.exists(xmlPath) == True:
                detector = cv2.CascadeClassifier(xmlPath)
                detector_param = {}
                detector_param[\'scaleFactor\'] = None
                detector_param[\'minNeighbors\'] = None
                #利用Canny边缘检测器排除一些边缘很少或很多的图像区域
                #cv2.CASCADE_DO_CANNY_PRUNING
                #只做初步检测
                #cv2.CASCADE_DO_ROUGH_SEARCH
                #只检测最大物体
                #cv2.CASCADE_FIND_BIGGEST_OBJECT
                #按比例检测
                #cv2.CASCADE_SCALE_IMAGE
                detector_param[\'flags\'] = None
                detector_param[\'minSize\'] = None
                detector_param[\'maxSize\'] = None
                detector_param[\'color\'] = bordercolor
                self.face_detectionArray[detectorName] = [detector,detector_param]
    def DelDetector(self,detectorName = 'face'):
        """'+Language.G_Language[1308]+'"""
        if detectorName in self.face_detectionArray:
            self.face_detectionArray.pop(detectorName)
    def SetDetectorScaleFactor(self,detectorName,scaleFactor):
        """'+Language.G_Language[2649]+'"""
        if detectorName in self.face_detectionArray:
            if \'scaleFactor\' in self.face_detectionArray[detectorName][1]:
                self.face_detectionArray[detectorName][1][\'scaleFactor\'] = scaleFactor
    def GetDetectorScaleFactor(self,detectorName):
        """'+Language.G_Language[2650]+'"""
        if detectorName in self.face_detectionArray:
            if \'scaleFactor\' in self.face_detectionArray[detectorName][1]:
                return self.face_detectionArray[detectorName][1][\'scaleFactor\']
        return None
    def SetDetectorMinNeighbors(self,detectorName,minNeighbors):
        """'+Language.G_Language[2651]+'"""
        if detectorName in self.face_detectionArray:
            if \'minNeighbors\' in self.face_detectionArray[detectorName][1]:
                self.face_detectionArray[detectorName][1][\'minNeighbors\'] = minNeighbors
    def GetDetectorMinNeighbors(self,detectorName):
        """'+Language.G_Language[2652]+'"""
        if detectorName in self.face_detectionArray:
            if \'minNeighbors\' in self.face_detectionArray[detectorName][1]:
                return self.face_detectionArray[detectorName][1][\'minNeighbors\']
        return None
    def SetDetectorMinSize(self,detectorName,minSize):
        """'+Language.G_Language[2653]+'"""
        if detectorName in self.face_detectionArray:
            if \'minSize\' in self.face_detectionArray[detectorName][1]:
                if type(minSize) == type(()):
                    self.face_detectionArray[detectorName][1][\'minSize\'] = minSize
                elif type(minSize) == type(1):
                    self.face_detectionArray[detectorName][1][\'minSize\'] = (minSize,minSize)
    def GetDetectorMinSize(self,detectorName):
        """'+Language.G_Language[2654]+'"""
        if detectorName in self.face_detectionArray:
            if \'minSize\' in self.face_detectionArray[detectorName][1]:
                return self.face_detectionArray[detectorName][1][\'minSize\']
        return None
    def SetDetectorMaxSize(self,detectorName,maxSize):
        """'+Language.G_Language[2655]+'"""
        if detectorName in self.face_detectionArray:
            if \'maxSize\' in self.face_detectionArray[detectorName][1]:
                if type(maxSize) == type(()):
                    self.face_detectionArray[detectorName][1][\'maxSize\'] = maxSize
                elif type(maxSize) == type(1):
                    self.face_detectionArray[detectorName][1][\'maxSize\'] = (maxSize,maxSize)
    def GetDetectorMaxSize(self,detectorName):
        """'+Language.G_Language[2656]+'"""
        if detectorName in self.face_detectionArray:
            if \'maxSize\' in self.face_detectionArray[detectorName][1]:
                return self.face_detectionArray[detectorName][1][\'maxSize\']
        return None
    def SetDetectorColor(self,detectorName,color):
        """'+Language.G_Language[2657]+'"""
        if detectorName in self.face_detectionArray:
            if \'color\' in self.face_detectionArray[detectorName][1]:
                self.face_detectionArray[detectorName][1][\'color\'] = color
    def GetDetectorColor(self,detectorName):
        """'+Language.G_Language[2658]+'"""
        if detectorName in self.face_detectionArray:
            if \'color\' in self.face_detectionArray[detectorName][1]:
                return self.face_detectionArray[detectorName][1][\'color\']
        return None
    def ChooseDetectorFlags_NONE(self,detectorName = 'face'):
        """'+Language.G_Language[2643]+'"""
        if detectorName in self.face_detectionArray:
            if \'flags\' in self.face_detectionArray[detectorName][1]:
                self.face_detectionArray[detectorName][1][\'flags\'] = None
    def ChooseDetectorFlags_CANNY_PRUNING(self,detectorName = 'face'):
        """'+Language.G_Language[2644]+'"""
        if detectorName in self.face_detectionArray:
            if \'flags\' in self.face_detectionArray[detectorName][1]:
                self.face_detectionArray[detectorName][1][\'flags\'] = cv2.CASCADE_DO_CANNY_PRUNING
    def ChooseDetectorFlags_ROUGH_SEARCH(self,detectorName = 'face'):
        """'+Language.G_Language[2645]+'"""
        if detectorName in self.face_detectionArray:
            if \'flags\' in self.face_detectionArray[detectorName][1]:
                self.face_detectionArray[detectorName][1][\'flags\'] = cv2.CASCADE_DO_ROUGH_SEARCH
    def ChooseDetectorFlags_FIND_BIGGEST(self,detectorName = 'face'):
        """'+Language.G_Language[2646]+'"""
        if detectorName in self.face_detectionArray:
            if \'flags\' in self.face_detectionArray[detectorName][1]:
                self.face_detectionArray[detectorName][1][\'flags\'] = cv2.CASCADE_FIND_BIGGEST_OBJECT
    def ChooseDetectorFlags_SCALE_IMAGE(self,detectorName = 'face'):
        """'+Language.G_Language[2647]+'"""
        if detectorName in self.face_detectionArray:
            if \'flags\' in self.face_detectionArray[detectorName][1]:
                self.face_detectionArray[detectorName][1][\'flags\'] = cv2.CASCADE_SCALE_IMAGE
    def GetDetectorFlags(self,detectorName = 'face'):
        """'+Language.G_Language[2648]+'"""
        if detectorName in self.face_detectionArray:
            if \'flags\' in self.face_detectionArray[detectorName][1]:
                if self.face_detectionArray[detectorName][1][\'flags\'] == cv2.CASCADE_DO_CANNY_PRUNING:
                    return "CANNY_PRUNING"
                if self.face_detectionArray[detectorName][1][\'flags\'] == cv2.CASCADE_DO_ROUGH_SEARCH:
                    return "ROUGH_SEARCH"
                if self.face_detectionArray[detectorName][1][\'flags\'] == cv2.CASCADE_FIND_BIGGEST_OBJECT:
                    return "FIND_BIGGEST"
                if self.face_detectionArray[detectorName][1][\'flags\'] == cv2.CASCADE_SCALE_IMAGE:
                    return "SCALE_IMAGE"
        return None
    def Detect(self,frame,scale_w,scale_h):
        """'+Language.G_Language[1313]+'"""
        grayImage = None
        for detectorName in self.face_detectionArray.keys():
            detectorInfo = self.face_detectionArray[detectorName]
            if grayImage is None:
                grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_array = detectorInfo[0].detectMultiScale(grayImage,scaleFactor = detectorInfo[1]['scaleFactor'],minNeighbors = detectorInfo[1]['minNeighbors'],flags = detectorInfo[1]['flags'],minSize = detectorInfo[1]['minSize'],maxSize = detectorInfo[1]['maxSize'])
            for x,y,w,h in face_array:
                l = int(x * scale_w)
                t = int(y * scale_h)
                r = int((x + w) * scale_w)
                b = int((y + h) * scale_h)
                self.canvas.create_rectangle(l,t,r,b,outline=detectorInfo[1]['color'],width=1,tag=\"detector\")
                self.canvas.create_text(l,t,text=detectorName,anchor=tkinter.NW,fill = detectorInfo[1]['color'],tag=\"detector\")
    #Thread
    def thread_playvideo(self):
        try:
            if self.canvas is None:
                return
            frame = None
            if (type(self.imageFrame) is np.ndarray):
                frame = self.imageFrame
                #行是高度，列是宽度
                frame_h,frame_w,channels = frame.shape
            else:
                if self.stopFlag:
                    return
                ret,frame = self.capture.read()
                frame_w = int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH))
                frame_h = int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
            if self.frameCallBackFunction:
                self.frameCallBackFunction(frame,frame_w,frame_h)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            canvas_w = self.canvas.winfo_width()
            canvas_h = self.canvas.winfo_height()
            img = Image.fromarray(cv2image).resize((canvas_w, canvas_h))
            self.photoImage = ImageTk.PhotoImage(img)
            self.canvas.delete("image")
            self.canvas.delete("detector")
            self.canvas.create_image(0,0,anchor=tkinter.NW,image=self.photoImage,tag='image')
            self.Detect(frame,canvas_w/frame_w,canvas_h/frame_h)
            if self.savePath != "":
                root = GetElement(self.uiName,"root")
                dpi = root.winfo_fpixels(\'1i\')
    #f.write('                dpi_scale = dpi/72.0
                dpi_scale = 1.0
                parentID = self.canvas.winfo_parent()
                parentWidget = self.canvas._nametowidget(parentID)
                x = self.canvas.winfo_x()
                y = self.canvas.winfo_y()
                while parentWidget != root:
                    px = parentWidget.winfo_rootx()
                    py = parentWidget.winfo_rooty()
                    x = x + px
                    y = y + py
                    parentID = parentWidget.winfo_parent()
                    parentWidget = parentWidget._nametowidget(parentID)
                x1 = x + int(canvas_w * dpi_scale)
                y1 = y + int(canvas_h * dpi_scale)
                from PIL import ImageGrab
                ImageGrab.grab().crop((x, y, x1, y1)).save(self.savePath)
                self.savePath = ""
                if self.saveFinishCallBackFunction:
                    self.saveFinishCallBackFunction()
            self.canvas.update()
            self.canvas.after(self.framefps_delay,self.thread_playvideo)
        except Exception as e:
            print(e)
    def StartCapture(self,captureIndex = 0,fps = 30,format = "rgb"):
        """'+Language.G_Language[1253]+'"""
        self.SetFps(fps)
        self.imageFrame = None
        self.SetImageFormat(format)
        try:
            self.capture = cv2.VideoCapture(captureIndex)
            if self.capture is None:
                return False
            self.stopFlag = False
            self.thread_playvideo()
            return True
        except Exception as e:
            print(e)
        return False
    def Stop(self):
        """'+Language.G_Language[1252]+'"""
        self.stopFlag = True
        if self.capture:
            self.capture = None
    def UseImageFile(self,fileName):
        """'+Language.G_Language[2659]+'"""
        try:
            self.imageFrame = cv2.imread(fileName)
        except Exception as e:
            print(e)
''' 
    f.write(code)
#写入SOCKET
def WriteSocket(f):
    code='''
class Socket():
    """'+Language.G_Language[1783]+'"""
    def __init__(self,protocol='tcp',ip='127.0.0.1',port=8888,encoding='utf-8',listen=10,buffsize=1024,netMsgTable=None):
        super().__init__()
        self.protocol = protocol
        self.ip = ip
        self.port = port
        self.encoding = encoding
        self.listen = listen
        self.buffsize = buffsize
        self.socket = None
        self.connSocketList = []
        self.socketAddrDic = {}
        self.recvAddrList = []
        self.recvMessageDic = {}
        self.recvNetMsgDic = {}
        self.netMsgTable = netMsgTable
        self.netMsgFuncDict = {}
        self.stopFlag = False
        self.uiName = None
        self.elementName = None
        self.MsgListBox = None
        if self.protocol == "udp":
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.bind((self.ip, int(self.port)))
            self.run_thread = threading.Thread(target=self.thread_Udp_recMsg, args=[])
            self.run_thread.Daemon = True
            self.run_thread.start()  
    def GetLocalIP(self):
        """'+Language.G_Language[1471]+'"""
        testSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            testSocket.connect(('10.255.255.255',1))
            IP = testSocket.getsockname()[0]
        except Exception as e:
            IP = '127.0.0.1'
        finally:
            testSocket.close()
        return IP
    def GetPort(self):
        """'+Language.G_Language[1472]+'"""
        return self.port
    def CreateServer(self,port=8888):
        """'+Language.G_Language[1254]+'"""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.port = port
        try:
            self.socket.bind((self.ip, int(self.port)))
            self.socket.listen(self.listen)
        except Exception as e:
            print(e)
            self.stopFlag = True
            self.Print("'+Language.G_Language[1885]+'")
            return
        else:
            self.Print("'+Language.G_Language[1886]+'")
            self.connSocketList.append(self.socket)
            self.run_thread = threading.Thread(target=self.thread_Tcp_Server, args=[])
            self.run_thread.Daemon = True
            self.run_thread.start()
    def ConvertStringToParamList(self,text):
        while text[-1] == '\\n':
            text = text[0:-1]
        return text.split(',')
    def GetNetMsgList(self,tableName):
        """'+Language.G_Language[1898]+'"""
        global G_ResDir
        projpath, resdirname = os.path.split(G_ResDir)
        MsgDBFile = os.path.join(projpath,"netmsg.db")
        allColumnList = []
        if os.path.exists(MsgDBFile) == True:
            dbInstance = sqlite3.connect(MsgDBFile)
            sqliteCursor = dbInstance.cursor()
            SQLString = "select * from "+tableName
            sqliteCursor.execute(SQLString)
            allColumnList = sqliteCursor.fetchall()
    # f.write('            for columnInfo in allColumnList:
    # f.write('                MsgID = columnInfo[1]
    # f.write('                MsgSending = columnInfo[2]
    # f.write('                MsgName = columnInfo[3]
    # f.write('                Remark = columnInfo[4]
    # f.write('                if MsgSending == 0:
    # f.write('                    ItemText = str("%d_%s_REQUEST"%(MsgID,MsgName))
    # f.write('                elif MsgSending == 1:
    # f.write('                    ItemText = str("%d_%s_RESPONSE"%(MsgID,MsgName))
    # f.write('                else:
    # f.write('                    ItemText = str("%d_%s_NOTICE"%(MsgID,MsgName))
            dbInstance.close()
        return allColumnList
    def SetNetMsgCallback(self,msg_id,msg_sending,callback):
        global G_UIElementDictionary
        if msg_id not in self.netMsgFuncDict:
            self.netMsgFuncDict[msg_id] = {}
        self.netMsgFuncDict[msg_id][msg_sending] = callback
        if self.uiName is None or self.elementName is None:
            for uiName in G_UIElementDictionary.keys():
                for elementName in G_UIElementDictionary[uiName]:
                    if G_UIElementDictionary[uiName][elementName] is self:
                        self.uiName = uiName
                        self.elementName = elementName
                        return
    def ParseNetMsg(self,conn_socket,data_str):
        if self.netMsgTable:
            begin = data_str.find("\
            if begin >= 0 :
                data_split_array = data_str.split("\
                data_count = len(data_split_array)
                if data_str[-1]!="\\n":
                    data_count = data_count - 1
                    self.recvNetMsgDic[conn_socket] = data_split_array[-1]
                for data_index in range(data_count):
                    netmsg = data_split_array[data_index]
                    if netmsg:
                        if data_index == 0 and self.recvNetMsgDic[conn_socket]:
                            netmsg = self.recvNetMsgDic[conn_socket] + data_split_array[data_index]
                            self.recvNetMsgDic[conn_socket] = None
                        if netmsg.find(",") > 0:
                            netmsg_split = netmsg.split(",")
                            if len(netmsg_split) > 2:
                                if netmsg_split[0].isdigit() == False:
                                    return
                                if netmsg_split[1].isdigit() == False:
                                    return
                                msg_id = int(netmsg_split[0])
                                msg_sending = int(netmsg_split[1])
                                if msg_id in self.netMsgFuncDict:
                                    if msg_sending in self.netMsgFuncDict[msg_id]:
                                        self.netMsgFuncDict[msg_id][msg_sending](self.uiName,self.elementName,conn_socket,netmsg_split[2:])
                                    else:
                                        msg_sendingText = str(msg_sending)
                                        if msg_sending == 0:
                                            msg_sendingText = "'+Language.G_Language[1880]+'"
                                        elif msg_sending == 1:
                                            msg_sendingText = "'+Language.G_Language[1881]+'"
                                        elif msg_sending == 2:
                                            msg_sendingText = "'+Language.G_Language[1882]+'"
                                        msg = "'+Language.G_Language[1883]+'" + str(msg_id)+" : "+msg_sendingText
                                        self.Print(msg)
                            else:
                                msg = "'+Language.G_Language[1883]+'" + str(msg_id)
                                self.Print(msg)
            else:
                self.recvNetMsgDic[conn_socket] = self.recvNetMsgDic[conn_socket] + data_str
    def PackNetMsg(self,msg_id,msg_sending,paramList):
        data_str = str(msg_id)+","+str(msg_sending)
        paramIndex = 0
        for paramText in paramList:
            data_str = data_str + "," + paramText
            paramIndex = paramIndex + 1
        data_str = data_str + "\\n"
        return data_str
    def thread_Udp_recMsg(self):
        while True:
            if(self.stopFlag):
                break
            data_bytes, addr = self.socket.recvfrom(self.buffsize)
            if (data_bytes == b""):
                self.socket.close()
                self.stopFlag = True
                time.sleep(1)
                self.Print("'+Language.G_Language[1900]+':" + str(addr))
                index = 0
                for addr_saved in self.recvAddrList:
                    if addr_saved == addr:
                        self.recvAddrList.pop(index)
                    index = index + 1
                break
            msg = "'+Language.G_Language[1884]+':" + data_bytes.decode(self.encoding)
            self.Print(msg)
            if addr not in self.recvAddrList:
                self.recvAddrList.append(addr)
        self.socket.close()
        print("'+Language.G_Language[1901]+'")
    def thread_Tcp_Server(self):
        msg = "'+Language.G_Language[1887]+'"
        self.Print(msg)
        while True:
            if(self.stopFlag):
                break
            r_list, w_list, e_list = select.select(self.connSocketList, [], self.connSocketList, 1)
            for sk1_or_conn in r_list:
                if sk1_or_conn == self.socket:
                    conn, address = sk1_or_conn.accept()
                    self.connSocketList.append(conn)
                    self.recvMessageDic[conn] = []
                    self.recvNetMsgDic[conn] = ""
                    self.socketAddrDic[conn] = address
                    msg = "'+Language.G_Language[1888]+':" + str(address)
                    self.Print(msg)
                else:
                    try:
                        data_bytes = sk1_or_conn.recv(1024)
                        # 对方断开连接
                        if (data_bytes == b""):
                            sk1_or_conn.close()
                            self.connSocketList.remove(sk1_or_conn)
                            self.Print("'+Language.G_Language[1889]+'")
                            continue
                        data_str = str(data_bytes, encoding=self.encoding)
                        msg = "'+Language.G_Language[1890]+'["+str(self.socketAddrDic[sk1_or_conn])+"]:" + data_str
                        self.Print(msg)
                        self.ParseNetMsg(sk1_or_conn,data_str)
                        #sk1_or_conn.sendall(bytes(data_str, encoding=self.encoding))
                    except Exception as ex:
                        errorText = "'+Language.G_Language[1891]+'["+str(self.socketAddrDic[sk1_or_conn])+"]:" + str(ex)+",'+Language.G_Language[1892]+'"
                        self.Print(errorText)
                        self.connSocketList.remove(sk1_or_conn)
                    else:
                        data_str = str(data_bytes, encoding=self.encoding)
                        self.recvMessageDic[sk1_or_conn].append(data_str)

                for conn in w_list:
                    recv_str = self.recvMessageDic[conn][0]
                    del self.recvMessageDic[conn][0]
                    conn.sendall(bytes(recv_str, encoding=self.encoding))

                for sk in e_list:
                    self.connSocketList.remove(sk)
                    self.recvNetMsgDic.remove(sk)
        self.socket.close()
        self.connSocketList.clear()
        self.recvMessageDic.clear()
        print("'+Language.G_Language[1893]+'")
    def StopServer(self):
        """'+Language.G_Language[1255]+'"""
        self.stopFlag = True
    def ConnServer(self):
        """'+Language.G_Language[1256]+'"""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((self.ip, int(self.port)))
        except Exception as e :
            print(e)
            self.Print("'+Language.G_Language[1894]+'")
            self.stopFlag = True
            return
        else:
            self.recvNetMsgDic[self.socket] = ""
            self.Print("'+Language.G_Language[1895]+'")
            self.run_thread = threading.Thread(target=self.thread_Tcp_Client, args=[])
            self.run_thread.Daemon = True
            self.run_thread.start()  
    #Thread
    def thread_Tcp_Client(self):
        while True:
            if(self.stopFlag):
                break
            try:
                data_bytes = self.socket.recv(self.buffsize)
                if (data_bytes == b""):
                    self.socket.close()
                    self.stopFlag = True
                    time.sleep(1)
                    self.Print("'+Language.G_Language[1896]+'")
                    break
                data_str = data_bytes.decode(self.encoding)
                msg = "'+Language.G_Language[1884]+':" + data_str
                self.Print(msg)
                self.ParseNetMsg(self.socket,data_str)
            except Exception as ex:
                errorText = "'+Language.G_Language[1897]+':" + str(ex)
                self.Print(errorText)
        self.socket.close()
        print("'+Language.G_Language[1889]+'")
    def GetConnSocketList(self):
        """'+Language.G_Language[1257]+'"""
        return self.connSocketList
    def GetRecvAddrList(self):
        """'+Language.G_Language[1258]+'"""
        return self.recvAddrList
    def SendTcpMsgToClient(self,client,sndText):
        """'+Language.G_Language[1259]+'"""
        msg = sndText.encode(self.encoding)
        print("'+Language.G_Language[1259]+':"+sndText)
        client.send(msg)
    def SendTcpMsgToAllClient(self,sndText):
        """'+Language.G_Language[1260]+'"""
        msg = sndText.encode(self.encoding)
        print("'+Language.G_Language[1260]+':"+sndText)
        for client in self.connSocketList:
            client.send(msg)
    def SendTcpMsgToServer(self,sndText):
        """'+Language.G_Language[1261]+'"""
        msg = sndText.encode(self.encoding)
        print("'+Language.G_Language[1261]+':"+sndText)
        if self.socket:
            self.socket.send(msg)
        else:
            print("'+Language.G_Language[1843]+'")
    def SendUdpMsgToAddr(self,ip,port,sndText):
        """'+Language.G_Language[1262]+'"""
        msg = sndText.encode(self.encoding)
        print("'+Language.G_Language[1262]+':"+sndText)
        sendArr = (ip,port)
        if self.socket:
            self.socket.sendto(msg,sendArr)
        else:
            print("'+Language.G_Language[1843]+'")
    def SendUdpMsgToAllAddr(self,sndText):
        """'+Language.G_Language[1263]+'"""
        msg = sndText.encode(self.encoding)
        print("'+Language.G_Language[1263]+':"+sndText)
        for sendArr in self.recvAddrList:
            #sendArr = (ip,port)
            if self.socket:
                self.socket.sendto(msg,sendArr)
            else:
                print("'+Language.G_Language[1843]+'")
    def SendTcpRequestToClient(self,socket,msg_id,paramList):
        """'+Language.G_Language[1874]+'"""
        if type(paramList) == type(""):
            paramList = self.ConvertStringToParamList(paramList)
        sndText = self.PackNetMsg(msg_id,0,paramList)
        msg = sndText.encode(self.encoding)
        socket.send(msg)
    def SendTcpRequestToServer(self,msg_id,paramList):
        """'+Language.G_Language[1874]+'"""
        if type(paramList) == type(""):
            paramList = self.ConvertStringToParamList(paramList)
        sndText = self.PackNetMsg(msg_id,0,paramList)
        msg = sndText.encode(self.encoding)
        if self.socket:
            self.socket.send(msg)
        else:
            print("'+Language.G_Language[1843]+'")
    def SendTcpResponseToClient(self,socket,msg_id,paramList):
        """'+Language.G_Language[1875]+'"""
        if type(paramList) == type(""):
            paramList = self.ConvertStringToParamList(paramList)
        sndText = self.PackNetMsg(msg_id,1,paramList)
        msg = sndText.encode(self.encoding)
        socket.send(msg)
    def SendTcpResponseToServer(self,msg_id,paramList):
        """'+Language.G_Language[1875]+'"""
        if type(paramList) == type(""):
            paramList = self.ConvertStringToParamList(paramList)
        sndText = self.PackNetMsg(msg_id,1,paramList)
        msg = sndText.encode(self.encoding)
        if self.socket:
            self.socket.send(msg)
        else:
            print("'+Language.G_Language[1843]+'")
    def SendTcpNotice(self,msg_id,paramList):
        """'+Language.G_Language[1876]+'"""
        if type(paramList) == type(""):
            paramList = self.ConvertStringToParamList(paramList)
        sndText = self.PackNetMsg(msg_id,2,paramList)
        msg = sndText.encode(self.encoding)
        for client in self.connSocketList:
            client.send(msg)
    def SendUdpRequest(self,ip,port,msg_id,paramList):
        """'+Language.G_Language[1877]+'"""
        if type(paramList) == type(""):
            paramList = self.ConvertStringToParamList(paramList)
        sndText = self.PackNetMsg(msg_id,0,paramList)
        msg = sndText.encode(self.encoding)
        sendArr = (ip,port)
        if self.socket:
            self.socket.sendto(msg,sendArr)
        else:
            print("'+Language.G_Language[1843]+'")
    def SendUdpResponse(self,ip,port,msg_id,paramList):
        """'+Language.G_Language[1878]+'"""
        if type(paramList) == type(""):
            paramList = self.ConvertStringToParamList(paramList)
        sndText = self.PackNetMsg(msg_id,1,paramList)
        msg = sndText.encode(self.encoding)
        sendArr = (ip,port)
        if self.socket:
            self.socket.sendto(msg,sendArr)
        else:
            print("'+Language.G_Language[1843]+'")
    def SendUdpNotice(self,msg_id,paramList):
        """'+Language.G_Language[1879]+'"""
        if type(paramList) == type(""):
            paramList = self.ConvertStringToParamList(paramList)
        sndText = self.PackNetMsg(msg_id,2,paramList)
        msg = sndText.encode(self.encoding)
        for sendArr in self.recvAddrList:
            #sendArr = (ip,port)
            if self.socket:
                self.socket.sendto(msg,sendArr)
            else:
                print("'+Language.G_Language[1843]+'")
    def SetListBox(self,listBox):
        """'+Language.G_Language[1264]+'"""
        self.MsgListBox = listBox
    def Print(self,msgText):
        """'+Language.G_Language[1265]+'"""
        if self.MsgListBox is not None:
            self.MsgListBox.insert(tkinter.END, msgText)
''' 
    f.write(code)
#MQTT通讯
def WriteMQTT(f):
    code='''
class MQTT():
    """'+Language.G_Language[1795]+'"""
    def __init__(self,broker='',port=1383,username=None,password=None,keeplive=600,encoding='utf-8',block=False):
        super().__init__()
        self.MsgListBox = None
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message  = self.on_message
        self.client.on_disconnect = self.on_disconnect
        self.client.on_subscribe = self.on_subscribe
        self.client.on_unsubscribe = self.on_unsubscribe
        self.client.on_publish = self.on_publish
        self.ReceiveMsgCallBack = None
        self.DisconnectCallBack = None
        self.encoding = encoding
        self.Connect(broker,port,username,password,keeplive,block)
    def __exit__(self):
        if self.client:
            self.client.close()
            self.connected = False
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self.connected = True
            self.Print("'+Language.G_Language[9830]+'")
        else:
            self.Print("'+Language.G_Language[9831]+':rc="+str(rc))
    def on_message(self, client, userdata, msg):
        if self.ReceiveMsgCallBack is not None:
            self.ReceiveMsgCallBack(msg.topic,msg.payload)
        self.Print("'+Language.G_Language[9832]+'"+msg.topic+"'+Language.G_Language[9833]+'"+str(msg.payload.decode(self.encoding)))
    def on_disconnect(self, client, userdata, rc):
        self.connected = False
        if self.DisconnectCallBack is not None:
            self.DisconnectCallBack()    
        self.Print("'+Language.G_Language[9834]+'")
    def on_subscribe(self, client, userdata, mid, granted_qos):
        self.Print("'+Language.G_Language[9835]+'")
    def on_unsubscribe(self, client, userdata, mid):
        self.Print("'+Language.G_Language[9836]+'")
    def on_publish(self, client, userdata, mid):
        self.Print("'+Language.G_Language[9837]+'")
    def Connect(self,broker,port,username,password,keeplive,block):
        """'+Language.G_Language[9838]+'"""
        if username is not None and password is not None:
            self.client.username_pw_set(username,password)
        self.client.connect(broker,port,keeplive)
        if block:
            self.client.loop_forever()
        else:
            self.client.loop_start()
        self.connected = True
    def Disconnect(self):
        """'+Language.G_Language[9834]+'"""
        self.client.disconnect()
        self.connected = False
    def Subscribe(self,topic,qos=0):
        """'+Language.G_Language[9835]+'"""
        self.client.subscribe(topic,qos=0)
    def Unsubscribe(self,topic):
        """'+Language.G_Language[9836]+'"""
        self.client.unsubscribe(topic)
    def Publish(self,topic,msg,qos=0):
        """'+Language.G_Language[9837]+'"""
        self.client.publish(topic,msg,qos=0)
    def SetCallBack_onReceiveMsg(self,callBack):
        """'+Language.G_Language[9840]+'"""
        self.ReceiveMsgCallBack = callBack
    def SetCallBack_onDisconnect(self,callBack):
        """'+Language.G_Language[9841]+'"""
        self.DisconnectCallBack = callBack
    def SetListBox(self,listBox):
        """'+Language.G_Language[1264]+'"""
        self.MsgListBox = listBox
    def Print(self,msgText):
        """'+Language.G_Language[1265]+'"""
        try:
            if self.ReceiveMsgCallBack:
                self.ReceiveMsgCallBack(msgText)
            if self.MsgListBox is not None:
                self.MsgListBox.insert(tkinter.END, msgText)
            else:
                print(msgText)
        except Exception as Ex:
            print(msgText)
''' 
    f.write(code)
#SSH通讯
def WriteSSH(f):
    code='''
class SSH():
    """'+Language.G_Language[1791]+'"""
    def __init__(self,hostname='',port=22,username='',password='',encoding='utf-8'):
        super().__init__()
        self.MsgListBox = None
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.channel = None
        self.ReceiveMsgCallBack = None
        self.Connect(hostname,port,username,password,encoding)
    def __exit__(self):
        if self.client:
            self.client.close()
            if self.channel:
                self.channel.close()
                self.channel = None
            self.connected = False
    # f.write('    def Execute(self,command):
    # f.write('        """'+Language.G_Language[1818]+'"""
    # f.write('        if self.connected == True:
    # f.write('            stdin, stdout, stderr = self.client.exec_command(command)
    # f.write('            stdoutLines = stdout.readlines()
    # f.write('            for line in stdoutLines:
    # f.write('                self.Print(line.encode(self.encoding))
    # f.write('            stderrLines = stderr.readlines()
    # f.write('            for line in stderrLines:
    # f.write('                self.Print(line.encode(self.encoding))
    # f.write('        else:
    # f.write('            self.Print("'+Language.G_Language[1825]+'")
    #Thread
    def thread_read_data(self):
        try:
            lastline = ""
            while True:
                if(self.stopFlag):
                    break
                resp = self.channel.recv(1024)
                output = resp.decode(self.encoding)
                outputLines = output.split("\
                if lastline != "":
                    outputLines[0] = lastline + outputLines[0]
                    lastline = ""
                if  output.endswith('# ') or output.endswith('\:
                    pass
                else:
                    lastline = outputLines[-1]
                    outputLines.pop(-1)
                for line in outputLines:
                    self.Print(line)
            self.channel.close()
            self.channel = None
        except Exception as Ex:
            self.Print(Ex)
    def Connect(self,hostname='',port=22,username='',password='',encoding='utf-8'):
        """'+Language.G_Language[1832]+'"""
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.encoding = encoding
        self.stopFlag = False
        self.connected = False
        try:
            if self.hostname != '':
                self.client.connect(self.hostname,port=self.port ,username=self.username,password=self.password)
                self.channel = self.client.invoke_shell()
                self.run_thread = threading.Thread(target=self.thread_read_data, args=[])
                self.run_thread.Daemon = True
                self.run_thread.start()
                self.connected = True
                return True
        except paramiko.AuthenticationException as Ex:
            self.Print("'+Language.G_Language[1824]+'"+str(Ex))
        except Exception as Ex:
            self.Print(str(Ex))
        return False
    def SetCallBack_onReceiveMsg(self,callBack):
        """'+Language.G_Language[1837]+'"""
        self.ReceiveMsgCallBack = callBack
    def SendCmd(self,command,echoMode = False):
        """'+Language.G_Language[1818]+'"""
        if self.connected == True:
            if echoMode == True:
                self.channel.send('echo \"'+ command+'\"\
            else:
                self.channel.send(command+'\
        else:
            self.Print("'+Language.G_Language[1825]+'")
    def UpLoadFile(self,localpath,remotepath):
        """'+Language.G_Language[1819]+'"""
        if self.connected == True:
            sftp = self.client.open_sftp()
            #sftp = paramiko.SFTPClient.from_transport(self.client.get_transport())
            result = sftp.put(localpath,remotepath)
            sftp.close()
            return result
        else:
            self.Print("'+Language.G_Language[1825]+'")
            return None
    def DownLoadFile(self,remotepath,localpath):
        """'+Language.G_Language[1820]+'"""
        if self.connected == True:
            sftp = self.client.open_sftp()
            result = sftp.get(remotepath,localpath)
            sftp.close()
            return result
        else:
            self.Print("'+Language.G_Language[1825]+'")
            return None
    def GetCurrWorkDir(self):
        """'+Language.G_Language[1826]+'"""
        if self.connected == True:
            sftp = self.client.open_sftp()
            currPath = sftp.getcwd()
            sftp.close()
            return currPath
        else:
            self.Print("'+Language.G_Language[1825]+'")
            return None
    def ListDir(self,remotepath):
        """'+Language.G_Language[1821]+'"""
        if self.connected == True:
            sftp = self.client.open_sftp()
            fileList = sftp.listdir(remotepath)
            sftp.close()
            return fileList
        else:
            self.Print("'+Language.G_Language[1825]+'")
            return None
    def RemoveFile(self,remotepath):
        """'+Language.G_Language[1822]+'"""
        if self.connected == True:
            sftp = self.client.open_sftp()
            sftp.remove(remotepath)
            sftp.close()
        else:
            self.Print("'+Language.G_Language[1825]+'")
    def RenameFile(self,oldremotepath,newremotepath):
        """'+Language.G_Language[1827]+'"""
        if self.connected == True:
            sftp = self.client.open_sftp()
            sftp.rename(oldremotepath,newremotepath)
            sftp.close()
        else:
            self.Print("'+Language.G_Language[1825]+'")
    def CreateDir(self,remotepath):
        """'+Language.G_Language[1828]+'"""
        if self.connected == True:
            sftp = self.client.open_sftp()
            sftp.mkdir(remotepath)
            sftp.close()
        else:
            self.Print("'+Language.G_Language[1825]+'")
    def DeleteDir(self,remotepath):
        """'+Language.G_Language[1829]+'"""
        if self.connected == True:
            sftp = self.client.open_sftp()
            sftp.rmdir(remotepath)
            sftp.close()
        else:
            self.Print("'+Language.G_Language[1825]+'")
    def SetListBox(self,listBox):
        """'+Language.G_Language[1264]+'"""
        self.MsgListBox = listBox
    def Print(self,msgText):
        """'+Language.G_Language[1265]+'"""
        try:
            if self.ReceiveMsgCallBack:
                self.ReceiveMsgCallBack(msgText)
            if self.MsgListBox is not None:
                self.MsgListBox.insert(tkinter.END, msgText)
            else:
                print(msgText)
        except Exception as Ex:
            print(msgText)
    
''' 
    f.write(code)
#串口
def WriteSerial(f):
    code='''
class Serial():
    """'+Language.G_Language[1784]+'"""
    def __init__(self,serialport='',baudrate=9600,databit=8,parity=None,stopbit=None,readbufsize=4096,sendbufsize=4096,encoding='utf-8'):
        super().__init__()
        self.MsgListBox = None
        self.ReceiveMsgCallBack = None
        self.Connect(serialport,baudrate,databit,parity,stopbit,readbufsize,sendbufsize,encoding)
    def __exit__(self):
        self.stopFlag = True
    #Thread
    def thread_read_data(self):
        try:
            while True:
                if(self.stopFlag):
                    break
                read_data = self.ser.readline()
                msg = read_data.decode(self.encoding)
                self.Print(msg)
            self.ser.close()
            self.ser = None
        except Exception as e:
            self.Print(e)
    def ListPorts(self):
        """'+Language.G_Language[1838]+'"""
        return list(serial.tools.list_ports.comports())
    def Connect(self,serialport='',baudrate=9600,databit=8,parity=None,stopbit=None,readbufsize=4096,sendbufsize=4096,encoding='utf-8'):
        """'+Language.G_Language[1832]+'"""
        self.serialport = serialport
        beginIndex = self.serialport.find('COM')
        if beginIndex >= 0:
            endIndex = self.serialport.find(' ')
            if endIndex > 0:
                self.serialport = self.serialport[beginIndex:endIndex]
        self.baudrate = baudrate
        self.encoding = encoding
        self.stopFlag = False
        self.ser = None
        if self.serialport is not None and len(self.serialport) > 0:
            self.ser = serial.Serial(self.serialport,self.baudrate)
            try:
                self.ser.close()
                if databit == 7:
                    self.ser.bytesize = serial.SEVENBITS
                else:
                    self.ser.bytesize= serial.EIGHTBITS
                if parity == 'EVEN':
                    self.ser.parity = serial.PARITY_EVEN
                elif parity == 'ODD':
                    self.ser.parity = serial.PARITY_ODD
                else:
                    self.ser.parity = serial.PARITY_NONE
                if stopbit == 'ONE':
                    self.ser.stopbits = serial.STOPBITS_ONE
                elif stopbit == 'TWO':
                    self.ser.stopbits = serial.STOPBITS_TWO
                self.ser.read_buffer_size  = readbufsize
                self.ser.write_buffer_size = sendbufsize
                self.ser.read_buffer_size  = readbufsize
                self.ser.open()
                self.run_thread = threading.Thread(target=self.thread_read_data, args=[])
                self.run_thread.Daemon = True
                self.run_thread.start()
                return True
            except Exception as e:
                self.Print(e)
        return False
    def SetCallBack_onReceiveMsg(self,callBack):
        """'+Language.G_Language[1837]+'"""
        self.ReceiveMsgCallBack = callBack
    def Stop(self):
        """'+Language.G_Language[1252]+'"""
        self.stopFlag = True
    def SendData(self,sndText):
        """'+Language.G_Language[1266]+'"""
        if self.ser is not None and self.ser.is_open:
            msg = sndText.encode(self.encoding)
            print("'+Language.G_Language[1831]+'"+sndText)
            self.ser.write(msg)
            self.ser.flush()
    def SetListBox(self,listBox):
        """'+Language.G_Language[1264]+'"""
        self.MsgListBox = listBox
    def Print(self,msgText):
        """'+Language.G_Language[1265]+'"""
        try:
            if self.ReceiveMsgCallBack:
                self.ReceiveMsgCallBack(msgText)
            if self.MsgListBox is not None:
                self.MsgListBox.insert(tkinter.END, msgText)
            else:
                print(msgText)
        except Exception as Ex:
            print(msgText)
''' 
    f.write(code)
#USB
def WriteUSB(f):
    code='''
class USB():
    """'+Language.G_Language[1784]+'"""
    def __init__(self,readbufsize=4096,sendbufsize=4096,encoding='utf-8'):
        super().__init__()
        self.idVendor = None
        self.idProduct = None
        self.currDevice = None
        self.devicesList = []
        self.read_buffer_size  = readbufsize
        self.write_buffer_size = sendbufsize
        self.encoding = encoding
        self.MsgListBox = None
    # f.write('        self.ReceiveMsgCallBack = None
    def __exit__(self):
        self.stopFlag = True
    # f.write("    def DiscoverDevices(self,threadCallback=None):
    # f.write('        """'+Language.G_Language[9089]+'"""
    # f.write("        def DiscoverThread():
    # f.write("            self.devicesList = usb.core.find(find_all=True)
    # f.write("            for device in self.devicesList:
    # f.write('                print("Device VendorID=#%x,ProductID=#%x"%(hex(device.idVendor),hex(device.idProduct)))
    # f.write("            if threadCallback:
    # f.write("                threadCallback(self.devicesList)
    # f.write("        if threadCallback:
    # f.write("            t = threading.Thread(target=DiscoverThread)
    # f.write("            t.setDaemon(True)
    # f.write("            t.start()
    # f.write("        else:
    # f.write("            DiscoverThread()
    # f.write("        return self.devicesList
    # f.write('    #Thread
    # f.write('    def thread_read_data(self):
    # f.write('        try:
    # f.write('            while True:
    # f.write('                if(self.stopFlag):
    # f.write('                    break
    # f.write('                read_data = self.currDevice.read(0x82,self.read_buffer_size)
    # f.write('                msg = read_data.decode(self.encoding)
    # f.write('                self.Print(msg)
    # f.write('        except Exception as e:
    # f.write('            self.Print(e)
    def ListDevices(self):
        """'+Language.G_Language[1839]+'"""
        self.devicesList = usb.core.find(find_all=True)
        return self.devicesList
    def Connect(self,idVendor=None,idProduct=None,readbufsize=4096,sendbufsize=4096,encoding='utf-8'):
        """'+Language.G_Language[1840]+'"""
        self.currDevice = None
        if idVendor is not None and idProduct is not None:
            self.idVendor = idVendor
            self.idProduct = idProduct
            self.read_buffer_size  = readbufsize
            self.write_buffer_size = sendbufsize
            self.encoding = encoding
            self.currDevice = usb.core.find(idVendor = idVendor,idProduct = idProduct)
            if self.currDevice != None:
                self.currDevice.set_configuration()
                return True
        return False
    def Stop(self):
        """'+Language.G_Language[1252]+'"""
        self.stopFlag = True
    def ReadData(self,endPoint):
        """'+Language.G_Language[1841]+'"""
        if self.currDevice:
            read_data = self.currDevice.read(endPoint,self.read_buffer_size)
            msg = read_data.decode(self.encoding)
            self.Print(msg)
            return msg
        return None
    def SendData(self,endPoint,sndText):
        """'+Language.G_Language[1842]+'"""
        if self.currDevice:
            msg = sndText.encode(self.encoding)
            print("'+Language.G_Language[1831]+'"+sndText)
            write_len = self.currDevice.write(endPoint,sndText)
            return write_len
        return 0
    def SetListBox(self,listBox):
        """'+Language.G_Language[1264]+'"""
        self.MsgListBox = listBox
    def Print(self,msgText):
        """'+Language.G_Language[1265]+'"""
        try:
            if self.MsgListBox is not None:
                self.MsgListBox.insert(tkinter.END, msgText)
            else:
                print(msgText)
        except Exception as Ex:
            print(msgText)
''' 
    f.write(code)
#蓝牙
def WriteBluetooth(f):
    code='''
class Bluetooth():
    """'+Language.G_Language[1792]+'"""
    def __init__(self,encoding='utf-8'):
        self.encoding = encoding
        self.devicesList = []
        self.MsgListBox = None
        self.stopFlag = False
        self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.sock.settimeout(1)
        self.sock.bind(('',bluetooth.PORT_ANY))
        self.sock.listen(1)
        self.ReceiveMsgCallBack = None
    def __exit__(self):
        if self.sock:
            self.sock.close()
            self.sock = None
        self.stopFlag = True
    def DiscoverDevices(self,threadCallback=None):
        """'+Language.G_Language[9089]+'"""
        def DiscoverThread():
            self.devicesList = bluetooth.discover_devices()
            for device in self.devicesList:
                print("Device Name:",bluetooth.lookup_name(device),"(",device,")")
            if threadCallback:
                threadCallback(self.devicesList)
        if threadCallback:
            t = threading.Thread(target=DiscoverThread)
            t.setDaemon(True)
            t.start()
        else:
            DiscoverThread()
        return self.devicesList
    #Thread
    def thread_read_data(self):
        try:
            while True:
                if(self.stopFlag):
                    break
                read_data = self.sock.recv(1024)
                msg = read_data.decode(self.encoding)
                self.Print(msg)
            self.sock.close()
            self.sock = None
        except Exception as e:
            self.Print(e)
    def Connect(self,device_addr):
        """'+Language.G_Language[9088]+'"""
        self.sock.connect(device_addr)
        services = bluetooth.find_service(address=device_addr)
        for service in services:
            print("Service Name:",service["name"])
            print("Host:",service["host"])
            print("Description:",service["description"])
            print("Protocol:",service["protocol"])
            print("Port:",service["port"])
            print("Service Classes:",service["service-classes"])
            print()
        self.run_thread = threading.Thread(target=self.thread_read_data, args=[])
        self.run_thread.Daemon = True
        self.run_thread.start()
        return True
    def SetCallBack_onReceiveMsg(self,callBack):
        """'+Language.G_Language[1837]+'"""
        self.ReceiveMsgCallBack = callBack
    def Stop(self):
        self.stopFlag = True
    def SendData(self,sndText):
        msg = sndText.encode(self.encoding)
        self.sock.send(msg)
    def SetListBox(self,listBox):
        self.MsgListBox = listBox
    def Print(self,msgText):
        try:
            if self.ReceiveMsgCallBack:
                self.ReceiveMsgCallBack(msgText)
            if self.MsgListBox is not None:
                self.MsgListBox.insert(tkinter.END, msgText)
            else:
                print(msgText)
        except Exception as Ex:
            print(msgText)
''' 
    f.write(code)
#SMTP
def WriteSMTP(f):
    code='''
class SMTP():
    """'+Language.G_Language[1793]+'"""
    def __init__(self,server=None,port=0,email='',password=''):
        self.Login(server,port,email,password)
    def __exit__(self):
        smtp.quit()
    def Login(self,server=None,port=0,email='',password=''):
        """'+Language.G_Language[9090]+'"""
        self.server = server
        self.port = port
        self.email = email
        self.password = password
        self.smtp = None
        if self.server and port != 0:
            self.smtp = smtplib.SMTP(server,port)
            self.smtp.starttls()
            self.smtp.login(email,password)
    def SendMail(self,toMail,subject,content):
        """'+Language.G_Language[9091]+'"""
        if self.smtp:
            msg = MIMEMultipart()
            msg['From']=self.email
            msg['To']=toMail
            msg['Subject']=subject
            msg.attach(MIMEText(content,'plain'))
            smtp.send_message(msg)
    def Quit(self):
        """'+Language.G_Language[9092]+'"""
        smtp.quit()
''' 
    f.write(code)
#SMTP
def WriteDHT(f):
    code='''
class DHT():
    """'+Language.G_Language[1793]+'"""
    def __init__(self,sensor=Adafruit_DHT.DHT11,pin=4):
        self.sensor = sensor
        self.pin = pin
    def __exit__(self):
        smtp.quit()
    def Read(self):
        """'+Language.G_Language[9095]+'"""
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        return humidity,temperature
''' 
    f.write(code)
#浏览器
def WriteSelenium(f):
    code='''
class Selenium():
    """'+Language.G_Language[1790]+'"""
    def __init__(self,drivertype='',url='',headless=False,profile_dir='',proxy_path='',server_path=''):
        super().__init__()
        self.browser = None
        self.wait = None
        self.proxy = None
        if profile_dir != "":
            if profile_dir.find(":") < 0:
                profile_dir = os.path.join(os.getcwd(),profile_dir)
                profile_dir = profile_dir.replace("\\\\", "/")
            if os.path.exists(profile_dir) == False:
                os.mkdir(profile_dir)
        if proxy_path != "":
            if proxy_path.find(":") < 0:
                proxy_path = os.path.join(os.getcwd(),proxy_path)
                proxy_path = proxy_path.replace("\\\\", "/")
            if os.path.exists(proxy_path) == False:
                MessageBox("'+Language.G_Language[9865]+'")
        if server_path != "":
            if server_path.find(":") < 0:
                server_path = os.path.join(os.getcwd(),server_path)
                server_path = server_path.replace("\\\\", "/")
            if os.path.exists(server_path) == False:
                MessageBox("'+Language.G_Language[9866]+'")
        if drivertype == \'Chrome\':
            chrome_options = Options()
            if headless == True:
                # 使用headless无界面浏览器模式
    # f.write('                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument(\'--headless\')
                # 如果不加这个选项，有时定位会出现问题
                chrome_options.add_argument(\'--disable-gpu\')
            if profile_dir != "":
                chrome_options.add_argument(\'--user-data-dir=\'+profile_dir)
            if proxy_path:
                self.proxy_server = Server(proxy_path)
                self.proxy_server.start()
                self.proxy = self.proxy_server.create_proxy()
                proxy_caps = webdriver.DesiredCapabilities.CHROME
                proxy_caps['proxy'] = {
                    'httpProxy': self.proxy.proxy,
                    'ftpProxy': self.proxy.proxy,
                    'sslProxy': self.proxy.proxy,
                    'noProxy': '',
                    'proxyType': 'MANUAL',
                    'autodetect': False
                }
                chrome_options.add_argument('--proxy-server={host}:{port}'.format(host='localhost', port=self.proxy.port))
                proxy_option = f"--proxy-server={self.proxy.proxy}"
                chrome_options.add_argument('--proxy-server={0}'.format(self.proxy.proxy))
                chrome_options.add_argument('ignore-certificate-errors')
                chrome_options.add_argument(proxy_option)
                service = Service(server_path)
                self.browser  = webdriver.Chrome(service=service, options=chrome_options)
            else:
                self.browser  = webdriver.Chrome(options=chrome_options)
        elif drivertype == \'Firefox\':
            if profile_dir != "":
                firefox_profile = webdriver.FirefoxProfile(profile_dir)
                self.browser  = webdriver.Firefox(firefox_profile)
            else:
                self.browser  = webdriver.Firefox()
        elif drivertype == \'IE\':
            self.browser  = webdriver.Ie()
        elif drivertype == \'Edge\':
            self.browser  = webdriver.Edge()
        elif drivertype == \'Safari\':
            self.browser  = webdriver.Safari()
        elif drivertype == \'Opera\':
            self.browser  = webdriver.Safari()
        if self.browser:
            self.wait = WebDriverWait(self.browser,10,0.5)
            if url != \'\':
                if url.find("http://") < 0 and url.find("https://") < 0:
                    url = "http://"+url
                self.browser.get(url)
    def __exit__(self):
        self.Exit()
    def start_har(self, har_name="default"):
        """'+Language.G_Language[8241]+'"""
        if self.proxy:
            self.proxy.new_har(har_name, options={'captureHeaders': True, 'captureContent': True})
    def stop_har(self, save_path=None,shaixuan="",shaixuan1="sdasddadsf"):
        """'+Language.G_Language[8242]+'"""
        urls = []
        if self.proxy and hasattr(self.proxy, 'new_har'):
            har_data = self.proxy.har
            for entry in har_data['log']['entries']:
                _url = entry['request']['url']
                if shaixuan in _url or shaixuan1 in _url:
                    _response = entry['response']
                    _content = _response['content']
                    urls.append(_url)
                    if save_path:
                        with open(save_path, 'w', encoding='utf-8') as f:
                            f.write(str(_content))
                    self.proxy.new_har()
        return urls
    def Exit(self):
        """'+Language.G_Language[8243]+'"""
        if self.browser:
            self.browser.quit()
        if self.proxy_server:
            self.proxy_server.stop()
        self.browser = None
        self.proxy = None
        self.proxy_server = None
    def Open(self,url):
        """'+Language.G_Language[8237]+'"""
        if self.browser:
            self.browser.get(url)
    def GoToURL(self,url):
        """'+Language.G_Language[8237]+'"""
        if self.browser:
            self.browser.get(url)
    def Quit(self):
        """'+Language.G_Language[8201]+'"""
        if self.browser:
            self.browser.quit()
            self.browser = None
    def GetBrowser(self):
        """'+Language.G_Language[8202]+'"""
        if self.browser:
            return self.browser
        return None
    def GetBrowserName(self):
        """'+Language.G_Language[8203]+'"""
        if self.browser:
            return self.browser.name
        return None
    def GetURL(self):
        """'+Language.G_Language[8204]+'"""
        if self.browser:
            return self.browser.current_url
        return None
    def GetWebCode(self):
        """'+Language.G_Language[8205]+'"""
        if self.browser:
            return self.browser.page_source
        return None
    def GetTitle(self):
        """'+Language.G_Language[8206]+'"""
        if self.browser:
            return self.browser.title
        return None
    def Maximize(self):
        """'+Language.G_Language[8207]+'"""
        if self.browser:
            self.browser.maximize_window()
    def Minimize(self):
        """'+Language.G_Language[8208]+'"""
        if self.browser:
            self.browser.minimize_window()
    def SetBrowserSize(self,width,height):
        """'+Language.G_Language[8209]+'"""
        if self.browser:
            self.browser.set_window_size(width, height)
    def GoFront(self):
        """'+Language.G_Language[8210]+'"""
        if self.browser:
            self.browser.forword()
    def GoBack(self):
        """'+Language.G_Language[8211]+'"""
        if self.browser:
            self.browser.back()
    def Refresh(self):
        """'+Language.G_Language[8212]+'"""
        if self.browser:
            self.browser.refresh()
    def Close(self):
        """'+Language.G_Language[8213]+'"""
        if self.browser:
            self.browser.close()
    def ExecuteJS(self,JScode):
        """'+Language.G_Language[8214]+'"""
        if self.browser:
            self.browser.execute_script(JScode)
    def GetCookies(self,key=\'\'):
        """'+Language.G_Language[8215]+'"""
        if self.browser:
            if key != \'\':
                return self.browser.get_cookie(key)
            else:
                return self.browser.get_cookies()
        return None
    def AddCookie(self,key,value):
        """'+Language.G_Language[8238]+'"""
        if self.browser:
            if key != \'\':
                cookie = {}
                cookie[key] = value
                self.browser.add_cookie(cookie)
    def SetCookies(self,cookies={}):
        """'+Language.G_Language[8239]+'"""
        if self.browser:
            if cookies:
                self.browser.add_cookie(cookies)
    def DeleteCookies(self,key=\'\'):
        """'+Language.G_Language[8216]+'"""
        if self.browser:
            if key != \'\':
                self.browser.delete_cookie(key)
            else:
                self.browser.delete_all_cookies()
    def ImplicitlyWait(self,waitTime=5):
        """'+Language.G_Language[8240]+'"""
        if self.browser:
            self.browser.implicitly_wait(waitTime)
    def FindElement_By_ID(self,id,waitflag='presence'):
        """'+Language.G_Language[8217]+'"""
        try:
            if waitflag =='invisibility':
                element = self.wait.until(EC.invisibility_of_element_located((By.ID,id)))
            elif waitflag =='clickable':
                element = self.wait.until(EC.element_to_be_clickable((By.ID,id)))
            elif waitflag =='presence':
                element = self.wait.until(EC.presence_of_element_located((By.ID,id)))
            return element
        except:
            print("Can\'t find Element by id \""+id+"\"")
        return None
    def FindAllElement_By_ID(self,id):
        """'+Language.G_Language[8218]+'"""
        try:
            elementList = self.wait.until(EC.presence_of_all_elements_located((By.ID,id)))
            return elementList
        except:
            print("Can\'t find Element by id \""+id+"\"")
        return None
    def FindElement_By_Name(self,name,waitflag='presence'):
        """'+Language.G_Language[8219]+'"""
        try:
            if waitflag =='invisibility':
                element = self.wait.until(EC.invisibility_of_element_located((By.NAME,name)))
            elif waitflag =='clickable':
                element = self.wait.until(EC.element_to_be_clickable((By.NAME,name)))
            elif waitflag =='presence':
                element = self.wait.until(EC.presence_of_element_located((By.NAME,name)))
            return element
        except:
            print("Can\'t find Element by name \""+name+"\"")
        return None
    def FindAllElement_By_Name(self,name):
        """'+Language.G_Language[8220]+'"""
        try:
            elementList = self.wait.until(EC.presence_of_all_elements_located((By.NAME,name)))
            return elementList
        except:
            print("Can\'t find Element by name \""+name+"\"")
        return None
    def FindElement_By_TagName(self,tagName,waitflag='presence'):
        """'+Language.G_Language[8221]+'"""
        try:
            if waitflag =='invisibility':
                element = self.wait.until(EC.invisibility_of_element_located((By.TAG_NAME,tagName)))
            elif waitflag =='clickable':
                element = self.wait.until(EC.element_to_be_clickable((By.TAG_NAME,tagName)))
            elif waitflag =='presence':
                element = self.wait.until(EC.presence_of_element_located((By.TAG_NAME,tagName)))
            return element
        except:
            print("Can\'t find Element by tagName \""+tagName+"\"")
        return None
    def FindAllElement_By_TagName(self,tagName):
        """'+Language.G_Language[8222]+'"""
        try:
            elementList = self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,tagName)))
            return elementList
        except:
            print("Can\'t find Element by tagName \""+tagName+"\"")
        return None
    def FindElement_By_ClassName(self,className,waitflag='presence'):
        """'+Language.G_Language[8223]+'"""
        try:
            if waitflag =='invisibility':
                element = self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME,className)))
            elif waitflag =='clickable':
                element = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,className)))
            elif waitflag =='presence':
                element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,className)))
            return element
        except:
            print("Can\'t find Element by className \""+className+"\"")
        return None
    def FindAllElement_By_ClassName(self,className):
        """'+Language.G_Language[8224]+'"""
        try:
            elementList = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,className)))
            return elementList
        except:
            print("Can\'t find Element by className \""+className+"\"")
        return None
    def FindElement_By_CSS(self,selector,waitflag='presence'):
        """'+Language.G_Language[8225]+'"""
        try:
            if waitflag =='invisibility':
                element = self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR,className)))
            elif waitflag =='clickable':
                element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,className)))
            elif waitflag =='presence':
                element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,className)))
            return element
        except:
            print("Can\'t find Element by className \""+className+"\"")
        return None
    def FindAllElement_By_CSS(self,selector):
        """'+Language.G_Language[8226]+'"""
        try:
            elementList = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,className)))
            return elementList
        except:
            print("Can\'t find Element by className \""+className+"\"")
        return None
    def FindElement_By_XPath(self,xpath,waitflag='presence'):
        """'+Language.G_Language[8227]+'"""
        try:
            if waitflag =='invisibility':
                element = self.wait.until(EC.invisibility_of_element_located((By.XPATH,xpath)))
            elif waitflag =='clickable':
                element = self.wait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
            elif waitflag =='presence':
                element = self.wait.until(EC.presence_of_element_located((By.XPATH,xpath)))
            return element
        except:
            print("Can\'t find Element by xpath \""+xpath+"\"")
        return None
    def FindAllElement_By_XPath(self,xpath):
        """'+Language.G_Language[8228]+'"""
        try:
            elementList = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,xpath)))
            return elementList
        except:
            print("Can\'t find Element by xpath \""+xpath+"\"")
        return None
    def FindElement_By_LinkText(self,linktext,waitflag='presence'):
        """'+Language.G_Language[8229]+'"""
        try:
            if waitflag =='invisibility':
                element = self.wait.until(EC.invisibility_of_element_located((By.LINK_TEXT,linktext)))
            elif waitflag =='clickable':
                element = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,linktext)))
            elif waitflag =='presence':
                element = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT,linktext)))
            return element
        except:
            print("Can\'t find Element by link text \""+linktext+"\"")
        return None
    def FindAllElement_By_LinkText(self,linktext):
        """'+Language.G_Language[8230]+'"""
        try:
            elementList = self.wait.until(EC.presence_of_all_elements_located((By.LINK_TEXT,linktext)))
            return elementList
        except:
            print("Can\'t find Element by link text \""+linktext+"\"")
        return None
    def FindElement_By_ParitalLinkText(self,linktext,waitflag='presence'):
        """'+Language.G_Language[8231]+'"""
        try:
            if waitflag =='invisibility':
                element = self.wait.until(EC.invisibility_of_element_located((By.PARTIAL_LINK_TEXT,linktext)))
            elif waitflag =='clickable':
                element = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,linktext)))
            elif waitflag =='presence':
                element = self.wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,linktext)))
            return element
        except:
            print("Can\'t find Element by parital link text \""+linktext+"\"")
        return None
    def FindAllElement_By_ParitalLinkText(self,linktext):
        """'+Language.G_Language[8232]+'"""
        try:
            elementList = self.wait.until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT,linktext)))
            return elementList
        except:
            print("Can\'t find Element by parital link text \""+linktext+"\"")
        return None
    def GetActionChains(self):
        """'+Language.G_Language[8233]+'"""
        if self.browser:
            return ActionChains(self.browser)
        return None
    def RunAction(self,element,actionName,valueList=None):
        """'+Language.G_Language[8234]+'"""
        if self.browser:
            if actionName == "click":
                ActionChains(self.browser).click(element).perform()
            elif actionName == "click_and_hold":
                ActionChains(self.browser).click_and_hold(element).perform()
            elif actionName == "context_click":
                ActionChains(self.browser).context_click(element).perform()
            elif actionName == "double_click":
                ActionChains(self.browser).double_click(element).perform()
            elif actionName == "drag_and_drop":
                ActionChains(self.browser).drag_and_drop(element,valueList[0]).perform()
            elif actionName == "drag_and_drop_by_offset":
                ActionChains(self.browser).drag_and_drop_by_offset(element,valueList[0],valueList[1]).perform()
            elif actionName == "key_down":
                ActionChains(self.browser).key_down(valueList[0],element).perform()
            elif actionName == "key_up":
                ActionChains(self.browser).key_up(valueList[0],element).perform()
            elif actionName == "move_by_offset":
                ActionChains(self.browser).move_by_offset(valueList[0],valueList[1]).perform()
            elif actionName == "move_to_element":
                ActionChains(self.browser).move_to_element(valueList[0]).perform()
            elif actionName == "move_to_element_with_offset":
                ActionChains(self.browser).move_to_element_with_offset(valueList[0],valueList[1],valueList[2]).perform()
            elif actionName == "perform":
                ActionChains(self.browser).perform()
            elif actionName == "release":
                ActionChains(self.browser).release(element).perform()
            elif actionName == "send_keys":
                ActionChains(self.browser).send_keys(valueList).perform()
            elif actionName == "send_keys_to_element":
                ActionChains(self.browser).send_keys_to_element(element,valueList).perform()
    def AddActionToChains(self,element,actionName,valueList=None):
        """'+Language.G_Language[8235]+'"""
        if self.browser:
            if actionName == "click":
                ActionChains(self.browser).click(element)
            elif actionName == "click_and_hold":
                ActionChains(self.browser).click_and_hold(element)
            elif actionName == "context_click":
                ActionChains(self.browser).context_click(element)
            elif actionName == "double_click":
                ActionChains(self.browser).double_click(element)
            elif actionName == "drag_and_drop":
                ActionChains(self.browser).drag_and_drop(element,valueList[0])
            elif actionName == "drag_and_drop_by_offset":
                ActionChains(self.browser).drag_and_drop_by_offset(element,valueList[0],valueList[1])
            elif actionName == "key_down":
                ActionChains(self.browser).key_down(valueList[0],element)
            elif actionName == "key_up":
                ActionChains(self.browser).key_up(valueList[0],element)
            elif actionName == "move_by_offset":
                ActionChains(self.browser).move_by_offset(valueList[0],valueList[1])
            elif actionName == "move_to_element":
                ActionChains(self.browser).move_to_element(valueList[0])
            elif actionName == "move_to_element_with_offset":
                ActionChains(self.browser).move_to_element_with_offset(valueList[0],valueList[1],valueList[2])
            elif actionName == "release":
                ActionChains(self.browser).release(element)
            elif actionName == "send_keys":
                ActionChains(self.browser).send_keys(valueList)
            elif actionName == "send_keys_to_element":
                ActionChains(self.browser).send_keys_to_element(element,valueList)
    def PerformActionChains(self):
        """'+Language.G_Language[8236]+'"""
        if self.browser:
            ActionChains(self.browser).perform()
''' 
    f.write(code)
#打印机
def WritePrinter(f):
    code='''
class Printer():
    """'+Language.G_Language[1788]+'"""
    def __init__(self):
        self.PrinterName = win32print.GetDefaultPrinter()
        self.hPrinter = win32print.OpenPrinter(self.PrinterName)
    def EnumPrinters(self):
        """'+Language.G_Language[1267]+'"""
        return win32print.EnumPrinters(2)
    def PrintDocument(self,fileName):
        """'+Language.G_Language[1268]+'"""
        if os.path.exists(fileName) == True:
            ThePath, TheFile = os.path.split(fileName)
            if fileName.find(".py") > 0:
                f = open(fileName,'rb')
                content = f.read()
                f.close()
                import tempfile
                TempFileName = tempfile.mktemp (TheFile.replace('.py','.txt'))
                open (TempFileName, "wb").write (content)
                fileName = TempFileName
            try:
                hJob = win32print.StartDocPrinter(self.hPrinter, 1, ('PrintJobName', None, 'RAW'))
            except:
                pass
            try:
                win32api.ShellExecute(0, "print", fileName, TheFile, ".", 0)
                win32print.StartPagePrinter(self.hPrinter)
                win32print.EndPagePrinter(self.hPrinter)
                return True
            finally:
                win32print.EndDocPrinter(self.hPrinter)
        return False
    def PrintImage(self,fileName,HORZRES = 8,VERTRES = 10,LOGPIXELSX = 88,LOGPIXELSY = 90,PHYSICALWIDTH = 110,PHYSICALHEIGHT = 111,PHYSICALOFFSETX = 112,PHYSICALOFFSETY = 113):
        """'+Language.G_Language[1269]+'"""
        if os.path.exists(fileName) == True:
            try:
                hDC = win32ui.CreateDC ()
                hDC.CreatePrinterDC (self.PrinterName)
                printable_area = hDC.GetDeviceCaps (HORZRES), hDC.GetDeviceCaps (VERTRES)
                printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT)
                printer_margins = hDC.GetDeviceCaps (PHYSICALOFFSETX), hDC.GetDeviceCaps (PHYSICALOFFSETY)
                bmp = Image.open (fileName)
                ratios = [1.0 * printable_area[0] / bmp.size[0], 1.0 * printable_area[1] / bmp.size[1]]
                scale = min (ratios)
                hDC.StartDoc(fileName)
                hDC.StartPage()
                dib = ImageWin.Dib (bmp)
                scaled_width, scaled_height = [int (scale * i) for i in bmp.size]
                dib.draw (hDC.GetHandleOutput(), (0, 0, scaled_width, scaled_height))
                hDC.EndPage()
                hDC.EndDoc()
                hDC.DeleteDC()
                return True
            finally:
                return False
        return False
''' 
    f.write(code)
#定时器
def WriteTimer(f):
    code='''
class Timer():
    """'+Language.G_Language[1789]+'"""
    def __init__(self,Interval,callbackFunction):
        self.Interval = Interval
        self.Widget = None
        self.TimerIndex = 0
        self.TimeID = None
        self.Running = False
        self.CallBackFunction = callbackFunction
    def SetInterval(self,Interval):
        """'+Language.G_Language[1270]+'"""
        self.Interval = Interval
    def SetWidget(self,Widget):
        """'+Language.G_Language[1271]+'"""
        self.Widget = Widget
    def GetWidget(self):
        """'+Language.G_Language[1867]+'"""
        return self.Widget
    def Start(self):
        """'+Language.G_Language[1272]+'"""
        if self.Widget:
            self.TimerIndex = 0
            self.TimeID = self.Widget.after(self.Interval, lambda : self.Timer_CallBack(self.TimerIndex))
            self.Running = True
    def Stop(self):
        """'+Language.G_Language[1252]+'"""
        if self.Widget and self.Running == True:
            self.Running = False
            if self.TimeID:
                self.Widget.after_cancel(self.TimeID)
        self.TimeID = None

    def IsRunning(self):
        """'+Language.G_Language[1866]+'"""
        return self.Running
    def Timer_CallBack(self,TimerIndex):
        """Timer callback function"""
        if self.Widget and self.Running == True:
            self.CallBackFunction()
            self.TimerIndex = self.TimerIndex + 1
            self.TimeID = self.Widget.after(self.Interval, lambda : self.Timer_CallBack(self.TimerIndex))
''' 
    f.write(code)
#定时器
def WriteWMI(f):
    code='''
class WMI():
    """'+Language.G_Language[1796]+'"""
    def __init__(self):
        self.Wmi = wmi.WMI()
        self.CS = None
        self.OS = None
        self.CPU = None
        self.NetworkAdapter = None
        self.DiskList = None
        self.DisplayMonitorList = None
    def buildWMIInfo(self,infoType):
        if infoType == "CS" and self.CS is None:
           self.CS = self.Wmi.Win32_ComputerSystem()[0]
        elif infoType == "OS" and self.OS is None:
           self.OS = self.Wmi.Win32_OperatingSystem()[0]
        elif infoType == "CPU"  and self.CPU is None:
           self.CPU = self.Wmi.Win32_Processor()[0]
        elif infoType == "Network" and self.NetworkAdapter is None:
           self.NetworkAdapter = [_ for _ in self.Wmi.Win32_NetworkAdapterConfiguration() if _.MACAddress]
        elif infoType == "Disk" and self.DiskList is None:
           self.DiskList = [_ for _ in self.Wmi.Win32_DiskDrive() if _.InterfaceType != 'USB']
        elif infoType == "DisplayMonitor" and self.DisplayMonitorList is None:
           self.DisplayMonitorList = self.Wmi.Win32_DesktopMonitor()
    def GetComputerName(self):
        """'+Language.G_Language[6800]+'"""
        self.buildWMIInfo("CS")
        return self.CS.Caption
    def GetModelName(self):
        """'+Language.G_Language[6801]+'"""
        self.buildWMIInfo("CS")
        return self.CS.Model
    def GetNumberOfLogicalProcessors(self):
        """'+Language.G_Language[6802]+'"""
        self.buildWMIInfo("CS")
        return self.CS.NumberOfLogicalProcessors
    def GetNumberOfProcessors(self):
        """'+Language.G_Language[6803]+'"""
        self.buildWMIInfo("CS")
        return self.CS.NumberOfProcessors
    def GetUserName(self):
        """'+Language.G_Language[6804]+'"""
        self.buildWMIInfo("CS")
        return self.CS.UserName
    def GetWorkgroup(self):
        """'+Language.G_Language[6805]+'"""
        self.buildWMIInfo("CS")
        return self.CS.Workgroup
    def GetOSName(self):
        """'+Language.G_Language[6806]+'"""
        self.buildWMIInfo("OS")
        return self.OS.CSName
    def GetOSBuildNumber(self):
        """'+Language.G_Language[6807]+'"""
        self.buildWMIInfo("OS")
        return self.OS.BuildNumber
    def GetOSCaption(self):
        """'+Language.G_Language[6808]+'"""
        self.buildWMIInfo("OS")
        return self.OS.Caption
    def GetFreePhysicalMemory(self):
        """'+Language.G_Language[6809]+'"""
        self.buildWMIInfo("OS")
        return int(self.OS.FreePhysicalMemory)
    def GetFreeVirtualMemory(self):
        """'+Language.G_Language[6810]+'"""
        self.buildWMIInfo("OS")
        return int(self.OS.FreeVirtualMemory)
    def GetCPUCaption(self):
        """'+Language.G_Language[6811]+'"""
        self.buildWMIInfo("CPU")
        return self.CPU.Cpation
    def GetCPUDescription(self):
        """'+Language.G_Language[6812]+'"""
        self.buildWMIInfo("CPU")
        return self.CPU.Description
    def GetCPUName(self):
        """'+Language.G_Language[6813]+'"""
        self.buildWMIInfo("CPU")
        return self.CPU.Name

    def GetNetworkAdapterCount(self):
        """'+Language.G_Language[6814]+'"""
        self.buildWMIInfo("Network")
        return len(self.NetworkAdapter)
    def GetNetworkAdapter_Caption(self,ApaterIndex=0):
        """'+Language.G_Language[6815]+'"""
        self.buildWMIInfo("Network")
        return self.NetworkAdapter[ApaterIndex].Caption
    def GetNetworkAdapter_DefaultIPGateway(self,ApaterIndex=0):
        """'+Language.G_Language[6816]+'"""
        self.buildWMIInfo("Network")
        return self.NetworkAdapter[ApaterIndex].DefaultIPGetway
    def GetNetworkAdapter_DHCPEnable(self,ApaterIndex=0):
        """'+Language.G_Language[6817]+'"""
        self.buildWMIInfo("Network")
        return self.NetworkAdapter[ApaterIndex].DHCPEnable
    def GetNetworkAdapter_IPAddress(self,ApaterIndex=0):
        """'+Language.G_Language[6818]+'"""
        self.buildWMIInfo("Network")
        return self.NetworkAdapter[ApaterIndex].IPAddress
    def GetNetworkAdapter_IPEnabled(self,ApaterIndex=0):
        """'+Language.G_Language[6819]+'"""
        self.buildWMIInfo("Network")
        return self.NetworkAdapter[ApaterIndex].IPEnabled
    def GetNetworkAdapter_IPSubnet(self,ApaterIndex=0):
        """'+Language.G_Language[6820]+'"""
        self.buildWMIInfo("Network")
        return self.NetworkAdapter[ApaterIndex].IPSubnet
    def GetNetworkAdapter_MACAddress(self,ApaterIndex=0):
        """'+Language.G_Language[6821]+'"""
        self.buildWMIInfo("Network")
        return self.NetworkAdapter[ApaterIndex].MACAddres

    def GetDiskCount(self):
        """'+Language.G_Language[6822]+'"""
        self.buildWMIInfo("Disk")
        return len(self.DiskList)
    def GetDiskCapabilityDescript(self,DaskIndex):
        """'+Language.G_Language[6823]+'"""
        self.buildWMIInfo("Disk")
        return self.DiskList[DaskIndex].CapabilityDescriptions
    def GetDiskCaption(self,DaskIndex):
        """'+Language.G_Language[6824]+'"""
        self.buildWMIInfo("Disk")
        return self.DiskList[DaskIndex].Caption
    def GetDiskDescription(self,DaskIndex):
        """'+Language.G_Language[6825]+'"""
        self.buildWMIInfo("Disk")
        return self.DiskList[DaskIndex].Description
    def GetDiskInterfaceType(self,DaskIndex):
        """'+Language.G_Language[6826]+'"""
        self.buildWMIInfo("Disk")
        return self.DiskList[DaskIndex].InterfaceType
    def GetDiskMediaType(self,DaskIndex):
        """'+Language.G_Language[6827]+'"""
        self.buildWMIInfo("Disk")
        return self.DiskList[DaskIndex].MediaType
    def GetDiskModel(self,DaskIndex):
        """'+Language.G_Language[6828]+'"""
        self.buildWMIInfo("Disk")
        return self.DiskList[DaskIndex].Model
    def GetDiskPartitions(self,DaskIndex):
        """'+Language.G_Language[6829]+'"""
        self.buildWMIInfo("Disk")
        return self.DiskList[DaskIndex].Partitions
    def GetDiskSerialNumber(self,DaskIndex):
        """'+Language.G_Language[6830]+'"""
        self.buildWMIInfo("Disk")
        return self.DiskList[DaskIndex].SerialNumber
    def GetDiskSize(self,DaskIndex):
        """'+Language.G_Language[6831]+'"""
        self.buildWMIInfo("Disk")
        return self.DiskList[DaskIndex].Size

    def GetDisplayMonitorCount(self):
        """'+Language.G_Language[6832]+'"""
        self.buildWMIInfo("DisplayMonitor")
        return len(self.DisplayMonitorList)
    def GetDisplayMonitorDescription(self,MonitorIndex):
        """'+Language.G_Language[6833]+'"""
        self.buildWMIInfo("DisplayMonitor")
        return self.DisplayMonitorList[MonitorIndex].Description
    def GetDisplayMonitorType(self,MonitorIndex):
        """'+Language.G_Language[6834]+'"""
        self.buildWMIInfo("DisplayMonitor")
        return self.DisplayMonitorList[MonitorIndex].MonitorType
    def GetDisplayMonitorName(self,MonitorIndex):
        """'+Language.G_Language[6835]+'"""
        self.buildWMIInfo("DisplayMonitor")
        return self.DisplayMonitorList[MonitorIndex].Name
    def GetDisplayMonitorPixelsPerXLogicalInch(self,MonitorIndex):
        """'+Language.G_Language[6836]+'"""
        self.buildWMIInfo("DisplayMonitor")
        return self.DisplayMonitorList[MonitorIndex].PixelsPerXLogicalInch
    def GetDisplayMonitorPixelsPerYLogicalInch(self,MonitorIndex):
        """'+Language.G_Language[6837]+'"""
        self.buildWMIInfo("DisplayMonitor")
        return self.DisplayMonitorList[MonitorIndex].PixelsPerYLogicalInch
    def GetDisplayMonitorScreenWidth(self,MonitorIndex):
        """'+Language.G_Language[6838]+'"""
        self.buildWMIInfo("DisplayMonitor")
        return self.DisplayMonitorList[MonitorIndex].ScreenWidth
    def GetDisplayMonitorScreenHeight(self,MonitorIndex):
        """'+Language.G_Language[6839]+'"""
        self.buildWMIInfo("DisplayMonitor")
        return self.DisplayMonitorList[MonitorIndex].ScreenHeight

''' 
    f.write(code)
#多线程下载文件支持
def WriteDownLoadFileProgressDialog(f):
    code='''
#下载进度对话框
class   DownLoadFileProgressDialog:
    def __init__(self,uiName,showDialog = True,title='"+Language.G_Language[3240]+"',bgColor='#EFEFEF',fgColor='#000000'):
        self.FinishFlag = False
        self.LocalSaveFile = ""
        self.showDialog = showDialog
        if self.showDialog == True:
            self.root = GetElement(uiName,"root")
            self.Dialog = tkinter.Toplevel()
            self.Dialog.attributes("-toolwindow", 1)
            self.Dialog.resizable(0,0) 
            self.Dialog.wm_attributes("-topmost", 1)
            self.Title = title
            self.bgColor = bgColor
            self.fgColor = fgColor
            self.Dialog.title(self.Title)
            self.Form = tkinter.Canvas(self.Dialog,width = 280,height=140,bg = bgColor)
            self.Form.place(x=0, y=0,width=280,height=140)
            self.ShowDownLoadProgressDialog()
    #取得当前窗口句柄
    def GetWindHandle(self):
        _handle = None
        if self.showDialog == True:
            import win32gui
            _handle = win32gui.FindWindow(None,self.Title)
        return _handle
    def downloadFileFromURL(self,url,saveToDir=None,ReDownLoadIfExist = True,autoExtractZip = False,progressCallBack = None,finishCallBack = None,errorCallBack = None):
        """'+Language.G_Language[3241]+'"""
        global G_ResDir
        self.URLFile = url
        self.LocalDir = saveToDir
        self.autoExtractZip = autoExtractZip
        self.progressCallBack = progressCallBack
        self.errorCallBack = errorCallBack
        self.finishCallBack = finishCallBack
        projpath, resdirname = os.path.split(G_ResDir)
        _handle = self.GetWindHandle()
        WebSite, FileName = os.path.split(self.URLFile)
        if self.LocalDir:
            self.LocalSaveFile = os.path.join(self.LocalDir,FileName)
        else:
            self.LocalSaveFile = os.path.join(projpath,FileName)
        IsZipFile = False
        if FileName.find(".zip") > 0 :
            IsZipFile = True
        if os.path.exists(self.LocalSaveFile) == True:
            if ReDownLoadIfExist == True:
                os.remove(self.LocalSaveFile)
            else:
                if IsZipFile == True and self.autoExtractZip == True:
                    if self.LocalDir:
                        LocalDir, LocalFile = os.path.split(self.LocalDir)
                        self.extractZipFile(self.LocalSaveFile,LocalDir)
                    else:
                        self.extractZipFile(self.LocalSaveFile,projpath)
                return 
        try:
            resp = requests.get(self.URLFile,stream=True)
            total_length = int(resp.headers.get('content-length',0))
            def handle_ThreadDownload(theResp,theTotallength):
                if resp.status_code == 404:
                    if self.showDialog == True:
                        MessageBox("'+Language.G_Language[978]+'",_handle)
                    if self.errorCallBack:
                        self.errorCallBack(self.URLFile,1)
                    self.cancle()
                else:
                    step = int(theTotallength / 100)
                    if step < 320:
                        step = 320
                    maximum = int (theTotallength/step)
                    if maximum == 0:
                        maximum = 1
                    if self.showDialog == True:
                        self.ProgressBar['maximum'] = maximum
                    self.FinishFlag = False
                    if os.path.exists(self.LocalSaveFile) == False:
                        with open(self.LocalSaveFile, 'wb') as f:
                            progress = 0
                            for i in theResp.iter_content(chunk_size=step):  
                                f.write(i)
                                progress = progress + 1
                                if progress <= maximum:
                                    if self.showDialog == True:
                                        self.ProgressBar['value'] = progress
                                        self.TitleLabel.configure(text="'+Language.G_Language[3276]+'" + str("(%d%%)"%progress))
                                    if self.progressCallBack:
                                        self.progressCallBack(self.LocalSaveFile,progress)
                        #下载完毕后解压，并删除ZIP文件
                        if IsZipFile == True and self.autoExtractZip == True:
                            if self.showDialog == True:
                                self.TitleLabel.configure(text="'+Language.G_Language[3277]+'")
                            if self.LocalDir:
                                self.extractZipFile(self.LocalSaveFile,self.LocalDir)
                            else:
                                self.extractZipFile(self.LocalSaveFile,projpath)
                        else:
                            self.FinishFlag = True 
                            if self.showDialog == True:
                                self.TitleLabel.configure(text="'+Language.G_Language[3238]+'")
                                self.OKButton.configure(text="'+Language.G_Language[69]+'")
                            if self.finishCallBack:
                                self.finishCallBack(self.LocalSaveFile)
            self.run_thread_download = threading.Thread(target=handle_ThreadDownload, args=[resp,total_length])
            self.run_thread_download.Daemon = True
            self.run_thread_download.start() 
        except Exception as Ex:
            if self.errorCallBack:
                self.errorCallBack(self.URLFile,1)
            if self.showDialog == True:
                MessageBox(str(Ex),_handle)
    def downloadFilesFromURLList(self,urllist,saveToDir,ReDownLoadIfExist = True,progressCallBack = None,finishCallBack = None,errorCallBack = None):
        """'+Language.G_Language[3242]+'"""
        global G_ResDir
        self.URLFileList = urllist
        self.URLFile = ""
        self.LocalDir = saveToDir
        self.progressCallBack = progressCallBack
        self.errorCallBack = errorCallBack
        self.finishCallBack = finishCallBack
        self.FinishFlag = False
        projpath, resdirname = os.path.split(G_ResDir)
        _handle = self.GetWindHandle()
        if self.showDialog == True:
            self.ProgressBar[\'maximum\'] = len(urllist)
        try:
            def handle_ThreadDownloadFiles():
                progress = 0
                for url in self.URLFileList:
                    self.URLFile = url
                    resp = requests.get(self.URLFile,stream=True)
                    total_length = int(resp.headers.get(\'content-length\',0))
                    if resp.status_code == 404:
                        if self.showDialog == True:
                            MessageBox(self.URLFile+"'+Language.G_Language[978]+'",_handle)
                        if self.errorCallBack:
                            self.errorCallBack(self.URLFile,1)
                    else:
                        WebSite, FileName = os.path.split(self.URLFile)
                        if self.LocalDir:
                            self.LocalSaveFile = os.path.join(self.LocalDir,FileName)
                        else:
                            self.LocalSaveFile = os.path.join(projpath,FileName)
                        if os.path.exists(self.LocalSaveFile) == True:
                            if ReDownLoadIfExist == True:
                                 os.remove(self.LocalSaveFile)
                        if os.path.exists(self.LocalSaveFile) == False:
                            step = 1024   
                            with open(self.LocalSaveFile, \'wb\') as f:
                                for i in resp.iter_content(chunk_size=step):
                                    f.write(i)
                        progress = progress + 1
                        if self.showDialog == True:
                            self.ProgressBar[\'value\'] = progress
                            self.TitleLabel.configure(text="'+Language.G_Language[3240]+'" + str("(%d%%)"%progress))
                        if self.progressCallBack:
                            self.progressCallBack(self.LocalSaveFile,progress)
    
                self.FinishFlag = True 
                if self.showDialog == True:
                    self.TitleLabel.configure(text="'+Language.G_Language[3238]+'")
                    self.OKButton.configure(text="'+Language.G_Language[69]+'")
                if self.finishCallBack:
                    self.finishCallBack(self.LocalSaveFile)
            self.run_thread_download = threading.Thread(target=handle_ThreadDownloadFiles, args=[])
            self.run_thread_download.Daemon = True
            self.run_thread_download.start() 
        except Exception as Ex:
            if self.errorCallBack:
                self.errorCallBack(self.URLFile,1)
            if self.showDialog == True:
                MessageBox(str(Ex),_handle)
    #解压
    def extractZipFile(self,ZipFile,ExtractDir):
        _handle = self.GetWindHandle()
        try:
            block_size = 8192
            z = zipfile.ZipFile(ZipFile)
            namecount = len(z.namelist())
            if self.showDialog == True:
                self.ProgressBar['maximum'] = namecount
            nameindex = 0
            for zip_file in z.namelist():
                old_dir,old_fileName = os.path.split(zip_file)
                file_name = zip_file
                file_name_utf8 = file_name.encode(\'cp437\').decode(\'gbk\') 
    # f.write('                try:
    # f.write('                    file_name_utf8 = file_name.encode(\'cp437\').decode(\'gbk\') 
    # f.write('                except:
    # f.write('                    file_name_utf8 = filename.encode(\'utf-8\').decode(\'utf-8\')
    #f.write('                new_dir,new_fileName = os.path.split(file_name_utf8)
                progress = int(nameindex / namecount * 100)
                if self.showDialog == True:
                    self.TitleLabel.configure(text="'+Language.G_Language[3279]+'" + str("(%d%%)"%progress))
                entry_info = z.getinfo(file_name)
                i = z.open(file_name)
                print(file_name)
                if file_name[-1] != '/':
                    o = open(f"{ExtractDir}/{file_name_utf8}", "wb")
                    offset = 0
                    while True:
                        b = i.read(block_size)
                        offset += len(b)
                        if b == b'':
                            break
                        o.write(b)
                    o.close()
                else:
                    dir_name = os.path.dirname(file_name_utf8)
                    p = Path(f"{ExtractDir}/{file_name_utf8}")
                    p.mkdir(parents=True, exist_ok=True)
                i.close()
                nameindex = nameindex + 1
                if self.showDialog == True:
                    self.ProgressBar['value'] = nameindex
            z.close()
            if self.autoExtractZip == True:
                os.remove(ZipFile)
            self.FinishFlag = True  
            if self.showDialog == True:
                self.TitleLabel.configure(text="'+Language.G_Language[3239]+'")
                self.OKButton.configure(text="'+Language.G_Language[69]+'")
            if self.finishCallBack:
                self.finishCallBack(ExtractDir)
            return True
        except Exception as Ex:
            try:
                zip_1 = zipfile.ZipFile(ZipFile,'r')
                zip_1.extractall(path=ExtractDir)
                zip_1.close()
                os.remove(ZipFile)
                self.FinishFlag = True  
                if self.showDialog == True:
                    self.TitleLabel.configure(text="'+Language.G_Language[3239]+'")
                    self.OKButton.configure(text="'+Language.G_Language[69]+'")
                if self.finishCallBack:
                    self.finishCallBack(ExtractDir)
                return True
            except Exception as Ex:
                if self.showDialog == True:
                    MessageBox(str(Ex),_handle)
                if self.errorCallBack:
                    self.errorCallBack(self.LocalSaveFile,2)
                return False
    #确定TitleLabel
    def submit(self):
        if self.showDialog == True:
            _handle = self.GetWindHandle()
            if self.FinishFlag == False:
                if  AskBox("'+Language.G_Language[3275]+'",_handle) == False:
                    return 
                if self.LocalSaveFile:
                    if os.path.exists(self.LocalSaveFile) == True:
                        os.remove(self.LocalSaveFile)
            self.Dialog.destroy()
    #取消
    def cancle(self):
        if self.showDialog == True:
            self.Dialog.destroy()
    #显示设置列表
    def ShowDownLoadProgressDialog(self):
        if self.showDialog == True:
            self.TitleFont =tkinter.font.Font(family=\"Arial\", size=10,weight='normal',slant='roman',underline=0,overstrike=0)
            self.TitleLabel = tkinter.Label(self.Form,anchor = tkinter.W,bg=self.bgColor,fg=self.fgColor,font = self.TitleFont,text=self.Title,width = 100,height = 1)
            self.TitleLabel.place(x = 10,y = 10,width = 260,height = 24)
            self.ProgressBar = tkinter.ttk.Progressbar(self.Form, length=200, mode='determinate',style=\"TProgressbar\", orient=tkinter.HORIZONTAL)
            self.ProgressBar.place(x=10,y=40,width=260,height=15)
            self.ProgressBar['maximum'] = 100
            self.ProgressBar['value'] = 0
            self.OKButton = tkinter.Button(self.Form,anchor = tkinter.CENTER,text="'+Language.G_Language[70]+'",width = 100,height = 1,bg=self.bgColor,fg=self.fgColor,command=self.submit)
            self.OKButton.place(x = 180,y = 70,width = 80,height = 24) 
            #居中显示
            sx = self.root.winfo_x()
            sy = self.root.winfo_y()
            sw = self.root.winfo_width()
            sh = self.root.winfo_height()
            nx = sx + (sw - 280)/2
            ny = sy + (sh - 110)/2
            geoinfo = str('%dx%d+%d+%d'%(280,110,nx,ny))
            self.Dialog.geometry(geoinfo)   '''
    f.write(code)
