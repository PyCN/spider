#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2018, Deamon Cao,deamoncao100@gmail.com. 
@contact: deamoncao100@gmail.com
@software: garner
@file: JsonDemon.py
@time: 2017/11/8 8:53
@desc:
'''

import demjson

if __name__ == '__main__':
    data = [{'code':'XN20171108','name':'虚拟单号0001','memo':'虚拟测试单号'}]
    print(demjson.encode(data))
