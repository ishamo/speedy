# -*- coding: utf-8 -*-

import scrapy
from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.images import ImagesPipeline
import json
import sys
import torndb


db = torndb.Connection('127.0.0.1', '51artist', 'root', '123456')

reload(sys)
sys.setdefaultencoding('utf-8')
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ArtworkPipeline(object):

    def process_item(self, item, spider):
        try:
            # db.query("insert into goods(amount, title, description, photo, age) value (%s, %s, %s, %s, %s)",
            #          item['amount'][0], item['title'][0], item['description'][0],
            #          u'http://www.mdguoji.cn' + item['photo'][0], item['age'][0])
            pass
        except:
            DropItem('item %s' % item)


class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        yield scrapy.Request('http://www.mdguoji.cn/' + item['photo'][0])

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
