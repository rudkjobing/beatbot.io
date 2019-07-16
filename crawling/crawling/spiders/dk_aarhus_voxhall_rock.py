from crawling.crawling.spiders.dk_aarhus_voxhall_base import DkAarhusVoxhallBaseSpider


class DkAarhusVoxhallRockSpider(DkAarhusVoxhallBaseSpider):
    name = 'dk_aarhus_voxhall'
    allowed_domains = ['fondenvoxhall.dk']
    start_urls = ['https://fondenvoxhall.dk/genre/rock/']

    def get_genre(self):
        return "Rock"

