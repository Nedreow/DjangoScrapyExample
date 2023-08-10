import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scraper.scraper.items import ScrapingSandboxItem
from scraper.scraper.loaders import ScrapingSandboxLoader


class ScrapethissiteSpider(CrawlSpider):
    name = "scrapethissite"
    allowed_domains = ["scrapethissite.com"]
    start_urls = ["https://scrapethissite.com/pages/"]

    rules = (Rule(LinkExtractor(allow=r"pages/"), callback="parse_item", follow=False),)

    def parse_item(self, response):
        loader = ScrapingSandboxLoader(item=ScrapingSandboxItem(), response=response)

        loader.add_value('source_url', response.request.url)

        loader.add_xpath('name', '//h1/text()')
        loader.add_xpath('description', '//p[@class="lead"]/text()')

        return loader.load_item()
