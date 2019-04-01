# Standard library imports
import json

# 3rd party imports
from pprint import pprint

# Project imports
from second_db_engine import Session
from first_database_schema_design import Campaign, Portal, Offer


session = Session()

# Create first object representing portal 'allegro'
allegro = Portal(name = 'allegro')
session.add(allegro)
session.commit()
# Check database status
print(session.query(Portal).all())

# Create second object representing campaign '2018.11.31'
allegro_campaign = Campaign(portal_id = 1, date = '2018.11.31')
session.add(allegro_campaign)
session.commit()
# Check database status
print(session.query(Campaign).all())

# Create third object representing offers
with open('stored_offers_data.json', 'r', encoding="utf-8") as data_file:
    reader = json.load(data_file)

    for offers_data in reader:
        # i = reader.index(element) + 1
        # for key, value in element.items():
        #     print(key, value)

        print(offers_data)

        # jak to zrobic, zeby jak nie ma elementu to, zeby go nie wrzucal?
        offer = Offer(offer_id = offers_data['ID oferty'] , seller_id = offers_data['ID sprzedajacego'], location = offers_data['Lokalizacja'], title = offers_data['Tytul'], price = offers_data['Cena'], brand = offers_data['Marka'], model = offers_data['Model'],
        production_year = offers_data['Rok produkcji'], course = offers_data['Przebieg'], capacity = offers_data['Pojemność silnika'], power = offers_data['Moc'], fuel_type = offers_data['Rodzaj paliwa'], colour = offers_data['Kolor'], damaged = offers_data['Uszkodzony'],
        country = offers_data['Kraj pochodzenia'], driving_gear = offers_data['Napęd'], number_of_seats = offers_data['Liczba miejsc'])
        session.add(offer)
        session.commit()


# Check database status
print(session.query(Offer).all())