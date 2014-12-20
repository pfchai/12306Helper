#!/usr/bin/env python
# encoding: utf-8

import requests
import json
import time
import sys
import ConfigParser



class trainHelper():
    """ 查询12306火车票余票 """

    def __init__(self, fromStation, toStation, date, personType='ADULT'):
        self.header = {}
        self.zidian = {u'yz_num':u'硬座', u'rz_num':u'软座', u'yw_num':u'硬卧', u'rw_num':u'软卧', u'zy_num':u'一等', u'ze_num':u'二等',
            u'wz_num':u'无座', u'qt_num':u'其他'}
        self.fromStation = fromStation
        self.toStation = toStation
        self.date = date
        self.personType = personType
        self.ticketNum = {}

    def getTicketNum(self):
        url = self.__makeGetUrl()
        data = self.getTicketInfo(url)
        self.ticketNum = {}
        for train in data:
            train_info = train['queryLeftNewDTO']
            train_No = train_info['station_train_code']
            self.ticketNum[train_No] = {}
            num = {}
            for k in self.zidian:
                num[k] = train_info[k]
                if train['queryLeftNewDTO'][k] != u'无' and train['queryLeftNewDTO'][k] != u'--' :
                    print (u"傻逼！快去看12306，有{0}票了！！！".format(k))
            self.ticketNum[train_No] = num
        return self.ticketNum

    def printTicketNum(self):
        print "{0:<3} -> {1:<3} {2}".format(self.fromStation, self.toStation, self.date)
        for train in self.ticketNum:
            print(u'车次: {0:^5}'.format(train)),
            for (k,v) in self.ticketNum[train].items():
                print(u"{0}:{1}".format(self.zidian[k], v)),
            print ''

    def getTicketInfo(self, url):
        # 防止一次get没有得到查询信息
        for i in range(5):
            r = requests.get(url, verify=False)
            text = json.loads(r.content)
            if text.has_key('data'):
                return text['data']

    def __makeGetUrl(self):
        return ("https://kyfw.12306.cn/otn/leftTicket/queryT?" + "leftTicketDTO.train_date=" +
            self.date + "&leftTicketDTO.from_station=" + self.fromStation + "&leftTicketDTO.to_station=" +
            self.toStation + "&purpose_codes=" + self.personType)

def trans(fstation, t):
    t = unicode(t, 'utf-8')
    fstation = unicode(fstation, 'utf-8')
    with open('stationName.ini') as f:
        text = f.readline()
        js = json.loads(text)
        return js[fstation], js[t]

if __name__ == '__main__':
    config = ConfigParser.ConfigParser()
    config.read('infor.conf')
    fstation, tstation = trans(config.get('info','from'), config.get('info','to'))
    date = config.get('info','date')
    print date
    hh = trainHelper(fstation, tstation, date)
    # hh = trainHelper('BJP', 'LFV', '2015-02-15')
    hh.getTicketNum()
    hh.printTicketNum()

