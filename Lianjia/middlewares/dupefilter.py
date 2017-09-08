# coding:utf-8

import logging
import redis
from scrapy.exceptions import IgnoreRequest
from Lianjia.settings import REDIS_HOST, REDIS_PORT, REDIS_DB


logger = logging.getLogger('dupefilter_middleware')

class DupefilterMiddleware(object):
	def __init__(self):
		self.redis = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

	def process_request(self, request, spider):
		if request.dont_filter:
			return None
		else:
			not_exist = self.redis.sadd('{}:dupefilter'.format(spider.name), request.url)
			if not_exist:
				return None
			else:
				logger.info('dupefilter request: {}'.format(request.url))
				raise IgnoreRequest()


