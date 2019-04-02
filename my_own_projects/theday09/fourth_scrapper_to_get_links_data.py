# Standard library imports
import json
import requests

# Open json file with stored links
with open('stored_links.json', 'r') as data_file:
    data = json.load(data_file)
    for item in data:
        print(item)
        i = data.index(item) + 1
        url = item
        response = requests.get(url)
        content = response.text
        if i<10:
            path = f'offers/offer_0{i}.html'
        else:
            path = f'offers/offer_{i}.html'
        # Get offers html data and save each offer data as separate file
        with open(path, 'w', encoding='utf-8') as output_data:
            output_data.write(content)
