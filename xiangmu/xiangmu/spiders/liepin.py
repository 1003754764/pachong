# -*- coding: utf-8 -*-
import scrapy
import re
from w3lib.html import remove_tags
from xiangmu.items import ZhaopinItem

class LiepinSpider(scrapy.Spider):
    name = 'liepin'
    allowed_domains = ['liepin.com']
    start_urls = ['https://www.liepin.com/it/']

    def parse(self, response):
        headers = {
            'User - Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }
        html = response.text
        # print(html)
        # 匹配分类页
        a_href_list = re.findall(r'<a target="_blank" rel="nofollow" href="(.*?)">',html)
        for a_href in a_href_list:
            # print(a_href)
            a_href_fenlei = response.urljoin(a_href)
            yield scrapy.Request(a_href_fenlei, callback=self.parse_fenlei)

    def parse_fenlei(self,response):
        # 循环具体分类页
        html = response.text
        # print(response.url)
        for i in range(0,99):
            url = response.url+'&curPage={}'.format(i)
            yield scrapy.Request(url, callback=self.parse_xiangqing)

    def parse_xiangqing(self,response):
        html = response.text
        # 匹配出详情页
        a_href_list = re.findall(r'a href="(.*?\d+.shtml)"',html)
        # print(len(a_href_list))
        # /a/1111111.shtml
        for a_href in a_href_list:
            if '/a/' in a_href:
                a_href_xiangqing = 'https://www.liepin.com'+ a_href
            else:
                a_href_xiangqing = a_href
            # print(a_href_xiangqing)
            yield scrapy.Request(a_href_xiangqing,callback=self.parse_item)

    def parse_item(self,response):
        # 职位名称， 薪水， 位置，
        # 经验要求， 学历要求， 发布时间，
        #  职位描述， 那个网站
        html = response.text
        # print(response.url)
        # print(html)
        item = ZhaopinItem()
        # 职位名称
        try:
            jobname = re.search(r'<h1 title=".*?">(.*?)</h1>',html).group(1)
        except:
            jobname = re.search(r'<h1>(.*?)</h1>',html).group(1)
        # print(jobname)
        item['jobname'] = jobname
        #薪水
        try:
            salary = re.search(r'"salaryName": "(.*?)",',html).group(1)
        except:
            salary = re.findall(r'<strong>(.*?)</strong>',html)[0]
        # print(salary)
        item['salary'] = salary
        # 位置
        try:
            weizhi =  re.search(r'"dqName": "(.*?)",',html).group(1)
        except:
            weizhi = re.findall(r'<em class="icons24 icons24-position"></em>(.*?)</span>',html,re.S)[0]
        # print(weizhi)
        item['weizhi'] = weizhi
        #经验要求
        try:
            jingyan = re.search(r'<span>(\d.*?)</span>',html).group(1)
        except:
            jingyan = '经验不限'
        # print(jingyan)
        item['jingyan'] = jingyan
        # 学历要求
        try:
            pat = re.compile(r'<div class="job-qualifications">.*?<span>(.*?)</span>',re.S)
            xueli = pat.findall(html)[0]
        except:
            pat = re.compile(r'<div class="resume clearfix">.*?<span>(.*?)</span>',re.S)
            xueli = pat.findall(html)[0]
        # print(xueli)
        item['xueli'] = xueli
        # 发布时间
        try:

            time = re.search(r'<time title="(.*?)">',html).group(1)
        except:
            time = re.search(r'<em class="icons24 icons24-time"></em>(.*?)</span>',html).group(1)
        # print(time)
        item['time'] = time
        # 岗位职责
        try:
            zhize = remove_tags(re.findall('<div class="content content-word">(.*?)</div>',html,re.S)[0])
        except:
            zhize = remove_tags(re.findall('<div class="job-info-content">(.*?)</div>',html,re.S)[0])
        # print(zhize)
        item['zhize'] = zhize
        # item['wangzhan'] = '猎聘网'
        yield item