# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from ali_first.items import AliFirstItem

class FstSpider(scrapy.Spider):
    name = 'fst'
    allowed_domains = ['aliwx.com.cn']
    start_urls = ['http://www.aliwx.com.cn/']

    def parse(self, response):
        item =  AliFirstItem()
        item['title'] = response.xpath("//p[@class='title']/text()").extract()
        yield item

        ## 分页
        # for i in range(2, 100):
        #     url="http://categray.dangdang.com/pg="+i
        #     yield scrapy.Request(url=url, callback=self.parse)
