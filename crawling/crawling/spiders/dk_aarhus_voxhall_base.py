import re

import dateparser
import scrapy
from scrapy.http import Response

from core.genres import determine_genres
from crawling.crawling.items import EventItem


class DkAarhusVoxhallBaseSpider(scrapy.Spider):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.voxhall = "VoxHall"
        self.atlas = "Atlas"

    def get_genre(self):
        raise NotImplementedError()

    def parse(self, response: Response):
        links = response.xpath("//div[@class='concert-thumbnail']/a/@href").getall()
        for link in links:
            yield scrapy.Request(link, callback=self.parse_detail_page)

    def parse_detail_page(self, response: Response):
        band = response.xpath("//aside/hgroup/h1/text()").extract_first()
        date = response.xpath("//aside[contains(@class, 'sidebar-concert')]/div/table/tr[1]/td[2]/text()"
                                     ).extract_first().replace("\t", "").replace("\n", "")
        time = response.xpath("//aside[contains(@class, 'sidebar-concert')]/div/table/tr[2]/td[2]/text()"
                                     ).extract_first()

        venue = response.xpath("//tr[@class='concert-place']//a/text()").extract_first()
        ticket_price = response.xpath("//aside[@class='sidebar-concert']//tr[last()]/td[last()]/text()").extract_first()
        description = response.xpath("//div[@id='full-content']").extract_first()
        item = EventItem()

        if venue is None:
            return None

        if venue.lower() == self.voxhall.lower():
            item["venue"] = self.voxhall
        elif venue.lower() == self.atlas.lower():
            item["venue"] = self.atlas

        item["artist"] = band.strip()
        item["ticket_price"] = re.search("(\d+),-", ticket_price).group(1)
        item["raw_genres"] = [self.get_genre()]
        item["genres"] = list(determine_genres(self.get_genre()))
        item["datetime_of_performance"] = DkAarhusVoxhallBaseSpider.__make_date(date, time)
        item["source_url"] = response.url.strip()
        item["source_url"] = response.url.strip()
        item["description"] = description

        yield item

    @staticmethod
    def __make_date(date_string: str, time_string: str):
        time_string = time_string.replace(".", ":")
        date_string = date_string.replace("d. ", "")
        doors_open, concert_begins = time_string.split("/")
        datetime_string = f"{date_string} {concert_begins} CET"
        dt = dateparser.parse(datetime_string)
        return dt
