import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'author'

    def start_requests(self):
        print(getattr(self, 'hello', 'none'))
        lst = ['http://quotes.toscrape.com']
        for item in lst:
            yield scrapy.Request(item)

    def parse(self, response):
        for href in response.css('small.author + a::attr(href)').extract():
            yield response.follow(href, self.parse_author)

        # Unlike scrapy.Request, response.follow supports relative URLs directly - no need to call urljoin.
        # By default, Scrapy filters out duplicated requests to URLs already visited, avoiding the problem of
        # hitting servers too much because of a programming mistake. This can be configured by the setting
        # DUPEFILTER_CLASS.
        for href in response.css('li.next > a::attr(href)').extract():
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        author_title = extract_with_css('h3.author-title::text')
        author_born_date = extract_with_css('span.author-born-date::text')
        author_born_location = extract_with_css('span.author-born-location::text')
        yield {
            "title": author_title,
            "born_date": author_born_date,
            "born_location": author_born_location
        }
