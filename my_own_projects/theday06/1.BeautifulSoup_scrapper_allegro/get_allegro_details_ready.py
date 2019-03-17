import os
import requests
from bs4 import BeautifulSoup

# Function to get page from url
def get_page(url, filename):
    response = requests.get(url)
    _data = response.text
    with open(filename, 'w', encoding='utf-8') as output_data:
        output_data.write(_data)
    return _data

# Function to load offer data from file
def load_offer(_offer):
    file_name = os.path.join('data', _offer)
    with open(file_name, encoding='utf-8') as _file_in:
        _data = _file_in.read()
    return _data

# Function to get searched data from the page
def get_details(_data):
    soup = BeautifulSoup(_data, 'html.parser')

    # Search for a container with the indicated attribute
    filtered = soup.find_all(attrs={"data-box-name": "Parameters"})

    # Create the list of searched parameters
    labels = ("Faktura", "Informacje dodatkowe", "Pojemność silnika", "Moc", "Kolor", "Przebieg", "Rodzaj paliwa", "Rok produkcji")

    for element in filtered:
        for label in labels:
            # Search for an item with a label
            anchor = element.find("div", text=label + ":")
            # Display the next element (sibling)
            print(label, ':', anchor.find_next_sibling("div").text)

    # Search for an item with an itemprop = "price" attribute
    filtered_price = soup.find(itemprop="price")
    print(filtered_price.get('content'))

    # Search for a price currency
    filtered_currency = soup.find(itemprop="priceCurrency")
    print(filtered_currency.get('content'))

    # Search for a seller's login
    filtered_login = soup.find(attrs={"data-analytics-click-value": "sellerLogin"})
    print(filtered_login.next)

    # Search for location
 #   filtered_login = soup.find(attrs={"data-analytics-interaction-value": "LocationShow"}) # does not work in new version of allegro sites
 #   print(filtered_login.next)

    # Search for auction title
    print(soup.title.text)
    # print(soup.title.string)

    return ''

offers = (
    'offer_7192730975_mk3.html',
    'offer_7350326221_mk3.html'
)

urls = (
    'https://allegro.pl/ogloszenie/ford-focus-mk3-trend-sport-priv-w-wa-7880155768',
    'https://allegro.pl/ogloszenie/ford-fokus-mk3-zadbany-serwisowany-7875274072/'
)

filenames = (
    'data\offer_7192730975_mk3.html',
    'data\offer_7350326221_mk3.html'
)

''' For each file if file exists load the file, get searched data and print them in console; 
if file does not exist get page from url, save the data in file, load the file, get searched data and print them in console'''
for filename in filenames:
    filename_index = filenames.index(filename)
    if os.path.isfile(filename):
        data = load_offer(offers[filename_index])
        get_details(data)
        print('-' * 80)
    else:
        get_page(urls[filename_index], filename)
        data = load_offer(offers[filename_index])
        get_details(data)
        print('-' * 80)
