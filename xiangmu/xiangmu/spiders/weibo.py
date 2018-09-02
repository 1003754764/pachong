# -*- coding: utf-8 -*-
import scrapy
import json
from xiangmu.items import WeiboItem

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.com']
    start_urls = ['https://m.weibo.cn/api/container/getIndex?uid=1259110474&luicode=10000011&lfid=100103type%3D1%26q%3D%E8%B5%B5%E4%B8%BD%E9%A2%96&type=uid&value=1259110474&containerid=1076031259110474']
    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        }
        #微博名：['mblog']['user']['screen_name'] 微博内容：['mblog']['text']，
        # 时间（月日）['mblog']['created_at']， 转发数量，['mblog']['reposts_count']
        # 评论数量['mblog']['comments_count']， 点赞数量['mblog']['attitudes_count']
        res_dict = json.loads(response.body)
        # 微博总数量
        total = res_dict['data']['cardlistInfo']['total']
        res_list = res_dict['data']['cards']
        for res in res_list:
            if res['card_type'] == 9:
                item = WeiboItem()
                # 微博名
                screen_name = res['mblog']['user']['screen_name']
                print(screen_name)
                item['screen_name'] = screen_name
                # 微博内容
                text = res['mblog']['text']
                print(text)
                item['text'] = text
                # 时间
                time = res['mblog']['created_at']
                if ':' in time:
                    if '昨天' in time:
                        time = '08-28'
                    else:
                        time = '08-29'
                if '小时前' in time:
                    time = '08-30'
                print(time)
                item['time'] = time
                # 转发数量
                reposts_count = res['mblog']['reposts_count']
                # print(reposts_count)
                item['reposts_count'] = reposts_count
                # 评论数量
                comments_count = res['mblog']['comments_count']
                # print(comments_count)
                item['comments_count'] = comments_count
                # 点赞数量
                attitudes_count = res['mblog']['attitudes_count']
                # print(attitudes_count)
                item['attitudes_count'] = attitudes_count

                yield item
            elif res['card_type'] == 11:
                print(11111)
                # 关注的博主的列表页
                try:

                    bozhu_list_href = res['card_group'][0]['scheme']
                    # print(bozhu_list_href)
                    # https://m.weibo.cn/p/index?
                    # https://m.weibo.cn/api/container/getIndex?
                    bozhu_api = 'https://m.weibo.cn/api/container/getIndex?'
                    # 拼接博主列表页api
                    bozhu_list_api = bozhu_api + bozhu_list_href.split('?')[1]
                    # print(bozhu_list_api)
                    yield scrapy.Request(bozhu_list_api,headers=headers,callback=self.parse_bozhu_list,dont_filter=True)
                except:
                    print('没有关注')
            else:
                continue
        for i in range(2,150):
            url = response.url + '&page={}'.format(i)
            # print(url)
            yield scrapy.Request(url, callback=self.parse_detail,dont_filter=True)
            # print(1112)

    def parse_bozhu_list(self, response):
        # print(222222)
        # 关注博主所有页
        bozhu_dict = json.loads(response.body)
        bozhu_href = bozhu_dict['data']['cards'][0]['card_group'][0]['scheme']
        bozhu_api = 'https://m.weibo.cn/api/container/getIndex?'
        bozhu_list_api = bozhu_api + bozhu_href.split('?')[1]
        # print(bozhu_list_api)
        yield scrapy.Request(bozhu_list_api, callback=self.parse_href, dont_filter=True)

    def parse_href(self,response):
        bozhu_dict = json.loads(response.body)
        bozhu_href_list = bozhu_dict['data']['cards'][0]['card_group']
        for bozhu_href in bozhu_href_list[1:]:
            scheme = bozhu_href['scheme']
            # # 拼接博主列表页api  &type=uid&value=2142058927
            bozhu_id = bozhu_href['user']['id']
            bozhu_api = 'https://m.weibo.cn/api/container/getIndex?'
            bozhu_url = bozhu_api + scheme.split('?')[1]+'&type=uid&value='+ str(bozhu_id)
            yield scrapy.Request(bozhu_url, callback=self.parse_url,dont_filter=True)


    def parse_url(self,response):
        # 拼接详情页接口
        res_dict = json.loads(response.body)
        containerid = res_dict['data']['tabsInfo']['tabs'][1]['containerid']
        bozhu_url = response.url + '&containerid=' + str(containerid)
        print(bozhu_url)
        yield scrapy.Request(bozhu_url, callback=self.parse, dont_filter=True)


    def parse_detail(self, response):
        # print(111111)
        res_dict = json.loads(response.body)
        res_list = res_dict['data']['cards']
        for res in res_list:
            item = WeiboItem()
            # 微博名
            screen_name = res['mblog']['user']['screen_name']
            print(screen_name)
            item['screen_name'] = screen_name
            # 微博内容
            text = res['mblog']['text']
            print(text)
            item['text'] = text
            # 时间
            time = res['mblog']['created_at']
            if ':' in time:
                if '昨天' in time:
                    time = '08-29'
                else:
                    time = '08-30'
            if '小时前' in time:
                time = '08-30'
            print(time)
            item['time'] = time
            # 转发数量
            reposts_count = res['mblog']['reposts_count']
            # print(reposts_count)
            item['reposts_count'] = reposts_count
            # 评论数量
            comments_count = res['mblog']['comments_count']
            # print(comments_count)
            item['comments_count'] = comments_count
            # 点赞数量
            attitudes_count = res['mblog']['attitudes_count']
            # print(attitudes_count)
            item['attitudes_count'] = attitudes_count

            yield item






