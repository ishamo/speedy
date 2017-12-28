# -*- coding: utf-8 -*-
import scrapy
from ..items import ArtworkItem


class MdguojiSpider(scrapy.Spider):
    name = 'mdguoji'
    allowed_domains = ['www.mdguoji.cn']
    start_urls = [
        'http://www.mdguoji.cn/auction.aspx?ParentId=2&BaseInfoCateId=20&CateId=20',  # 瓷器
        # 'http://www.mdguoji.cn/auction.aspx?ParentId=2&BaseInfoCateId=22&CateId=22',  # 字画
        # 'http://www.mdguoji.cn/auction.aspx?ParentId=2&BaseInfoCateId=21&CateId=21', # 玉器
        # 'http://www.mdguoji.cn/auction.aspx?BaseInfoCateId=41&CateId=41', # 杂项
    ]

    def parse(self, response):
        for sel in response.xpath('/html/body/ul/li'):
            item = ArtworkItem()
            item['photo'] = sel.xpath('a/img/@src').extract()
            item['title'] = sel.xpath('a/h4/text()').extract()
            item['amount'] = sel.xpath('a/h5').extract()
            follow_url = sel.xpath('a/@href').extract()
            follow_url = 'http://www.mdguoji.cn/' + follow_url[0]
            yield scrapy.Request(follow_url, callback=self.parse_description, meta={'item': item})

    def parse_description(self, response):
        item = response.meta['item']
        item['description'] = response.xpath('/html/body/div[6]/div[1]/div[1]/div[2]/div[2]/div/p[2]/text()').extract()
        item['age'] = response.xpath('/html/body/div[6]/div[1]/div[1]/div[2]/div[2]/div/p[1]/text()').extract()
        return item
