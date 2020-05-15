#coding=utf-8
import GameFun
import BG
import GameOverUI

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

        self.gameoverUI = GameOverUI.GameUI()
        self.AddGameNode("UI",self.gameoverUI)

    def SetKillCount(self,killCount):
        self.gameoverUI.SetKillCount(killCount)
