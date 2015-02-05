#!/usr/bin/env python
# encoding: utf-8
# @author: cc <chai_pengfei@163.com>

import requests
from PIL import Image
from StringIO import StringIO



def login():
    url = "https://kyfw.12306.cn/otn/login/init"
    s = requests.session()
    r = s.get(url, verify=False)

    url2 = "https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=login&rand=sjrand";
    r2 = s.get(url2, verify = False)
    i = Image.open(StringIO(r2.content))
    i.show()

    codeStr = raw_input('')

    print '-------------check code'
    ajaxUrl = 'https://kyfw.12306.cn/otn/passcodeNew/checkRandCodeAnsy'
    dc = {'randCode' : codeStr,
            'rand':'sjrand'}
    r3 = s.get(ajaxUrl, verify = False, params=dc)
    print r3

    LoginUrl = "http://kyfw.12306.cn/otn/login/loginAysnSuggest"
    dc = {
        'randCode'      :  codeStr,
        'userDTO.password'     : "sunyuke1989",
        'loginUserDTO.user_name': "sunyuke@qq.com",
        "NDgyMjA2" :  "NDVlNGE4YzZhMmJmMTI3ZQ=="
    }
    r4 = s.post(LoginUrl, data=dc)
    print r4.text


if __name__ == '__main__':
    login()

