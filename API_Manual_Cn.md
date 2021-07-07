# 

# **TKinterDesigner 函数说明**

| Author | Honghaier  |
| -------: | ---------- |
| Version | V1.5.1     |
| Last Update Date | 2021-07-06 |
| Twitter: | honghaier_2020@honghaier_game |
| Email: | 285421210@qq.com |
| QQ Group | 100180960 |

网址:www.tkinterdesigner.com


GitHub: https://github.com/honghaier-game/TKinterDesigner.git 

## Fun.py是什么？

Py是TkinterDesigner的函数库，它提供了访问UI控件及其属性的常用函数。同时，它还包含一些常用函数封装的函数。。

## Fun.py 包括哪些功能?

Tkinterdesigner v1.4.8 版本的API包括以下函数:



1. **Register: 在控件列表中注册控件。**

2. **GetElement: 通过控件名称访问控件实体.**

3. **AddTKVariable: 为控件增加tkinter变量.**

4. **SetTKVariable: 设置控件的tkinter变量.**

5. **GetTKVariable: 取得控件的tkinter变量.**

6. **AddUserData: 为控件增加用户自定义变量**

7. **SetUserData: 设置控件的用户自定义变量.**

8. **GetUserData: 取得控件的用户自定义变量.**

9. **SetTKAttrib: 设置控件的tkinter属性.**

10. **GetTKAttrib: 取得控件的tkinter属性.**

11. **SetText: 设置控件的文本属性.**

12. **GetText: 取得控件的文本字符串.**

13. **SetImage: 设置控件的背景图属性.**

14. **GetImage:取得控件的背景图文件名.****

15. **InitElementData:初始化界面各控件初始数据.**

16. **InitElementStyle:初始化界面各控件初始样式.**

17. **UpdateUIInputDataArray:取得对应界面对话框的所有输入数据值列表**

18. **CenterDlg:将一个对话框居中**

19. **SetRoundedRectangle:未初始化前调用设置控件的圆角属性，只限WINDOWS平台**

20. **ShowRoundedRectangle:立即设置控件的圆角属性，只限WINDOWS平台.**

21. **MessageBox:弹出一个信息对话框**

22. **InputBox:弹出一个输入对话框**

23. **AskBox:弹出一个选择对话框，你需要选择YES或NO.**

24. **WalkAllResFiles:返回对应目录的所有指定类型文件**

25. **EventFunction_Adaptor:重新定义消息映射函数，自定义参数**

26. **SetControlPlace:设置控件的绝对或相对位置**

27. **SetRootRoundRectangle:使用TKinter方式设置窗口圆角, 支持跨平台. **

28. **ReadFromFile:从一个文件中读取内容.** 

29. **WriteToFile:将内容写入到一个文件中.**

30. **ReadStyleFile:读取样式定义文件**



## 函数解析:

1. **Register**: 注册控件就是将名称绑定到控件实体。如果要按名称访问控制实体，则必须对其进行注册。这里，参数'uiName'用于区分属于哪个接口实例的控件。因为项目中可能有多个接口，所以使用UI名称来区分它们。

   `def Register(uiName,elementName,element):
       if uiName not in G_UIElementArray:
           G_UIElementArray[uiName]={}
       G_UIElementArray[uiName][elementName]=element`

   **Example:**

   `Fun.Register(className,'Form_1',Form_1)`

   

2. **GetElement**: 通过控件名称访问控件实体。

   `def GetElement(uiName,elementName):
       global G_UIElementArray
       if uiName in G_UIElementArray:
           return G_UIElementArray[uiName][elementName]
       return None`

   **Example:**

   `Entry_3 = Fun.GetUIEle(className,'Entry_3 ')`

   

3. **AddTKVariable**: 为控件增加tkinter变量.

   `def AddTKVariable(uiName,elementName,defaultValue = None):
       if uiName not in G_UIElementVariableArray:
           G_UIElementVariableArray[uiName]={}
       NameLower = elementName.lower()
       if NameLower.find('combobox_') >= 0:
           G_UIElementVariableArray[uiName][elementName]=tkinter.IntVar()
       elif NameLower.find('group_') >= 0:
           G_UIElementVariableArray[uiName][elementName]=tkinter.IntVar()
       elif NameLower.find('checkbutton_') >= 0:
           G_UIElementVariableArray[uiName][elementName]=tkinter.BooleanVar()
       else:
           G_UIElementVariableArray[uiName][elementName]=tkinter.StringVar()
       if defaultValue:
           G_UIElementVariableArray[uiName][elementName].set(defaultValue)
       return G_UIElementVariableArray[uiName][elementName]`

   **Example:**

   `CheckButton_6_Variable = Fun.AddTKVariable(className,'CheckButton_6')`

   `CheckButton_6_Variable.set(False)`

   

4. **SetTKVariable**: 设置控件的tkinter变量.

   `
   def SetTKVariable(uiName,elementName,value):
       if uiName in G_UIElementVariableArray:
           if elementName in G_UIElementVariableArray[uiName]:
               G_UIElementVariableArray[uiName][elementName].set(value)`

   Example:

   `Fun.SetTKVariable(className,'CheckButton_6',True)`

5. **GetTKAttrib:** 取得控件的tkinter变量.

   `def GetTKVariable(uiName,elementName):
       if uiName in G_UIElementVariableArray:
           if elementName in G_UIElementVariableArray[uiName]:
               return G_UIElementVariableArray[uiName][elementName].get()`

   **Example:**

   `CheckButton_6_Variable = Fun.GetTKVariable(className,'CheckButton_6')`

6. **AddUserData**: 为控件添加一个用户数据，参数dataname为数据名，datatype为数据类型，可以包括int、float、string、list、dictionary等，一般在设计软件中用鼠标右键操作控件，在弹出的“绑定数据”对话枉中设置，参数datavalue为数据值，而ismaptotext则是是否将数据直接反映到控件的text变量中

   `def AddUserData(uiName,elementName,dataName,datatype,datavalue,isMapToText):
       global G_UIElementUserDataArray
       if uiName not in G_UIElementUserDataArray:
           G_UIElementUserDataArray[uiName]={}
       if elementName not in G_UIElementUserDataArray[uiName]:
           G_UIElementUserDataArray[uiName][elementName]=[]
       G_UIElementUserDataArray[uiName][elementName].append([dataName,datatype,datavalue,isMapToText])`

   **Example:**

   `Fun.AddUserData(className,'Label_7','AAA','int',0,0)`

   `Fun.AddUserData(className,'Label_7','DDD','list',[],0)`

7. **SetUserData: 设置控件的用户数据值。**

   `def SetUserData(uiName,elementName,dataName,datavalue):
       global G_UIElementArray
       global G_UIElementUserDataArray
       if uiName in G_UIElementUserDataArray:
           if elementName in G_UIElementUserDataArray[uiName]:
               for EBData in G_UIElementUserDataArray[uiName][elementName]:
                   if EBData[0] == dataName:
                       EBData[2] = datavalue
                       if EBData[3] == 1:
                           SetText(uiName,elementName,datavalue)
                       return`

   Example:

   `Fun.AddUserData(className,'Label_7','AAA',888)`

8. **GetUserData: 获取控件的用户数据值。**

   `def GetUserData(uiName,elementName,dataName):
       global G_UIElementUserDataArray
       if  uiName in G_UIElementUserDataArray:
           if elementName in G_UIElementUserDataArray[uiName]:
               for EBData in G_UIElementUserDataArray[uiName][elementName]:
                   if EBData[0] == dataName:
                       if EBData[1]=='int':
                           return int(EBData[2])
                       elif EBData[1]=='float':
                           return float(EBData[2])
                       else:
                           return EBData[2]
       return None`

   Example:

   `aaa = Fun.GetUserData(className,'Label_7','AAA')`

9. **SetTKAttrib: 设置控件的tkinter属性值。**

   `def SetTKAttrib(uiName,elementName,AttribName,attribValue):
       global G_UIElementArray
       if uiName in G_UIElementArray:
           if AttribName in G_UIElementArray[uiName][elementName].configure().keys():
               G_UIElementArray[uiName][elementName][AttribName]=attribValue` 

   **Example:**

   `Fun.SetTKAttrib(className,'Label_7','bg','#000000')`

   `Fun.SetTKAttrib(className,'Label_7','fg','#ffffff')`

10. **GetTKAttrib: 获取控件的tkinter属性值。**

    `def GetTKAttrib(uiName,elementName,AttribName):
        global G_UIElementArray
        if uiName in G_UIElementArray:
            return G_UIElementArray[uiName][elementName].cget(AttribName)
        return None`

    **Example:**

    `bgColor = Fun.GetTKAttrib(className,'Label_7','bg')`

    `fgColor = Fun.GetTKAttrib(className,'Label_7','fg')`

11. **SetText: 设置控件的文本（标签、按钮、条目和文本）**

    `def SetText(uiName,elementName,textValue):
        global G_UIElementArray
        global G_UIElementVariableArray
        showtext = str("%s"%textValue)
        if uiName in G_UIElementVariableArray:
            if elementName in G_UIElementVariableArray[uiName]:
                G_UIElementVariableArray[uiName][elementName].set(showtext)
                return
        if uiName in G_UIElementArray:
            if elementName in G_UIElementArray[uiName]:
                if elementName.find('Text_') >= 0:
                    G_UIElementArray[uiName][elementName].delete('0.0',tkinter.END)
                    G_UIElementArray[uiName][elementName].insert(tkinter.END,showtext)
                else:
                    G_UIElementArray[uiName][elementName].configure(text=showtext)`

    **Example:**

    `Fun.SetText(className,'Label_2','Name')`

    `Fun.SetText(className,'Entry_3','Honghaier')`

12. **GetText: 获取控件的文本。**

    `def GetText(uiName,elementName):
        global G_UIElementArray
        global G_UIElementVariableArray
        if uiName in G_UIElementVariableArray:
            if elementName in G_UIElementVariableArray[uiName]:
                return G_UIElementVariableArray[uiName][elementName].get()
        if uiName in G_UIElementArray:
            if elementName in G_UIElementArray[uiName]:
                if elementName.find('Text_') >= 0:
                    return G_UIElementArray[uiName][elementName].get('0.0', tkinter.END)
                elif elementName.find('Spinbox_') >= 0:
                    return str(G_UIElementArray[uiName][elementName].get())
                else:
                    return G_UIElementArray[uiName][elementName].cget('text')
        return str("")`

    **Example:**

    `Name = Fun.GetText(className,'Entry_3')`

13. **SetImage: 设置控件的背景图像（标签、按钮）。**

    `def SetImage(uiName,elementName,imagePath):
        global G_UIElementVariableArray
        if elementName.find('Label_') == 0 or elementName.find('Button_') == 0 :
            Control = GetElement(uiName,elementName)
            if Control != None:
                if uiName in G_UIElementUserDataArray:
                    if elementName in G_UIElementUserDataArray[uiName]:
                        for EBData in G_UIElementUserDataArray[uiName][elementName]:
                            if EBData[0] == 'image':
                                EBData[1] = imagePath
                                from   PIL import Image,ImageTk
                                image=Image.open(imagePath).convert('RGBA')
                                image_Resize = image.resize((Control.winfo_width(), Control.winfo_height()),Image.ANTIALIAS)
                                EBData[2] = ImageTk.PhotoImage(image_Resize)
                                Control.configure(image = EBData[2])
                                return
                from   PIL import Image,ImageTk
                image=Image.open(imagePath).convert('RGBA')
                image_Resize = image.resize((Control.winfo_width(), Control.winfo_height()),Image.ANTIALIAS)
                EBData2 = ImageTk.PhotoImage(image_Resize)
                AddUserData(uiName,elementName,'image',imagePath,EBData2,0)
                Control.configure(image = EBData2)`

    **Example:**

    `Fun.SetImage(className,'Label_2','C:\\bg.jpg')`

14. **GetImage: 获取控件的背景图像文件（标签、按钮）。**

    `def GetImage(uiName,elementName):
        global G_UIElementVariableArray
        if elementName.find('Label_') == 0 or elementName.find('Button_') == 0 :
            Control = GetElement(uiName,elementName)
            if Control != None:
                if uiName in G_UIElementUserDataArray:
                    if elementName in G_UIElementUserDataArray[uiName]:
                        for EBData in G_UIElementUserDataArray[uiName][elementName]:
                            if EBData[0] == 'image':
                                return EBData[1]
        return str("")`

    **Example:**

    `bgImage = Fun.GetImage(className,'Label_2')`

15. **InitElementData:初始化界面各控件初始数据.**

    `def InitElementData(uiName):
        global G_UIElementUserDataArray
        if uiName in G_UIElementUserDataArray:
            for elementName in G_UIElementUserDataArray[uiName].keys():
                for EBData in G_UIElementUserDataArray[uiName][elementName]:
                    if EBData[3] == 1:
                        SetText(uiName,elementName,EBData[2])
                        SetText(uiName,elementName,EBData[2])`

    

16. **InitElementStyle:初始化界面各控件初始样式.**

    `def InitElementStyle(uiName,Style):
        StyleArray = ReadStyleFile(Style+".py")
        global G_UIElementArray
        if uiName in G_UIElementArray:
            for elementName in G_UIElementArray[uiName].keys():
                Widget = G_UIElementArray[uiName][elementName]
                try:
                    if  Widget.winfo_exists() == 1:
                        WinClass = Widget.winfo_class()
                        StyleName = ".T"+WinClass
                        if  StyleName == '.TLabel':
                            Root = GetElement(uiName,'root')
                            Root['background'] = StyleArray[StyleName]['background']
                        for attribute in StyleArray[StyleName].keys():
                            Widget[attribute] = StyleArray[StyleName][attribute]
                except BaseException:
                    continue`

17. **UpdateUIInputDataArray:Get all the entry data of an interface**

    `def  GetInputDataArray(uiName):
        global G_UIElementArray
        global G_UIInputDataArray
        global G_UIElementVariableArray
        G_UIInputDataArray.clear()
        if uiName in G_UIElementArray:
            for elementName in G_UIElementArray[uiName].keys():
                G_UIInputDataArray[elementName] = []
                Widget = G_UIElementArray[uiName][elementName]
                if elementName.find('Text_') >= 0:
                    content = Widget.get('0.0', tkinter.END)
                    G_UIInputDataArray[elementName].append(content)
                elif elementName.find('Entry_') >= 0:
                    content = G_UIElementVariableArray[uiName][elementName].get()
                    G_UIInputDataArray[elementName].append(content)
        if uiName in G_UIElementVariableArray:
            for elementName in G_UIElementVariableArray[uiName].keys():
               if elementName.find('Group_') >= 0:
                    ElementIntValue = G_UIElementVariableArray[uiName][elementName].get()
                    G_UIInputDataArray[elementName] = []
                    G_UIInputDataArray[elementName].append(ElementIntValue)
        return G_UIInputDataArray`

    **Example:**

    `import RegDlg`

     `RegDlg.RegDlg(topLevel)`

     `tkinter.Tk.wait_window(topLevel)`

     `InputDataArray = RegDlg.Fun.G_UIInputDataArray`

     `print(InputDataArray)`

     `print('Name:'+InputDataArray['Entry_5'][0])`

18. **CenterDlg:将弹出界面对话框居中，将弹出界面对话框居中。如果参数未指定宽度和高度，请使用对话框本身的宽度和高度。如果在注册Tk root之前使用，即主窗口根在中间，则windows屏幕的中心在中间。**

    `def CenterDlg(uiName,popupDlg,dw=0,dh=0):
        if dw == 0:
            dw = popupDlg.winfo_width()
        if dh == 0:
            dh = popupDlg.winfo_height()
        root = GetElement(uiName,'root')
        if root != None:
           sw = root.winfo_width()
           sh = root.winfo_height()
           sx = root.winfo_x()
           sy = root.winfo_y()
           popupDlg.geometry('%dx%d+%d+%d'%(dw,dh,sx+(sw-dw)/2,sy+(sh-dh)/2))
        else:
           import ctypes
           user32 = ctypes.windll.user32
           sw = user32.GetSystemMetrics(0)
           sh = user32.GetSystemMetrics(1)
           sx = 0
           sy = 0
           popupDlg.geometry('%dx%d+%d+%d'%(dw,dh,sx+(sw-dw)/2,sy+(sh-dh)/2))` 

    **Example:**

     `Fun.CenterDlg(uiName,popDlg)`

     

19. **SetRoundedRectangle:在界面布局文件中调用设置控件的圆角属性，但由于尚未创建接口，因此有必要在两次之后调用ShowRoundedRectangle。注意：此功能不跨平台。**

    `def SetRoundedRectangle(control,WidthEllipse=20,HeightEllipse=20):
        if control != None:
           control.after(10, lambda: ShowRoundedRectangle(control,WidthEllipse,HeightEllipse))`

    **Example:**

    `SetRoundedRectangle(Button_2,20,20)`

20. **ShowRoundedRectangle: 立即设置控件的圆角属性。**

    `def ShowRoundedRectangle(control,WidthEllipse,HeightEllipse):
        import win32gui
        HRGN = win32gui.CreateRoundRectRgn(0,0,control.winfo_width(),control.winfo_height(),WidthEllipse,HeightEllipse)
        win32gui.SetWindowRgn(control.winfo_id(), HRGN,1)`

    **Example:**

    `Fun.ShowRoundedRectangle(Button_2,20,20)`

21. **MessageBox:弹出一个信息对话框**

    `def MessageBox(text):
        tkinter.messagebox.showwarning('info',text)`

    **Example:**

    `Fun.MessageBox("Thank you")`

22. **InputBox:弹出一个输入对话框**

    `def InputBox(title,text):
        res = tkinter.simpledialog.askstring(title,'Input Box',initialvalue=text)
        return res`

    **Example:**

    `Fun.InputBox("Please input the name")`

23. **AskBox:弹出一个选择对话框，你需要选择YES或NO.**

    `def AskBox(title,text):
        res = tkinter.messagebox.askyesno(title,text)
        return res`

    **Example:**

    `Result = Fun.AskBox("Are you sure to delete?")`

    `if Result == True:`

    ​	`....`

24. **WalkAllResFiles:返回对应目录的所有指定类型文件**

    `def WalkAllResFiles(parentPath,alldirs=True,extName=None):
        ResultFilesArray = []
        if os.path.exists(parentPath) == True:
            for fileName in os.listdir(parentPath):
                if '__pycache__' not in fileName:
                    if '.git' not in fileName:
                        newPath = parentPath +'\\'+ fileName
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
                                file_extName_lower = extName.lower().strip()
                                if file_extension_lower == file_extName_lower:
                                    ResultFilesArray.append(newPath)
        return ResultFilesArray`

    **Example:**

    `jsonFileArray = Fun.WalkAllResFiles(path,False,'json')`

25. **EventFunction_Adaptor:重新定义消息映射函数，自定义参数**

    `def EventFunction_Adaptor(fun,  **params):
        return lambda event, fun=fun, params=params: fun(event, **params)`

    **Example:**

    `Button_7.configure(command=lambda:Project1_cmd.Button_7_onCommand(className,"Button_7"))`

26. **SetControlPlace:设置控件的绝对或相对位置**

    `def SetControlPlace(control,x,y,w,h):
        control.place(x=0,y=0,width=0,height=0)
        control.place(relx=0,rely=0,relwidth=0,relheight=0)
        if type(x) == type(1.0):
            if type(y) == type(1.0):
                if type(w) == type(1.0):
                    if type(h) == type(1.0):
                       control.place(relx=x,rely=y,relwidth=w,relheight=h)
                    else:
                       control.place(relx=x,rely=y,relwidth=w,height=h)
                else:
                    if type(h) == type(1.0):
                       control.place(relx=x,rely=y,width=w,relheight=h)
                    else:
                       control.place(relx=x,rely=y,width=w,height=h)
            else:
                if type(w) == type(1.0):
                    if type(h) == type(1.0):
                       control.place(relx=x,y=y,relwidth=w,relheight=h)
                    else:
                       control.place(relx=x,y=y,relwidth=w,height=h)
                else:
                    if type(h) == type(1.0):
                       control.place(relx=x,y=y,relwidth=w,relheight=h)
                    else:
                       control.place(relx=x,y=y,relwidth=w,height=h)
        else:
            if type(y) == type(1.0):
                if type(w) == type(1.0):
                    if type(h) == type(1.0):
                       control.place(x=x,rely=y,relwidth=w,relheight=h)
                    else:
                       control.place(x=x,rely=y,relwidth=w,height=h)
                else:
                    if type(h) == type(1.0):
                       control.place(x=x,rely=y,width=w,relheight=h)
                    else:
                       control.place(x=x,rely=y,width=w,height=h)
            else:
                if type(w) == type(1.0):
                    if type(h) == type(1.0):
                       control.place(x=x,y=y,relwidth=w,relheight=h)
                    else:
                       control.place(x=x,y=y,relwidth=w,height=h)
                else:
                    if type(h) == type(1.0):
                       control.place(x=x,y=y,width=w,relheight=h)
                    else:
                       control.place(x=x,y=y,width=w,height=h)`

    **Example:**

    `Fun.SetControlPlace(Button_1,10,10,100,24)`

27. **SetRootRoundRectangle:使用TKinter方式设置窗口圆角, 支持跨平台. **

    `def SetRootRoundRectangle(canvas,x1, y1, x2, y2, radius=25,**kwargs):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,`

    `return canvas.create_polygon(points, **kwargs, smooth=True)`

    **Example:**

    `Fun.SetControlPlace(Button_1,10,10,100,24)`

28. **ReadFromFile:从一个文件中读取内容.** 

    `def ReadFromFile(filePath):
        content = None
        if filePath != None:
            if os.path.exists(filePath) == True:
                f = open(filePath,mode='r',encoding='utf-8')
                if f != None:
                    content = f.read()
                    f.close()
        return content`

    **Example:**

    `content = Fun.ReadFromFile('test.txt')`

    `print(content)`

29. **WriteToFile:将内容写入到一个文件中.**

    `def WriteToFile(filePath,content):
        if filePath != None:
            f = open(filePath,mode='w',encoding='utf-8')
            if f != None:
                if content != None:
                    f.write(content)
                f.close()
                return True
        return False`

    **Example:**

    `content = "welcome to use tkinter designer." `

    `Fun.WriteToFile('test.txt',content)`

30. **ReadStyleFile:读取样式定义文件，返回样式列表**

    `def ReadStyleFile(filePath):
        StyleArray = {}
        if len(filePath)==0 :
            return StyleArray
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
                    stylename = splitarray2[0].replace('"','')
                else:
                    splitarray2 = splitarray1[2].partition(')')
                    stylename = splitarray2[0].replace('"','')
                sytleValueText = splitarray2[2]
                fontindex_begin = sytleValueText.find('font=(')
                fontindex_end = fontindex_begin
                StyleArray[stylename] = {}
                othertext = sytleValueText
                if fontindex_begin >= 0:
                    fontindex_end = sytleValueText.find(')')
                    fonttext = sytleValueText[fontindex_begin+6:fontindex_end]
                    fontsplitarray = fonttext.split(',')
                    StyleArray[stylename]['font'] = tkinter.font.Font(family=fontsplitarray[0].replace('"','').strip(), size=int(fontsplitarray[1].replace('"','').strip()),weight=fontsplitarray[2].replace('"','').strip())
                    othertext = sytleValueText[0:fontindex_begin] + sytleValueText[fontindex_end+1:-1]
                else:
                    splitarray4 = sytleValueText.partition(')')
                    othertext = splitarray4[0]
                splitarray3 = othertext.split(',')
                for stylecfgtext in splitarray3:
                    if stylecfgtext.find('=') > 0:
                        splitarray4 = stylecfgtext.partition('=')
                        key = splitarray4[0].replace('"','').strip()
                        value = splitarray4[2].replace('"','').strip()
                        StyleArray[stylename][key] = value
                continue
            if text.find('style.map(') >= 0:
                continue
        f.close()
        return StyleArray`

    **Example:**

    `StyleArray= ReadStyleFile('Project1_sty.py')`





​		
