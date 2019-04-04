# Standard library imports
import json
import requests

# 3rd party imports
from parsel import Selector


# Get page from url
# url = 'https://allegro.pl/kategoria/porsche-911-14667?order=m&bmatch=baseline-n-ann-1-2-0131'
url = 'https://allegro.pl/kategoria/samochody-osobowe-4029?order=m&bmatch=baseline-n-ann-1-5-0131'
response = requests.get(url)
content = response.text

# Get offer links from url
selector = Selector(text=content)
links_data = selector.css('.ebc9be2 > a::attr(href)').getall()

# Create a json file to store the page data
with open('stored_links.json', 'w', encoding="utf-8") as stored_links:
    # Save offers links to json's file
    json.dump(links_data, stored_links, indent=4, ensure_ascii=False)

