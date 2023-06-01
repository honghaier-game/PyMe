import requests
import json
import tkinter
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Ticket():
    def __init__(self):
        self.fromStation = "北京"
        self.toStation = "昆明"
        self.ticketDate = "2021-07-06"

    def set_FromStation(self,fromStation):
        self.fromStation = fromStation
    def get_FromStation(self):
        return self.fromStation
    def set_ToStation(self,toStation):
        self.toStation = toStation
    def get_ToStation(self):
        return self.toStation
    def set_TicketDate(self,ticketDate):
        self.ticketDate = ticketDate
    def get_TicketDate(self):
        return self.ticketDate

    def createUrl(self):
        url = "https://train.qunar.com/dict/open/s2s.do?callback=jQuery17204587142557768573_1625466376212&dptStation=" + self.fromStation
        url = url + "&arrStation=" + self.toStation
        url = url + "&date=" + self.ticketDate
        url = url + "&type=normal&user=neibu&source=site&start=1&num=500&sort=3&_=1625466376638"
        return url

    def curlData(self,ListBox):
        ListBox.delete(0, tkinter.END)
        url = self.createUrl()
        try:
            r = requests.get(url, verify=False)
            if(r.status_code != 200):
                ListBox.insert(tkinter.END, "页面响应错误!")
                return
            # print(r.text)

            content = r.text
            index1 = content.find("(")
            index2 = content.find(")")
            content = content[index1 + 1:index2]
            dict = json.loads(content)
            #print(dict)
            if(not dict["ret"]):
                ListBox.insert(tkinter.END, "页面响应错误!")
                return

            dataList = dict['data']['s2sBeanList']
            for item in dataList:
                #print(item['trainNo'], item['dptStationName'], item['arrStationName'], item['dptTime'], item['arrTime'])
                showTxt = item['trainNo'] + "  |  " + item['dptStationName'] +"  |  " + item['arrStationName'] +"  |  "+ item['dptTime'] + "  |  " +item['arrTime'] + "  "

                for seat in item['seats'].values():
                    #print(seat['seatName'], seat['count'])
                    showTxt = showTxt + "  |  " + seat['seatName'] + "  " + str(seat['count']) + "张"
                ListBox.insert(tkinter.END,showTxt)
        except Exception as e:
            print(e)
            ListBox.insert(tkinter.END, "请求数据出现异常!")

'''
if __name__ == '__main__':
    query = Ticket()
    query.curlData()
'''