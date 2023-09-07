import os

from django.apps import AppConfig
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class ScraperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scraper'


class SpiderController:

    @staticmethod
    def run_spider(spider, signal=True):
        settings_file_path = 'scraper.scraper.settings'  # The path seen from root, ie. from main.py
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
        process = CrawlerProcess(get_project_settings())

        process.crawl(spider)
        process.start(stop_after_crawl=True, install_signal_handlers=signal)
