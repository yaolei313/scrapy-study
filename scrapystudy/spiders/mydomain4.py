# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider


class Mydomain4Spider(XMLFeedSpider):
    name = 'mydomain4'
    allowed_domains = ['mydomain4.com']
    start_urls = ['http://mydomain4.com/feed.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly

    def parse_node(self, response, selector):
        i = {}
        #i['url'] = selector.select('url').extract()
        #i['name'] = selector.select('name').extract()
        #i['description'] = selector.select('description').extract()
        return i
