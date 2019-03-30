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
    pprint(reader)

    # for element in reader:
    #     # i = reader.index(element) + 1
    #     for key, value in element.items():
    #         print(key, value)

        # To be thought over:
        # offer = Offer(offer_id = , seller_id = , location = , title = , price = , brand = , model = ,
        # production_year = , course = , capacity = , power = , fuel_type = , colour = , damaged = ,
        # country = , driving_gear = , number_of_seats = )
        # session.add(offer)
        # session.commit()


# Check database status
print(session.query(Offer).all())