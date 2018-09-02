# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from xiangmu.items import ZhaopinItem

class QianchengwuyouSpider(CrawlSpider):
    name = 'qianchengwuyou'
    allowed_domains = ['51job.com']
    start_urls = ['http://51job.com/']

    rules = (
        Rule(LinkExtractor(allow=r'https://search\.51job\.com/\w+/.*\.html\?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=$'),follow=True),
        Rule(LinkExtractor(allow=r'https://jobs\.51job\.com/\w+?/\d+\.html\?s=01&t=0'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = ZhaopinItem()
        jobname = response.xpath('//h1/@title').extract_first()
        # print(jobname)
        item['jobname'] = jobname
        salary = response.xpath('//div[@class="cn"]/strong[1]/text()').extract_first()
        if not salary:
            salary = '面议'
        # print(salary)
        item['salary'] = salary
        # 含有位置 经验 学历 发布时间的list
        juti_str = response.xpath('//p[@class="msg ltype"]/text()').extract()
        if len(juti_str) == 5:
            weizhi = juti_str[0].strip()
            jingyan = juti_str[1].strip()
            xueli = juti_str[2].strip()
            time = juti_str[4].strip()
        else:
            weizhi = juti_str[0].strip()
            jingyan = juti_str[1].strip()
            xueli = '学历不限'
            time = juti_str[3].strip()
        # print(weizhi)
        # print(jingyan)
        # print(xueli)
        # print(time)
        item['weizhi'] = weizhi
        item['jingyan'] = jingyan
        item['xueli'] = xueli
        item['time'] = time
        zhize = ''.join(response.xpath('//div[@class="bmsg job_msg inbox"]/p/text()').extract())
        # print(zhize)
        item['zhize'] = zhize
        wangzhan = '前程无忧'
        item['wangzhan'] = wangzhan

        yield item













