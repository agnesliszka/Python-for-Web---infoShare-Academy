# 3rd party imports
from parsel import Selector

# project imports
from beautiful_soup_example import get_page

if __name__ =='__main__':
    url = 'https://allegro.pl/ogloszenie/porsche-911-turbo-s-techart-680km-salonpl-fv23-7867148731'
    filename = 'allegro_css.html'
    html_content = get_page(url, filename)

    selector = Selector(text=html_content)

    invoice = selector.css('body > div.main-wrapper > div:nth-child(3) > div > div > div:nth-child(4) > div > div > div:nth-child(2) > div > ul > li > div > div.e6337613._925400d5 > ul:nth-child(1) > li:nth-child(2) > div > div._2036b558::text').get()
    print(invoice)

    additional_information = selector.css('body > div.main-wrapper > div:nth-child(3) > div > div > div:nth-child(4) > div > div > div:nth-child(2) > div > ul > li > div > div:nth-child(2) > ul > li:nth-child(5) > div > div._2036b558::text').get()
    print(additional_information)

    engine_capacity = selector.css('body > div.main-wrapper > div:nth-child(3) > div > div > div:nth-child(4) > div > div > div:nth-child(2) > div > ul > li > div > div.e6337613._925400d5 > ul:nth-child(1) > li:nth-child(5) > div > div._2036b558::text').get()
    print(engine_capacity)

    power = selector.css('body > div.main-wrapper > div:nth-child(3) > div > div > div:nth-child(4) > div > div > div:nth-child(2) > div > ul > li > div > div.e6337613._925400d5 > ul:nth-child(1) > li:nth-child(6) > div > div._2036b558::text').get()
    print(power)

    colour = selector.css('body > div.main-wrapper > div:nth-child(3) > div > div > div:nth-child(4) > div > div > div:nth-child(2) > div > ul > li > div > div.e6337613._925400d5 > ul:nth-child(2) > li:nth-child(2) > div > div._2036b558::text').get()
    print(colour)

    course = selector.css('body > div.main-wrapper > div:nth-child(3) > div > div > div:nth-child(4) > div > div > div:nth-child(2) > div > ul > li > div > div.e6337613._925400d5 > ul:nth-child(1) > li:nth-child(4) > div > div._2036b558::text').get()
    print(course)

    fuel_type = selector.css('body > div.main-wrapper > div:nth-child(3) > div > div > div:nth-child(4) > div > div > div:nth-child(2) > div > ul > li > div > div.e6337613._925400d5 > ul:nth-child(1) > li:nth-child(7) > div > div._2036b558::text').get()
    print(fuel_type)

    yearbook = selector.css('body > div.main-wrapper > div:nth-child(3) > div > div > div:nth-child(4) > div > div > div:nth-child(2) > div > ul > li > div > div.e6337613._925400d5 > ul:nth-child(1) > li:nth-child(3) > div > div._2036b558::text').get()
    print(yearbook)

