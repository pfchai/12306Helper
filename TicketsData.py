#!/usr/bin/env python
# encoding: utf-8
# @author: cc <chai_pengfei@163.com>

class TicketsData:
    """ process tickets data"""

    def __init__(self):
        self.seatType = {'硬座':'yz_num', '软座':'rz_num', '硬卧':'yw_num', '软卧':'rw_num', '一等座':'zy_num', '二等座':'ze_num',
                 '无座':'wz_num', '其他':'qt_num', '商务座':'swz_num', '特等座':'gg_num', '高级软卧':'gr_num'}
       #  self.seatType = {'No':'车次', 'st':'出发时间', 'at':'到达时间', 'la':'历时', seat = {'swz_num':'商务座', 'gg_num':'特等座',
       #      'zy_num':'一等座','ze_num':'二等座', 'gr_num':'高级软卧', 'rz_num':'软卧', 'yw_num':'硬卧', 'rz_num':'软座',
       #      'yz_num':'硬座', 'wz_num':'无座', 'qt_num':'其他'}}
        self.tickets = []
        self.beautifulFormat = "{0:^8}{1:^10} {2:^10} {3:^8}|{4:^10}{5:^10}{6:^10}{7:^10}{8:^10}{9:^8}{10:^8}{11:^8}{12:^8}{13:^8}{14:^8}"
        # self.beautifulFormat = ("{No:^8}{st:^10} {at:^10} {la:^8}|"
        #         "{seat[swz_num]:^10}{seat[gg_num]:^10}{seat[zy_num]:^10}{seat[ze_num]:^10}{seat[gr_num]:^10}{seat[rz_num]:^8}"
        #         "{seat[yw_num]:^8}{seat[rz_num]:^8}{seat[yz_num]:^8}{seat[wz_num]:^8}{seat[qt_num]:^8}")
        self.dataTitle = self.beautifulFormat.format('车次', '出发时间', '到达时间', '历时', '商务座', '特等座', '一等座',
                '二等座', '高级软卧', '软卧', '硬卧', '软座', '硬座', '无座', '其他')
        # self.beautifulData = self.dataTitle + '\n'
        self.beautifulData = '\n'

    def format_data(self, data):
        for train in data:
            print train
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
            line = self.beautifulFormat.format(t['trainNo'], t['trainStartTime'], t['trainArriveTime'], t['trainLast'],
                    t['trainSeat']['商务座'], t['trainSeat']['特等座'], t['trainSeat']['一等座'],
                    t['trainSeat']['二等座'], t['trainSeat']['高级软卧'], t['trainSeat']['软卧'], t['trainSeat']['硬卧'],
                    t['trainSeat']['软座'], t['trainSeat']['硬座'], t['trainSeat']['无座'], t['trainSeat']['其他'])
            self.beautifulData += (line + '\n')

    def __str__(self):
        return self.beautifulData

if __name__ == '__main__':
    tb = TicketsData()
