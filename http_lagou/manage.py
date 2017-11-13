#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2018, Deamon Cao,deamoncao100@gmail.com. 
@contact: deamoncao100@gmail.com
@software: garner
@file: manage.py
@time: 2017/11/8 8:48
@desc:
'''
from http_lagou.https import HttpUtil
from http_lagou.parse import Parse
from http_lagou.setting import headers as hd
# from http_lagou.setting import cookies as ck
import time
import logging
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s Process%(process)d:%(thread)d %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='diary.log',
                    filemode='a')


def getInfo(url, para):
    """
    获取信息
    """
    generalHttp = HttpUtil()
    htmlCode = generalHttp.post(url, params=para, headers=hd, cookies=None)
    print(htmlCode)
    generalParse = Parse(htmlCode)
    pageCount = generalParse.parsePage()
    info = []
    for i in range(1, pageCount+1):
        print('第%s页' % i)
        para['pn'] = str(i)
        htmlCode = generalHttp.post(url, params=para, headers=hd, cookies=None)
        generalParse = Parse(htmlCode)
        info = info + getInfoDetail(generalParse)
        time.sleep(1000)
    return info


def getInfoDetail(generalParse):
    """
    信息解析
    """
    info = generalParse.parseInfo()
    return info


def processInfo(info, para):
    """
    信息存储
    """
    logging.error('Process start')
    try:
        title = 'companyName,companyType,companyStage,companyLabel,companySize,companyDistrict,' \
                'positionType,positionEducation,positionAdvantage,positionSalary,positionWorkYear\n'
        file = open('%s.txt' % para['city'], 'a')
        file.write(title)
        for p in info:
            line = str(p['companyName']) + ',' + str(p['companyType']) + ',' + str(p['companyStage']) + ',' + \
                   str(p['companyLabel']) + ',' + str(p['companySize']) + ',' + str(p['companyDistrict']) + ',' + \
                   str(p['positionType']) + ',' + str(p['positionEducation']) + ',' + str(p['positionAdvantage']) + ',' +\
                   str(p['positionSalary']) + ',' + str(p['positionWorkYear']) + '\n'
            file.write(line)
        file.close()
        return True
    except:
        logging.error('Process except')
        return None


def main(url, para):
    """
    主函数逻辑
    """
    logging.error('Main start')
    print("Main Start.......")
    if url:
        info = getInfo(url, para)             # 获取信息
        flag = processInfo(info, para)             # 信息储存
        return flag
    else:
        return None


if __name__ == '__main__':
    kdList = [u'数据工程']
    cityList = [u'广州', u'深圳']
    url = 'https://www.lagou.com/jobs/positionAjax.json'
    for city in cityList:
        print('爬取%s' % city)
        para = {'first': 'true','pn': '1', 'kd': kdList[0], 'city': city}
        flag = main(url, para)
        if flag: print('%s爬取成功' % city)
        else: print('%s爬取失败' % city)
