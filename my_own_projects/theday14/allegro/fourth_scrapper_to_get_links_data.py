# Standard library imports
import os
import json
import requests


# Open json file with stored links
with open('stored_links.json', 'r') as data_file:
    data = json.load(data_file)
    for list_with_offers in data:
        for item in list_with_offers:
            print(item)
            offers = os.listdir('offers')
            number_of_offers = len(offers)
            i = number_of_offers + 1
            url = item
            response = requests.get(url)
            content = response.text
            if i<10:
                path = f'offers/offer_000{i}.html'
            elif i<100:
                path = f'offers/offer_00{i}.html'
            elif i<1000:
                path = f'offers/offer_0{i}.html'
            else:
                path = f'offers/offer_{i}.html'
            # Get offers data and save each offer data as separate html file
            with open(path, 'w', encoding='utf-8') as output_data:
                output_data.write(content)

