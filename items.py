# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    director = scrapy.Field()
    screenwriters = scrapy.Field()
    actors = scrapy.Field()
    category = scrapy.Field()
    region = scrapy.Field
    date = scrapy.Field()
    runtime = scrapy.Field()
    rate = scrapy.Field()
    rating_people = scrapy.Field()
    stars_rate = scrapy.Field()
