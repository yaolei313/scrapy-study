from scrapy import cmdline
#cmdline.execute("scrapy runspider spiders/quotes_spider.py -o quotes.json".split())
#cmdline.execute("scrapy runspider spiders/room_spider.py -o rooms.json".split())
cmdline.execute("scrapy crawl mydomain2 -o mydomain2.json".split())