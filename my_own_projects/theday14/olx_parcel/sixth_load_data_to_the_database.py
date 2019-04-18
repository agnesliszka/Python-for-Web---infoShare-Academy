# Standard library imports
import json
import datetime

# Project imports
from second_db_engine import Session
from first_database_schema_design import Campaign, Portal, Offer


session = Session()

html = []

# Create first object representing portal 'olx' and input required data
olx = Portal(name = 'olx')
session.add(olx)
session.commit()

# Check database status
print(session.query(Portal).all())

# Create second object representing campaign and input required data
current_date = datetime.date.today()
olx_campaign = Campaign(portal_id = 2, date = current_date)
session.add(olx_campaign)
session.commit()

# Check database status
print(session.query(Campaign).all())

# Create first object representing portal 'otomoto' and input required data
otomoto = Portal(name='otomoto')
session.add(otomoto)
session.commit()

# Check database status
print(session.query(Portal).all())

# Create second object representing campaign and input required data
current_date = datetime.date.today()
otomoto_campaign = Campaign(portal_id=3, date=current_date)
session.add(otomoto_campaign)
session.commit()

# Check database status
print(session.query(Campaign).all())

# Create third object representing offers and input required data
with open('stored_offers_data.json', 'r', encoding="utf-8") as stored_offers_data:
    reader = json.load(stored_offers_data)

    # Get html path
    with open('stored_links.json', 'r') as stored_links:
        data = json.load(stored_links)
        for list_with_offers in data:
            for html in list_with_offers:
                idx = list_with_offers.index(html)
                portal = html[idx][12:15]
                if portal == "olx":
                    for single_offers_data in reader:
                        offer_data = Offer(**single_offers_data, campaign_id='2')
                        session.add(offer_data)
                        session.commit()
                elif portal == "oto":
                    for single_offers_data in reader:
                        offer_data = Offer(**single_offers_data, campaign_id='3')
                        session.add(offer_data)
                        session.commit()

# Check database status
print(session.query(Offer).all())