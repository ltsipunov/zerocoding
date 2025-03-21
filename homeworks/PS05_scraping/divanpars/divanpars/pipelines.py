# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DivanparsPipeline:
    def open_spider(self, object):
        self.file = open('divan.csv','w')
        self.file.write(','.join(['name', 'price', 'url'])+'\n')

    def process_item(self, item, spidy):
        self.file.write(','.join([ item['name'],item['price'],item['url'] ])+'\n')
        return item

    def close_spider(self,spidy):
        self.file.close()


class SvetparsPipeline:

    def open_spider(self, spidy):
        self.file = open('svet.csv','w')
        self.file.write(','.join(['name', 'price', 'url'])+'\n')

    def close_spider(self,spidy):
        self.file.close()

    def process_item(self, item, spider):
        self.file.write(','.join([ item['name'],item['price'],item['url'] ])+'\n')
        return item