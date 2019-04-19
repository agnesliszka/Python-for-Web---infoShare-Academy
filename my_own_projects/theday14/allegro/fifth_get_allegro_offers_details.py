# Standard library imports
import os
import re
import json

# 3rd party imports
from bs4 import BeautifulSoup
from parsel import Selector
from decimal import *


# Create output list
output = []

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

    # List of searched labels
    labels = ["Rok produkcji", "Przebieg", "Pojemność silnika", "Moc", "Rodzaj paliwa",
              "Kolor", "Uszkodzony", "Kraj pochodzenia", "Napęd", "Liczba miejsc"]

    database_labels = ['production_year', 'course', 'capacity', 'power', 'fuel_type', 'colour', 'damaged', 'country', 'driving_gear', 'number_of_seats']

    # Loop for searched data (listed as labels)
    for element in filtered:

        # Search for offer_id
        filtered = soup.find("span", attrs={"class": "_6c864829"})
        print("ID oferty : ", filtered.find_next_sibling("span").text)
        offers_data['offer_id'] = filtered.find_next_sibling("span").text

        # Search for seller_id
        filtered = soup.find(attrs={"data-analytics-click-value": "sellerLogin"})
        print("ID sprzedajacego : " + filtered.text)
        offers_data['seller_id'] = filtered.text
        # for i in filtered:
        #     print("Nazwa firmy : " + i)
        #     offers_data['Nazwa firmy'] = i

        # Search for location
        filtered = soup.find(attrs={'data-analytics-interaction-value': "locationShow"})
        print("Lokalizacja : " + filtered.text)
        offers_data['location'] = filtered.text
        # for i in filtered:
        #     print("Lokalizacja : " + i, '---', len(filtered), '+++')
        #     offers_data['Lokalizacja'] = i, '---', len(filtered), '+++'

        # Search for title
        filtered = soup.find("title")
        print("Tytul : " + filtered.text)
        offers_data['title'] = filtered.text

        # Search for price
        filtered = soup.find(itemprop="price")
        print("Cena : " + filtered.get('content'))
        offers_data['price'] = Decimal(filtered.get('content'))

        selector2 = Selector(text=_data)

        # Search for brand
        filtered = selector2.css('body > div.main-wrapper > div:nth-child(3) > div > div > div:nth-child(1) > div > div > div > div > div > div:nth-child(6) > a > span::text').get()
        print("Marka : " + filtered)
        offers_data['brand'] = filtered
        # filtered = soup.find("title")
        # print("Marka : " + (filtered.text.split(' ', 1)[0]).capitalize())
        # offers_data['Marka'] = (filtered.text.split(' ', 1)[0]).capitalize()

        # Search for model
        filtered = selector2.css('body > div.main-wrapper > div:nth-child(3) > div > div > div:nth-child(1) > div > div > div > div > div > div:nth-child(7) > a > span::text').get()
        print("Model : " + str(filtered))
        offers_data['model'] = filtered
        # filtered = name_filtered[2]

        # Search for additional parameters and their values
        for label in labels:
            index = labels.index(label)
            anchor = element.find("div", text=label + ":")
            if label in ["Przebieg", "Pojemność silnika", "Moc"]:
                if (label+":") in filtered_div_data:
                    output_data = anchor.find_next_sibling("div").text
                    # pattern = '\d+'
                    pattern = '[0-9]+'
                    match = re.search(pattern, output_data)
                    start_position = match.start()
                    end_position = match.end()
                    data_without_units = output_data[start_position:end_position]
                    data_without_units = int(data_without_units)

                    print(label, ':', anchor.find_next_sibling("div").text)
                    offers_data[database_labels[index]] = data_without_units
                else:
                    continue
            else:
                if (label+":") in filtered_div_data:
                    print(label, ':', anchor.find_next_sibling("div").text)
                    offers_data[database_labels[index]] = anchor.find_next_sibling("div").text
                else:
                    continue
        print('')
    return ''

# Create a json file to store the offers data
with open('stored_offers_data.json', 'w', encoding="utf-8") as data_file:
    offers = os.listdir('offers')
    for offer in offers:
        offers_data = {}
        # Print offer file name
        print(offer)
        # Load an offer file data from offer catalog
        data = load_offer(offer)
        # Print searched data of the corresponding offer
        get_details(data)
        # Add searched data to the output list
        output.append(offers_data)

    # Save offers details to a json's file
    json.dump(output, data_file, indent=4, ensure_ascii=False)
