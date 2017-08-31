# coding:utf-8

from sqlalchemy import Column, String, TIMESTAMP, Text, Date, Integer
from sqlalchemy.sql import func

from basic_db import Base


class Lianjia(Base):
    __tablename__ = "lianjia_table"

    house_id = Column(String(200), primary_key=True)
    area_name = Column(String(200))
    position_name = Column(String(200))
    name = Column(String(200))
    unit_all = Column(String(200))
    price = Column(String(200))
    unit_price = Column(String(200))
    unit = Column(String(200))

    house_type = Column(String(200))
    house_floor = Column(String(200))
    build_area = Column(String(200))
    house_instruct = Column(String(200))
    house_area_inter = Column(String(200))
    build_type = Column(String(200))
    house_turend = Column(String(200))
    build_instruct = Column(String(200))
    fitment = Column(String(200))
    stairs = Column(String(200))
    heating = Column(String(200))
    lift = Column(String(200))
    property_years = Column(String(200))

    hang_out_time = Column(String(200))
    trade = Column(String(200))
    pre_trade = Column(String(200))
    house_effect = Column(String(200))
    house_years = Column(String(200))
    property_blong = Column(String(200))
    pledge_info = Column(String(200))
    backups = Column(String(200))
    res_block_position = Column(String(200))

    create_time = Column(TIMESTAMP, server_default=func.now())   
    page_url = Column(String(200))
    
    
class LianjiaSale(Base):
    __tablename__ = "lianjia_sale_table"

    house_id = Column(String(200), primary_key=True)  # 房屋id
    area_name = Column(String(200))  # 区名
    position_name = Column(String(200))  # 地点名
    name = Column(String(200))  # 名称
    sale_time = Column(String(200))  # 成交日期
    sale_price = Column(String(200))  # 售价
    unit_price = Column(String(200))  # 单价
    start_price = Column(String(200))  # 挂牌价
    deal_time = Column(String(200))  # 成交周期

    house_type = Column(String(200))  # 户型
    house_floor = Column(String(200))  # 楼层
    build_area = Column(String(200))  # 建筑面积
    house_instruct = Column(String(200))  # 结构
    house_area_inter = Column(String(200))  # 套内面积
    build_type = Column(String(200))  # 建筑类型
    house_turend = Column(String(200))  # 朝向
    build_year = Column(String(200))  # 建成年代
    fitment = Column(String(200))  # 装修情况
    build_instruct = Column(String(200))  # 建筑结构
    heating = Column(String(200))  # 供暖方式
    lift = Column(String(200))  # 电梯
    property_years = Column(String(200))  # 产权
    is_lift = Column(String(200))  # 是否配备电梯

    res_block_position = Column(String(200))    # 经纬度

    create_time = Column(TIMESTAMP, server_default=func.now())
    page_url = Column(String(200))