# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import BaseSpider
from scrapy.http import FormRequest, Request
from scrapy.http import HtmlResponse
from scrapy.selector import Selector
class FlightsSpider(BaseSpider):
	name = "flights"

	def start_requests(self):
		urls = [
			'https://www.southwest.com/flight/search-flight.html?int=HOMEQBOMAIR',
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	"""
	def parse(self, response):
		page = response.url.split("/")[-2]
		filename = "flights-%s.html" % page
		with open(filename, 'wb') as f:
			f.write(response.body)
			f.log('Saved file %s' % filename)
	"""

	def parse(self, response):
		yield FormRequest.from_response(
			response,
			formname='buildItineraryForm',
			formdata = {
				'originAirport': 'IAD',
				'originAirport_displayed': 'Washington (Dulles), DC - IAD',
				'destinationAirport': 'FLL',
				'destinationAirport_displayed': 'Ft. Lauderdale, FL - FLL',
				'outboundDateString': '02/20/2017',
				'returnDateString': '03/30/2017'
			},
			callback=self.parseFlights
		)

	def parseFlights(self, response):
		filename = "flights.html"
		with open(filename, 'wb') as f:
			x = response.css(".searchResultsTable").extract()
			f.write(x[0].encode('utf-8').strip())
			f.write(x[1].encode('utf-8').strip())
		self.log('Saved file %s' % filename)
