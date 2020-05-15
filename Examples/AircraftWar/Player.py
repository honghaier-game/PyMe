#coding=utf-8
import GameFun
import pygame
def check_coll(Character,bullet):
    if Character.Coll_Rect(bullet):
        return True
    return False

class Character(GameFun.GameCharacter):
     def __init__(self,parent = None,x = 0,y = 0):
          super(Character, self).__init__(parent,x,y)

     def OnLoad(self,sceneInstance):
          super(Character, self).OnLoad(sceneInstance)
          #Add your Varial Here: (Keep This Line of comments)
          self.SetResDir("player")
          self.PlayAction("Idle")

          self.X = 200
          self.Y = 460
          self.SetBindingVar("isMoving",False)
          self.SetBindingVar("Speed",5.0)
          self.SetBindingVar("Direction",0)
          self.SetBindingVar("KeyCount",0)

          self.SetKeyDownFunction(pygame.K_LEFT,self.MoveLeft)
          self.SetKeyDownFunction(pygame.K_RIGHT,self.MoveRight)
          self.SetKeyDownFunction(pygame.K_a,self.MoveLeft)
          self.SetKeyDownFunction(pygame.K_d,self.MoveRight)
          self.SetKeyUpFunction(pygame.K_LEFT,self.StopMove)
          self.SetKeyUpFunction(pygame.K_RIGHT,self.StopMove)
          self.SetKeyUpFunction(pygame.K_a,self.StopMove)
          self.SetKeyUpFunction(pygame.K_d,self.StopMove)
          self.SetMouseDownFunction(1,self.Fire_player)
          self.SetUpdateFunction(self.UpdateMove_player)


     def MoveLeft(self,Character):
          Character.SetBindingVar("isMoving",True)
          Character.SetBindingVar("Direction",-1)
          keycount = Character.GetBindingVar("KeyCount")
          Character.SetBindingVar("KeyCount",keycount+1)

     def MoveRight(self,Character):
          Character.SetBindingVar("isMoving",True)
          Character.SetBindingVar("Direction",1)
          keycount = Character.GetBindingVar("KeyCount")
          Character.SetBindingVar("KeyCount",keycount+1)

     def UpdateMove_player(self,Character):
          isMoving = Character.GetBindingVar("isMoving")
          direction = Character.GetBindingVar("Direction")
          speed = Character.GetBindingVar("Speed")
          if isMoving == True:
               if direction  == -1:
                    if Character.x < 10:
                         return
               if direction  == 1:
                    if Character.x > 370:
                         return
               Character.x += direction * speed

     def StopMove(self,Character):
          keycount = Character.GetBindingVar("KeyCount")
          Character.SetBindingVar("KeyCount",keycount-1)
          if keycount == 1:
               Character.SetBindingVar("isMoving",False)
               Character.SetBindingVar("Direction",0)

     def EnemyDead(self,enemy):
          sceneInstance = enemy.GetSceneInstance()
          sceneInstance.DelGameNode("Character",enemy.GetInstanceID())
          killCount = GameFun.gameAppInstance.GetBindingVar("KillCount")
          GameFun.gameAppInstance.SetBindingVar("KillCount",killCount + 1)
          sceneInstance.CreateNewEnemy()

     def BulletMove_player(self,bullet):
          sceneInstance = bullet.GetSceneInstance()
          bullet.Y = bullet.Y - 5.0
          # print("BulletMove")
          if bullet.Y < 0:
               sceneInstance.DelGameNode("Bullet",bullet.GetInstanceID())
               return 
          player = bullet.GetBindingVar("player")
          layer = sceneInstance.GetLayer("Character")
          if layer is not None:
               # print("CheckAllGameNode")
               hitArray = layer.CheckAllGameNode(check_coll,bullet,[player])
               if len(hitArray) > 0:
                    sceneInstance.DelGameNode("Bullet",bullet.GetInstanceID())
                    for enemy in hitArray:
                         enemy.PlayAction("Dead",self.EnemyDead)

     def Fire_player(self,Character):
          sceneInstance = Character.GetSceneInstance()
          bgW,bgH = Character.GetImageSize()
          bullet = GameFun.GameCharacter()
          bullet.SetResDir("bullet")
          bullet.PlayAction("player")
          bullet.X = Character.X + bgW * 0.5
          bullet.Y = Character.Y
          bullet.SetUpdateFunction(self.BulletMove_player)
          bullet.SetBindingVar("player",Character)
          sceneInstance.AddGameNode("Bullet",bullet)
          print("Fire")
          sceneInstance.PlaySound("music","fire.wav")
