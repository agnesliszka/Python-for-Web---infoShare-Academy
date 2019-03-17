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

# For each offer load the file, get required data and print them in console
for offer in offers:
    data = load_offer(offer)
    get_details(data)
    print('-' * 40)
