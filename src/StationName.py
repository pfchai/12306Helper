#!/usr/bin/env python
# encoding: utf-8
# @author: cc <chai_pengfei@163.com>

import json

class StationName():

    def __init__(self):
        with open('stationName.ini', 'r') as f:
            text = f.readline()
            self.names = json.loads(text)

    def short2word(self, shorthan):
        pass

    def word2short(self, word):
        word = unicode(word, 'utf-8')
        if word in self.names:
            return self.names[word]

if __name__ == '__main__':
    sn = StationName()
    print sn.word2short('临汾')
