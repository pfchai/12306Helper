#!/usr/bin/env python
# encoding: utf-8
# @author: cc <chai_pengfei@163.com>

class TicketsData:
    """ process tickets data"""

    def __init__(self):
        self.seatType = {'硬座':'yz_nm', '软座':'rz_nm', '硬卧':'yw_nm', '软卧':'rw_nm', '一等':'zy_nm', '二等':'ze_nm',
                '无座':'wz_nm', '其他':'qt_nm', '商务座':'swz_nm', '特等座':'gg_nm', '高级软卧':'gr_nm'}
        self.tickets = []
        self.beautifulFormat = "{0:^8}{1:^10} {2:^10} {3:^8}|{4:^10}{5:^10}{6:^10}{7:^10}{8:^10}{9:^8}{10:^8}{11:^8}{12:^8}{13:^8}{14:^8}"
        self.dataTitle = self.beautifulFormat.format('车次', '出发时间', '到达时间', '历时', '商务座', '特等座', '一等座',
                '二等座', '高级软卧', '软卧', '硬卧', '软座', '硬座', '无座', '其他')
        self.beautifulData = self.dataTitle + '\n'

    def format_data(self, data):
        for train in data:
            trainInfo = {}
            trainInfo['trainNo'] = train['station_train_code']
            trainInfo['trainStartTime'] = train['start_time']
            trainInfo['trainArriveTime'] = train['arrive_time']
            trainInfo['trainLast'] = train['lishi']
            trainSeat = {}
            for key, value in self.seatType.items():
                trainSeat[key] = train[value]
            trainInfo['trainSeat'] = trainSeat
            self.tickets.append(trainInfo)
        return self.tickets

    def beautifulData(self, tickets):
        for train in tickets:
            print train

    def format_print(self, data):
        tickets = self.format_data(data)
        for t in tickets:
            # s = beautifulFormat.format(t['trainNo'], t['trainStartTime'], t['trainArriveTime'], t['trainLast'], t['trainSeat'])
            pass

    def __str__(self):
        pass

if __name__ == '__main__':
    tb = TicketsData()
