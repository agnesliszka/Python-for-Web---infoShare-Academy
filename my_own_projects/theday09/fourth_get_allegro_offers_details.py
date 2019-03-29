# Standard library imports
import os
import json

# 3rd party imports
from bs4 import BeautifulSoup
from parsel import Selector


offers_data = {}

# Function to load an offer file data from offer catalog
def load_offer(_offer):
    file_name = os.path.join('offers', _offer)
    with open(file_name, 'r', encoding="utf-8") as _file_in:
        _data = _file_in.read()
    return _data

# Function to get required data of the corresponding offer
def get_details(_data):
    soup = BeautifulSoup(_data, 'html.parser')

    # Get table where searched parameters and their values are stored
    filtered = soup.find_all(attrs={"data-box-name": "Parameters"})
    filtered_string = str(filtered)

    # Get each element of table where searched parameters and their values are stored as a separate list element
    selector = Selector(text=filtered_string)
    filtered_div_data = selector.css('div::text').getall()

    # List searched labels
    labels = ["Faktura", "Informacje dodatkowe",
              "Kierownica po prawej (Anglik)", "Kolor", "Kraj pochodzenia",
              "Lakier", "Liczba drzwi", "Liczba miejsc", "Moc", "Napęd",
              "Pojemność silnika", "Przebieg", "Rodzaj paliwa",
              "Rok produkcji", "Stan", "Uszkodzony", ]

    # Loop for searched data (listed as labels)
    for element in filtered:
        for label in labels:
            anchor = element.find("div", text=label + ":")
            if (label+":") in filtered_div_data:
                print(label, ':', anchor.find_next_sibling("div").text)
                offers_data[label] = anchor.find_next_sibling("div").text
            else:
                continue

    # Search for price
    filtered = soup.find(itemprop="price")
    print("Cena : "+filtered.get('content'))
    offers_data['Cena'] = filtered.get('content')

    # Search for price currency
    filtered = soup.find(itemprop="priceCurrency")
    print("Waluta : "+filtered.get('content'))
    offers_data['Waluta'] = filtered.get('content')

    # Search for company name
    filtered = soup.find(attrs={"data-analytics-click-value": "sellerLogin"})
    for i in filtered:
        print("Nazwa firmy : "+i, len(filtered), '--')
        offers_data['Nazwa firmy'] = i, len(filtered), '--'

    # Search for location
    filtered = soup.find(attrs={'data-analytics-interaction-value': "LocationShow"})
    for i in filtered:
        print("Lokalizacja : "+i, '---', len(filtered), '+++')
        offers_data['Lokalizacja'] = i, '---', len(filtered), '+++'

    return ''

# Create a json file to store the offers data
with open('stored_offers_data_css.json', 'w', encoding="utf-8") as data_file:
    offers = os.listdir('offers')
    for offer in offers:
        # Print offer file name
        print(offer)
        # Save offers title to json's file
        json.dump(offer, data_file, indent=4, ensure_ascii=False)
        # Load an offer file data from offer catalog
        data = load_offer(offer)
        # Print searched data of the corresponding offer
        print(get_details(data))
        # Save offers details to json's file
        json.dump(offers_data, data_file, indent=4, ensure_ascii=False)

