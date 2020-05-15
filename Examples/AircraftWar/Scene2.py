#coding=utf-8
import GameFun
import BG
import Player
import Enemy


class   Scene(GameFun.GameScene):
    #初始化
    def __init__(self):
        super(Scene, self).__init__()
        self.AddLayer("BG")
        self.AddLayer("Character")
        self.AddLayer("Bullet")
        self.AddLayer("UI")

    def OnLoad(self):
        super(Scene, self).OnLoad()
        
        bg = BG.Character()
        self.AddGameNode("BG",bg)

        #玩家角色
        player1 = Player.Character()
        self.AddGameNode("Character",player1)
        
        #敌人
        self.CreateNewEnemy()

    def CreateNewEnemy(self):
        #玩家角色
        enemy1 = Enemy.Character()
        self.AddGameNode("Character",enemy1)
