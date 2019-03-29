# Standard library imports
import json
import requests

# 3rd party imports
from parsel import Selector


# Function to load offer data from file
def load_offer(offer):
    file_name = os.path.join('data', offer)
    with open(file_name, 'r', encoding='utf-8') as _file_in:
        data = _file_in.read()
    return data

# Get page from url
url = 'https://allegro.pl/kategoria/porsche-911-14667?order=m&bmatch=baseline-n-ann-1-2-0131'
response = requests.get(url)
content = response.text

# Get offer links from url
selector = Selector(text=content)
links_data = selector.css('.ebc9be2 > a::attr(href)').getall()

# Create a json file to store the page data
with open('stored_links.json', 'w', encoding="utf-8") as data_file:
    # Save offers links to json's file
    json.dump(links_data, data_file, indent=4, ensure_ascii=False)

# Open json file with stored links
with open('stored_links.json', 'r') as data_file:
    data = json.load(data_file)
    for item in data:
        print(item)

