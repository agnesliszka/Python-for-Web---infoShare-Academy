# 3rd party imports
from parsel import Selector

# project imports
from beautiful_soup_example import get_page

if __name__ =='__main__':
    url = 'https://allegro.pl/ogloszenie/porsche-911-turbo-s-techart-680km-salonpl-fv23-7867148731'
    filename = 'allegro_mozilla_css.html'
    html_content = get_page(url, filename)

    selector = Selector(text=html_content)

    invoice = selector.css('div.e6337613:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > div:nth-child(1) > div:nth-child(2)::text').get()
    print(invoice)

    additional_information = selector.css('._6a5fe2e9 > li:nth-child(5) > div:nth-child(1) > div:nth-child(2)::text').get()
    print(additional_information)

    engine_capacity = selector.css('div.e6337613:nth-child(1) > ul:nth-child(1) > li:nth-child(5) > div:nth-child(1) > div:nth-child(2)::text').get()
    print(engine_capacity)

    power = selector.css('div.e6337613:nth-child(1) > ul:nth-child(1) > li:nth-child(6) > div:nth-child(1) > div:nth-child(2)::text').get()
    print(power)

    colour = selector.css('ul._25470ea2:nth-child(2) > li:nth-child(2) > div:nth-child(1) > div:nth-child(2)::text').get()
    print(colour)

    course = selector.css('div.e6337613:nth-child(1) > ul:nth-child(1) > li:nth-child(4) > div:nth-child(1) > div:nth-child(2)::text').get()
    print(course)

    fuel_type = selector.css('div.e6337613:nth-child(1) > ul:nth-child(1) > li:nth-child(7) > div:nth-child(1) > div:nth-child(2)::text').get()
    print(fuel_type)

    yearbook = selector.css('div.e6337613:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > div:nth-child(1) > div:nth-child(2)::text').get()
    print(yearbook)