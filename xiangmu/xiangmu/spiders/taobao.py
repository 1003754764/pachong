# -*- coding: utf-8 -*-
import scrapy
import json
from xiangmu.items import TaobaoItem

class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']
    start_urls = ['https://s.m.taobao.com/search?event_submit_do_new_search_auction=1&_input_charset=utf-8&topSearch=1&atype=b&searchfrom=1&action=home%3Aredirect_app_action&from=1&sst=1&n=20&buying=buyitnow&m=api4h5&abtest=2&wlsort=2']
# 'https://s.m.taobao.com/search?event_submit_do_new_search_auction=1&_input_charset=utf-8&topSearch=1&atype=b&searchfrom=1&action=home%3Aredirect_app_action&from=1&q=%E6%98%A5%E7%A7%8B%E5%A4%96%E5%A5%97%E5%A5%B3%E4%BF%AE%E8%BA%AB&sst=1&n=20&buying=buyitnow&m=api4h5&abtest=23&wlsort=23&page=1'
# 'https://s.m.taobao.com/search?event_submit_do_new_search_auction=1&_input_charset=utf-8&topSearch=1&atype=b&searchfrom=1&action=home%3Aredirect_app_action&from=1&sst=1&n=20&buying=buyitnow&m=api4h5&abtest=2&wlsort=2&page=1'
    def parse(self, response):
        headers ={
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        }

        # 搜索关键字
        q_list = ['T恤','衬衫','毛衣','针织衫','小背心/吊带','蕾丝衫/雪纺衫','外套','风衣','大衣','棉衣','羽绒服','皮衣','马夹','卫衣','西装']
        for q in q_list:
            # 初始接口
            url = response.url + '&q={}'.format(q)
            yield scrapy.Request(url,headers=headers,callback=self.parse_fenye)

    def parse_fenye(self,response):
        for i in range(1,101):
            # 分页接口
            url = response.url+'&page={}'.format(i)
            yield scrapy.Request(url,callback=self.parse_item)
            # break

    def parse_item(self,response):
        # 详情页接口
        res_json = json.loads(response.body)
        res_list = res_json['listItem']
        for res in res_list:
            # 标题，
            item = TaobaoItem()
            title = res['title']
            # print(title)
            item['title'] = title
            # 原价，
            originalPrice = res['originalPrice']
            # print(originalPrice)
            item['originalPrice'] = originalPrice
            # 现价，
            price = res['price']
            # print(price)
            item['price'] = price
            # 公司，
            nick = res['nick']
            # print(nick)
            item['nick'] = nick
            # 地点，
            location = res['location']
            # print(location)
            item['location'] = location
            # 图片（url），
            pic_path = res['pic_path']
            # print(pic_path)
            item['pic_path'] = pic_path
            # 付款人数
            sold = res['sold']
            # print(sold)
            item['sold'] = sold

            yield item
