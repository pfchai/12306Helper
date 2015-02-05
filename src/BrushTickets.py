#!/usr/bin/env python
# encoding: utf-8
# @author: cc <chai_pengfei@163.com>

from Tickets import Tickets
from StationName import StationName
from TicketsData import TicketsData
import time
import os


class BrushTickets:

    def __init__(self, fromStation, toStation, queryDate):
        self.stationNames = StationName()
        self.fromStation = self.stationNames.word2short(fromStation)
        self.toStation = self.stationNames.word2short(toStation)
        self.queryDate = queryDate
        self.tickets = Tickets(self.fromStation, self.toStation, self.queryDate)

        self.isAuto = False

    def run(self):
        if self.isAuto:
            while True:
                ticketsInfo = self.tickets.get_tickets_info()
                td = TicketsData(ticketsInfo )
                print td.had_tickets()
                if td.had_tickets():
                    os.system('sl')
                print time.ctime()
                td.format_print()
                time.sleep(10)
        else:
            ticketsInfo = self.tickets.get_tickets_info()
            td = TicketsData(ticketsInfo )
            print time.ctime()
            td.format_print()

    def setAuto(self, isAuto):
        " 设置是否自动查票 "
        self.isAuto = isAuto

if __name__ == '__main__':
    bt = BrushTickets('临汾', '无锡', '2015-02-07')
    bt.setAuto(True)
    bt.run()
