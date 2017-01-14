#!/env/bin/activate python3
"""
Scraping Southwest Airlines for Search Results
@author: tokyobuffalo
@creation date: 1/5/2017 Year of the Trump
"""

import requests
import datetime
import scrapy

dateNow = datetime.datetime.now()
year = dateNow.year
month = dateNow.month
day = dateNow.day

class SouthwestSpider(scrapy.Spider):

    def start_request(self):
        url = 'https://www.southwest.com'
        name = 'southwest'
        allowed_domains = ['southwest.com']
        scrapy.Requests(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'flights-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

def main():
    print("%d / %d / %d" % (month, day, year))

if __name__ == "__main__":
    main()
