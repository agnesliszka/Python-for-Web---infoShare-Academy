import os
import requests

from parsel import Selector

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
    selector = Selector(text=_data)

    # Get title of the page
    # Alternative solutions:
    print(selector.css('title::text'))
    print(selector.css('head > title::text'))
    # Get HTML text
    # Alternative solutions:
    print(selector.css('title::text').get())
    print(selector.css('head > title::text').get())

    # Get category
    print(selector.css('#parameters > ul:nth-child(1) > li:nth-child(2) > span::text').get(), ' ', end="")
    print(selector.css('#parameters > ul:nth-child(1) > li:nth-child(2) > div > a::attr(title)').get())

    # Get a price currency
    print(selector.css('.offer-price__currency::text').get())

    # Get location
    print(selector.css('#siteWrap > main > div.offer-content.offer-content--primary > div > div.offer-content__aside > div > div.seller-box__seller-address > span.seller-box__seller-address__label::text').getall())

    # Get an engine capacity
    print(selector.css('#parameters > ul:nth-child(1) > li:nth-child(8) > div::text').get())

    # Get a power
    print(selector.css('#parameters > ul:nth-child(1) > li:nth-child(10) > div::text').get())

    # Get a colour
    print(selector.css('#parameters > ul:nth-child(2) > li:nth-child(2) > div > a::text').get())

    # Get a course
    print(selector.css('#parameters > ul:nth-child(1) > li:nth-child(7) > div::text').get())

    # Get a fuel type
    print(selector.css('#parameters > ul:nth-child(1) > li:nth-child(9) > div > a::text').get())

    # Get a production year
    print(selector.css('#parameters > ul:nth-child(1) > li:nth-child(6) > div::text').get())

offers = (
    'ford-focus-salon-polska-klima-sprawy-zadbany-polecam-ID6BxpMS.html',
    'ford-focus-1-6-tdci-salon-polska-serwis-aso-klima-ID6BwGlg.html'
)

urls = (
    'https://www.otomoto.pl/oferta/ford-focus-focus-1-6-tdci-115km-salon-polska-serwisowany-ID6BKDkl.html#de41e6ae06',
    'https://www.otomoto.pl/oferta/ford-focus-1-8-tdci-fv23-ID6BBmwH.html#de41e6ae06'
)

filenames = (
    'data\\ford-focus-salon-polska-klima-sprawy-zadbany-polecam-ID6BxpMS.html',
    'data\\ford-focus-1-6-tdci-salon-polska-serwis-aso-klima-ID6BwGlg.html'
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
