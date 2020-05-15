#Author: Honghaier Description: a small pygame engine frame.
import os
from   os.path import abspath, dirname
import glob
import pygame
from   pygame.locals import *
BorderVisible = False
BorderColor = [255,0,0]
gameAppInstance = None
class ActionAnimation(pygame.sprite.Sprite):
    def __init__(self, imagesArray,callbackfun,callbackparam):
        super(ActionAnimation, self).__init__()
        self.imagesArray = imagesArray
        self.callbackfun = callbackfun
        self.callbackparam = callbackparam
        self.frameCount = len(self.imagesArray)
        self.index = 0
        self.u_add = 0
        self.v_add = 0
        self.scale = 1.0
        self.rotate = 0.0
        self.flipx = False
        self.flipy = False
        self.rect = self.imagesArray[0].get_rect()
        self.image = self.imagesArray[0]
        self.framedelay_changeframe = 0.5
        self.framedelay_time = 0.0
        self.time_passed_last = 0.0
    def update(self):
        if self.index >= self.frameCount:
            if self.callbackfun is not None:
                self.callbackfun(self.callbackparam)
            self.index = 0
        tempImage = self.imagesArray[self.index]   
        if self.flipx == True or self.flipy == True:
            tempImage = pygame.transform.flip(self.imagesArray[self.index], self.flipx , self.flipy)
        if self.rotate != 0.0 and self.scale != 0.0:
            self.image = pygame.transform.rotazoom(tempImage, self.rotate,self.scale)
        elif self.rotate != 0.0:
            self.image = pygame.transform.rotate(tempImage, self.rotate)  
        elif self.scale != 0.0:
            self.image = pygame.transform.smoothscale(tempImage, (int(self.rect.width * self.scale),int(self.rect.height * self.scale)))
        else:
            self.image = tempImage
        #计时
        if self.frameCount > 1:
            time_passed = pygame.time.get_ticks()
            time_delay = time_passed - self.time_passed_last
            self.time_passed_last = time_passed
            self.framedelay_time += time_delay
            if self.framedelay_time > self.framedelay_changeframe:
                self.index += 1
                self.framedelay_time = self.framedelay_time - self.framedelay_changeframe
    def draw(self,screen):
        global BorderVisible
        global BorderColor
        screen.blit(self.image, self.rect)
        if BorderVisible == True:
            pygame.draw.rect(screen,BorderColor,self.rect,3)
    def GetFrameCount(self):
        return self.frameCount
    def SetFrameDelay(self,delay):
        self.framedelay_changeframe = delay
    def GetFrameDelay(self):
        return self.framedelay_changeframe
    def GetImageSize(self):
        if self.image is not None:
            rect = self.image.get_rect()
            return rect.width,rect.height
        return 0,0
    def GetImageRect(self):
        if self.image is not None:
            return self.image.get_rect()
        return pygame.Rect(0, 0, 0, 0)
    def GetX(self):
        return self.rect.x
    def SetX(self, value):
        self.rect.x = value
    X = property(GetX, SetX)
    def GetY(self):
        return self.rect.y
    def SetY(self, value):
        self.rect.y = value
    Y = property(GetY, SetY)
    def GetXY(self):
        return self.rect.topleft
    def SetXY(self, x,y):
        self.rect.x = x
        self.rect.y = y
    def GetScale(self):
        return self.scale
    def SetScale(self, value):
        self.scale = value  
    S = property(GetScale, SetScale)
    def GetRotate(self):
        return self.rotate
    def SetRotate(self, value):
        self.rotate = value  
    R = property(GetRotate, SetRotate)
    def GetFlipX(self):
        return self.flipx
    def SetFlipX(self, value):
        self.flipx = value
    FX = property(GetFlipX, SetFlipX)
    def GetFlipY(self):
        return self.flipy
    def SetFlipY(self, value):
        self.flipy = value
    FY = property(GetFlipY, SetFlipY)
class  ActionSprite():
    def __init__(self, actionAnimation):
        self.ActionAnimation = actionAnimation
        if self.ActionAnimation.GetFrameCount() > 1:
            self.SpriteGroup = pygame.sprite.Group(actionAnimation)
        else:
            self.SpriteGroup = None
    def update(self):
        if self.ActionAnimation.GetFrameCount() > 1:
            self.SpriteGroup.update()
        else:
            self.ActionAnimation.update()
    def draw(self,screen):
        if self.ActionAnimation.GetFrameCount() > 1:
            self.SpriteGroup.draw(screen)
        else:
            self.ActionAnimation.draw(screen)  
    def GetActionAnimation(self):
        return self.ActionAnimation
class PyGameResManager:
    #初始化
    def  __init__(self,resdir):
        self.resdir = os.getcwd()+"\\" + resdir
        self.fontdir = None
        self.resDict = {}
        self.imageDict = {}
        self.soundDict = {}
        self.soundPlayCount = 0
        self.resDict["root"]=[self.resdir,[]]
        self.FoundAllResFile(self.resdir,"root")
        print(self.resDict)
    #定义字体目录
    def SetFontDir(self,path):
        self.fontdir = path
    #查询所有的资源文件
    def FoundAllResFile(self,parentDir,resname):
        for fileName in os.listdir(parentDir):
            if "__pycache__" not in fileName:
                if ".git" not in fileName:
                    newPath = parentDir +"\\"+ fileName
                    if os.path.isdir(newPath):
                        self.resDict[fileName]=[newPath,[]]
                        self.FoundAllResFile(newPath,fileName)
                    else:
                        self.resDict[resname][1].append(fileName)
    #取得资源路径           
    def GetResPath(self,resname):
        if resname in self.resDict:
            return self.resDict[resname][0]
        return None
    #取得资源文件列表
    def GetResFileList(self,resname):
        if resname in self.resDict:
            return self.resDict[resname][1]
        return None
    #加载一个图片资源
    def LoadImage(self,resname,fileName):
        newImage = None
        if resname in self.resDict:
            ImagePath = self.resDict[resname][0]
            ImageFile = ImagePath +"\\"+ fileName
            newImage = pygame.image.load(ImageFile)
        return newImage
    #加载一个动画资源
    def GetAnimation(self,resname,action,callbackfun,callbackparam):
        if resname in self.resDict:
            ImagePath = self.resDict[resname][0]
            QueryPath = None
            if action is None:
                QueryPath = os.path.join(ImagePath,f"*.png")
                print(QueryPath)   
            else:
                QueryFile = str(f"%s*.png"%action)
                QueryPath = os.path.join(ImagePath,QueryFile)
                print(QueryPath) 
            im = glob.glob(QueryPath)
            frameCount = len(im)
            if frameCount == 1:
                newImage = pygame.image.load(im[0])
                NewActionAnimation = ActionAnimation([newImage],callbackfun,callbackparam)
                return ActionSprite(NewActionAnimation),1
            lenim = len(im[0])
            imagesArray1 = [pygame.image.load(img) for img in glob.glob(QueryPath) if len(img) == lenim]
            imagesArray2 = [pygame.image.load(img) for img in glob.glob(QueryPath) if len(img) > lenim]
            imagesArray1.extend(imagesArray2)
            print(imagesArray1)
            NewActionAnimation = ActionAnimation(imagesArray1,callbackfun,callbackparam)
            return ActionSprite(NewActionAnimation),len(imagesArray1)
        print("No Find ResDir")
        return None,0
    #播放音乐 支持MP3,WAV,MIDI
    def PlayMusic(self,resname,fileName,loopcount = 0):
        if resname in self.resDict:
            MusicPath = self.resDict[resname][0]
            MusicFile = MusicPath + "\\" + fileName 
            pygame.mixer.music.load(MusicFile)
            pygame.mixer.music.play(loopcount,0)
            return True
        return False  
    def StopMusic(self):
        pygame.mixer.music.stop()
    #播放音效 支持MP3,WAV,OGG
    def PlaySound(self,resname,fileName):
        if resname in self.resDict:
            SoundPath = self.resDict[resname][0]
            SoundFile = SoundPath + "\\" + fileName 
            self.soundDict[self.soundPlayCount] = pygame.mixer.Sound(SoundFile)
            self.soundDict[self.soundPlayCount].play()
            self.soundPlayCount = self.soundPlayCount + 1
            return self.soundPlayCount - 1
        return -1  
    def StopSound(self,soundID):
        if soundID in self.soundDict:
            self.soundDict[soundID].stop()
        else:
            print("No Find Sound")
    #取得字体
    def GetFont(self,ttfFile,fontSize):
        if self.fontdir is not None:
            if self.fontdir in self.resDict:
                FontPath = self.resDict[self.fontdir][0]
                FontFile = FontPath + "\\" + ttfFile 
                return pygame.font.Font(FontFile, fontSize)
        return None
Res = PyGameResManager("res")
Res.SetFontDir("Fonts")
class  GameNode:
    def  __init__(self,parent = None,x = 0,y = 0 ):
        self.NodeType = "GameNode"
        self.sceneInstance = None
        self.parent = parent
        if self.parent:
            self.parent.AddChild(self)
        self.children = []
        self.KeyDownFunctionDict = {}
        self.KeyUpFunctionDict = {}
        self.MouseDownFunction = {}
        self.MouseUpFunction = {}
        self.BindingVarArray = {}
        self.PickDownFunction = None
        self.PickUpFunction = None 
        self.UpdateFunction = None
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.instanceID = -1
        self.visible = True
    def OnLoad(self,sceneInstance):
        self.sceneInstance = sceneInstance
        for child in self.children:
            child.OnLoad(sceneInstance)
    def OnDestroy(self):
        for child in self.children:
            child.OnDestroy()
        self.children = []
        self.KeyDownFunctionDict = {}
        self.KeyUpFunctionDict = {}
        self.MouseDownFunction = {}
        self.MouseUpFunction = {}
        self.BindingVarArray = {}
        self.instanceID = -1
    #取得游戏
    def GetSceneInstance(self):
        return self.sceneInstance
    def SetInstanceID(self,instanceID):
        self.instanceID = instanceID
    def GetInstanceID(self):
        return self.instanceID
    def GetParent(self):
        return self.parent
    def SetParent(self, node):
        self.parent = node
        if self.parent:
            self.parent.AddChild(node)
    Parent = property(GetParent, SetParent)
    def AddChild(self,child):
        self.children.append(child)
    def RemoveChild(self,child):
        if child in self.children:
            child.RemoveAllChild()
            self.children.pop(child)
        else:
            print("No Find Child")
    def GetAllChildrens(self):
        allchildren = []
        for child in self.children:
            childchildrens = child.GetAllChildrens()
            for childchild in childchildrens:
                allchildren.append(childchild)
            allchildren.append(child)
        return allchildren
    def RemoveAllChild(self):
        for child in self.children:
            child.RemoveAllChild()
        self.children = []
    #设置显示
    def SetVisible(self,visible):
        self.visible = visible
    #取得显示
    def IsVisible(self):
        return self.visible
    #更新
    def update(self):
        for child in self.children:
            child.update()
        if self.UpdateFunction is not None:
            self.UpdateFunction(self)
    #显示
    def draw(self,screen):
        if  self.IsVisible() == True:
            for child in self.children:
                child.draw(screen)
    def GetX(self):
        return self.x
    def GetWX(self):
        if self.parent is not None:
            return self.parent.GetWX() + self.x
        return self.x
    def SetX(self, value):
        self.x = value
    X = property(GetX, SetX)
    def GetY(self):
        return self.y
    def GetWY(self):
        if self.parent is not None:
            return self.parent.GetWY() + self.y
        return self.y
    def SetY(self, value):
        self.y = value
    Y = property(GetY, SetY)
    def GetXY(self):
        return self.x,self.y
    def GetWXY(self):
        return self.GetWX(),self.GetWY()
    def SetXY(self, position):
        self.x,self.y = position
    XY = property(GetXY, SetXY)
    #设置键盘响应函数映射
    def SetKeyDownFunction(self,keyname,function):
        self.KeyDownFunctionDict[keyname] = function
    #响应键盘输入
    def OnKeyDownFunction(self,keyname):
        if  self.IsVisible() == True:
            if keyname in self.KeyDownFunctionDict:
                self.KeyDownFunctionDict[keyname](self)
    #设置键盘响应函数映射
    def SetKeyUpFunction(self,keyname,function):
        self.KeyUpFunctionDict[keyname] = function
    #响应键盘输入
    def OnKeyUpFunction(self,keyname):
        if  self.IsVisible() == True:
            if keyname in self.KeyUpFunctionDict:
                self.KeyUpFunctionDict[keyname](self)
    #设置鼠标按下函数映射
    def SetMouseDownFunction(self,buttonid,function):
        self.MouseDownFunction[buttonid] = function
    #响应鼠标按下
    def OnMouseDownFunction(self,buttonid):
        if  self.IsVisible() == True:
            if buttonid in self.MouseDownFunction:
                self.MouseDownFunction[buttonid](self)
     #设置鼠标松开响应函数映射
    def SetMouseUpFunction(self,buttonid,function):
        self.MouseUpFunction[buttonid] = function
    #响应鼠标松开
    def OnMouseUpFunction(self,buttonid):
        if  self.IsVisible() == True:
            if buttonid in self.MouseUpFunction:
                self.MouseUpFunction[buttonid](self)
     #设置点击当前角色时响应函数
    def SetPickDownFunction(self,function):
        self.PickDownFunction = function
    #响应点击当前角色
    def OnPickDownFunction(self,x,y):
        if  self.IsVisible() == True:
            for child in self.children:
                if child.OnPickDownFunction(x,y) == True:
                    return True
        return False
     #设置点击当前角色时响应函数
    def SetPickUpFunction(self,function):
        self.PickUpFunction = function
    #响应点击当前角色
    def OnPickUpFunction(self,x,y):
        if  self.IsVisible() == True:
            for child in self.children:
                if child.OnPickUpFunction(x,y) == True:
                    return True
        return False
    #增加更新函数
    def SetUpdateFunction(self,function):
        self.UpdateFunction= function
    #设置绑定变量
    def SetBindingVar(self,varname,varvalue):
        self.BindingVarArray[varname] = varvalue
    #取得绑定变量
    def GetBindingVar(self,varname):
        if varname in self.BindingVarArray:
            return self.BindingVarArray[varname]
        print("No Find Variable")    
        return None
    #删除绑定变量
    def DelBindingVar(self,varname):
        self.BindingVarArray.pop(varname)
    #清空绑定变量
    def CleanUpBindingVar(self):
        self.BindingVarArray.clear()
class  Label(GameNode):
    def  __init__(self,parent = None,x = 0,y = 0 ,text = "",fontname = "Arial",fontsize = 16):
        global Res
        super(Label, self).__init__(parent,x,y)
        self.NodeType = "Label"
        if fontname.lower().find(".ttf") >= 0:
            self.font = Res.GetFont(fontname,fontsize)
        else:
            self.font = pygame.font.SysFont(fontname, fontsize)
        self.text = text
        self.textColor = pygame.Color("white")
        self.bgColor = None
        self.image = None
    #设置宽度
    def SetWidth(self,width):
        self.width = width
    #设置高度
    def SetHeight(self,height):
        self.height = height
    #设置文字
    def SetText(self,text):
        self.text = text
    #设置颜色
    def SetTextColor(self,r,g,b):
        self.textColor = pygame.Color(r,g,b,255)
    #设置颜色
    def SetBGColor(self,r,g,b):
        self.bgColor = pygame.Color(r,g,b,255)
    #设置图像
    def SetImage(self,resdir,imagefile,autosize = True):
        global Res
        self.image = Res.LoadImage(resdir,imagefile)
        if autosize == True:
            imgrect = self.image.get_rect()
            self.width = imgrect.width
            self.height = imgrect.height
    #显示
    def draw(self,screen):
        global BorderVisible
        global BorderColor
        if  self.IsVisible() == True:
            WX = self.GetWX()
            WY = self.GetWY()
            rect = pygame.Rect(WX,WY, self.width, self.height)
            strlen = len(self.text)
            if self.bgColor is not None:
                pygame.draw.rect(screen, self.bgColor, (WX,WY, self.width, self.height), 0) 
            if self.image is not None:
                renderimage = pygame.transform.smoothscale(self.image, (self.width,self.height))
                screen.blit(renderimage, (WX,WY))
            if strlen > 0:
                text_to_show = self.font.render(self.text, 0, self.textColor)
                fontPixelSize = self.font.size(self.text) 
                screen.blit(text_to_show, (WX + self.width * 0.5 - fontPixelSize[0] * 0.5,WY + self.height * 0.5 - fontPixelSize[1] * 0.5))
            if BorderVisible == True:
                pygame.draw.rect(screen,BorderColor,rect,3)
            super(Label, self).draw(screen)
class  Button(Label):
    def  __init__(self,parent = None,x = 0,y = 0 ,text="",fontname = "Arial",fontsize = 16):
        super(Button, self).__init__(parent,x,y,text,fontname,fontsize)
        self.NodeType = "Button"
        self.PickDownFunction = None
        self.PickUpFunction = None
        self.textColor_hover = pygame.Color("white")
        self.bgColor_hover  = None
        self.image_hover = None
        self.textColor_click = pygame.Color("white")
        self.bgColor_click = None
        self.image_click = None
        self.clicked = False
    #设置颜色
    def SetTextColor_Hover(self,r,g,b):
        self.textColor_hover = pygame.Color(r,g,b,255)
    #设置颜色
    def SetBGColor_Hover(self,r,g,b):
        self.bgColor_hover = pygame.Color(r,g,b,255)
    #设置图像
    def SetImage_Hover(self,resdir,imagefile):
        global Res
        self.image_hover = Res.LoadImage(resdir,imagefile)
    #设置颜色
    def SetTextColor_Click(self,r,g,b):
        self.textColor_click = pygame.Color(r,g,b,255)
    #设置颜色
    def SetBGColor_Click(self,r,g,b):
        self.bgColor_click = pygame.Color(r,g,b,255)
    #设置图像
    def SetImage_Click(self,resdir,imagefile):
        global Res
        self.image_click = Res.LoadImage(resdir,imagefile)   
    #设置是否选中状态
    def SetClicked(self,checked):
        self.clicked = checked
    def OnPickDownFunction(self,px,py):
        if  self.IsVisible() == True:
            if super(Button, self).OnPickDownFunction(px,py) == True:
                print("super(Button).OnPickDownFunction")
                return True
            rect = pygame.Rect(self.GetWX(), self.GetWY(), self.width, self.height)    
            if rect.collidepoint(px,py):
                print("OnPickDownFunction1")
                if self.PickDownFunction is not None:
                    print("OnPickDownFunction2")
                    self.PickDownFunction(self)
                self.clicked = True
    def OnPickUpFunction(self,px,py):
        if  self.IsVisible() == True:
            print("Button:OnPickUpFunction")
            if super(Button, self).OnPickUpFunction(px,py) == True:
                print("super(Button).OnPickUpFunction")
                return True
            if self.clicked == True:
                if self.PickUpFunction is not None:
                    print("OnPickUpFunction2")
                    self.PickUpFunction(self)
                self.clicked = False
    #显示
    def draw(self,screen):
        global BorderVisible
        global BorderColor
        if  self.IsVisible() == True:
            WX = self.GetWX()
            WY = self.GetWY()
            rect = pygame.Rect(WX,WY, self.width, self.height)
            strlen = len(self.text)
            if self.clicked== True:
                    if self.bgColor_click is not None:
                        pygame.draw.rect(screen, self.bgColor_click, (WX,WY,  self.width, self.height), 0)
                    if self.image_click is not None:
                        screen.blit(self.image_click, (WX,WY))
                    if strlen > 0:
                        text_to_show = self.font.render(self.text, 0, self.textColor_click)
                        fontPixelSize = self.font.size(self.text) 
                        screen.blit(text_to_show, (WX + self.width * 0.5 - fontPixelSize[0] * 0.5,WY + self.height * 0.5 - fontPixelSize[1] * 0.5))
            else:
                px,py = pygame.mouse.get_pos()
                if rect.collidepoint(px,py) and self.NodeType == "Button":
                    if self.bgColor_hover is not None:
                        pygame.draw.rect(screen, self.bgColor_hover, (WX,WY,  self.width, self.height), 0)
                    if self.image_hover is not None:
                        screen.blit(self.image_hover, (WX,WY))
                    if strlen > 0:
                        text_to_show = self.font.render(self.text, 0, self.textColor_hover)
                        fontPixelSize = self.font.size(self.text) 
                        screen.blit(text_to_show, (WX + self.width * 0.5 - fontPixelSize[0] * 0.5,WY + self.height * 0.5 - fontPixelSize[1] * 0.5))
                else:
                    if self.bgColor is not None:
                        pygame.draw.rect(screen, self.bgColor, (WX,WY, self.width, self.height), 0) 
                    if self.image is not None:
                        screen.blit(self.image, (WX,WY))
                    if strlen > 0:
                        text_to_show = self.font.render(self.text, 0, self.textColor)
                        fontPixelSize = self.font.size(self.text) 
                        screen.blit(text_to_show, (WX + self.width * 0.5 - fontPixelSize[0] * 0.5,WY + self.height * 0.5 - fontPixelSize[1] * 0.5))
            if BorderVisible == True:
                pygame.draw.rect(screen,BorderColor,rect,3)
            super(Button, self).draw(screen)
class  CheckButton(Button):
    def  __init__(self,parent = None,x = 0,y = 0 ,text="",fontname = "Arial",fontsize = 16):
        super(CheckButton, self).__init__(parent,x,y,text,fontname,fontsize)
        self.NodeType = "CheckButton"
        self.PickDownFunction = None
        self.PickUpFunction = None
    def OnPickDownFunction(self,px,py):
        if  self.IsVisible() == True:
            if super(CheckButton, self).OnPickDownFunction(px,py) == True:
                return True
            print("OnPickDownFunction")
            rect = pygame.Rect(self.GetWX(), self.GetWY(), self.width, self.height)    
            if rect.collidepoint(px,py):
                if self.PickDownFunction is not None:
                    self.PickDownFunction(self)
    def OnPickUpFunction(self,px,py):
        if  self.IsVisible() == True:
            if super(CheckButton, self).OnPickUpFunction(px,py) == True:
                return True
            print("OnPickUpFunction")
            rect = pygame.Rect(self.GetWX(), self.GetWY(), self.width, self.height)    
            if rect.collidepoint(px,py):
                if self.PickUpFunction is not None:
                    self.PickUpFunction(self)
            if self.clicked == False:
                self.clicked = True
            else:
                self.clicked = False
class  ProgressBar(GameNode):
    def  __init__(self,parent = None,x = 0,y = 0 ,fontname = "Arial",fontsize = 16):
        global Res
        super(ProgressBar, self).__init__(parent,x,y)
        self.NodeType = "ProgressBar"
        if fontname.lower().find(".ttf") >= 0:
            self.font = Res.GetFont(fontname,fontsize)
        else:
            self.font = pygame.font.SysFont(fontname, fontsize)
        self.textColor = pygame.Color("white")
        self.bgColor = None
        self.imagefile_up = None
        self.imagefile_down = None
        self.imagefile_pos = None
        self.currvalue = 0
        self.minvalue = 0
        self.maxvalue = 100
        self.width = 100
        self.height = 20
    #设置宽度
    def SetWidth(self,width):
        self.width = width
    #设置高度
    def SetHeight(self,height):
        self.height = height
    #设置颜色
    def SetTextColor(self,r,g,b):
        self.textColor = pygame.Color(r,g,b,255)
    #设置颜色
    def SetBGColor(self,r,g,b,a = 255):
        self.bgColor = pygame.Color(r,g,b,a)
    #设置图像
    def SetImages(self,resdir,imagefile_down,imagefile_up,imagefile_pos):
        global Res
        if imagefile_up is not None:
            self.imagefile_up = Res.LoadImage(resdir,imagefile_up)
            imgrect = self.imagefile_up.get_rect()
            self.width = imgrect.width
            self.height = imgrect.height
        if imagefile_down is not None:
            self.imagefile_down = Res.LoadImage(resdir,imagefile_down)
            imgrect = self.imagefile_down.get_rect()
            self.width = imgrect.width
            self.height = imgrect.height
        if imagefile_pos is not None:
            self.imagefile_pos = Res.LoadImage(resdir,imagefile_pos)
    def SetRange(self,minvalue,maxvalue):
        self.minvalue = minvalue
        self.maxvalue = maxvalue
    def SetValue(self,value):
        self.currvalue = value
    #显示
    def draw(self,screen):
        if  self.IsVisible() == True:
            WX = self.GetWX()
            WY = self.GetWY()
            rangelength = self.maxvalue - self.minvalue
            currpos = self.currvalue / rangelength
            if self.bgColor is not None:
                pygame.draw.rect(screen, self.bgColor, (WX,WY, self.width, self.height), 0)   
            if self.imagefile_down is not None:
                screen.blit(self.imagefile_down, (WX,WY))
            if self.imagefile_up is not None:
                chopimage = pygame.transform.chop(self.imagefile_up,[0,0,self.width*currpos,self.height])
                screen.blit(chopimage, (WX,WY))
                # screen.blit(self.imagefile_up, (WX,WY))
            if self.imagefile_pos is not None:
                imgrect = self.imagefile_pos.get_rect()
                screen.blit(self.imagefile_pos, (WX + self.width * currpos - imgrect.width * 0.5 , WY + self.height * 0.5 - imgrect.height * 0.5))
            text = str("%d/%d"%(self.currvalue,self.maxvalue))
            text_to_show = self.font.render(text, 0, self.textColor)
            fontPixelSize = self.font.size(text) 
            screen.blit(text_to_show, (WX + self.width * 0.5 - fontPixelSize[0] * 0.5,WY + self.height * 0.5 - fontPixelSize[1] * 0.5))
            super(ProgressBar, self).draw(screen)
#角色
class  GameCharacter(GameNode):
    #初始化
    def __init__(self,parent = None,x = 0,y = 0):
        super(GameCharacter, self).__init__(parent,x,y)
        self.NodeType = "GameCharacter"
        self.ActionSprite = None
        self.frameCount = 0
        self.resdir = None
    #打开资源
    def SetResDir(self,resdir):
        self.resdir = resdir
    #播放动作
    def PlayAction(self,action = None,callbackfun = None):
        global Res
        self.ActionSprite,self.frameCount = Res.GetAnimation(self.resdir,action,callbackfun,self)
        self.width,self.height = self.GetImageSize()
        return self.frameCount
    def GetActionSprite(self):
        return self.ActionSprite
    def GetFrameCount(self):
        return self.frameCount
    def GetImageSize(self):
        return self.ActionSprite.GetActionAnimation().GetImageSize()
    def GetImageRect(self):
        return self.ActionSprite.GetActionAnimation().GetImageRect()
    def Coll_Rect(self,other):
        W1,H1 = self.GetImageSize()
        rect1 = pygame.Rect(self.GetWX(), self.GetWY(), W1,H1) 
        W2,H2 = other.GetImageSize()
        rect2 = pygame.Rect(other.GetWX(), other.GetWY(), W2,H2) 
        if rect1.colliderect(rect2):
            return True
        return False
    def Coll_Pt(self,x,y):
        W1,H1 = self.GetImageSize()
        rect1 = pygame.Rect(self.GetWX(), self.GetWY(), W1,H1) 
        if rect1.collidepoint(x,y):
            return True
        return False
    #更新
    def update(self):
        super(GameCharacter, self).update()
        if self.ActionSprite is not None:
            self.ActionSprite.update()
    #显示
    def draw(self,screen):
        super(GameCharacter, self).draw(screen)
        if self.ActionSprite is not None:
            self.ActionSprite.GetActionAnimation().SetXY(self.x,self.y)
            self.ActionSprite.draw(screen)
class  GameLayer:
    def  __init__(self):
        self.sceneInstance  = None
        self.GameNodeArray = {}
        self.GameNodeKeyArray = []
        self.DelGameNodeArray = []
        self.instanceID = 0
        self.visible = True
    #加载
    def OnLoad(self,sceneInstance):
        self.sceneInstance = sceneInstance
        for p in self.GameNodeArray.keys():
            self.GameNodeArray[p].OnLoad(sceneInstance)
    #销毁
    def OnDestroy(self):
        for p in self.GameNodeArray.keys():
            self.GameNodeArray[p].OnDestroy()
        self.GameNodeArray = {}
        self.GameNodeKeyArray = []
        self.DelGameNodeArray = []
    #取得游戏
    def GetSceneInstance(self):
        return self.sceneInstance   
    #设置显示
    def SetVisible(self,visible):
        self.visible = visible
    #取得显示
    def IsVisible(self):
        return self.visible
    #遍历角色调用函数
    def CheckAllGameNode(self,function = None,param = None,nochekCharacter = None):
        resultArray = []
        if  len(self.GameNodeArray) > 0:
            if function is None:
                if nochekCharacter is  None:
                    for p in self.GameNodeArray.keys():   
                        resultArray.append(self.GameNodeArray[p])    
                else:
                    for p in self.GameNodeArray.keys():   
                        if self.GameNodeArray[p] not in nochekCharacter:
                            resultArray.append(self.GameNodeArray[p])     
            else:
                self.GameNodeKeyArray = []
                if nochekCharacter is  None:
                    for p in self.GameNodeArray.keys():
                        self.GameNodeKeyArray.append(p)
                else:
                    for p in self.GameNodeArray.keys():   
                        if self.GameNodeArray[p] not in nochekCharacter:
                            self.GameNodeKeyArray.append(p)   
                for p in self.GameNodeKeyArray:
                    if function(self.GameNodeArray[p],param) == True:
                        resultArray.append(self.GameNodeArray[p])
        return resultArray
    #加入一个游戏结点
    def AddGameNode(self,gameNode):
        self.GameNodeArray[self.instanceID] = gameNode
        self.GameNodeArray[self.instanceID].SetInstanceID(self.instanceID)
        self.instanceID = self.instanceID + 1
        return self.instanceID - 1
    #取得一个游戏结点
    def GetGameNode(self,instanceID):
        if instanceID in self.GameNodeArray:
            return self.GameNodeArray[instanceID] 
        else:
            print("No Find GameNode")
            return None
    #删除一个游戏结点
    def DelGameNode(self,instanceID):
        if instanceID in self.GameNodeArray:
            if instanceID not in self.DelGameNodeArray:
                allchildrens = self.GameNodeArray[instanceID].GetAllChildrens()
                print("DelGameNode")
                print(allchildrens)
                for childchild in allchildrens:
                    self.DelGameNodeArray.append(childchild.GetinstanceID())
                self.DelGameNodeArray.append(instanceID)
        else:
            print("No Find GameNode")
    #删除所有游戏结点
    def CleanUpGameNode(self):
        for p in self.GameNodeArray.keys():    
            self.DelGameNodeArray.append(p)    
    #主更新
    def update(self):
        if  self.IsVisible() == True:
            if  len(self.GameNodeArray) > 0:
                self.GameNodeKeyArray = []
                for p in self.GameNodeArray.keys():
                    self.GameNodeKeyArray.append(p)
                for p in self.GameNodeKeyArray:
                    self.GameNodeArray[p].update()
            if  len(self.DelGameNodeArray) > 0:
                for p in self.DelGameNodeArray:
                    self.GameNodeArray.pop(p)
                self.DelGameNodeArray = []
    #显示
    def draw(self,screen):
        if  self.IsVisible() == True:
            if  len(self.GameNodeArray) > 0:
                for p in self.GameNodeArray.keys():
                    self.GameNodeArray[p].draw(screen)
    #响应键盘按下
    def OnKeyDownFunction(self,keyname):
        if  self.IsVisible() == True:
            if  len(self.GameNodeArray) > 0:
                self.GameNodeKeyArray = []
                for p in self.GameNodeArray.keys():
                    self.GameNodeKeyArray.append(p)
                for p in self.GameNodeKeyArray:
                    self.GameNodeArray[p].OnKeyDownFunction(keyname)
    #响应键盘松开
    def OnKeyUpFunction(self,keyname):
        if  self.IsVisible() == True:
            if  len(self.GameNodeArray) > 0:
                self.GameNodeKeyArray = []
                for p in self.GameNodeArray.keys():
                    self.GameNodeKeyArray.append(p)
                for p in self.GameNodeKeyArray:
                    self.GameNodeArray[p].OnKeyUpFunction(keyname)
     #响应鼠标按下
    def OnMouseDownFunction(self,buttonid):
        if  self.IsVisible() == True:
            if  len(self.GameNodeArray) > 0:
                self.GameNodeKeyArray = []
                for p in self.GameNodeArray.keys():
                    self.GameNodeKeyArray.append(p)
                for p in self.GameNodeKeyArray:
                    self.GameNodeArray[p].OnMouseDownFunction(buttonid)
     #响应鼠标按下
    def OnMouseUpFunction(self,buttonid):
        if  self.IsVisible() == True:
            if  len(self.GameNodeArray) > 0:
                self.GameNodeKeyArray = []
                for p in self.GameNodeArray.keys():
                    self.GameNodeKeyArray.append(p)
                for p in self.GameNodeKeyArray:
                    self.GameNodeArray[p].OnMouseUpFunction(buttonid)
    #响应点击当前角色
    def OnPickDownFunction(self,x,y):
        if  self.IsVisible() == True:
            if  len(self.GameNodeArray) > 0:
                self.GameNodeKeyArray = []
                for p in self.GameNodeArray.keys():
                    self.GameNodeKeyArray.append(p)
                for p in self.GameNodeKeyArray:
                    self.GameNodeArray[p].OnPickDownFunction(x,y)
    #响应点击当前角色
    def OnPickUpFunction(self,x,y):
        if  self.IsVisible() == True:
            if  len(self.GameNodeArray) > 0:
                self.GameNodeKeyArray = []
                for p in self.GameNodeArray.keys():
                    self.GameNodeKeyArray.append(p)
                for p in self.GameNodeKeyArray:
                    self.GameNodeArray[p].OnPickUpFunction(x,y)
#游戏场景类
class  GameScene:
    #初始化
    def  __init__(self):
        self.LayerArray = {}
        self.LayerRenderArray = []
    #加载
    def OnLoad(self):
        for l in self.LayerRenderArray:
            self.LayerArray[l].OnLoad(self)
    #销毁
    def OnDestroy(self):
        for l in self.LayerRenderArray:
            self.LayerArray[l].OnDestroy()
    #加入一个图层
    def AddLayer(self,layername):
        self.LayerArray[layername] = GameLayer()
        self.LayerRenderArray.append(layername)
        return self.LayerArray[layername]
    #取得一个图层
    def GetLayer(self,layername):
        if layername in self.LayerArray:
            return self.LayerArray[layername]
        else:
            print("No Find layer")
            return None
    #删除一个图层
    def DelLayer(self,layername):
        if layername in self.LayerArray:
            self.LayerArray.pop(layername)
        else:
            print("No Find layer")
    #加入一个游戏结点
    def AddGameNode(self,layername,character):
        if layername in self.LayerArray:
            instanceID = self.LayerArray[layername].AddGameNode(character)
            character.OnLoad(self)
            return instanceID
        else:
            print("No Find layer")
        return None
    #删除一个游戏结点
    def DelGameNode(self,layername,instanceID):
        if layername in self.LayerArray:
            self.LayerArray[layername].DelGameNode(instanceID)
        else:
            print("No Find layer")
    #删除所有游戏结点
    def CleanUpGameNode(self,layername):
        if layername in self.LayerArray:
            self.LayerArray[layername].CleanUpGameNode()
        else:
            print("No Find layer")
    #播放音乐 支持MP3,WAV,MIDI
    def PlayBGMusic(self,resname,fileName,loopcount = 0):
        global Res
        return Res.PlayMusic(resname,fileName,loopcount)
    def StopBGMusic(self):
        global Res
        Res.StopMusic()
    #播放音效 支持MP3,WAV,OGG
    def PlaySound(self,resname,fileName):
        global Res
        return Res.PlaySound(resname,fileName)
    def StopSound(self,soundID):
        global Res
        Res.StopSound(soundID)
    #主更新
    def update(self):
        global gameAppInstance
        #键盘
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameAppInstance.exit()
                return 
            elif event.type == pygame.KEYDOWN:
                text = str("pygame.KEYDOWN:%s"%event.key)
                print(text)
                for l in self.LayerRenderArray:
                    self.LayerArray[l].OnKeyDownFunction(event.key)
            elif event.type == pygame.KEYUP:
                text = str("pygame.KEYUP:%s"%event.key)
                print(text)
                for l in self.LayerRenderArray:
                    self.LayerArray[l].OnKeyUpFunction(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                text = str("pygame.MOUSEBUTTONDOWN:%d"%event.button)
                print(text)
                px,py = pygame.mouse.get_pos()
                for l in self.LayerRenderArray:
                    self.LayerArray[l].OnMouseDownFunction(event.button)
                    self.LayerArray[l].OnPickDownFunction(px,py)
            elif event.type == pygame.MOUSEBUTTONUP:
                text = str("pygame.MOUSEBUTTONUP:%d"%event.button)
                print(text)
                px,py = pygame.mouse.get_pos()
                for l in self.LayerRenderArray:
                    self.LayerArray[l].OnMouseUpFunction(event.button)
                    self.LayerArray[l].OnPickUpFunction(px,py)
        for l in self.LayerRenderArray:
            self.LayerArray[l].update()
    #显示
    def draw(self,screen):
        #按顺序渲染
        for l in self.LayerRenderArray:
            self.LayerArray[l].draw(screen)
#游戏框架类
class  GameApp:
    #初始化
    def  __init__(self,caption,width,height):
        global gameAppInstance
        gameAppInstance = self
        self.BindingVarArray = {}
        self.screenWidth = width
        self.screenHeight = height
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((self.screenWidth,self.screenHeight), 0, 32)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(caption)
        self.fps_font = pygame.font.SysFont("Arial", 16)
        self.BGColor_R = 0 
        self.BGColor_G = 0 
        self.BGColor_B = 0 
        self.fps = 30
        self.exitloop = False
        self.sceneInstance = None
        self.DelSceneArray = []
    #取得当前Screen
    def GetScreen(self):
        return self.screen
    #取得ALPHASURFACE
    def GetAlphaSurface(self):
        return self.alphasurface
    #设置帧率
    def SetFPS(self,fps):
        self.fps = fps
    #设置当前场景
    def SetCurrentScene(self,sceneInstance,destroyLast = True):
        if self.sceneInstance is not None and destroyLast == True:
            self.DelSceneArray.append(self.sceneInstance)
        self.sceneInstance = sceneInstance
        self.sceneInstance.OnLoad()
    #设置当前场景
    def GetCurrentScene(self):
        return  self.sceneInstance
    #设置绑定变量
    def SetBindingVar(self,varname,varvalue):
        self.BindingVarArray[varname] = varvalue
    #取得绑定变量
    def GetBindingVar(self,varname):
        if varname in self.BindingVarArray:
            return self.BindingVarArray[varname]
        print("No Find Variable")    
        return None
    #删除绑定变量
    def DelBindingVar(self,varname):
        self.BindingVarArray.pop(varname)
    #清空绑定变量
    def CleanUpBindingVar(self):
        self.BindingVarArray.clear()
    #加入一个背景
    def SetBGColor(self,Red,Green,Blue):
        self.BGColor_R = Red 
        self.BGColor_G = Green 
        self.BGColor_B = Blue
    #设置当前鼠标所在位置
    def GetCursorPosition(self):
        return  pygame.mouse.get_pos()
    #设置当前鼠标光标图像
    def SetCursorImage(self,image):
        pygame.mouse.set_cursor(image)
    #主更新
    def update(self):
        self.clock.tick(self.fps)
        if self.sceneInstance is not None:
            self.sceneInstance.update()
        if  len(self.DelSceneArray) > 0:
            for scene in self.DelSceneArray:
                scene.OnDestroy()
            self.DelSceneArray = []
    #显示
    def draw(self):
        self.screen.fill((self.BGColor_R,self.BGColor_G,self.BGColor_B))
        #按顺序渲染
        if self.sceneInstance is not None:
            self.sceneInstance.draw(self.screen)
        text_fps = str("FPS:%d"%(int(self.clock.get_fps())))
        text_to_show = self.fps_font.render(text_fps, 0, pygame.Color("red"))
        self.screen.blit(text_to_show, (0,0))
        pygame.display.update()
    #主循环
    def loop(self):
        while (self.exitloop == False):
            self.update()
            self.draw()    
    #退出游戏
    def exit(self):
        self.exitloop = True
