from crawling.crawling.spiders.dk_aarhus_voxhall_base import DkAarhusVoxhallBaseSpider


class DkAarhusVoxhallWorldSpider(DkAarhusVoxhallBaseSpider):
    name = 'dk_aarhus_voxhall'
    allowed_domains = ['fondenvoxhall.dk']
    start_urls = ['https://fondenvoxhall.dk/genre/world/']

    def get_genre(self):
        return "World"

