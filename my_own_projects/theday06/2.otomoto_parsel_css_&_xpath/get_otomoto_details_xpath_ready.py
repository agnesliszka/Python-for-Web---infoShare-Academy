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
    print(selector.xpath('//title/text()'))

    # Get HTML text
    print(selector.xpath('//title/text()').get())  # pojedynczy, pierwszy rezultat

    # Get category
    print(selector.xpath('//*[@id="parameters"]/ul[1]/li[2]/span/text()').get(), ' ', end="")
    print(selector.xpath('//*[@id="parameters"]/ul[1]/li[2]/div/a/@title').get())

    # Get a price currency
    print(selector.xpath('//*[@id="siteWrap"]/main/section/div[3]/div[1]/span[1]/span/text()').get())

    # Get location
    # Alternative solutions:
    print(selector.xpath('//*[@id="siteWrap"]/main/div[1]/div/div[5]/div/div[2]/span[2]/text()').getall())
    print(selector.xpath('//*[@id="siteWrap"]/main/div[1]/div/div[5]/div/div[3]/span[2]/text()').getall())

    # Get an engine capacity
    print(selector.xpath('//*[@id="parameters"]/ul[1]/li[8]/div/text()').get())

    # Get a power
    print(selector.xpath('//*[@id="parameters"]/ul[1]/li[10]/div/text()').get())

    # Get a colour
    print(selector.xpath('//*[@id="parameters"]/ul[2]/li[2]/div/a/text()').get())

    # Get a course
    print(selector.xpath('//*[@id="parameters"]/ul[1]/li[7]/div/text()').get())

    # Get a fuel type
    print(selector.xpath('//*[@id="parameters"]/ul[1]/li[9]/div/a/text()').get())

    # Get a production year
    print(selector.xpath('//*[@id="parameters"]/ul[1]/li[6]/div/text()').get())

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
