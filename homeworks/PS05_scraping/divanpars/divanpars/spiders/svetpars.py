import scrapy


class SvetparsSpider(scrapy.Spider):
    name = "svetpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://divan.ru/category/svet"]

    def parse(self, response):

        svets = response.css('div._Ud0k')
        # Настраиваем работу с каждым отдельным диваном в списке
        for svet in svets:
             print( {
                'name': svet.css('div.lsooF span::text').get(),
                # Создаём словарик цен, используем поиск по диву, а внутри дива — по тегу span
                'price': svet.css('div.pY3d2 span::text').get(),
                # Создаём словарик ссылок, используем поиск по тегу "a", а внутри тега — по атрибуту
                # Атрибуты — это настройки тегов
                'url': svet.css('a').attrib['href']
            })
