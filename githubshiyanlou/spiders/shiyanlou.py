# -*- coding: utf-8 -*-
import scrapy
from githubshiyanlou.items import GithubshiyanlouItem

class ShiyanlouSpider(scrapy.Spider):
    name = 'shiyanlou'
    allowed_domains = ['github.com']
    start_urls = []
    base_url = 'https://github.com/shiyanlou?tab=repositories&page={}'
    for i in range(1, 5):
        start_urls.append(base_url.format(i))

    def parse(self, response):
        # print(response.url)
        for i in response.xpath('//*[@id="user-repositories-list"]/ul/li'):
            item = GithubshiyanlouItem()
            item['name'] = i.xpath('div[1]/h3/a/text()').extract()[0].strip()
            item['update_time'] = i.xpath('div[3]/relative-time/@datetime').extract()[0]
            
            repo_url = 'https://github.com' + i.xpath('div[1]/h3/a/@href').extract()[0]
            # print(repo_url)
            request = scrapy.Request(repo_url, callback=self.parse_detail)
            request.meta['item'] = item
            yield request 

    def parse_detail(self, response):
        item = response.meta['item']
        item['commits'] = response.xpath('//*[@class="numbers-summary"]/li[1]/a/span/text()').extract()[0].strip()
        item['branche'] = response.xpath('//*[@class="numbers-summary"]/li[2]/a/span/text()').extract()[0].strip()
        item['releases'] = response.xpath('//*[@class="numbers-summary"]/li[3]/a/span/text()').extract()[0].strip()
        # print(item)
        yield item
        
