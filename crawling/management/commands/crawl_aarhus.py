import os

from django.core.management import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from crawling.crawling.spiders.dk_aarhus_radar import DkAarhusRadarSpider
from crawling.crawling.spiders.dk_aarhus_voxhall_heavy import DkAarhusVoxhallHeavySpider
from crawling.crawling.spiders.dk_aarhus_voxhall_jazz import DkAarhusVoxhallJazzSpider
from crawling.crawling.spiders.dk_aarhus_voxhall_rock import DkAarhusVoxhallRockSpider
from crawling.crawling.spiders.dk_aarhus_voxhall_urban import DkAarhusVoxhallUrbanSpider
from crawling.crawling.spiders.dk_aarhus_voxhall_world import DkAarhusVoxhallWorldSpider


class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        settings_file_path = 'crawling.crawling.settings'
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
        process = CrawlerProcess(get_project_settings())

        process.crawl(DkAarhusVoxhallWorldSpider)
        process.crawl(DkAarhusVoxhallHeavySpider)
        process.crawl(DkAarhusVoxhallRockSpider)
        process.crawl(DkAarhusVoxhallUrbanSpider)
        process.crawl(DkAarhusVoxhallJazzSpider)
        process.crawl(DkAarhusRadarSpider)
        process.start()
