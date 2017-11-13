#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2018, Deamon Cao,deamoncao100@gmail.com. 
@contact: deamoncao100@gmail.com
@software: garner
@file: book_spider.py
@time: 2017/11/6 23:32
@desc:
'''

import scrapy
# from ..items import DoubanBookItem
from douban_book.items import DoubanBookItem

class BookSpider(scrapy.Spider):
    name = 'douban_book'
    start_urls = ['https://book.douban.com/top250']

    def parse(self,response):
        # 请求第一页
        yield scrapy.Request(response.url,callback=self.parse_page)

        # 请求其他页
        for page in response.xpath('//div[@class="paginator"]/a'):
            link = page.xpath('@href').extract()[0]
            yield scrapy.Request(link, callback=self.parse_page)

    def parse_page(self,response):
        for item in response.xpath('//tr[@class="item"]'):
            book = DoubanBookItem()
            book['name'] = item.xpath('td[2]/div[1]/a/@title').extract()[0]
            book['ratings'] = item.xpath('td[2]/div[2]/span[@class="rating_nums"]/text()').extract()[0]
            book_info = item.xpath('td[2]/p[1]/text()').extract()[0]
            book_info_contents = book_info.strip().split(" / ")
            book['author'] = book_info_contents[0]
            book['publisher'] = book_info_contents[1]
            book['edition_year'] = book_info_contents[2]
            book['price'] = book_info_contents[3]
            yield book


