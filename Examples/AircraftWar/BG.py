#coding=utf-8
import GameFun

class   Character(GameFun.GameCharacter):
    #初始化
    def __init__(self):
        super(Character, self).__init__()


    def OnLoad(self,sceneInstance):
        print("BG_OnLoad")
        super(Character, self).OnLoad(sceneInstance)
        bg1 = GameFun.GameCharacter()
        bg1.SetResDir("bg")
        bg1.PlayAction("bg")
        bg1.SetBindingVar("voff",0.0)
        bg1.SetUpdateFunction(self.BGUVAni)
        bgW,bgH = bg1.GetImageSize()
        print(str("bgW:%d bgH:%d"%(bgW,bgH)))
        sceneInstance.AddGameNode("BG",bg1)

        bg2 = GameFun.GameCharacter()
        bg2.SetResDir("bg")
        bg2.PlayAction("bg")
        bg2.Y = -852
        bg2.SetBindingVar("voff",0.0)
        bg2.SetUpdateFunction(self.BGUVAni)
        sceneInstance.AddGameNode("BG",bg2)

    def BGUVAni(self,Character):
        bgW,bgH = Character.GetImageSize()
        voff = Character.GetBindingVar("voff")
        voff = voff + 1.0
        if voff > bgH :
            Character.Y = Character.Y - voff
            voff = 0.0
        else:
            Character.Y = Character.Y + 1.0
        Character.SetBindingVar("voff",voff)

