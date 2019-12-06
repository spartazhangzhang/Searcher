# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    keywords = scrapy.Fielf()
    url = scrapy.Field()
    links = scrapy.Field()
    link_texts = scrapy.Field()
    simhash = scrapy.Field() # simhash code ,depend on title description keywords and link texts
