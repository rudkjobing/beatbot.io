from crawling.crawling.spiders.dk_aarhus_voxhall_base import DkAarhusVoxhallBaseSpider


class DkAarhusVoxhallHeavySpider(DkAarhusVoxhallBaseSpider):
    name = 'dk_aarhus_voxhall'
    allowed_domains = ['fondenvoxhall.dk']
    start_urls = ['https://fondenvoxhall.dk/genre/heavy/']

    def get_genre(self):
        return "Heavy"
