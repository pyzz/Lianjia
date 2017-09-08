# -*- coding: utf-8 -*-
import re
import math
import scrapy
from Lianjia.items import LianjiaItem, LianjiaSaleItem
from Lianjia.parses import HOUSE_INFO, SALE_HOUSE_INFO
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']


    def __init__(self, home_type, areas=None, *args, **kwargs):
        super(LianjiaSpider, self).__init__(*args, **kwargs)
        self.home_type = home_type
        self.start_url = 'https://bj.lianjia.com/{}/'.format(home_type)
        ascii_area_list = areas.split(' ')
        self.areas = [unicode(i) for i in ascii_area_list]

    def start_requests(self):
        return [scrapy.Request(self.start_url, callback=self.area, dont_filter=True)]

    def area(self, response):
        """区"""
        area_infos = response.xpath('/html/body/div[3]/div[1]/dl[2]/dd/div[1]/div/a')
        print area_infos, '=========='
        # 筛选地区
        if self.areas is not None:
            area_infos = [area for area in area_infos if area.xpath('text()').extract_first() in self.areas]
        print area_infos, '---------'
        print self.areas
        for area in area_infos:
            area_url = response.urljoin(area.xpath('@href').extract_first())
            area_name = area.xpath('text()').extract_first()
            yield scrapy.Request(
                area_url,
                meta={'area_name': area_name},
                callback=self.position,
                priority=2,
                dont_filter=True
            )

    def position(self, response):
        positions = response.xpath('/html/body/div[3]/div[1]/dl[2]/dd/div[1]/div[2]/a')
        for pos in positions:
            pos_name = pos.xpath('text()').extract_first()
            pos_href = pos.xpath('@href').extract_first()
            yield scrapy.Request(
                response.urljoin(pos_href),
                callback=self.pos_count_page,
                priority=3,
                meta={
                    'area_name': response.meta['area_name'],
                    'position_name': pos_name
                },
                dont_filter=True
            )

    def pos_count_page(self, response):
        house_count = 0
        if self.home_type == 'ershoufang':
            house_count = int(response.xpath('/html/body/div[4]/div[1]/div[2]/h2/span/text()').extract_first())
        elif self.home_type == 'chengjiao':
            house_count = int(response.xpath('/html/body/div[5]/div[1]/div[2]/div[1]/span/text()').extract_first())
        if house_count != 0:
            page_nums = int(math.ceil(house_count / 30.0))
            pages = page_nums if page_nums <= 100 else 100
            for next_page in range(1, pages + 1):
                url = ''.join((response.url, 'pg{}/'.format(next_page)))
                yield scrapy.Request(
                    url,
                    callback=self.list_page,
                    meta=response.meta,
                    priority=4,
                    dont_filter=True
                )


    def list_page(self, response):
        home_urls = []
        if self.home_type == 'ershoufang':
            home_urls = response.xpath('/html/body/div[4]/div[1]/ul/li/div[1]/div[1]/a/@href').extract()
        elif self.home_type == 'chengjiao':
            home_urls = response.xpath('/html/body/div[5]/div[1]/ul/li/a/@href').extract()

        for url in home_urls:
            yield scrapy.Request(
                response.urljoin(url),
                meta=response.meta,
                callback=self.detail_page,
                priority=10,
            )


    def detail_page(self, response):
        res = {}
        res['area_name'] = response.meta['area_name']
        res['position_name'] = response.meta['position_name']
        res['page_url'] = response.url
        res['res_block_position'] = re.search(r"resblockPosition:'(.*?)'", response.body).group(1)

        if self.home_type == 'ershoufang':
            for key, patt in HOUSE_INFO.iteritems():
                try:
                    res[key] = response.xpath(patt).extract_first().strip()
                except:
                    res[key] = None
            yield LianjiaItem(**res)

        elif self.home_type == 'chengjiao':
            for key, patt in SALE_HOUSE_INFO.iteritems():
                try:
                    res[key] = response.xpath(patt).extract_first().strip()
                except:
                    res[key] = None
            yield LianjiaSaleItem(**res)




