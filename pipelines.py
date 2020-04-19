# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MoviespiderPipeline(object):
    def __init__(self):
        print("新建文件")
        self.f = open('./DouBanMovieInfo.txt', 'w')

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        print("关闭文件")
        self.f.close()

    def process_item(self, item, spider):
        try:
            self.f.write("名称：" + str(item['name']) + '\n')
            self.f.write("导演：" + str(item['director']) + "\n")
            self.f.write("编剧：" + str(item['screenwriters']) + "\n")
            self.f.write("演员：" + str(item['actors']) + "\n")
            self.f.write("种类：" + str(item['category']) + "\n")
            self.f.write("上映地区：" + str(item['region']) + "\n")
            self.f.write("上映时间：" + str(item['date']) + "\n")
            self.f.write("片长：" + str(item['runtime']) + "\n")
            self.f.write("评分：" + str(item['rate']) + "\n")
            self.f.write("评分人数：" + str(item['rating_people']) + "\n")
            self.f.write("评分比例：" + str(item['stars_rate']) + "\n")
            self.f.write('\n')
        except:
            pass
        return item
