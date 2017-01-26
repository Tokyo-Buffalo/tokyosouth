import scrapy

class FlightsSpider(scrapy.Spider):
	name = "flights"

	def start_requests(self):
		urls = [
			'https://www.southwest.com',
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		page = response.url.split("/")[-2]
		filename = "flights-%s.html" % page
		with open(filename, 'wb') as f:
			f.write(response.body)
			f.log('Saved file %s' % filename)
