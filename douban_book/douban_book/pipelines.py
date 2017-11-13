# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import xlwt

class DoubanBookPipeline(object):

    def open_spider(self, out_file):
        self.row = 0
        # self.out = open(out_file,'w'
        self.workbook=xlwt.Workbook(encoding='utf-8')
        self.booksheet=self.workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
        self.booksheet.write(self.row,0,'书名')
        self.booksheet.write(self.row,1,'作者')
        self.booksheet.write(self.row,2,'价格')
        self.booksheet.write(self.row,3,'出版年份')
        self.booksheet.write(self.row,4,'出版社')
        self.booksheet.write(self.row,5,'评分')

    def close_spider(self, out_file):
        self.workbook.save('C:\develop\code\Python\scrapy\spider\douban_book\douban_book.xls')

    def process_item(self, item, spider):
        if item['name'].strip() != '':
            self.row = self.row + 1
            self.booksheet.write(self.row, 0,item['name'])
            self.booksheet.write(self.row, 1, item['author'])
            self.booksheet.write(self.row, 2, item['price'])
            self.booksheet.write(self.row, 3, item['edition_year'])
            self.booksheet.write(self.row, 4, item['publisher'])
            self.booksheet.write(self.row, 5, item['ratings'])
        return item
