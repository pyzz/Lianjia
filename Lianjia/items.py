# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    house_id = scrapy.Field()    # 房屋id
    area_name = scrapy.Field()  # 区名
    position_name = scrapy.Field()  # 地点名
    name = scrapy.Field()	# 名称
    price = scrapy.Field()	# 总价
    unit_all = scrapy.Field()	# 总价单位
    unit_price = scrapy.Field()	# 单价
    unit = scrapy.Field()	# 单位
    
    house_type = scrapy.Field()    # 户型
    house_floor = scrapy.Field()	# 楼层
    build_area = scrapy.Field()		# 建筑面积
    house_instruct = scrapy.Field() 	# 结构
    house_area_inter = scrapy.Field()	# 套内面积
    build_type = scrapy.Field()		# 建筑类型
    house_turend = scrapy.Field()	# 朝向
    build_instruct = scrapy.Field()   # 建筑结构
    fitment = scrapy.Field()   # 装修情况
    stairs = scrapy.Field()   # 梯户比例
    heating = scrapy.Field()   # 供暖方式
    lift = scrapy.Field()   # 电梯
    property_years = scrapy.Field()   # 产权

    hang_out_time = scrapy.Field()   # 挂牌时间
    trade = scrapy.Field()   # 交易权属
    pre_trade = scrapy.Field()   # 上次交易
    house_effect = scrapy.Field()   # 房屋用途
    house_years = scrapy.Field()   # 房屋年限
    property_blong = scrapy.Field() 	# 产权所属
    pledge_info = scrapy.Field() 	# 抵押信息
    backups = scrapy.Field() 	# 房本备件

    res_block_position = scrapy.Field()   # 经纬度
    page_url = scrapy.Field()   # 页面地址



class LianjiaSaleItem(scrapy.Item):
    house_id = scrapy.Field()  # 房屋id
    area_name = scrapy.Field()  # 区名
    position_name = scrapy.Field()  # 地点名
    name = scrapy.Field()	# 名称
    sale_time = scrapy.Field()  # 成交日期
    sale_price = scrapy.Field()  # 售价
    unit_price = scrapy.Field()  # 单价
    start_price = scrapy.Field()    # 挂牌价
    deal_time = scrapy.Field()  # 成交周期

    house_type = scrapy.Field() # 户型
    house_floor = scrapy.Field()  # 楼层
    build_area = scrapy.Field()  # 建筑面积
    house_instruct = scrapy.Field()  # 结构
    house_area_inter = scrapy.Field()  # 套内面积
    build_type = scrapy.Field()  # 建筑类型
    house_turend = scrapy.Field()  # 朝向
    build_year = scrapy.Field()     # 建成年代
    fitment = scrapy.Field()  # 装修情况
    build_instruct = scrapy.Field()  # 建筑结构
    heating = scrapy.Field()  # 供暖方式
    lift = scrapy.Field()  # 电梯
    property_years = scrapy.Field()  # 产权
    is_lift = scrapy.Field()    # 是否配备电梯

    res_block_position = scrapy.Field()   # 经纬度
    page_url = scrapy.Field()   # 页面地址


    
