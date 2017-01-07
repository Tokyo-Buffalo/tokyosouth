#!/env/bin/activate python3
"""
Scraping Southwest Airlines for Search Results
@author: tokyobuffalo
@creation date: 1/5/2017 Year of the Trump
"""

from lxml import html
import requests

page = requests.get("http://www.southwest.com")
tree = html.fromstring(page.content)


def main():

	print(tree)

if __name__ == "__main__":
	main()