import scrapy
from divanpars.items import DivanparsItem

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        divans = response.css('div._Ud0k')
        for divan in divans:
            item = DivanparsItem()
            item['name'] = divan.css('div.lsooF span::text').get()
            item['price']= divan.css('div.pY3d2 span::text').get()
            item['url']= divan.css('a').attrib['href']
            yield(item)
