# -*- coding: utf-8 -*-
import re

import scrapy
from django.utils import timezone
from scrapy.http import Response

from crawling.crawling.spiders.dk_aarhus_voxhall import EventItem


class DkAarhusRadarSpider(scrapy.Spider):
    name = 'dk_aarhus_radar'
    allowed_domains = ['radarlive.dk']
    start_urls = ['https://fondenvoxhall.dk/']

    def parse(self, response: Response):
        links = response.xpath('normalize-space(/html/body/div[1]/main/div[1]/div/a/@href)').extract()
        for link in links[0]:
            absolute_url = response.urljoin(link)
            yield scrapy.Request(absolute_url, callback=self.parse_concert, dont_filter=True)

    def parse_concert(self, response):
        venue = "Radar"
        band = response.xpath("/html/body/div[1]/main/article/aside/h1/text()")
        # detail_url = response.url
        # image = response.urljoin(response.xpath("/html/body/div[1]/main/article/header/img/@src").extract_first())
        # price = response.xpath("//div[contains(@class,'val-price')]/text()").extract_first()
        # ticket_url = response.xpath("//a[contains(@class,'ticket')]/@href").extract_first()
        date = response.xpath("//div[contains(@class,'val-date')]/text()").extract_first()
        time = response.xpath("//div[contains(@class,'val-hours')]/text()").extract_first()
        # genres_string = response.xpath("//div[contains(@class,'val-genre')]/text()").extract_first()
        # genres = [str.strip(genre) for genre in str.split(genres_string, "/")]
        # detail_text = response.xpath("//div[contains(@class,'paragraph')]").extract_first()
        item = EventItem()
        item["band"] = band.extract_first()
        item["datetime_of_performance"] = DkAarhusRadarSpider.make_date(date, time)
        yield item

    @staticmethod
    def make_date(date_string: str, time_string: str):
        performance_time = re.split(time_string, "/")
        datetime_string = date_string + time_string
        return timezone.now()
