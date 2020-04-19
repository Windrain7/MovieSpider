# -*- coding: utf-8 -*-
import json
import scrapy
import re

from MovieSpider.items import MovieItem


class DoubanspiderSpider(scrapy.Spider):
    name = 'DouBanSpider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/tag/#/']

    def parse(self, response):
        #第三个参数是步长
        for count in range(0, 100, 20):
            fir_url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start={}'.format(count)
            yield scrapy.Request(fir_url, callback=self.parse_main)

    def parse_main(self, response):
        datas = json.loads(response.text)['data']
        for data in datas:
            try:
                url = data['url']  # 详情url
                yield scrapy.Request(url, callback=self.parse_detail)
            except:
                continue

    def parse_detail(self, response):
        contents = response.xpath('//div[@id="content"]')
        for info in contents:
            try:
                item = MovieItem()
                item['name'] = info.xpath('h1/span[1]/text()').extract()
                item['director'] = info.xpath('//div[@id="info"]/span[1]/span[2]/a/text()').extract()
                item['screenwriters'] = info.xpath('//div[@id="info"]/span[2]/span[2]/a/text()').extract()
                item['actors'] = info.xpath('//div[@id="info"]/span[@class="actor"]/span[2]//a/text()').extract()
                item['category'] = info.xpath('//div[@id="info"]//span[@property="v:genre"]/text()').extract()
                text = str(info.xpath('//*[@id="info"]/text()'))
                region = re.search(r'[\u4e00-\u9fa5]+', text).group(0)
                item['region'] = region
                item['date'] = info.xpath('//div[@id="info"]/span[@property="v:initialReleaseDate"]/text()').extract()
                item['runtime'] = info.xpath('//div[@id="info"]/span[@property="v:runtime"]/text()').extract()
                item['rate'] = info.xpath('//div[@id="interest_sectl"]//strong[@class="ll rating_num"]/text()').extract()
                item['rating_people'] = info.xpath('//div[@id="interest_sectl"]//span[@property="v:votes"]/text()').extract()
                item['stars_rate'] = info.xpath('//div[@id="interest_sectl"]//span[@class="rating_per"]/text()').extract()
                yield item
            except:
                continue

