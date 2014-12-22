#!/usr/bin/env python
# encoding: utf-8

import requests
import json
import time
import ConfigParser
import datetime



class TrainHelper():
    """ 查询12306火车票余票 """

    def __init__(self):
        self.header = {}
        self.zidian = {u'yz_num':u'硬座', u'rz_num':u'软座', u'yw_num':u'硬卧', u'rw_num':u'软卧', u'zy_num':u'一等', u'ze_num':u'二等',
            u'wz_num':u'无座', u'qt_num':u'其他'}
        self.__init_paras()
        self.ticketNum = {}

    def acqureTick(self):
        for d in self.Dates:
            ticket_num = self.getTicketNum(d.strftime('%Y-%m-%d'))
            print d
            self.printTicketNum(ticket_num)

    def getTicketNum(self, the_date):
        url = self.__makeGetUrl(the_date)
        data = self.getTicketInfo(url)
        self.ticketNum = {}
        for train in data:
            train_info = train['queryLeftNewDTO']
            train_No = train_info['station_train_code']
            self.ticketNum[train_No] = {}
            num = {}
            for k in self.zidian:
                num[k] = train_info[k]
          #       if train['queryLeftNewDTO'][k] != u'无' and train['queryLeftNewDTO'][k] != u'--' :
          #           print (u"傻逼！快去看12306，有{0}票了！！！".format(k))
            self.ticketNum[train_No] = num
        return self.ticketNum

    def printTicketNum(self, ticket_num):
        print "{0:<3} -> {1:<3}".format(self.fromStation, self.toStation,)
        for train in ticket_num:
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

    def __makeGetUrl(self, the_date):
        return ("https://kyfw.12306.cn/otn/leftTicket/queryT?" + "leftTicketDTO.train_date=" +
            the_date + "&leftTicketDTO.from_station=" + self.fromStation + "&leftTicketDTO.to_station=" +
            self.toStation + "&purpose_codes=" + self.personType)

    def __init_paras(self):
        config = ConfigParser.ConfigParser()
        config.read('conf.ini')

        begin_date = config.get('Date','BeginDate')
        end_date = config.get('Date','EndDate')
        self.Dates = []
        begin_date = time.strptime(begin_date, "%Y-%m-%d")
        end_date = time.strptime(end_date, "%Y-%m-%d")
        begin_date = datetime.datetime(begin_date[0], begin_date[1], begin_date[2])
        end_date = datetime.datetime(end_date[0], end_date[1], end_date[2])
        while begin_date <= end_date:
            self.Dates.append(begin_date)
            begin_date = begin_date + datetime.timedelta(days=1)

        self.personType = config.get('PersonType', 'Type')
        fromStation = unicode(config.get('StationInfo', 'FromStation'), 'utf-8')
        toStation = unicode(config.get('StationInfo', 'ToStation'), 'utf-8')
        with open('stationName.ini') as f:
            text = f.readline()
            js = json.loads(text)
            self.fromStation = js[fromStation]
            self.toStation = js[toStation]


if __name__ == '__main__':
    hh = TrainHelper()
    hh.acqureTick()

