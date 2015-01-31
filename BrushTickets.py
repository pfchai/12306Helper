#!/usr/bin/env python
# encoding: utf-8
# @author: cc <chai_pengfei@163.com>

from Tickets import Tickets
from StationName import StationName

class BrushTickets:

    def __init__(self, fromStation, toStation, queryDate):
        self.sn = StationName()
        self.fromStation = self.sn.word2short(fromStation)
        self.toStation = self.sn.word2short(toStation)
        self.queryDate = queryDate
        self.tickets = Tickets(self.fromStation, self.toStation, self.queryDate)

        self.isAuto = False

    def run(self):
        print self.tickets.tickets_info()

    def setAuto(self, isAuto):
        " 设置是否自动查票 "
        self.isAuto = isAuto

if __name__ == '__main__':
    bt = BrushTickets('临汾', '无锡', '2015-03-03')
    bt.run()
