# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from xiangmu.items import ZhaopinItem

class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['http://lagou.com/']
    # 在setting文件中需要加上user-agent和cookie
    rules = (
        Rule(LinkExtractor(allow=r'https://www\.lagou\.com/zhaopin/\w+/'), follow=True,),
        Rule(LinkExtractor(allow=r'https://www\.lagou\.com/jobs/\d+.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = ZhaopinItem()
        jobname = response.xpath('//span[@class="name"]/text()').extract_first()
        # print(jobname)
        item['jobname'] = jobname
        salary = response.xpath('//span[@class="salary"]/text()').extract_first()
        # print(salary)
        item['salary'] = salary
        weizhi = response.xpath('//dd[@class="job_request"]/p/span[2]/text()').extract_first()
        # print(weizhi)
        item['weizhi'] = weizhi
        jingyan = response.xpath('//dd[@class="job_request"]/p/span[3]/text()').extract_first()
        # print(jingyan)
        item['jingyan'] = jingyan
        xueli = response.xpath('//dd[@class="job_request"]/p/span[4]/text()').extract_first()
        # print(xueli)
        item['xueli'] = xueli
        time = response.xpath('//p[@class="publish_time"]/text()').extract_first()
        # print(time)
        if ':' in time:
            time = '8-30'
        elif '1天前' in time:
            time = '8-29'
        elif '2天前' in time:
            time = '8-28'
        else:
            time = '8-27'
        item['time'] = time
        zhize = ''.join(response.xpath('//dd[@class="job_bt"]//text()').extract())
        # print(zhize)
        item['zhize'] = zhize
        wangzhan = '拉钩网'
        item['wangzhan'] = wangzhan

        yield item



