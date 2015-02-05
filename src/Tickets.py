#!/usr/bin/env python
# encoding: utf-8
# @author: cc <chai_pengfei@163.com>

import requests
import json

class TicketsException(Exception):
    pass

class Tickets():
    """ 从12306网站查询指定城市指定时间的车次信息 """

    def __init__(self, fromStation, toStation, queryDate, passType='ADULT'):
        self.fromStation = fromStation
        self.toStation = toStation
        self.queryDate = queryDate
        self.passType = passType
        self.ticketsInfo = None

    def tickets_info(self):
        " 返回查询到的车票信息 "
        return self.ticketsInfo
        pass

    def get_tickets_info(self):
        """ 查询车票信息 """
        req = self.__get_request()
        content = self.__process_data(req.content)
        if content == -1:
            raise TicketsException
        if content['data']['flag']:
            self.ticketsInfo = content['data']['datas']
            return self.ticketsInfo
        else:
            raise TicketsException

    def __process_data(self, content):
        " 将get请求得到的json数据转换为列表 "
        return json.loads(content)

    def __makeGetUrl(self):
        " 生成请求url "
        return("https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=" + self.passType +
                "&queryDate=" + self.queryDate + "&from_station=" + self.fromStation +
                "&to_station=" + self.toStation )

    def __make_headers(self, hasCookies):
        " 生成请求头文件 "
        " 暂时还没用到 "
        headers = ({'Accept' : '*/*',
                'Accept-Encoding' : 'gzip, deflate',
                'Accept-Language' : 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
                'Cache-Control' : 'no-cache',
                'Referer' : 'https://kyfw.12306.cn/otn/lcxxcx/init',
                'User-Agent' : 'Mozilla/5.0 (X11; Linux i686; rv:34.0) Gecko/20100101 Firefox/34.0',
                'Connection': 'keep-alive'})
        if hasCookies:
            headers['Cookies'] = self.__make_cookies()
            return headers
        else:
            return headers

    def __make_cookies():
        " 将cookies加到请求头文件中 "
        """ TODO: 修复cookies信息还的问题 """

        headers = self.__make_headers(False)
        r = requests.get('https://kyfw.12306.cn/otn/', headers = headers, verify=False)
        return ("JSSSIONID=" + r.cookies['JSESSIONID'] + "; BIGipServerotn=" + r.cookies['BIGipServerotn'] +
                '; jc_save_fromStation=%u4E34%u6C7E%2CLFV; _jc_save_toStation=%u5317%u4EAC%2CBJP; ' +
                '_jc_save_fromDate=2015-03-01; _jc_save_wfdc_flag=dc')

    def __get_request(self):
        " 发送get请求 "
        url = self.__makeGetUrl()
        headers = self.__make_headers(False)
        r = requests.get(url, headers = headers, verify=False)
        return r

    def __isGetInfo(self, req):
        " 判断是否得到余票结果 "
        if req['data']['flag']:
            return True
        else:
            return False

if __name__ == '__main__':
    t = Tickets('LFV', 'BJP', '2015-03-01', 'ADULT')
    print t.tickets_info()
