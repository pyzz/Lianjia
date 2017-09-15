# coding:utf-8

import os
import json
import click
import requests
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def req_citys():
    r = requests.get('https://bj.lianjia.com/ ')
    html = etree.HTML(r.content)
    city_objs = html.xpath('/html/body/div[1]/div/div[2]/div[3]//a')
    citys = {res.xpath('text()')[0]: res.xpath('@href')[0] for res in city_objs}
    with open('citys.json', 'w') as f:
        f.write(json.dumps(citys))
    return citys


def city_map(ctx, city):
    file_name = 'citys.json'
    if file_name in os.listdir('.'):
        with open(file_name) as f:
            return json.load(f)[city]
    else:
        citys = req_citys()
        return citys[city]


@click.command()
@click.option('--city', callback=city_map, default='北京', help="input the city name. default 北京")
@click.option('--types', default='ershoufang', help="ershoufang/chengjiaoliang. default ershoufang")
@click.option('--areas', default=None,
              help="please input the area name, example '海淀' or '海淀|东城'. if not input, spider will crawl all areas")
def main(city, types, areas):
    from scrapy.cmdline import execute
    if areas is None:
        start_command = "scrapy crawl lianjia -a city_url={} -a home_type={}".format(city, types)
        execute(start_command.split(' '))
    else:
        start_command = "scrapy crawl lianjia -a city_url={} -a home_type={} -a areas={}".format(city, types, areas)
        execute(start_command.split(' '))



if __name__ == '__main__':
    main()
