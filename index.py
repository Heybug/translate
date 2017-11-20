# coding: utf-8

"""
通过终端实现快速中文翻译
百度翻译API：
http://api.fanyi.baidu.com/api/trans/vip/translate
"""

import random
import hashlib  # MD5
import requests

# 翻译API
api = 'http://api.fanyi.baidu.com/api/trans/vip/translate'

# 参数
params = {
    'q': '',
    'from': 'auto',
    'to': 'en',
    'appid': 20171118000097027,
    'salt': random.randint(1000, 9999),
    'sign': ''
}


def fy():
    params['q'] = input('输入内容：')

    if params['q'] != 'end':
        # 判断输入的是否是英文
        if params['q'][0].encode('UTF-8').isalpha():
            params['to'] = 'zh'
        else:
            params['to'] = 'en'

        sing = str(params['appid']) + params['q'] + str(params['salt']) + 'QtgjZZ8qaS_wltn9klBj'
        params['sign'] = hashlib.md5(sing.encode('utf - 8')).hexdigest()

        # 发起post请求
        r = requests.post(api, data=params)
        z = r.json()['trans_result'][0]

        # 输出结果
        print('%s \n' % (z['dst']))
        fy()


fy()
