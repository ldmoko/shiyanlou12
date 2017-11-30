# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class GithubshiyanlouItem(scrapy.Item):
    # define the fields for your item here like:
    name = Field()
    update_time = Field()
    commits = Field()
    branche = Field()
    releases = Field()

