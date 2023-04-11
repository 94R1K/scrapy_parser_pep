import re

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_REG


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response, **kwargs):
        pep_link = response.css('section#numerical-index td a::attr(href)')
        for peps in pep_link:
            yield response.follow(peps, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get()
        number, name = re.search(PEP_REG, title).groups()
        status = response.css(
            'dt:contains("Status") + dd'
        ).css('abbr::text').get()
        yield PepParseItem(dict(number=number, name=name, status=status))
