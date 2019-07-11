# -*- coding: utf-8 -*-
import scrapy
from django.utils import timezone
from scrapy.http import Response

from crawling.crawling.items import EventItem


class DkAarhusVoxhallSpider(scrapy.Spider):
    name = 'dk_aarhus_voxhall'
    allowed_domains = ['fondenvoxhall.dk']
    start_urls = ['https://fondenvoxhall.dk/']

    def parse(self, response: Response):
        gigs = response.xpath("//article/@data-link").getall()
        for gig in gigs[:1]:
            yield scrapy.Request(gig, callback=self.parse_detail_page)

    def parse_detail_page(self, response: Response):
        band = response.xpath("//aside/hgroup/h1/text()")
        item = EventItem()
        item["band"] = band.extract_first()
        date_string = response.xpath("//aside[contains(@class, 'sidebar-concert')]/div/table/tr[1]/td[2]/text()"
                                     ).extract_first()
        time_string = response.xpath("//aside[contains(@class, 'sidebar-concert')]/div/table/tr[2]/td[2]/text()"
                                     ).extract_first()
        item["date"] = self.make_date(date_string, time_string)
        yield item

    def make_date(self, date_string: str, time_string: str):

        return timezone.now()
