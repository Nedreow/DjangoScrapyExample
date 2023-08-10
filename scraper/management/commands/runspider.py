from django.core.management.base import BaseCommand
from scraper.scraper.spiders.scrapethissite import ScrapethissiteSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os

class Command(BaseCommand):
    help = "Run the scrapethissite spider and store the results in the database"

    def handle(self, *args, **options):
        settings_file_path = 'scraper.scraper.settings'  # The path seen from root, ie. from main.py
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
        process = CrawlerProcess(get_project_settings())

        process.crawl(ScrapethissiteSpider)
        process.start()
