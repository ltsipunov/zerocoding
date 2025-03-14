import scrapy
from divanpars.items import SvetparsItem

class SvetparsSpider(scrapy.Spider):
    name = "svetpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://divan.ru/category/svet"]

    def parse(self, response):

        svets = response.css('div._Ud0k')
        # Настраиваем работу с каждым отдельным диваном в списке
        for svet in svets:
            item = SvetparsItem()
            item['name'] = svet.css('div.lsooF span::text').get()
            item['price'] = svet.css('div.pY3d2 span::text').get()
            item['url'] = svet.css('a').attrib['href']
            yield item

