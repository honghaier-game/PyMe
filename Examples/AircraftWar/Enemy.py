#coding=utf-8
import GameFun
import pygame
import random
import Scene3

def check_coll(Character,bullet):
    if Character.Coll_Rect(bullet):
        return True
    return False


class Character(GameFun.GameCharacter):
    def __init__(self,parent = None,x = 0,y = 0):
        super(Character, self).__init__(parent,x,y)

    def OnLoad(self,sceneInstance):
        super(Character, self).OnLoad(sceneInstance)
        self.SetResDir("enemy")
        self.PlayAction("Idle")
        self.X = random.randint(60,420)
        self.Y = 30
        # self.bgW,self.bgH = self.self.GetImageSize()
        # print(str("bgW:%d bgH:%d"%(self.bgW,self.bgH)))
        self.SetBindingVar("Speed",2.0)
        self.SetBindingVar("Direction",-1)
        self.SetBindingVar("FireWaitCount",100)
        self.SetUpdateFunction(self.UpdateMove_enemy)


    def UpdateMove_enemy(self,Character):
        speed = Character.GetBindingVar("Speed")
        direction = Character.GetBindingVar("Direction")
        firewaitcount = Character.GetBindingVar("FireWaitCount")
        Character.X += direction * speed
        if Character.X < 60:
            direction = 1
        if Character.X > 400:
            direction = -1
        Character.SetBindingVar("Speed",speed)
        Character.SetBindingVar("Direction",direction)
        firewaitcount = firewaitcount - 1
        if firewaitcount < 0:
            self.Fire_enemy(Character)
            firewaitcount = 100
        Character.SetBindingVar("FireWaitCount",firewaitcount)     

    def PlayerDead(self,player):
        sceneInstance = player.GetSceneInstance()
        sceneInstance.DelGameNode("Character",player.GetInstanceID())
        killCount = GameFun.gameAppInstance.GetBindingVar("KillCount")
        scene3 = Scene3.Scene()
        GameFun.gameAppInstance.SetCurrentScene(scene3)
        scene3.SetKillCount(killCount)   


    def BulletMove_enemy(self,bullet):
        sceneInstance = bullet.GetSceneInstance()
        bullet.Y = bullet.Y + 5.0
        if bullet.Y < 0:
            sceneInstance.DelGameNode("Bullet",bullet.GetInstanceID())
        enemy = bullet.GetBindingVar("enemy")
        layer = sceneInstance.GetLayer("Character")
        if layer is not None:
            # print("CheckAllGameNode")
            hitArray = layer.CheckAllGameNode(check_coll,bullet,[enemy])
            if len(hitArray) > 0:
                sceneInstance.DelGameNode("Bullet",bullet.GetInstanceID())
                for palyer in hitArray:
                    palyer.PlayAction("Dead",self.PlayerDead)

    def Fire_enemy(self,Character):
        sceneInstance = Character.GetSceneInstance()
        bgW,bgH = Character.GetImageSize()
        bullet = GameFun.GameCharacter()
        bullet.SetResDir("bullet")
        bullet.PlayAction("enemy")
        sceneInstance.AddGameNode("Bullet",bullet)
        bullet.X = Character.X + bgW * 0.5
        bullet.Y = Character.Y
        bullet.SetUpdateFunction(self.BulletMove_enemy)
        bullet.SetBindingVar("enemy",Character)
        print("Fire")