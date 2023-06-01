import time
from SelectServer import SelectServer
from CClientSocket import CClientSocket
class CServiceMangerBase():
    #listServer = []
    #serviceClass=SelectServer
    @staticmethod
    def startService(serviceClass,listServer,ip='127.0.0.1',port=8989):
        #需要先销毁，重新创建实例，才能重启
        aliveServer = None
        for server in listServer:
            if(server.is_alive() == False):
                listServer.remove(server)
            else:
                aliveServer = server
        if(aliveServer == None):
            #server = SelectServer(ip,port)
            server = serviceClass(ip, port)
            server.start()
            time.sleep(1)
            listServer.append(server)
            print(server.name)
            return (server.is_alive())
        return (aliveServer.is_alive())
    @staticmethod
    def stopService(listServer):
        for server in listServer:
            if(server.is_alive() == True):
                server.stopServer()
                time.sleep(1)
        listServer.clear()
        return True
    @staticmethod
    def getService(listServer):
        for server in listServer:
            if(server.is_alive() == True):
                return server
        return None
class CSelectServerManger(CServiceMangerBase):
    listServer = []
    serviceClass=SelectServer
    @staticmethod
    def startService(ip='127.0.0.1',port=8989):
        return CServiceMangerBase.startService(CSelectServerManger.serviceClass,CSelectServerManger.listServer)
    @staticmethod
    def stopService():
        return CServiceMangerBase.stopService(CSelectServerManger.listServer)
    @staticmethod
    def getService():
        return CServiceMangerBase.getService(CSelectServerManger.listServer)
class CClientSocketManger(CServiceMangerBase):
    listServer = []
    serviceClass=CClientSocket
    @staticmethod
    def startService(ip='127.0.0.1',port=8989):
        return CServiceMangerBase.startService(CClientSocketManger.serviceClass,CClientSocketManger.listServer)
    @staticmethod
    def stopService():
        return CServiceMangerBase.stopService(CClientSocketManger.listServer)
    @staticmethod
    def getService():
        return CServiceMangerBase.getService(CClientSocketManger.listServer)
