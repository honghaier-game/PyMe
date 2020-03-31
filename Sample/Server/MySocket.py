#coding=utf-8
import socket
import tkinter
import threading
import time

def handle_socket(ServerSocket, ListBox):
    conn, addr = ServerSocket.accept()
    text = "接受:"+str(addr)
    ListBox.insert(tkinter.END,text)
    while True:
        data = conn.recv(1024)
        text = "Receive Data:" + data.decode('utf-8')
        ListBox.insert(tkinter.END,text)
        time.sleep(3)
        send_data = 'got it'
        conn.send(send_data.encode('utf-8'))
    conn.close()

class   MySocket:
    def __init__(self):
        self.s = None
        self.HOST = '127.0.0.1'
        self.PORT = 8888
    def __del__(self):
        if self.s is not None:
            self.s.close()
    #设置HOST
    def set_HOST(self,host):
        self.HOST = host
    #获取HOST
    def get_HOST(self):
        return self.HOST

    #设置PORT
    def set_PORT(self,port):
        self.PORT = port
    #获取PORT
    def get_PORT(self):
        return self.PORT   

    #创建服务器
    def createServer(self,IPAddr,Port,ListBox):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.bind((self.HOST,int(self.PORT)))
        self.s.listen(5)
        ListBox.insert(tkinter.END,"Socket创建成功")
        client_thread = threading.Thread(target=handle_socket, args=[self.s, ListBox])
        client_thread.start()

    #连接服务器
    def connServer(self,IPAddr,Port):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect((self.HOST,int(self.PORT)))

    #发送信息
    def sendMessage(self,text):
        msg = text.encode('utf-8')
        print("SendMsg:"+text)
        self.s.send(msg)

        




  