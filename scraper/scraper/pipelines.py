# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from asgiref.sync import sync_to_async
from itemadapter import ItemAdapter
from scrapy_djangoitem import DjangoItem


class ScraperPipeline:
    def process_item(self, item, spider):
        return item


class SaveItemPipeline:
    async def process_item(self, item: DjangoItem, spider):
        await sync_to_async(item.save)()
        return item
