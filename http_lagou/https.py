#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2018, Deamon Cao,deamoncao100@gmail.com. 
@contact: deamoncao100@gmail.com
@software: garner
@file: https.py
@time: 2017/11/8 0:21
@desc: http工具类
'''

from http_lagou.setting import IP,UA,headers
import requests,random
import logging

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s Process%(process)d:%(thread)d %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='lagou.log',
                    filemode='a')

# http请求的工具类
class HttpUtil(object):

    def __init__(self):
        pass

    # 通过GET获取网页soucecode
    def get(self, url,headers=headers, cookies=None, proxy=IP, timeout=5, timeoutRetry=5):
        """
        :param url: 网页链接
        :param headers: headers
        :param cookies: cookies
        :param proxy: 代理
        :param timeout: 请求超时
        :param timeoutRetry: 超时重试次数
        :return:soucecode
        """
        if not url:
            logging.error('url not exits')
            return 'None'
        logging.info('get %s' % url)
        try:
            print('---headers:',UA[random.randint(0, len(UA) - 1)])
            if not headers:
                print('headers')
                headers = {'User-Agent': UA[random.randint(0, len(UA) - 1)]}
            response = requests.get(url, headers=headers, cookies=cookies, proxies=IP, timeout=timeout)
            if response.status_code == 200 or response.status_code == 302:
                htmlCode = response.text
            else:
                htmlCode = 'None'
            logging.info('get %s %s' % (str(response.status_code), url))
        except Exception as e:
            logging.error('get %s ' % str(e))
            if timeoutRetry > 0:
                htmlCode = self.get(url=url, timeoutRetry = (timeoutRetry-1))
            else:
                logging.error('get timeout %s ' % url)
                htmlCode='None'
        return htmlCode

    # 通过POST获取网页soucecode
    def post(self, url, params, headers=None, cookies=None, proxy=IP, timeout=5, timeoutRetry=5):
        '''
        :param url:
        :param params:
        :param headers:
        :param cookies:
        :param proxy:
        :param timeout:
        :param timeoutRetry:
        :return:
        '''
        print('ip..........')
        if not url or not params:
            logging.error('Post Error url or params not exit')
            return None
        logging.error('Post %s' % url)
        try:
            # print('---headers:', UA[random.randint(0, len(UA) - 1)])
            if not headers:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3'}
            response = requests.post(url, data=params, headers=headers, cookies=cookies, proxies=proxy, timeout=timeout)
            if response.status_code == 200 or response.status_code == 302:
                htmlCode = response.text
            else:
                htmlCode = None
            logging.error('Post %s %s' % (str(response.status_code), url))
        except Exception as e:
            logging.error('Post Except %s' % str(e))
            if timeoutRetry > 0:
                htmlCode = self.post(url=url, para=params, timeOutRetry=(timeoutRetry - 1))
            else:
                logging.error('Post timeout %s' % url)
                htmlCode = None
        return htmlCode

    # # 获取网页title判断是否被ban
    def confirm(self, htmlCode, url, headers, cookies, proxy, catch_retry=5):
        '''
        :param htmlCode:
        :param url:
        :param headers:
        :param cookies:
        :param proxy:
        :param catch_retry:
        :return:
        '''
        return htmlCode

    # 对url进行处理
    def urlprocess(self, items):
        '''
        :param items:
        :return:
        '''
        # +    URL 中+号表示空格               %2B
        # 空格 URL中的空格可以用+号或者编码    %20
        # /    分隔目录和子目录                %2F
        # ?    分隔实际的URL和参数             %3F
        # %    指定特殊字符                    %25
        # #    表示书签                        %23
        # &    URL 中指定的参数间的分隔符      %26
        # =    URL 中指定参数的值              %3D
        content = items.replace('&#047;', '%2F').replace('&#061;', '%3D').replace('+', '%2B').replace( \
            ' ', '%20').replace('/', '%2F').replace('?', '%3F').replace('=', '%3D')
        return content


