# -*- coding: utf-8 -*-
import re

import dateparser
import scrapy
from scrapy.http import Response

from core.genres import determine_genres
from crawling.crawling.items import EventItem


class DkAarhusRadarSpider(scrapy.Spider):
    name = 'dk_aarhus_radar'
    allowed_domains = ['radarlive.dk']
    start_urls = ['https://radarlive.dk/kalender/']

    def parse(self, response: Response):
        links = response.xpath('//main//a[@class="article"]/@href').extract()
        for link in links:
            absolute_url = response.urljoin(link)
            yield scrapy.Request(absolute_url, callback=self.parse_concert, dont_filter=True)

    def parse_concert(self, response):
        venue = "Radar"
        band = response.xpath(
            "/html/body/div[1]/main/article/aside/h1/text()"
        ).extract_first()
        price = response.xpath(
            "//div[contains(@class,'val-price')]/text()"
        ).extract_first()
        date = response.xpath(
            "//div[contains(@class,'val-date')]/text()"
        ).extract_first()
        time = response.xpath(
            "//div[contains(@class,'val-hours')]/text()"
        ).extract_first()
        genres = response.xpath(
            "//div[contains(@class,'val-genre')]/text()"
        ).extract_first()
        description = response.xpath(
            "//div[@class='content detail']"
        ).extract_first()

        item = EventItem()
        item["venue"] = venue
        item["artist"] = band.strip()
        item["ticket_price"] = re.search("(\d+),-", price).group(1)
        item["raw_genres"] = [genre.strip() for genre in genres.split("/")]
        item["genres"] = list(determine_genres(genres))
        item["datetime_of_performance"] = DkAarhusRadarSpider.__make_date(date, time)
        item["source_url"] = response.url.strip()
        item["description"] = description
        yield item

    @staticmethod
    def __make_date(date_string: str, time_string: str):
        doors_open, concert_begins = time_string.split("/")
        datetime_string = f"{date_string} {concert_begins} CET"
        dt = dateparser.parse(datetime_string)
        return dt
