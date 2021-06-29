import sqlite3
DbName = "test"
class Cdb:
    def __init__(self,dbName):
        self.dbName = dbName
        self.conn = None
        self.cursor = None
        self.__connect()
    def __connect(self):
        try:
            self.conn = sqlite3.connect(self.dbName)
            self.cursor = self.conn.cursor()
        except:
            print("conn db err!")
    def exec_query(self,sql,*parms):
        try:
            self.cursor.execute(sql,parms)
            values = self.cursor.fetchall()
        except:
            print("exec_query error,sql is=",sql)
            return None
        return values
    def exec_cmd(self,sql,*parms):
        try:
            self.cursor.execute(sql,parms)
            self.conn.commit()
        except:
            print("exec_cmd error,sql is=", sql)
    def close_connect(self):
        try:
            self.cursor.close()
            self.conn.close()
        except:
            print("close db err!")
def initDb():
    cdb = Cdb(DbName)
    sql = "create table if not exists user (id integer primary key autoincrement not null, name varchar(30), password varchar(30))"
    cdb.exec_cmd(sql)
    cdb.close_connect()
def deleteAccount(id):
    cdb = Cdb(DbName)
    sql1 = "delete from user where id=?"
    cdb.exec_cmd(sql1,id)
    cdb.close_connect()
def addAccountInfo(name,passWord):
    cdb = Cdb(DbName)
    sql1 = "insert into user (name,password) values (?,?)"
    cdb.exec_cmd(sql1, name, passWord)
    sql2 = "select max(id) from user"
    res = cdb.exec_query(sql2)
    cdb.close_connect()
    return res[0][0]
def editAccountInfo(id,name,passWord):
    cdb = Cdb(DbName)
    sql1 = "update user set name=?,password=? where id=?"
    cdb.exec_cmd(sql1, name, passWord, id)
    cdb.close_connect()
def getData():
    cdb = Cdb("test")
    sql2 = "select * from user"
    res = cdb.exec_query(sql2)
    cdb.close_connect()
    return res
if __name__ == '__main__':
    cdb = Cdb("test")
    delSql = "drop table user"
    #cdb.exec_cmd(delSql)
    sql1 = "insert into user (name,password) values (?,?)"
    cdb.exec_cmd(sql1,'sam','8888')
    sql2 = "select * from user where name=?"
    res = cdb.exec_query(sql2,'sam8')
    for item in res:
        print(item)
        print(item[0],item[1],item[2])
        id = item[0]
        name = item[1]
        password = item[2]
    cdb.close_connect()