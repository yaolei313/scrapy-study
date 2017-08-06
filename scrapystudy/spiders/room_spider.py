import scrapy


class RoomSpider(scrapy.Spider):
    name = 'room_spider'
    start_urls = ['http://www.ziroom.com/z/nl/z6.html']

    def parse(self, response):
        with open('tmp.txt', 'w') as df:
            if response.headers is None:
                df.write('emtpy header')
            else:
                df.write(str(response.headers))
            if response.body is None:
                df.write('emtpy body')
            else:
                df.write(str(response.body, encoding='utf-8'))

        for li in response.css('li.clearfix'):
            detail_list = li.css('div.detail span::text').extract()
            tags1_list = list.css('p.room_tags span.subway::text').extract()
            if len(tags1_list) == 2:
                tags_subway_distance = tags1_list[0]
                tags_central_heading = tags1_list[1]
            else:
                tags_subway_distance = ''
                tags_central_heading = tags1_list[0]
            tags_balcony = list.css('p.room_tags span.balcony::text').extract()
            tags_style = list.css('p.room_tags span.style::text').extract()
            yield {
                'url': li.xpath('div h3 attr("href")').extract_first(),  # //www.ziroom.com/z/vr/60594843.html
                'title': li.xpath('div/h3/a/text()').extract_first(),  # 房子标题
                'region': li.css('div.txt h4 a::text').extract_first(),  # 房子区域
                'area': detail_list[0],  # 95 ㎡
                'floor': detail_list[1],  # 7/8层
                'house_type': detail_list[2],  # 2室1厅
                'subway_distance': detail_list[3],  # 距房山线长阳站907米
                'tags_subway_time': tags_subway_distance,  # 地铁10分钟
                'tags_balcony': tags_balcony,  # 独立阳台
                'tags_central_heating': tags_central_heading,  # 集体供暖
                'tags_style': tags_style,  # 原味
                'price': li.css('p.price::text').extract_first(),  # 3990
                'price_type': li.css('p.price span::text').extract_first(),  # (每月)
            }
        next_page = response.css('div.pages a.next::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
