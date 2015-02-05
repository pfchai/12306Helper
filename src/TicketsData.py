#!/usr/bin/env python
# encoding: utf-8
# @author: cc <chai_pengfei@163.com>

class TicketsData:
    """ Beautiful print tickets data"""

    def __init__(self, data):
        self.data = data
        self.beautifulFormat = u"{0:<9}{1:<9}{2:<9}{3:<9}|{4:^6}{5:^6}{6:^6}{7:^6}{8:^6}{9:^6}{10:^6}{11:^6}{12:^6}{13:^6}{14:^6}"
        self.dataTitle = self.beautifulFormat.format(u'车次', u'出发时间', u'到达时间', u'历时', u'商务座', u'特等座', u'一等座',
                u'二等座', u'高级软卧', u'软卧', u'硬卧', u'软座', u'硬座', u'无座', u'其他')
        self.beautifulData = self.dataTitle
        self.isTickets = False
        seatType = [u'swz_num', u'gg_num', u'zy_num', u'ze_num', u'gr_num', u'rw_num', u'yw_num', u'rz_num', u'yz_num', u'wz_num', u'qt_num']
        for d in self.data:
            for t in seatType:
                if d[t] != u'--' or d[t] != u'无':
                    self.isTickets = True

    def had_tickets(self):
        return self.isTickets

    def format_data(self, data):
        pass

    def format_print(self):
        for t in self.data:
            self.beautifulData += u'\n' + self.beautifulFormat.format(t[u'station_train_code'], t[u'start_time'], t[u'arrive_time'], t[u'lishi'],
                    t[u'swz_num'], t[u'gg_num'], t[u'zy_num'], t[u'ze_num'], t[u'gr_num'], t[u'rw_num'], t[u'yw_num'],
                    t[u'rz_num'], t[u'yz_num'], t[u'wz_num'], t[u'qt_num'])
        print self.beautifulData


if __name__ == '__main__':
    from Tickets import Tickets
    t = Tickets('LFV', 'WXH', '2015-03-01', 'ADULT')
    ticketsInfo = t.tickets_info()

    tb = TicketsData(ticketsInfo)
    tb.format_print()
