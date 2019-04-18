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
    try:
        filtered = selector.xpath('//*[@id="siteWrap"]/main/div[1]/div/div[5]/div/div[1]/h2/text()').get()
        filtered = filtered.strip()
        print("ID sprzedajacego : " + filtered)
        offers_data['seller_id'] = filtered
    except:
        print("ok")
        filtered = selector.xpath('//*[@id="siteWrap"]/main/div[1]/div/div[5]/div/div[1]/h2/a/text()').get()
        filtered = filtered.strip()
        print("ID sprzedajacego : " + filtered)
        offers_data['seller_id'] = filtered

    # Search for location
    try:
        filtered = selector.xpath('//*[@id="siteWrap"]/main/div[1]/div/div[5]/div/div[2]/span[2]/text()').get()
        filtered = filtered.strip()
        print("Lokalizacja : " + filtered)
        offers_data['location'] = filtered
    except:
        filtered = selector.xpath('//*[@id="siteWrap"]/main/div[1]/div/div[5]/div/div[3]/span[2]/text()').get()
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
    # print(searched_row)
    # searched_row_string = str(searched_row)

    # List of searched labels
    labels1 = ["Marka pojazdu", "Model pojazdu", "Rodzaj paliwa", "Kolor", "Bezwypadkowy", "Kraj pochodzenia", "Napęd", ]
    labels_in_table1 = ["brand", "model", "fuel_type", "colour", "damaged", "country", "driving_gear"]

    labels2 = ["Rok produkcji", "Przebieg", "Pojemność skokowa", "Moc", "Liczba miejsc"]
    labels_in_table2 = ["production_year", "course", "capacity", "power", "number_of_seats"]

    for row in searched_row:
        soup = BeautifulSoup(str(row), 'html.parser')
        # selector_row = Selector(text=str(row))
        for label1 in labels1:
            idx1 = labels1.index(label1)
            if label1 in str(row):
                # Get label data
                searched_label_data1 = soup.a.string
                # searched_label_data = selector_row.xpath('//li/div/a/text()').get()
                searched_label_data1 = searched_label_data1.strip()
                if label1 == "Bezwypadkowy":
                    if searched_label_data1.lower() == "tak":
                        searched_label_data1 = "Bezwypadkowy"
                    elif searched_label_data1.lower() == "nie":
                        searched_label_data1 = "Uszkodzony"
                    else:
                        searched_label_data1 = "brak danych"
                    print("Uszkodzony : " + searched_label_data1)
                    offers_data[labels_in_table1[idx1]] = searched_label_data1
                else:
                    print(label1+" : " + searched_label_data1)
                    offers_data[labels_in_table1[idx1]] = searched_label_data1
        for label2 in labels2:
            idx2 = labels2.index(label2)
            if label2 in str(row):
                # Get label data
                searched_label_data2 = soup.div.string
                searched_label_data2 = searched_label_data2.strip()
                if label2 in ["Przebieg", "Pojemność skokowa", "Moc"]:
                    searched_label_data2 = searched_label_data2[:-3]
                    print(label2 + " : " + searched_label_data2)
                    offers_data[labels_in_table2[idx2]] = searched_label_data2
                else:
                    print(label2+" : " + searched_label_data2)
                    offers_data[labels_in_table2[idx2]] = searched_label_data2

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
    try:
        filtered = selector.xpath('//*[@id="offeractions"]/div[3]/div[2]/h4/a/text()').get()
        filtered = filtered.strip()
        print("ID sprzedajacego : " + filtered)
        offers_data['seller_id'] = filtered
    except:
        filtered = selector.xpath('//*[@id="offeractions"]/div[3]/div[2]/h4/text()').get()
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

    # Search for table with data
    searched_table = selector.xpath('//*[@id="offerdescription"]/div[3]/table').get()
    selector_row = Selector(text=searched_table)

    # Search for rows - list elements of table with searched data
    searched_row = selector_row.css(".col").getall()
    # print(searched_row)
    # searched_row_string = str(searched_row)

    # List of searched labels
    labels1 = ["Marka", "Model", "Paliwo", "Kolor", "Stan techniczny", "Kraj pochodzenia"]
    labels_in_table1 = ["brand", "model", "fuel_type", "colour", "damaged", "country"]

    labels2 = ["Rok produkcji", "Przebieg", "Poj. silnika", "Moc silnika"]
    labels_in_table2 = ["production_year", "course", "capacity", "power"]

    for row in searched_row:
        soup = BeautifulSoup(str(row), 'html.parser')
        # selector_row = Selector(text=str(row))
        for label1 in labels1:
            idx1 = labels1.index(label1)
            if label1 in str(row):
                # Get label data
                searched_label_data1 = soup.a.string
                # searched_label_data = selector_row.xpath('//li/div/a/text()').get()
                searched_label_data1 = searched_label_data1.strip()
                print(label1+" : " + searched_label_data1)
                offers_data[labels_in_table1[idx1]] = searched_label_data1
        for label2 in labels2:
            idx2 = labels2.index(label2)
            if label2 in str(row):
                # Get label data
                searched_label_data2 = soup.strong.string
                searched_label_data2 = searched_label_data2.strip()
                if label2 in ["Przebieg", "Poj. silnika", "Moc silnika"]:
                    searched_label_data2 = searched_label_data2[:-3]
                    print(label2 + " : " + searched_label_data2)
                    offers_data[labels_in_table2[idx2]] = searched_label_data2
                else:
                    print(label2+" : " + searched_label_data2)
                    offers_data[labels_in_table2[idx2]] = searched_label_data2

    # Search for driving_gear
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
            print("")
            get_details_otomoto(data)
        elif portal == "olx":
            get_details_olx(data)
        # Add searched data to the output list
        output.append(offers_data)

    # Save offers details to a json's file
    json.dump(output, data_file, indent=4, ensure_ascii=False)
