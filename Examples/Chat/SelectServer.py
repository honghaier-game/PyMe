import socket
import select
import threading
import time
import Fun
import tkinter
g_connSocketList = []
g_connMessageDic = {}
def Singleton(cls):
    _instance = {}
    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return _singleton
class SelectServer(threading.Thread):
    def __init__(self,ip='127.0.0.1',port=8989):
        super().__init__()
        self.ip = ip
        self.port = port
        self.s = None
        self.stopFlag = False
    def run(self):
        self.createServer()
    def stopServer(self):
        self.stopFlag = True
    def createServer(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.s.bind((self.ip, int(self.port)))
            self.s.listen(5)
        except Exception as e:
            print(e)
            self.stopFlag = True
            self.__dealReceiveMsg("服务器启动失败，请检查端口是否可用!")
            return
        else:
            self.__dealReceiveMsg("Server Created successfully!")
        g_connSocketList.append(self.s)
        while True:
            if(self.stopFlag):
                break
            r_list, w_list, e_list = select.select(g_connSocketList, [], g_connSocketList, 1)
            print("正在监听的socket对象%d" % len(g_connSocketList))
            print(r_list)
            for sk1_or_conn in r_list:
                if sk1_or_conn == self.s:
                    conn, address = sk1_or_conn.accept()
                    g_connSocketList.append(conn)
                    g_connMessageDic[conn] = []
                else:
                    try:
                        data_bytes = sk1_or_conn.recv(1024)
                        # 对方断开连接
                        if (data_bytes == b""):
                            sk1_or_conn.close()
                            g_connSocketList.remove(sk1_or_conn)
                            self.__dealReceiveMsg("客户端断开连接!")
                            continue
                        data_str = str(data_bytes, encoding="utf-8")
                        msg = "receive data from client:   " + data_str
                        self.__dealReceiveMsg(msg)
                        #print("server recieve msg=",data_str)
                        sk1_or_conn.sendall(bytes(data_str, encoding="utf-8"))
                    except Exception as ex:
                        g_connSocketList.remove(sk1_or_conn)
                    else:
                        data_str = str(data_bytes, encoding="utf-8")
                        g_connMessageDic[sk1_or_conn].append(data_str)
                for conn in w_list:
                    recv_str = g_connMessageDic[conn][0]
                    del g_connMessageDic[conn][0]
                    conn.sendall(bytes(recv_str + "好", encoding="utf-8"))
                for sk in e_list:
                    g_connSocketList.remove(sk)
        self.s.close()
        g_connSocketList.clear()
        g_connMessageDic.clear()
        print("loop end!")
    def __dealReceiveMsg(self,msg):
        listBox = Fun.GetElement("Chat", "ListBox_8")
        listBox.insert(tkinter.END, msg)
