#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2018, Deamon Cao,deamoncao100@gmail.com. 
@contact: deamoncao100@gmail.com
@software: garner
@file: ZipCodeSpider.py
@time: 2017/11/5 15:34
@desc: 爬取全国邮编编码,目前实现的只有省份的编码的爬取
'''

import requests
from xml.parsers.expat import ParserCreate

# 省份处理器
class ProvinceHandler(object):
    def __init__(self,provinces):
        self.provinces = provinces

    # 处理开始标签,仿照ParserCreate
    def proc_start_element(self,name,attrs):
        if name != 'map':
            name = attrs['title']
            herf = attrs['href']
            zipUrl = 'http://www.ip138.com' + herf
            zipCode = herf.replace('/','')
            self.provinces.append((name,zipCode,zipUrl))

    # 处理结束标签,仿照ParserCreate
    def proc_end_element(self,name):
        pass

    # 文本处理,仿照ParserCreate
    def proc_char_data(self,text):
        pass

# 城市处理器
class CityHandle(object):
    def __init__(self,citys):
        self.city

    def proc_start_element(self, name, attrs):
        pass

    # 处理结束标签
    def proc_end_element(self,name):
        pass

    # 文本处理
    def proc_char_data(self,text):
        pass



# 爬取省份编码信息
def get_province_entry(url):
    # 获取文本，并用gb2312解码
    content = requests.get(url).content.decode('gb2312')
    # 确定要查找字符串的开始结束位置，并用切片获取内容
    start = content.find('<map name="map_86" id="map_86">')
    end = content.find('</map>')
    content = content[start:end + len('</map>')].strip()
    provinces = []
    # 生成Sax处理器
    handler = ProvinceHandler(provinces)
    # 初始化分析器
    parser = ParserCreate()
    parser.StartElementHandler = handler.proc_start_element
    parser.EndElementHandler = handler.proc_end_element
    parser.CharacterDataHandler = handler.proc_char_data
    # 解析数据
    parser.Parse(content)
    # 结果字段为每一页的入口代码
    return provinces

if __name__ == '__main__':
    zipCodeUrl = 'http://www.ip138.com/post'
    provinces = get_province_entry(zipCodeUrl)
    print(provinces)
