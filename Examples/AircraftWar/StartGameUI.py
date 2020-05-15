#coding=utf-8
#import libs
import GameFun 
import Scene2

class   GameUI(GameFun.Label):
    def __init__(self):
        super(GameUI, self).__init__()
        self.SetWidth(480)
        self.SetHeight(640)
        self.label_2 = GameFun.Label(self,52,170,"","Arial",16)
        self.label_2.SetWidth(310)
        self.label_2.SetHeight(99)
        self.label_2.SetImage("ui","title.png",False)
        self.button_3 = GameFun.Button(self,150,366)
        self.button_3.SetWidth(162)
        self.button_3.SetHeight(50)
        self.button_3.SetImage("ui","restart1.png")
        self.button_3.SetPickUpFunction(self.button_3_PickUp)
        self.button_4 = GameFun.Button(self,153,453)
        self.button_4.SetWidth(159)
        self.button_4.SetHeight(45)
        self.button_4.SetImage("ui","exit1.png")
        self.button_4.SetPickUpFunction(self.button_4_PickUp)
    def OnLoad(self,sceneInstance):
        super(GameUI, self).OnLoad(sceneInstance)
    def button_3_PickUp(self,uiNode):
        sceneInstance = uiNode.GetSceneInstance()
        uiLayer1 = sceneInstance.GetLayer("UI")
        uiLayer1.SetVisible(False)
        scene2 = Scene2.Scene()
        GameFun.gameAppInstance.SetCurrentScene(scene2)
        GameFun.gameAppInstance.SetBindingVar("KillCount",0)
    def button_4_PickUp(self,uiNode):
        GameFun.gameAppInstance.exit()    