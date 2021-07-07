# coding=utf-8
import socket
import tkinter
import threading
import time
import Fun
BUFSIZ=1024
class CClientSocket(threading.Thread):
    def __init__(self,ip='127.0.0.1',port=8989):
        super().__init__()
        self.s = None
        self.ClientListBox = None
        self.HOST = ip
        self.PORT = port
        self.stopFlag = False
    # 设置HOST
    def set_HOST(self, host):
        self.HOST = host
    # 获取HOST
    def get_HOST(self):
        return self.HOST
    # 设置PORT
    def set_PORT(self, port):
        self.PORT = port
    # 获取PORT
    def get_PORT(self):
        return self.PORT
        # 设置MsgListBox
    # 设置ClientListBox
    def set_ClientListBox(self, listbox):
        self.ClientListBox = listbox
    # 获取ClientListBox
    def get_ClientListBox(self):
        return self.ClientListBox
    def getStopFlag(self):
        return self.stopFlag
    def run(self):
        self.__connServer()
    # 连接服务器
    def __connServer(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((self.HOST, int(self.PORT)))
        except Exception as e :
            print(e)
            self.__dealReceiveMsg("服务器连接不上，请检查服务器是否运行！")
            self.stopFlag = True
            return
        else:
            self.__dealReceiveMsg("Connect Server successfully!")
        while True:
            if(self.stopFlag):
                break
            #print("wait recv data...........")
            data_bytes = self.s.recv(BUFSIZ)
            #print("recv data...........")
            if (data_bytes == b""):
                self.s.close()
                self.stopFlag = True
                time.sleep(1)
                self.__dealReceiveMsg("连接断开......")
                break
            msg = "receive data from server:   " + data_bytes.decode('utf-8')
            self.__dealReceiveMsg(msg)
        self.s.close()
        print("client conn close...")
    #发送信息
    def sendMessage(self,text):
        msg = text.encode('utf-8')
        print("SendMsg:"+text)
        self.s.send(msg)
    def __dealReceiveMsg(self,msg):
        listBox = Fun.GetElement("Chat", "ListBox_9")
        listBox.insert(tkinter.END, msg)
'''
def runServer(ip='127.0.0.1',port=8989):
    s = CClientSocket(ip,port)
    s.start()
    print(s.name)
    return s.is_alive()
def stopServer():
    s = CClientSocket()
    s.stopServer()
    time.sleep(1)
    return s.is_alive()
'''
