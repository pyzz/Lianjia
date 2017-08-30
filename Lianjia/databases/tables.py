# coding:utf-8

from sqlalchemy import Column, String, TIMESTAMP, Text, Date, Integer
from sqlalchemy.sql import func

from basic_db import Base


class Lianjia(Base):
    __tablename__ = "lianjia_table"

    house_id = Column(String(200), primary_key=True)
    area_name = Column(String(200))   
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

    create_time = Column(TIMESTAMP, server_default=func.now())   
    page_url = Column(String(200))