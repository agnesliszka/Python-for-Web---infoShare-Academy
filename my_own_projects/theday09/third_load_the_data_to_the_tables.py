
# Project imports
from first_database_schema_design import Session, Campaign, Portal, Offers

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