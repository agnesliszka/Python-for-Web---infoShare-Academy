# Standard library imports
import os
import re
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

    # Get table where searched parameters and their values are storedclients_orm.db
    filtered = soup.find_all(attrs={"data-box-name": "Parameters"})
    filtered_string = str(filtered)

    # Get each element of table where searched parameters and their values are stored as a separate list element
    selector = Selector(text=filtered_string)
    filtered_div_data = selector.css('div::text').getall()

    # List searched labels
    labels = ["Rok produkcji", "Przebieg", "Pojemność silnika", "Moc", "Rodzaj paliwa",
              "Kolor", "Uszkodzony", "Faktura", "Informacje dodatkowe", "Kraj pochodzenia",
              "Napęd", "Liczba miejsc"]

    # Loop for searched data (listed as labels)
    for element in filtered:

        # Search for offer_id
        filtered = soup.find("span", attrs={"class": "_6c864829"})
        print("ID oferty : ", filtered.find_next_sibling("span").text)
        offers_data['ID oferty'] = filtered.find_next_sibling("span").text

        # Search for seller_id
        filtered = soup.find(attrs={"data-analytics-click-value": "sellerLogin"})
        print("ID sprzedajacego : " + filtered.text)
        offers_data['ID sprzedajacego'] = filtered.text
        # for i in filtered:
        #     print("Nazwa firmy : " + i)
        #     offers_data['Nazwa firmy'] = i

        # Search for location
        filtered = soup.find(attrs={'data-analytics-interaction-value': "locationShow"})
        print("Lokalizacja : " + filtered.text)
        offers_data['Lokalizacja'] = filtered.text
        # for i in filtered:
        #     print("Lokalizacja : " + i, '---', len(filtered), '+++')
        #     offers_data['Lokalizacja'] = i, '---', len(filtered), '+++'

        # Search for title
        filtered = soup.find("title")
        print("Tytul : " + filtered.text)
        offers_data['Tytul'] = filtered.text

        # Search for price
        filtered = soup.find(itemprop="price")
        print("Cena : " + filtered.get('content'))
        offers_data['Cena'] = filtered.get('content')

        selector2 = Selector(text=_data)

        # Search for brand
        filtered = selector2.css('body > div.main-wrapper > div:nth-child(3) > div > div > div:nth-child(1) > div > div > div > div > div > div:nth-child(6) > a > span::text').get()
        print("Marka : " + filtered)
        offers_data['Msrka'] = filtered
        # filtered = soup.find("title")
        # print("Marka : " + (filtered.text.split(' ', 1)[0]).capitalize())
        # offers_data['Marka'] = (filtered.text.split(' ', 1)[0]).capitalize()

        # Search for model
        filtered = selector2.css('body > div.main-wrapper > div:nth-child(3) > div > div > div:nth-child(1) > div > div > div > div > div > div:nth-child(7) > a > span::text').get()
        print("Model : " + filtered)
        offers_data['Model'] = filtered
        # # filtered = name_filtered[2]

        for label in labels:
            anchor = element.find("div", text=label + ":")
            if (label+":") in filtered_div_data:
                print(label, ':', anchor.find_next_sibling("div").text)
                offers_data[label] = anchor.find_next_sibling("div").text
            else:
                continue

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

