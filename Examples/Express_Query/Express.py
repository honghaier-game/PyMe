import urllib.request
import json
import tkinter


class   Express:
    def __init__(self):
        self.Company_Dict = {1:'shentong',2:'youzhengguonei',3:'yuantong',4:'shunfeng',5:'yunda',6:'zhongtong',7:"tiantian",8:"debang"}
        self.CompanyID = 4
        self.ExpressNumber = '0000001'
        self.ComboBox = None
    #设置CompanyID
    def set_CompanyID(self,companyID):
        self.CompanyID = companyID
    #获取CompanyID
    def get_CompanyID(self):
        return self.CompanyID
    #设置ExpressNumber
    def set_ExpressNumber(self,expressNumber):
        self.ExpressNumber = expressNumber
    #获取ExpressNumber
    def get_ExpressNumber(self):
        return self.ExpressNumber   
    #设置ComboBox
    def set_ComboBox(self,comboBox):
        self.ComboBox = comboBox
        self.ComboBox['values'] = ['申通快递','EMS邮政','圆通快递','顺丰快递','韵达快递','中通快递','天天快递','德邦快递']
        self.ComboBox.current(4)
    #获取ComboBox
    def get_ComboBox(self,comboBox):
        return self.ComboBox   
    #查询
    def Query(self,ListBox):
        ListBox.delete(0,tkinter.END)
        url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (self.Company_Dict[int(self.CompanyID)], self.ExpressNumber)
        response = urllib.request.urlopen(url)
        html = response.read().decode('utf-8')
        target = json.loads(html)
        #print(target)
        status = target['status']
        if status == '200':
            data = target['data']
            #print(data)
            data_len = len(data)
            
            for i in range(data_len):
                time_text = "时间: " + data[i]['time']
                ListBox.insert(tkinter.END,time_text)
                state_text = "状态: " + data[i]['context']
                ListBox.insert(tkinter.END,state_text)
        else:
            ListBox.insert(tkinter.END,"查询出现错误")
