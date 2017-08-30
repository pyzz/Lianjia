# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from databases.basic_db import engine, session
from databases.tables import *

class LianjiaPipeline(object):
    
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = session

    def process_item(self, item, spider):
    	try:
    		data = Lianjia(**item)
    		self.session.add(data)
    	except Exception as e:
            self.logger.warning(e)
    	else:
    		self.session.commit()

