# -*- coding: utf-8 -*-
# 爬后处理

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class AliFirstPipeline:
    def process_item(self, item, spider):
        arr = item['title']
        print('------')
        print(arr)
        print('------')
        for i in range(0, len(arr)-1) :
            print('------')
            print(item['title'][i])
            print('------')
        return item
