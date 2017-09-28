# -*- coding: utf-8 -*-
import json
import re

import scrapy
from jd.items import JdItem


class MJdSpider(scrapy.Spider):
    name = 'm.jd'
    allowed_domains = ['so.m.jd.com']
    # start_request=['https://so.m.jd.com/ware/searchList.action']


    def start_requests(self):#one page have 10 detail
        url='https://so.m.jd.com/ware/searchList.action'

        for i in range(1,10):
            fr={
                "_format_":"json",
                "page":str(i),
                "keyword": str("手机")
            }

            yield scrapy.FormRequest(url=url,formdata=fr,callback=self.parse,dont_filter=True)

    def parse(self,response):
        data=json.loads(response.text)

        da=data['value']

        pattern=re.compile('{.*?stockQuantity.*?}',re.S)
        result=re.findall(pattern,da)

        for r in result[1:]:
            i=json.loads(r)
            if 'catid' in i:
                try:
                    名字=i["wname"]
                    卖点1=i['gaiaAttrt']
                    卖点2=i['customAttrList']
                    价格=i['jdPrice']
                    评论数=i['totalCount']
                    好评率=i['good']
                    图片=i['longImgUrl']
                    详情页面='https://item.m.jd.com/product/{id}.html'.format(id=i['wareId'])
                    item=JdItem()
                    for field in item.fields:
                        try:
                            item[field]=eval(field)
                        except NameError:
                            print('Field is not Defind',field)
                    yield item
                except KeyError:
                    pass