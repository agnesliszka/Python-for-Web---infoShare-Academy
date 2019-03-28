# Standard libriary imports
import os
import requests

# 3rd party imports
from parsel import Selector
from bs4 import BeautifulSoup

# Project imports
from beautiful_soup_example import get_page

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

# Get page from url
if __name__ =='__main__':
    url = 'https://allegro.pl/ogloszenie/porsche-911-turbo-s-techart-680km-salonpl-fv23-7867148731'
    filename = 'allegro_css.html'
    html_content = get_page(url, filename)

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



