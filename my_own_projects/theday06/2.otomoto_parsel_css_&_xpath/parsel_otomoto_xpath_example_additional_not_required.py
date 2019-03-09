# 3rd party imports
from parsel import Selector

# project imports
from beautiful_soup_example import get_page

if __name__ =='__main__':
    url = 'https://www.otomoto.pl/oferta/porsche-911-turbo-s-burmester-acc-ceramika-faktura-vat-23-ID6ygzZw.html#aa8601bb82'
    filename = 'otomoto_xpath.html'
    html_content = get_page(url, filename)

    selector = Selector(text=html_content)

    title = selector.xpath('//*[@id="siteWrap"]/main/section/div[3]/h1/text()').getall()
    yearbook = selector.xpath('//*[@id="siteWrap"]/main/section/div[3]/span/span[1]/text()').getall()
    course = selector.xpath('//*[@id="siteWrap"]/main/section/div[3]/span/span[2]/text()').getall()
    engine_type = selector.xpath('//*[@id="siteWrap"]/main/section/div[3]/span/span[3]/text()').getall()
    car_class = selector.xpath('//*[@id="siteWrap"]/main/section/div[3]/span/span[4]/text()').getall()
    price = selector.xpath('//*[@id="siteWrap"]/main/section/div[3]/div[1]/span[1]/text()').getall()

    print(title)
    print(yearbook)
    print(course)
    print(engine_type)
    print(car_class)
    print(price)

