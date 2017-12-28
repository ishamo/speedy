# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArtworkItem(scrapy.Item):
    photo = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    age = scrapy.Field()
    amount = scrapy.Field()
