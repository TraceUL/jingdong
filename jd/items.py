# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    名字 = scrapy.Field()
    卖点1 = scrapy.Field()
    卖点2 = scrapy.Field()
    价格 = scrapy.Field()
    评论数 =scrapy.Field()
    好评率 = scrapy.Field()
    图片 = scrapy.Field()
    详情页面 = scrapy.Field()