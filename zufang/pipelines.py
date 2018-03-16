# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import pymongo

class ZufangPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost',27017)
        scrapy_db = client['scrapy_db']
        self.coll = scrapy_db['job_scrapy']
    # def open_spider(self,spider):

        # self.con = sqlite3.connect("zufang.sqlite")
        # self.cu = self.con.cursor()

    def process_item(self, item, spider):
        self.coll.insert_one(item)
        return item
    #     print(spider.name,'pipelines')
    #     insert_sql = "insert into zufang(title,money) VALUES ('{}','{}')".format(item['title'],item['money'])
    #     print(insert_sql)
    #     self.cu.execute(insert_sql)
    #     self.con.commit()
    #     return item
    # def spider_close(self,spider):
    #     self.con.close()