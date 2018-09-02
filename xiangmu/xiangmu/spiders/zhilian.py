# -*- coding: utf-8 -*-
import scrapy
import json
from xiangmu.items import ZhaopinItem

class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['zhaopin.com']
    start_urls = ['http://zhaopin.com/']

    def parse(self, response):
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        li_list = response.xpath('//ol[@class="zp-jobNavigater-list"]/li')
        for div_ele in li_list:
            div_list = div_ele.xpath('./div[2]/div/div')
            for a_ele in div_list[1:]:
                a_list = a_ele.xpath('./a')
                for a_res in a_list:
                    kw = a_res.xpath('./span/text()').extract_first()
                    # print(kw)
                    # 找到所有的小分类名称并且拼接起来
                    url = 'https://sou.zhaopin.com/?pageSize=60&jl=702&kw={}&kt=3'.format(kw)
                    print(url)
                    yield scrapy.Request(url,headers=headers,callback=self.parse_liebiao)
                    # break
                # break
            # break


    def parse_liebiao(self,response):
        url = response.url
        str = url.split('&')[2]
        # 拼接列表接口
        url_api = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=702&{}&kt=3'.format(str)
        yield scrapy.Request(url_api,callback=self.parse_xiangqing_list)

    def parse_xiangqing_list(self,response):
        res_dict = json.loads(response.body)
        res_list = res_dict['data']['results']
        for res in res_list:
            # 获取详情页链接
            href = res['positionURL']
            # print(href)
            yield scrapy.Request(href,callback=self.parse_item)
            # break

    def parse_item(self,response):
        item = ZhaopinItem()
        jobname = response.xpath('//h1/text()').extract_first()
        # print(jobname)
        item['jobname'] = jobname
        salary = response.xpath('//ul[@class="terminal-ul clearfix"]/li[1]/strong/text()').extract_first()
        # print(salary)
        item['salary'] = salary
        weizhi = response.xpath('//ul[@class="terminal-ul clearfix"]/li[2]/strong/a/text()').extract_first()
        # print(weizhi)
        item['weizhi'] = weizhi
        jingyan = response.xpath('//ul[@class="terminal-ul clearfix"]/li[5]/strong/text()').extract_first()
        # print(jingyan)
        item['jingyan'] = jingyan
        xueli = response.xpath('//ul[@class="terminal-ul clearfix"]/li[6]/strong/text()').extract_first()
        # print(xueli)
        item['xueli'] = xueli
        time = response.xpath('//ul[@class="terminal-ul clearfix"]/li[3]/strong/span/text()').extract_first()
        # print(time)
        item['time'] = time
        zhize = ''.join(response.xpath('//div[@class="tab-inner-cont"]/p/text()')[0:10].extract())
        # print(zhize)
        item['zhize'] = zhize
        wangzhan = '智联招聘'
        item['wangzhan'] = wangzhan

        yield item



