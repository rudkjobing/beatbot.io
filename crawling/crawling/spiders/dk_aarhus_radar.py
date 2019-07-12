# -*- coding: utf-8 -*-
import re

import dateparser
import scrapy
from django.utils import timezone
from scrapy.http import Response

from crawling.crawling.items import EventItem


class DkAarhusRadarSpider(scrapy.Spider):
    name = 'dk_aarhus_radar'
    allowed_domains = ['radarlive.dk']
    start_urls = ['https://radarlive.dk/kalender/']

    def parse(self, response: Response):
        links = response.xpath('//main//a[@class="article"]/@href').extract()
        # links = response.xpath('normalize-space(/html/body/div[1]/main/div[1]/div/a/@href)').extract()
        for link in links:
            absolute_url = response.urljoin(link)
            yield scrapy.Request(absolute_url, callback=self.parse_concert, dont_filter=True)

    def parse_concert(self, response):
        venue = "Radar"
        band = response.xpath("/html/body/div[1]/main/article/aside/h1/text()").extract_first()
        # detail_url = response.url
        # image = response.urljoin(response.xpath("/html/body/div[1]/main/article/header/img/@src").extract_first())
        price = response.xpath("//div[contains(@class,'val-price')]/text()").extract_first()
        date = response.xpath("//div[contains(@class,'val-date')]/text()").extract_first()
        time = response.xpath("//div[contains(@class,'val-hours')]/text()").extract_first()
        genres = response.xpath("//div[contains(@class,'val-genre')]/text()").extract_first()
        # detail_text = response.xpath("//div[contains(@class,'paragraph')]").extract_first()

        item = EventItem()
        item["venue"] = venue
        item["artist"] = band
        item["band"] = band
        item["ticket_price"] = re.search("(\d+),-", price).group(1)
        item["genres"] = [genre.strip() for genre in genres.split("/")]
        item["datetime_of_performance"] = DkAarhusRadarSpider.make_date(date, time)
        item["source_url"] = response.url
        yield item

    @staticmethod
    def make_date(date_string: str, time_string: str):
        doors_open, concert_begins = time_string.split("/")
        datetime_string = f"{date_string} {concert_begins} CET"
        dt = dateparser.parse(datetime_string)
        return dt
