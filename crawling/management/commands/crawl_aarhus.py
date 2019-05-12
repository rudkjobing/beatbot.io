import os

from django.core.management import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from crawling.crawling.spiders.dk_aarhus_voxhall import DkAarhusVoxhallSpider


class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        settings_file_path = 'crawling.crawling.settings'
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
        process = CrawlerProcess(get_project_settings())

        process.crawl(DkAarhusVoxhallSpider)
        process.start()
