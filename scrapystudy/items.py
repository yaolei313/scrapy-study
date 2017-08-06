# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapystudyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()  # //www.ziroom.com/z/vr/60594843.html
    title = scrapy.Field()  # 房子标题
    region = scrapy.Field()  # 房子区域
    area = scrapy.Field()  # 95 ㎡
    floor = scrapy.Field()  # 7/8层
    house_type = scrapy.Field()  # 2室1厅
    subway_distance = scrapy.Field()  # 距房山线长阳站907米
    tags_subway_time = scrapy.Field()  # 地铁10分钟
    tags_balcony = scrapy.Field()  # 独立阳台
    tags_central_heating = scrapy.Field()  # 集体供暖
    tags_style = scrapy.Field()  # 原味
    price = scrapy.Field()  # 3990
    price_type = scrapy.Field()  # (每月)
