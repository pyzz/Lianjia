# coding:utf-8

# areas = '海淀 东城'

home_type = 'chengjiao'
# home_type = 'ershoufang'



from scrapy.cmdline import execute
execute(['scrapy','crawl','lianjia', '-a', 'home_type={}'.format(home_type), '-a', 'areas={}'.format(areas)])
