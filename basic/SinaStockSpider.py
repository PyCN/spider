#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2018, Deamon Cao,deamoncao100@gmail.com. 
@contact: deamoncao100@gmail.com
@software: garner
@file: SinaStockSpider.py
@time: 2017/11/5 16:36
@desc:使用Sina API获取新浪财经的证券股票数据接口
      本文只是一个使用多线程来爬取数据的Demo
'''

import requests
import threading

class SinaStockHandle(object):
    def __init__(self,basicUrl):
        self.basicUrl = basicUrl

    # 爬取股票
    def get_stock(self,code):
        url = self.basicUrl + code
        response = requests.get(url).text
        print(response)

    # 单线程
    def single_thread(self,codes):
        for code in codes:
            code = code.strip()
            self.get_stock(code)

    # 多线程
    def multi_thread(self,tasks,codes):
        # 用列表推导生成线程。
        threads = [threading.Thread(target = self.single_thread, args = (codes,)) for codes in tasks]
        # 启动线程
        for task in threads:
            task.start()
        # 等待线程结束
        for task in threads:
            task.join()

if __name__ == '__main__':
    codes = ['sh600001', 'sh600002', 'sh600003', 'sh600004', 'sh600005', 'sh600006']
    # 计算每个线程要做多少工作
    thread_len = int(len(codes) / 4)
    t1 = codes[0: thread_len]
    t2 = codes[thread_len: thread_len * 2]
    t3 = codes[thread_len * 2: thread_len * 3]
    t4 = codes[thread_len * 3:]
    tasks = [t1,t2,t3,t4]

    #
    basicUrl = 'http://hq.sinajs.cn/list='
    sinaStockHandle = SinaStockHandle(basicUrl)
    sinaStockHandle.multi_thread(tasks,codes)




