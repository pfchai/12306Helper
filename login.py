#!/usr/bin/env python
# encoding: utf-8
# @author: cc <chai_pengfei@163.com>

import requests
from PIL import Image
from StringIO import StringIO
import pylab



def login():
    url = "https://kyfw.12306.cn/otn/login/init"
    s = requests.session()
    r = s.get(url, verify=False)

    url2 = "https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=login&rand=sjrand";
    r2 = s.get(url2, verify = False)
    i = Image.open(StringIO(r2.content))
    pylab.subplot(111)
    pylab.imshow(i)
    pylab.show()
    i.show()

    yanzhengma = raw_input('')


if __name__ == '__main__':
    login()

