# Standard library imports
import os
import re
import json

# 3rd party imports
from parsel import Selector
from bs4 import BeautifulSoup


# Create output list
output = []
html = []

# Function to load an offer file data from offer catalog
def load_offer(offer):
    file_name = os.path.join('offers', offer)
    with open(file_name, 'r', encoding="utf-8") as file_in:
        data = file_in.read()
    return data

# Function to get required data of the corresponding offer from otomoto portal
def get_details_otomoto(data):
    # Get each element of table where searched parameters and their values are stored as a separate list element
    selector = Selector(text=data)

    # Search for offer_id
    filtered = selector.xpath('//*[@id="siteWrap"]/main/div[1]/div/div[6]/div/span[2]/span[2]/text()').get()
    filtered = filtered.strip()
    print("ID oferty : " + filtered)
    offers_data['offer_id'] = filtered

    # Search for seller_id
    filtered = selector.xpath('//*[@id="siteWrap"]/main/div[1]/div/div[5]/div/div[1]/h2/text()').get()
    filtered = filtered.strip()
    print("ID sprzedajacego : " + filtered)
    offers_data['seller_id'] = filtered

    # Search for location
    filtered = selector.xpath('//*[@id="siteWrap"]/main/div[1]/div/div[5]/div/div[2]/span[2]/text()').get()
    filtered = filtered.strip()
    print("Lokalizacja : " + filtered)
    offers_data['location'] = filtered

    # Search for title
    filtered = selector.css('title::text').get()
    filtered = filtered.strip()
    print("Tytul : " + filtered)
    offers_data['title'] = filtered

    # Search for price
    filtered = selector.xpath('//*[@id="siteWrap"]/main/section/div[3]/div[1]/span[1]/text()').get()
    filtered = filtered.strip()
    print("Cena : " + filtered)
    offers_data['price'] = filtered

    # Search for table with data
    searched_table = selector.xpath('//*[@id="parameters"]').get()
    soup = BeautifulSoup(searched_table, 'html.parser')

    # Search for rows - list elements of table with searched data
    searched_row = soup.find_all('li')
    # searched_row_string = str(searched_row)

    # List of searched labels
    labels = ["Marka pojazdu", "Model pojazdu"]
    # index = searched_row.index(element)

    for row in searched_row:
        soup = BeautifulSoup(row, 'html.parser')
        for label in labels:
            if label in str(row):
                # Get label data
                searched_label_data = soup.a.string
                print(searched_label_data)
                # searched_label_data_string = str(searched_label_data)


        # if (label) in searched_data:
        #     print(label, ':', searched_label_data.find_next_sibling("div").text)
            # offers_data[database_labels[index]] = anchor.find_next_sibling("div").text


# Function to get required data of the corresponding offer from olx portal
# def get_details_olx(data):
#     # Get each element of table where searched parameters and their values are stored as a separate list element
#     selector = Selector(text=data)
#
#     # Search for offer_id
#     filtered_basic = selector.xpath('//*[@id="offerdescription"]/div[2]/div[1]/em/small/text()').get()
#     filtered_basic = filtered_basic.strip()
#     pattern = '[0-9]+'
#     match = re.search(pattern, filtered_basic)
#     if match:
#         start_position = match.start()
#         end_position = match.end()
#         filtered = filtered_basic[start_position:end_position]
#     print("ID oferty : " + filtered)
#     offers_data['offer_id'] = filtered
#
#     # Search for seller_id
#     filtered = selector.xpath('//*[@id="offeractions"]/div[3]/div[2]/h4/a/text()').get()
#     filtered = filtered.strip()
#     print("ID sprzedajacego : " + filtered)
#     offers_data['seller_id'] = filtered
#
#     # Search for location
#     filtered = selector.xpath('//*[@id="offerdescription"]/div[2]/div[1]/a/strong/text()').get()
#     filtered = filtered.strip()
#     print("Lokalizacja : " + filtered)
#     offers_data['location'] = filtered
#
#     # Search for title
#     filtered = selector.css('title::text').get()
#     filtered = filtered.strip()
#     print("Tytul : " + filtered)
#     offers_data['title'] = filtered
#
#     # Search for price
#     filtered = selector.xpath('//*[@id="offeractions"]/div[1]/strong/text()').get()
#     filtered = filtered.strip()
#     filtered = filtered[:-3]
#     print("Cena : " + filtered)
#     offers_data['price'] = filtered


# Get html path
with open('stored_links.json', 'r') as data_file:
    data = json.load(data_file)
    for list_with_offers in data:
        for item in list_with_offers:
            html.append(item)

# Create a json file to store the offers data
with open('stored_offers_data.json', 'w', encoding="utf-8") as data_file:
    offers = os.listdir('offers')
    for offer in offers:
        idx = offers.index(offer)
        portal = html[idx][12:15]
        offers_data = {}
        # Print offer file name
        print(offer)
        # Load an offer file data from offer catalog
        data = load_offer(offer)
        # Print searched data of the corresponding offer
        if portal == "oto":
            get_details_otomoto(data)
        elif portal == "olx":
            print("")
            # get_details_olx(data)
        # Add searched data to the output list
        output.append(offers_data)

    # Save offers details to a json's file
    json.dump(output, data_file, indent=4, ensure_ascii=False)
