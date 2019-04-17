# Standard library imports
import os
import re
import json

# 3rd party imports
from parsel import Selector


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

    # Search for brand
    filtered = selector.xpath('//*[@id="parameters"]/ul[1]/li[3]/div/a/text()').get()
    filtered = filtered.strip()
    print("Marka : " + filtered)
    offers_data['brand'] = filtered

    # Search for model
    filtered = selector.xpath('//*[@id="parameters"]/ul[1]/li[4]/div/a/text()').get()
    filtered = filtered.strip()
    print("Model : " + str(filtered))
    offers_data['model'] = filtered

    # Search for production_year
    pattern = '[0-9]{4}\s*<\/div>'
    match = re.search(pattern, data)
    start_position = match.start()
    end_position = match.end()
    regex_data = data[start_position:end_position]
    filtered = regex_data[ :-7]
    print("Rok produkcji : " + str(filtered))
    offers_data['production_year'] = filtered

    # Search for course
    pattern = '[0-9]*\s*[0-9]*\s*km\s*<\/div>'
    match = re.search(pattern, data)
    start_position = match.start()
    end_position = match.end()
    regex_data = data[start_position:end_position]
    filtered = regex_data[ :-17]
    print("Przebieg : " + str(filtered))
    offers_data['course'] = filtered

    # Search for capacity
    pattern = '[0-9]*\s*km\s*<\/div>' # to be corrected
    match = re.search(pattern, data)
    start_position = match.start()
    end_position = match.end()
    regex_data = data[start_position:end_position]
    filtered = regex_data[:-5]
    print("Pojemnosc : " + str(filtered))
    offers_data['capacity'] = filtered

    # Search for power
    filtered = selector.xpath('//*[@id="parameters"]/ul[1]/li[9]/div/text()').get()
    filtered = filtered.strip()
    filtered = filtered[:-3]
    print("Moc : " + str(filtered))
    offers_data['power'] = filtered

    # Search for fuel_type
    filtered = selector.xpath('//*[@id="parameters"]/ul[1]/li[8]/div/a/text()').get()
    filtered = filtered.strip()
    print("Rodzaj paliwa : " + str(filtered))
    offers_data['fuel_type'] = filtered

    # Search for colour
    filtered = selector.xpath('//*[@id="parameters"]/ul[2]/li[1]/div/a/text()').get()
    filtered = filtered.strip()
    print("Kolor : " + str(filtered))
    offers_data['colour'] = filtered

    # Search if damaged - in oto moto "Bezwypadkowy" category instead of "Uszkodzony"
    filtered = selector.xpath('//*[@id="parameters"]/ul[2]/li[8]/div/a/text()').get()
    filtered = filtered.strip().lower()
    if filtered == "tak":
        filtered = "Bezwypadkowy"
    elif filtered == "nie":
        filtered = "Uszkodzony"
    else:
        filtered = "brak danych"
    print("Uszkodzony : " + str(filtered))
    offers_data['damaged'] = filtered

    # Search for country
    filtered = selector.xpath('//*[@id="parameters"]/ul[2]/li[4]/div/a/text()').get()
    filtered = filtered.strip()
    print("Kraj pochodzenia : " + str(filtered))
    offers_data['country'] = filtered

    # Search for driving_gear
    filtered = selector.css('#parameters > ul:nth-child(2) > li:nth-child(1) > div > a::text').get()
    filtered = filtered.strip()
    print("Naped : " + str(filtered))
    offers_data['driving_gear'] = filtered

    # Search for number_of_seats
    filtered = selector.xpath('//*[@id="parameters"]/ul[1]/li[13]/div/text()').get()
    filtered = filtered.strip()
    print("Liczba miejsc : " + str(filtered))
    offers_data['number_of_seats'] = filtered

# Function to get required data of the corresponding offer from olx portal
def get_details_olx(data):
    # Get each element of table where searched parameters and their values are stored as a separate list element
    selector = Selector(text=data)

    # Search for offer_id
    filtered_basic = selector.xpath('//*[@id="offerdescription"]/div[2]/div[1]/em/small/text()').get()
    filtered_basic = filtered_basic.strip()
    pattern = '[0-9]+'
    match = re.search(pattern, filtered_basic)
    if match:
        start_position = match.start()
        end_position = match.end()
        filtered = filtered_basic[start_position:end_position]
    print("ID oferty : " + filtered)
    offers_data['offer_id'] = filtered

    # Search for seller_id
    filtered = selector.xpath('//*[@id="offeractions"]/div[3]/div[2]/h4/a/text()').get()
    filtered = filtered.strip()
    print("ID sprzedajacego : " + filtered)
    offers_data['seller_id'] = filtered

    # Search for location
    filtered = selector.xpath('//*[@id="offerdescription"]/div[2]/div[1]/a/strong/text()').get()
    filtered = filtered.strip()
    print("Lokalizacja : " + filtered)
    offers_data['location'] = filtered

    # Search for title
    filtered = selector.css('title::text').get()
    filtered = filtered.strip()
    print("Tytul : " + filtered)
    offers_data['title'] = filtered

    # Search for price
    filtered = selector.xpath('//*[@id="offeractions"]/div[1]/strong/text()').get()
    filtered = filtered.strip()
    filtered = filtered[:-3]
    print("Cena : " + filtered)
    offers_data['price'] = filtered

    # Search for brand
    filtered = selector.xpath('//*[@id="offerdescription"]/div[3]/table/tr/td[2]/table/tr/td/strong/a/text()').get()
    filtered = filtered.strip()
    print("Marka : " + filtered)
    offers_data['brand'] = filtered

    # Search for model
    filtered = selector.xpath('//*[@id="offerdescription"]/div[3]/table/tr[2]/td/table/tr/td/strong/a/text()').get()
    filtered = filtered.strip()
    print("Model : " + str(filtered))
    offers_data['model'] = filtered

    # Search for production_year
    filtered = selector.xpath('//*[@id="offerdescription"]/div[3]/table/tr[2]/td[2]/table/tr/td/strong/text()').get()
    filtered = filtered.strip()
    print("Rok produkcji : " + str(filtered))
    offers_data['production_year'] = filtered

    # Search for course
    filtered = selector.xpath('//*[@id="offerdescription"]/div[3]/table/tr[4]/td[2]/table/tr/td/strong/text()').get()
    filtered = filtered.strip()
    filtered = filtered[:-3]
    print("Przebieg : " + str(filtered))
    offers_data['course'] = filtered

    # Search for capacity
    filtered = selector.xpath('//*[@id="offerdescription"]/div[3]/table/tr[3]/td/table/tr/td/strong/text()').get()
    filtered = filtered.strip()
    filtered = filtered[:-3]
    print("Pojemnosc : " + str(filtered))
    offers_data['capacity'] = filtered

    # Search for power
    filtered = selector.xpath('//*[@id="offerdescription"]/div[3]/table/tr[4]/td/table/tr/td/strong/text()').get()
    filtered = filtered.strip()
    filtered = filtered[:-3]
    print("Moc : " + str(filtered))
    offers_data['power'] = filtered

    # Search for fuel_type
    filtered = selector.xpath('//*[@id="offerdescription"]/div[3]/table/tr[3]/td[2]/table/tr/td/strong/a/text()').get()
    filtered = filtered.strip()
    print("Rodzaj paliwa : " + str(filtered))
    offers_data['fuel_type'] = filtered

    # Search for colour
    filtered = selector.xpath('//*[@id="offerdescription"]/div[3]/table/tr[5]/td[2]/table/tr/td/strong/a/text()').get()
    filtered = filtered.strip()
    print("Kolor : " + str(filtered))
    offers_data['colour'] = filtered

    # Search if damaged - in oto moto "Bezwypadkowy" category instead of "Uszkodzony"
    filtered = selector.xpath('//*[@id="offerdescription"]/div[3]/table/tr[6]/td/table/tr/td/strong/a/text()').get()
    filtered = filtered.strip()
    print("Uszkodzony : " + str(filtered))
    offers_data['damaged'] = filtered

    # Search for country
    filtered = selector.xpath('//*[@id="offerdescription"]/div[3]/table/tr[7]/td/table/tr/td/strong/a/text()').get()
    filtered = filtered.strip()
    print("Kraj pochodzenia : " + str(filtered))
    offers_data['country'] = filtered

    # # Search for driving_gear
    filtered = 'brak danych'
    print("Naped : " + str(filtered))
    offers_data['driving_gear'] = filtered

    # Search for number_of_seats
    filtered = 'brak danych'
    print("Liczba miejsc : " + str(filtered))
    offers_data['number_of_seats'] = filtered

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
            get_details_olx(data)
        # Add searched data to the output list
        output.append(offers_data)

    # Save offers details to a json's file
    json.dump(output, data_file, indent=4, ensure_ascii=False)
