from django.core.management.base import BaseCommand

from scraper.apps import SpiderController

class Command(BaseCommand):
    help = "Run the scrapethissite spider and store the results in the database"

    def add_arguments(self, parser):
        parser.add_argument('spider')

    def handle(self, *args, **options):
        SpiderController.run_spider('scrapethissite')
