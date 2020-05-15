#coding=utf-8
#import libs
import GameFun 
import Scene1 

gameApp = GameFun.GameApp("Form1",480,640)
gameApp.SetBGColor(0,0,0)
gameApp.SetBindingVar("KillCount",0)
gameApp.SetBindingVar("BestKillCount",0)
scene1 = Scene1.Scene()
gameApp.SetCurrentScene(scene1)

gameApp.SetFPS(60)
gameApp.loop()
