# Standard library imports
import json
import requests

# 3rd party imports
from parsel import Selector


# Create required lists
url_list = ['https://www.olx.pl/motoryzacja/samochody/']
links_data_list = []

# Function to get links of pages where you can find links to the offers
def get_next_page_with_links():
    # Get page links where you can find offer links
    url = 'https://www.olx.pl/motoryzacja/samochody/'
    for i in range(2):
        response = requests.get(url)
        content = response.text
        selector = Selector(text=content)

        # Get next page url
        next_page_url = selector.css('#body-container > div:nth-child(3) > div > div.pager.rel.clr > span.fbold.next.abs.large > a::attr(href)').get()
        print(next_page_url)
        url_list.append(next_page_url)
        url = next_page_url

# Get page links where you can find offer links
get_next_page_with_links()

# Function to get offer links
def get_links(url):
    # Get page from url
    response = requests.get(url)
    content = response.text

    # Get offer links from url
    selector = Selector(text=content)
    links_data = selector.css('.marginright5.link.linkWithHash::attr(href)').getall()
    links_data_list.append(links_data)

for url in url_list:
    get_links(url)

# Create a json file to store the page data
with open('stored_links.json', 'w', encoding="utf-8") as stored_links:
    # Save offers links to json's file
    json.dump(links_data_list, stored_links, indent=4, ensure_ascii=False)