# -*- coding: utf-8 -*-
import scrapy


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['m.lianjia.com']
    start_urls = ['https://m.lianjia.com/bj/xiaoqu/']

    def parse(self, response):
        print response.body
