import os

from parsel import Selector

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

# For each offer load the file, get required data and print them in console
for offer in offers:
    data = load_offer(offer)
    get_details(data)
    print('-' * 40)
