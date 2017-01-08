#!/env/bin/activate python3
"""
Scraping Southwest Airlines for Search Results
@author: tokyobuffalo
@creation date: 1/5/2017 Year of the Trump
"""

import requests
import datetime
import scrapy
from lxml import html
from scrapy.spiders import CrawlSpider, Rule
#from scrapy.contrib.linkextractors import LinkExtractor

dateNow = datetime.datetime.now()
year = dateNow.year
month = dateNow.month
day = dateNow.day

page = requests.get("http://www.southwest.com")
tree = html.fromstring(page.content)

class SouthwestSpider(scrapy.Item, CrawlSpider):
	originAirport = scrapy.Field()
	destinationAirpot = scrapy.Field()
	name = 'southwest'
	allowed_domains = ['southwest.com']
	start_url = 'https://www.southwest.com'

def main():
	print(tree)
	print("%d / %d / %d" % (month, day, year))

if __name__ == "__main__":
	main()
