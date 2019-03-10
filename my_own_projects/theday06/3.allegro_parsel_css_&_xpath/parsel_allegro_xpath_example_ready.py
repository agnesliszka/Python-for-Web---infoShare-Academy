# 3rd party imports
from parsel import Selector

# project imports
from beautiful_soup_example import get_page

# Get page from url
if __name__ =='__main__':
    url = 'https://allegro.pl/ogloszenie/porsche-911-turbo-s-techart-680km-salonpl-fv23-7867148731'
    filename = 'allegro_xpath.html'
    html_content = get_page(url, filename)

    selector = Selector(text=html_content)

    # Search for particular item on the page
    invoice = selector.xpath('/html/body/div[2]/div[3]/div/div/div[4]/div/div/div[2]/div/ul/li/div/div[1]/ul[1]/li[2]/div/div[2]/text()').get()
    print(invoice)

    additional_information = selector.xpath('/html/body/div[2]/div[3]/div/div/div[4]/div/div/div[2]/div/ul/li/div/div[2]/ul/li[5]/div/div[2]/text()').get()
    print(additional_information)

    engine_capacity = selector.xpath('/html/body/div[2]/div[3]/div/div/div[4]/div/div/div[2]/div/ul/li/div/div[1]/ul[1]/li[5]/div/div[2]/text()').get()
    print(engine_capacity)

    power = selector.xpath('/html/body/div[2]/div[3]/div/div/div[4]/div/div/div[2]/div/ul/li/div/div[1]/ul[1]/li[6]/div/div[2]/text()').get()
    print(power)

    colour = selector.xpath('/html/body/div[2]/div[3]/div/div/div[4]/div/div/div[2]/div/ul/li/div/div[1]/ul[2]/li[2]/div/div[2]/text()').get()
    print(colour)

    course = selector.xpath('/html/body/div[2]/div[3]/div/div/div[4]/div/div/div[2]/div/ul/li/div/div[1]/ul[1]/li[4]/div/div[2]/text()').get()
    print(course)

    fuel_type = selector.xpath('/html/body/div[2]/div[3]/div/div/div[4]/div/div/div[2]/div/ul/li/div/div[1]/ul[1]/li[7]/div/div[2]/text()').get()
    print(fuel_type)

    yearbook = selector.xpath('/html/body/div[2]/div[3]/div/div/div[4]/div/div/div[2]/div/ul/li/div/div[1]/ul[1]/li[3]/div/div[2]/text()').get()
    print(yearbook)
