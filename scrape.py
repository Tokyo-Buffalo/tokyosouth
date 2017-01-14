#!/env/bin/activate python3
"""
Scraping Southwest Airlines for Search Results
@author: tokyobuffalo
@creation date: 1/5/2017 Year of the Trump
"""

import requests
import datetime
import scrapy

class SouthwestSpider(scrapy.Spider):
    name = 'flights'

    def start_requests(self):
        print("hello")
        url = 'https://www.southwest.com'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'flights-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

if __name__ == "__main__":
    scrapy = SouthwestSpider()
