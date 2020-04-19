# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook

class MoviespiderPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['名称', '导演', '编剧', '演员', '种类', '上映地区', '上映时间', '片长', '评分', '评分人数', '评分比例'])

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.wb.save('信息表.xlsx')

    def process_item(self, item, spider):
        try:
            line = []
            for k in item:
                if isinstance(item[k],list):
                    value = ','.join(item[k])
                else:
                    value = item[k]
                line.append(value)
            self.ws.append(line)
        except:
            pass
        return item
