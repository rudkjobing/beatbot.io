# -*- coding: utf-8 -*-
import dateparser
import scrapy
from django.utils import timezone
from scrapy.http import Response

from crawling.crawling.items import EventItem


class DkAarhusVoxhallSpider(scrapy.Spider):
    name = 'dk_aarhus_voxhall'
    allowed_domains = ['fondenvoxhall.dk']
    start_urls = ['https://fondenvoxhall.dk/koncerter/']

    def parse(self, response: Response):
        links = response.xpath("//div[@class='concert-thumbnail']/a/@href").getall()
        for link in [links[1]]:
            yield scrapy.Request(link, callback=self.parse_detail_page)

    def parse_detail_page(self, response: Response):
        band = response.xpath("//aside/hgroup/h1/text()").extract_first()
        date = response.xpath("//aside[contains(@class, 'sidebar-concert')]/div/table/tr[1]/td[2]/text()"
                                     ).extract_first()
        time = response.xpath("//aside[contains(@class, 'sidebar-concert')]/div/table/tr[2]/td[2]/text()"
                                     ).extract_first()

        venue = response.xpath("//tr[@class='concert-place']//a/text()").extract_first()

        item = EventItem()
        item["venue"] = venue
        item["artist"] = band.strip()
        item["band"] = band.strip()
        # item["ticket_price"] = re.search("(\d+),-", price).group(1)
        # item["genres"] = [genre.strip() for genre in genres.split("/")]
        item["datetime_of_performance"] = DkAarhusVoxhallSpider.__make_date(date, time)
        item["source_url"] = response.url.strip()

        yield item

    @staticmethod
    def __make_date(date_string: str, time_string: str):
        doors_open, concert_begins = time_string.split("/")
        datetime_string = f"{date_string} {concert_begins} CET"
        dt = dateparser.parse(datetime_string)
        return dt
