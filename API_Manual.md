# 

# **TKinterDesigner API Instruction**

| Author | Honghaier  |
| -------: | ---------- |
| Version | V1.4.8    |
| Last Update Date | 2021-06-12 |
| Twitter: | honghaier_2020@Honghaier_game |
| Email: | 285421210@qq.com |
| QQ Group | 100180960 |

WebSite:www.tkinterdesigner.com


GitHub: https://github.com/honghaier-game/TKinterDesigner.git 

## What's Fun.py？

​	Fun.py is a function library of  TkinterDesigner, which provides common functions to access UI controls and their properties. At the same time, it also contains some functions encapsulated by common functions..

## What are the functions of Fun.py ?

Tkinterdesigner v1.4.6 currently includes below functions:



1. **Register: Register a control in the control list.**

2. **GetElement: Access the control entity through the control name.**

3. **AddTKVariable: Add a tkinter variable to control.**

4. **SetTKVariable: Set the tkinter variable value of the control.**

5. **GetTKVariable: Get the tkinter variable value of the control.**

6. **AddUserData: Add a user data to control.**

7. **SetUserData: Set the user data value of the control.**

8. **GetUserData: Get the user data value of the control.**

9. **SetTKAttrib: Set the tkinter attribute value of the control.**

10. **GetTKAttrib: Get the tkinter attribute value of the control.**

11. **SetText: Set the text of the control.**

12. **GetText: Get the text of the control.**

13. **SetImage: Set the image of the control.**

14. **GetImage:Get the image of the control.**

15. **InitElementData:Initialize all control data.**

16. **InitElementStyle:Initialize all control style.**

17. **UpdateUIInputDataArray:Get all the entry data of an interface**

18. **CenterDlg:Center a pop-up interface dialog box**

19. **SetRoundedRectangle:Set the fillet properties of the control**

20. **ShowRoundedRectangle:Set the fillet property of the control immediately.**

21. **MessageBox:Pop up a message dialog box**

22. **InputBox:Pop up a input dialog box**

23. **AskBox:Pop up a question dialog box,You need choose yes or no.**

24. **WalkAllResFiles:Returns all the files in the directory**

25. **EventFunction_Adaptor:Redefine the event response function**

26. **SetControlPlace:Sets the absolute or relative position of the control**

27. **SetRootRoundRectangle:Set the fillet parameter of TK root, support cross platform. **

28. **ReadFromFile:Read content from file.** 

29. **WriteToFile:Writing content to a file.**

30. **ReadStyleFile:Read style file**



## Function explanation:

1. **Register**: To register a control is to bind the name to the control entity. If you want to access the control entity by name, it must be registered. Here, the param 'uiName' is used to distinguish the controls belonging to which interface instance. Because there may be multiple interfaces in the project, the UI name is used to distinguish them.

   `def Register(uiName,elementName,element):
       if uiName not in G_UIElementArray:
           G_UIElementArray[uiName]={}
       G_UIElementArray[uiName][elementName]=element`

   **Example:**

   `Fun.Register(className,'Form_1',Form_1)`

   

2. **GetElement**: Access the control entity through the control name.

   `def GetElement(uiName,elementName):
       global G_UIElementArray
       if uiName in G_UIElementArray:
           return G_UIElementArray[uiName][elementName]
       return None`

   **Example:**

   `Entry_3 = Fun.GetUIEle(className,'Entry_3 ')`

   

3. **AddTKVariable**: Add a tkinter variable to control.

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

   

4. **SetTKVariable**: Set the tkinter variable value of the control.

   `
   def SetTKVariable(uiName,elementName,value):
       if uiName in G_UIElementVariableArray:
           if elementName in G_UIElementVariableArray[uiName]:
               G_UIElementVariableArray[uiName][elementName].set(value)`

   Example:

   `Fun.SetTKVariable(className,'CheckButton_6',True)`

5. **GetTKAttrib:** Get the tkinter attribute value of the control.

   `def GetTKVariable(uiName,elementName):
       if uiName in G_UIElementVariableArray:
           if elementName in G_UIElementVariableArray[uiName]:
               return G_UIElementVariableArray[uiName][elementName].get()`

   **Example:**

   `CheckButton_6_Variable = Fun.GetTKVariable(className,'CheckButton_6')`

6. **AddUserData**: Add a user data to control.The parameter dataname is the data name and datatype is the data type, which can include int, float, string, list, dictionary, etc. generally, the control is operated by the right mouse button in the design software and set in the pop-up "bind data variable".The parameter datavalue is the data value, and ismaptotext is whether to directly reflect the data to the text variable of the control

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

7. **SetUserData: Set the user data value of the control.**

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

8. **GetUserData: Get the user data value of the control.**

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

9. **SetTKAttrib: Set the tkinter attribute value of the control.**

   `def SetTKAttrib(uiName,elementName,AttribName,attribValue):
       global G_UIElementArray
       if uiName in G_UIElementArray:
           if AttribName in G_UIElementArray[uiName][elementName].configure().keys():
               G_UIElementArray[uiName][elementName][AttribName]=attribValue` 

   **Example:**

   `Fun.SetTKAttrib(className,'Label_7','bg','#000000')`

   `Fun.SetTKAttrib(className,'Label_7','fg','#ffffff')`

10. **GetTKAttrib: Get the tkinter attribute value of the control.**

    `def GetTKAttrib(uiName,elementName,AttribName):
        global G_UIElementArray
        if uiName in G_UIElementArray:
            return G_UIElementArray[uiName][elementName].cget(AttribName)
        return None`

    **Example:**

    `bgColor = Fun.GetTKAttrib(className,'Label_7','bg')`

    `fgColor = Fun.GetTKAttrib(className,'Label_7','fg')`

11. **SetText: Set the text of the control(label, button, entry and text)**

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

12. **GetText: Get the text of the control.**

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

13. **SetImage: Set the image of the control(Label,Button).**

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

14. **GetImage: Get the image file path of the control(Label,Button).**

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

15. **InitElementData:Initialize all user binding data without manual call.**

    `def InitElementData(uiName):
        global G_UIElementUserDataArray
        if uiName in G_UIElementUserDataArray:
            for elementName in G_UIElementUserDataArray[uiName].keys():
                for EBData in G_UIElementUserDataArray[uiName][elementName]:
                    if EBData[3] == 1:
                        SetText(uiName,elementName,EBData[2])
                        SetText(uiName,elementName,EBData[2])`

    

16. **InitElementStyle:Initialize all control style without manual call. **

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

18. **CenterDlg:Center a pop-up interface dialog box,Center a pop-up interface dialog box. If the parameter does not specify the width and height, use the width and height of the dialog box itself. If it is used before registering root, that is, the main window root is in the center, the center of the windows screen is in the center.**

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

     

19. **SetRoundedRectangle:The rounded property of the control is called in the interface Layout Pyfile, but because the interface has not been created, it is necessary to call ShowRoundedRectangle two times later. Note: this function does not cross platform.**

    `def SetRoundedRectangle(control,WidthEllipse=20,HeightEllipse=20):
        if control != None:
           control.after(10, lambda: ShowRoundedRectangle(control,WidthEllipse,HeightEllipse))`

    **Example:**

    `SetRoundedRectangle(Button_2,20,20)`

20. **ShowRoundedRectangle: Set the fillet property of the control immediately.**

    `def ShowRoundedRectangle(control,WidthEllipse,HeightEllipse):
        import win32gui
        HRGN = win32gui.CreateRoundRectRgn(0,0,control.winfo_width(),control.winfo_height(),WidthEllipse,HeightEllipse)
        win32gui.SetWindowRgn(control.winfo_id(), HRGN,1)`

    **Example:**

    `Fun.ShowRoundedRectangle(Button_2,20,20)`

21. **MessageBox:Pop up a message dialog box**

    `def MessageBox(text):
        tkinter.messagebox.showwarning('info',text)`

    **Example:**

    `Fun.MessageBox("Thank you")`

22. **InputBox:Pop up a input dialog box**

    `def InputBox(title,text):
        res = tkinter.simpledialog.askstring(title,'Input Box',initialvalue=text)
        return res`

    **Example:**

    `Fun.InputBox("Please input the name")`

23. **AskBox:Pop up a question dialog box,You need choose yes or no.**

    `def AskBox(title,text):
        res = tkinter.messagebox.askyesno(title,text)
        return res`

    **Example:**

    `Result = Fun.AskBox("Are you sure to delete?")`

    `if Result == True:`

    ​	`....`

24. **WalkAllResFiles:Returns all the files in the directory**

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

25. **EventFunction_Adaptor:Redefine the event response function to have the specified parameter.**

    `def EventFunction_Adaptor(fun,  **params):
        return lambda event, fun=fun, params=params: fun(event, **params)`

    **Example:**

    `Button_7.configure(command=lambda:Project1_cmd.Button_7_onCommand(className,"Button_7"))`

26. **SetControlPlace:Sets the absolute or relative position of the control**

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

27. **SetRootRoundRectangle:Set the fillet parameter of TK root, support cross platform..**

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

28. **ReadFromFile:Read content from file.** 

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

29. **WriteToFile:Writing content to a file**

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

30. **ReadStyleFile:Read style file**

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
