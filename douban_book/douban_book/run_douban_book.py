#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2018, Deamon Cao,deamoncao100@gmail.com. 
@contact: deamoncao100@gmail.com
@software: garner
@file: run_douban_book.py
@time: 2017/11/7 8:46
@desc:
'''

from scrapy import cmdline

cmd = 'scrapy crawl douban_book'
cmdline.execute(cmd.split())