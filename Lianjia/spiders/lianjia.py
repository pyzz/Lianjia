# -*- coding: utf-8 -*-
import re
import scrapy
from Lianjia.items import LianjiaItem
from Lianjia.parses import HOUSE_INFO


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://bj.lianjia.com/ershoufang/']
    patt = re.compile(r'/pg\d{0,3}/')


    def parse(self, response):
        area_infos = response.xpath('/html/body/div[3]/div[1]/dl[2]/dd/div[1]/div/a')
        for area in area_infos[:1]:
        	area_url = response.urljoin(area.xpath('@href').extract_first())
        	area_name = area.xpath('text()').extract_first()
        	yield scrapy.Request(
        		area_url, 
        		meta={'area_name': area_name},
        		callback=self.list_page,
                priority=2,
        	)

    def list_page(self, response):
    	home_urls = response.xpath('/html/body/div[4]/div[1]/ul/li/div[1]/div[1]/a/@href').extract()
    	for url in home_urls[:1]:
    		yield scrapy.Request(
    			response.urljoin(url),
    			meta=response.meta,
    			callback=self.detail_page,
                priority=3,
    		)

        # 翻页
    	all_urls = response.xpath('//a/@href').extract()
    	next_page_urls = [url for url in all_urls if re.search(self.patt, url)]
    	for next_page in next_page_urls[:1]:
    		yield scrapy.Request(
    			response.urljoin(next_page),
    			callback=self.list_page,
    			meta=response.meta,
                priority=4,
    		)

    def detail_page(self, response):
        res_path = response.xpath
        item = LianjiaItem()
        item['area_name'] = response.meta['area_name']
    	item['page_url'] = response.url
        for key, patt in HOUSE_INFO.iteritems():
            item[key] = res_path(patt).extract_first()
        yield item







