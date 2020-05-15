#coding=utf-8
#import libs
import GameFun 
import Scene2

class   GameUI(GameFun.Label):
    def __init__(self):
        super(GameUI, self).__init__()
        self.SetWidth(480)
        self.SetHeight(640)
        self.label_2 = GameFun.Label(self,100,80,"","REGULAR.TTF",76)
        self.label_2.SetWidth(304)
        self.label_2.SetHeight(95)
        self.label_2.SetText("历史最高")
        self.label_2.SetTextColor(0,0,0)
        self.label_3 = GameFun.Label(self,186,205,"","黑体",76)
        self.label_3.SetWidth(94)
        self.label_3.SetHeight(58)
        self.label_3.SetText("0")
        self.label_3.SetTextColor(0,0,0)
        self.label_4 = GameFun.Label(self,100,300,"","REGULAR.TTF",76)
        self.label_4.SetWidth(304)
        self.label_4.SetHeight(95)
        self.label_4.SetText("本次得分")
        self.label_4.SetTextColor(0,0,0)
        self.label_5 = GameFun.Label(self,189,412,"","黑体",76)
        self.label_5.SetWidth(91)
        self.label_5.SetHeight(62)
        self.label_5.SetText("0")
        self.label_5.SetTextColor(0,0,0)
        self.button_6 = GameFun.Button(self,190,500)
        self.button_6.SetWidth(111)
        self.button_6.SetHeight(27)
        self.button_6.SetImage("ui","restart1.png")
        self.button_6.SetImage_Click("ui","restart2.png")
        self.button_6.SetPickUpFunction(self.button_6_PickUp)
    def OnLoad(self,sceneInstance):
        super(GameUI, self).OnLoad(sceneInstance)
    def button_6_PickUp(self,uiNode):
        sceneInstance = uiNode.GetSceneInstance()
        uiLayer1 = sceneInstance.GetLayer("UI")
        uiLayer1.SetVisible(False)
        scene2 = Scene2.Scene()
        GameFun.gameAppInstance.SetCurrentScene(scene2)
        GameFun.gameAppInstance.SetBindingVar("KillCount",0)  
    def SetKillCount(self,killCount):
        killCount_Best = GameFun.gameAppInstance.GetBindingVar("BestKillCount")
        if killCount_Best < killCount:
            killCount_Best = killCount
        GameFun.gameAppInstance.SetBindingVar("BestKillCount",killCount_Best)  
        text1 = str("%d"%killCount_Best)
        self.label_3.SetText(text1)
        text2 = str("%d"%killCount)
        self.label_5.SetText(text2)