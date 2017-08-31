# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from databases.basic_db import engine, session
from databases.tables import *
from items import LianjiaItem, LianjiaSaleItem

class LianjiaPipeline(object):
    
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = session

    def process_item(self, item, spider):
        data = None
        if isinstance(item, LianjiaItem):
            data = Lianjia(**item)
        elif isinstance(item, LianjiaSaleItem):
            data = LianjiaSale(**item)

        if data:
            try:
                self.session.add(data)
                self.session.commit()
            except Exception as e:
                print e
                self.session.rollback()
        return item

