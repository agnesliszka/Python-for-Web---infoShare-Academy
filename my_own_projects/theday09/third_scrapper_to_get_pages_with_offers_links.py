# Standard library imports
import json
import requests

# 3rd party imports
from parsel import Selector

url_list = ['https://allegro.pl/kategoria/samochody-osobowe-4029?order=m&bmatch=baseline-n-ann-1-5-0131']
links_data_list = []

def get_next_page_with_links():
    # Get page links where you can find offer links
    url = 'https://allegro.pl/kategoria/samochody-osobowe-4029?order=m&bmatch=baseline-n-ann-1-5-0131'
    for i in range(3):  # to be changed to 42
        response = requests.get(url)
        content = response.text
        selector = Selector(text=content)

        # Get next page url
        next_page_url = selector.css('.m-pagination__list ~ a::attr(href)').get()
        print(next_page_url)
        url_list.append(next_page_url)
        url = next_page_url

get_next_page_with_links()

def get_links(url):
    # Get page from url
    response = requests.get(url)
    content = response.text

    # Get offer links from url
    selector = Selector(text=content)
    links_data = selector.css('.ebc9be2 > a::attr(href)').getall()
    links_data_list.append(links_data)

for url in url_list:
    get_links(url)

# Create a json file to store the page data
with open('stored_links.json', 'a', encoding="utf-8") as stored_links:
    # Save offers links to json's file
    json.dump(links_data_list, stored_links, indent=4, ensure_ascii=False)