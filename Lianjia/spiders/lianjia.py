# -*- coding: utf-8 -*-
import re
import math
import scrapy
from Lianjia.items import LianjiaItem
from Lianjia.parses import HOUSE_INFO


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://bj.lianjia.com/ershoufang/']


    def __init__(self, home_type, *args, **kwargs):
        super(LianjiaSpider, self).__init__(*args, **kwargs)
        self.start_url = 'https://bj.lianjia.com/{}/'.format(home_type)

    def start_requests(self):
        return [scrapy.Request(self.start_url, callback=self.area)]

    def area(self, response):
        """区"""
        area_infos = response.xpath('/html/body/div[3]/div[1]/dl[2]/dd/div[1]/div/a')
        for area in area_infos[:1]:
            area_url = response.urljoin(area.xpath('@href').extract_first())
            area_name = area.xpath('text()').extract_first()
            yield scrapy.Request(
                area_url,
                meta={'area_name': area_name},
                callback=self.position,
                priority=2,
            )

    def position(self, response):
        positions = response.xpath('/html/body/div[3]/div[1]/dl[2]/dd/div[1]/div[2]/a')
        for pos in positions[:1]:
            pos_name = pos.xpath('text()').extract_first()
            pos_href = pos.xpath('@href').extract_first()
            yield scrapy.Request(
                response.urljoin(pos_href),
                callback=self.pos_count_page,
                meta={
                    'area_name': response.meta['area_name'],
                    'position_name': pos_name
                }
            )

    def pos_count_page(self, response):
        house_count = int(response.xpath('/html/body/div[4]/div[1]/div[2]/h2/span/text()').extract_first())
        if house_count != 0:
            pages = int(math.ceil(house_count / 30.0))
            for next_page in range(1, pages + 1)[:1]:
                url = ''.join((response.url, 'pg{}/'.format(next_page)))
                yield scrapy.Request(
                    url,
                    callback=self.list_page,
                    meta=response.meta,
                    priority=4,
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


    def detail_page(self, response):
        res_path = response.xpath
        item = LianjiaItem()
        item['area_name'] = response.meta['area_name']
        item['position_name'] = response.meta['position_name']
        item['page_url'] = response.url
        item['res_block_position'] = re.search(r"resblockPosition:'(.*?)'", response.body).group(1)
        for key, patt in HOUSE_INFO.iteritems():
            item[key] = res_path(patt).extract_first()
        yield item





