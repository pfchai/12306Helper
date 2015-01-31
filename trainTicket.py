#!/usr/bin/env python
# encoding: utf-8

import requests
import json
import time
import datetime
import collections



class trainTicket():
    """ 查询12306火车票余票信息 """

    def __init__(self, rideTime, fromStation, toStation, personType='ADULT'):
        # self.rideTime = time.strptime(rideTime, "%Y-%m-%d")
        self.rideTime = rideTime
        self.fromStation = fromStation
        self.toStation = toStation
        self.personType = personType

        self.header = {}
        self.zidian = {u'硬座':u'yz_num', u'软座':u'rz_num', u'硬卧':u'yw_num', u'软卧':u'rw_num', u'一等':u'zy_num', u'二等':u'ze_num',
            u'无座':u'wz_num', u'其他':u'qt_num'}
        self.ticketNum = {}
        self.seats = []


    def get_ticket_num(self):
        url = self.__makeGetUrl()
        data = self.__get_ticket_info(url)
        ticketNum = {}
        for train in data:
            train_info = train['queryLeftNewDTO']
            train_No = train_info['station_train_code']
            self.ticketNum[train_No] = {}
            num = collections.OrderedDict()
            for k in self.seats:
                num[k] = train_info[self.zidian[k]]
            ticketNum[train_No] = num

        self.printTicketNum(ticketNum)

        return ticketNum

    def printTicketNum(self, ticket_num):
        print "{0:<3} -> {1:<3}".format(self.fromStation, self.toStation,)
        for train in ticket_num:
            print(u'车次: {0:^5}'.format(train)),
            for (k,v) in ticket_num[train].items():
                print(u"{0}:{1}".format(k, v)),
            print ''

    def __get_ticket_info(self, url):
        # 防止一次get没有得到查询信息
        for i in range(5):
            r = requests.get(url, verify=False)
            print url
            print r.content
            text = json.loads(r.content)
            if text.has_key('data'):
                return text['data']

    def __makeGetUrl(self):
        return ("https://kyfw.12306.cn/otn/leftTicket/queryT?" + "leftTicketDTO.train_date=" +
            self.rideTime + "&leftTicketDTO.from_station=" + self.fromStation + "&leftTicketDTO.to_station=" +
            self.toStation + "&purpose_codes=" + self.personType)


if __name__ == '__main__':
    hh = trainTicket('2015-02-01', 'BJP',  'WXH')
    hh.get_ticket_num()

