# 3rd party imports
from parsel import Selector

# project imports
from beautiful_soup_example import get_page

if __name__ =='__main__':
    url = 'https://www.otomoto.pl/oferta/porsche-911-turbo-s-burmester-acc-ceramika-faktura-vat-23-ID6ygzZw.html#aa8601bb82'
    filename = 'otomoto_css.html'
    html_content = get_page(url, filename)

    selector = Selector(text=html_content)

    title = selector.css('#siteWrap > main > section > div.offer-header__row > h1::text').getall()
    yearbook = selector.css('#siteWrap > main > section > div.offer-header__row > span > span:nth-child(1)::text').getall()
    course = selector.css('#siteWrap > main > section > div.offer-header__row > span > span:nth-child(2)::text').getall()
    engine_type = selector.css('#siteWrap > main > section > div.offer-header__row > span > span:nth-child(3)::text').getall()
    car_class = selector.css('#siteWrap > main > section > div.offer-header__row > span > span:nth-child(4)::text').getall()
    price = selector.css('#siteWrap > main > section > div.offer-header__row > div.offer-price > span.offer-price__number::text').getall()

    print(title)
    print(yearbook)
    print(course)
    print(engine_type)
    print(car_class)
    print(price)
