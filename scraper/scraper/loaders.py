import re
from datetime import datetime
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst

class ScrapingSandboxLoader(ItemLoader):
    default_output_processor = TakeFirst()
