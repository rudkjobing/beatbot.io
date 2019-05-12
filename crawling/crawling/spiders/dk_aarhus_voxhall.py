# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Response
from scrapy_djangoitem import DjangoItem

from core.models import Event


class EventItem(DjangoItem):
    django_model = Event


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
        yield item

