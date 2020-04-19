import json

import scrapy
from bs4 import BeautifulSoup


class DouBanSpider(scrapy.Spider):
    name = 'adouban_spider'
    start_urls = ['https://movie.douban.com/tag/#/']
    allowed_domains = ['movie.douban.com']

    def parse(self, response):
        for count in range(0, 27002, 20):
            fir_url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start={}'.format(count)
            yield scrapy.Request(
                fir_url,
                callback=self.parse_main
            )

    def parse_main(self, response):
        infos = json.loads(response.body.decode('utf-8'))
        '名称 封面图片 简介 评分 短评top100'
        print(infos)
        datas = infos['data']
        for data in datas:
            title = data['title']  # 名称
            cover = data['cover']  # 封面图片
            rate = data['rate']  # 评分
            url = data['url']  # 详情url
            id = str(data['id'])
            if url:
                print(title, cover, rate, url)
                yield scrapy.Request(url, callback=self.parse_detail, meta={'id': id})

    def parse_detail(self, response):
        strid = response.meta['id']
        base_url = 'https://movie.douban.com/subject/{}/comments?'.format(strid)
        # 全部评论的链接
        b_url = 'https://movie.douban.com/subject/{}/comments?status=P'.format(strid)
        # 前一百条评论
        n_url = 'https://movie.douban.com/subject/4920528/comments?start=0&limit=20&sort=new_score&status=P'
        for page in range(0, 100, 20):
            n_url = base_url + 'start={}&limit=20&sort=new_score&status=P'.format(page)
            print('n_url################# ', n_url)
            if n_url:
                yield scrapy.Request(b_url, callback=self.parse_comment)

        soup = BeautifulSoup(response.body, 'lxml')
        # 简介(先隐藏后不隐藏的)
        try:
            abstract = soup.find('span', class_='all hidden').get_text()
        except:
            abstract = soup.find('span', attrs={'property': 'v:summary'}).get_text()
            pass
        # print('abstract -------- ',abstract)

    def parse_comment(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        shorts = soup.find_all('span', class_='short')
        for short in shorts:
            print('short =============  ', short.get_text())
