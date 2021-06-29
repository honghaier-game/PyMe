#coding=utf-8
import socket
import tkinter
import threading
import time
g_ClientSocketArray = []
g_ThreadActive = False
def handle_socket_server_msg(ServerSocket, MsgListBox, ClientListBox):
    global g_ClientSocketArray
    global g_ThreadActive
    while g_ThreadActive == True:
        ClientIndex = 0
        for client in g_ClientSocketArray:
            try: 
                data = client.recv(1024)
                if data != None and data != "":
                    text = "Receive Data:" + data.decode('utf-8')
                    MsgListBox.insert(tkinter.END,text)
            except Exception: 
                client.close()
                g_ClientSocketArray.remove(client)
                ClientListBox.Delete(ClientIndex)
                continue
            ClientIndex = ClientIndex + 1
def handle_socket_server_accept(ServerSocket, ClientListBox):
    global g_ClientSocketArray
    global g_ThreadActive
    while g_ThreadActive == True:
        conn, addr = ServerSocket.accept()
        text = "接受:"+str(addr)
        ClientListBox.insert(tkinter.END,text)
        conn.setblocking(0) 
        g_ClientSocketArray.append(conn)
        time.sleep(1)  
    ServerSocket.close()
def handle_socket_client(ClientSocket, MsgListBox):
    global g_ThreadActive
    while g_ThreadActive:
        data = ClientSocket.recv(1024)
        text = "Receive Data:" + data.decode('utf-8')
        MsgListBox.insert(tkinter.END,text)
    ClientSocket.close()
class   MySocket:
    def __init__(self):
        self.s = None
        self.MsgListBox = None
        self.ClientListBox = None
        self.HOST = '127.0.0.1'
        self.PORT = 8888
    def __del__(self):
        global g_ThreadActive
        g_ThreadActive = False
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
    #设置MsgListBox
    def set_MsgListBox(self,listbox):
        self.MsgListBox = listbox
    #获取MsgListBox
    def get_MsgListBox(self):
        return self.MsgListBox   
    #设置ClientListBox
    def set_ClientListBox(self,listbox):
        self.ClientListBox = listbox
    #获取ClientListBox
    def get_ClientListBox(self):
        return self.ClientListBox  
    #创建服务器
    def createServer(self,IPAddr,Port):
        global g_ThreadActive
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.bind((self.HOST,int(self.PORT)))
        self.s.listen(5)
        g_ThreadActive = True
        self.MsgListBox.insert(tkinter.END,"Server Created successfully!")
        client_thread1 = threading.Thread(target=handle_socket_server_accept, args=[self.s, self.ClientListBox])
        client_thread1.start()
        client_thread2 = threading.Thread(target=handle_socket_server_msg, args=[self.s, self.MsgListBox,self.ClientListBox])
        client_thread2.start()
    #连接服务器
    def connServer(self,IPAddr,Port):
        global g_ThreadActive
        g_ThreadActive = True
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect((self.HOST,int(self.PORT)))
        self.MsgListBox.insert(tkinter.END,"Successfully connected to  Server!")
        client_thread = threading.Thread(target=handle_socket_client, args=[self.s, self.MsgListBox])
        client_thread.start()
    #发送信息
    def sendMessage(self,text):
        msg = text.encode('utf-8')
        print("SendMsg:"+text)
        self.s.send(msg)
    #发送信息
    def sendMessageToClient(self,clientindex,text):
        global g_ClientSocketArray
        if clientindex < len(g_ClientSocketArray):
            msg = text.encode('utf-8')
            print("SendMsg:"+text)
            g_ClientSocketArray[clientindex].send(msg)
