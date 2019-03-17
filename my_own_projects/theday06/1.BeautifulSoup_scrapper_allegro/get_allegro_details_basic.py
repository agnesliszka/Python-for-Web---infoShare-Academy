import os

from bs4 import BeautifulSoup

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
    filtered_login = soup.find(attrs={"data-analytics-interaction-value": "LocationShow"})
    print(filtered_login.next)

    # Search for auction title
    print(soup.title.text)

    return ''

offers = (
    'offer_7192730975_mk3.html',
    'offer_7350326221_mk3.html'
)

# For each offer load the file, get required data and print them in console
for offer in offers:
    data = load_offer(offer)
    get_details(data)
    print('-' * 80)


