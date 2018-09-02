# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiangmuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class WeiboItem(scrapy.Item):
    screen_name = scrapy.Field()
    text = scrapy.Field()
    time = scrapy.Field()
    reposts_count = scrapy.Field()
    comments_count = scrapy.Field()
    attitudes_count = scrapy.Field()

    def insert_sql(self):
        sql = 'insert into weibo(screen_name,text,time,reposts_count,comments_count,attitudes_count) values (%s,%s,%s,%s,%s,%s)'
        data = (self['screen_name'],self['text'],self['time'],self['reposts_count'],self['comments_count'],self['attitudes_count'])
        return (sql,data)


class ZhaopinItem(scrapy.Item):
    jobname = scrapy.Field()
    salary = scrapy.Field()
    weizhi = scrapy.Field()
    jingyan = scrapy.Field()
    xueli = scrapy.Field()
    time = scrapy.Field()
    zhize = scrapy.Field()
    wangzhan = scrapy.Field()

    def insert_sql(self):
        sql = 'insert into liepin(jobname,salary,weizhi,jingyan,xueli,time,zhize,wangzhan) values (%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (self['jobname'],self['salary'],self['weizhi'],self['jingyan'],self['xueli'],self['time'],self['zhize'],self['wangzhan'])
        return (sql,data)

class TaobaoItem(scrapy.Item):
    title = scrapy.Field()
    originalPrice = scrapy.Field()
    price = scrapy.Field()
    nick = scrapy.Field()
    location = scrapy.Field()
    pic_path = scrapy.Field()
    sold = scrapy.Field()

    def insert_sql(self):
        sql = 'insert into taobao(title,originalPrice,price,nick,location,pic_path,sold) values (%s,%s,%s,%s,%s,%s,%s)'
        data = (self['title'],self['originalPrice'],self['price'],self['nick'],self['location'],self['pic_path'],self['sold'])
        return (sql,data)





