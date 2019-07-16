from crawling.crawling.spiders.dk_aarhus_voxhall_base import DkAarhusVoxhallBaseSpider


class DkAarhusVoxhallUrbanSpider(DkAarhusVoxhallBaseSpider):
    name = 'dk_aarhus_voxhall'
    allowed_domains = ['fondenvoxhall.dk']
    start_urls = ['https://fondenvoxhall.dk/genre/urban/']

    def get_genre(self):
        return "Urban"

