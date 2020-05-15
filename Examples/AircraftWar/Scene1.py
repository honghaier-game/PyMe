#coding=utf-8
import GameFun
import BG
import StartGameUI

class   Scene(GameFun.GameScene):
    #初始化
    def __init__(self):
        super(Scene, self).__init__()
        self.AddLayer("BG")
        self.AddLayer("UI")

    def OnLoad(self):
        super(Scene, self).OnLoad()
        
        bg = BG.Character()
        self.AddGameNode("BG",bg)

        startGameUI = StartGameUI.GameUI()
        self.AddGameNode("UI",startGameUI)


