# 3rd party imports
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Create 'campaign' database schema
class Campaign(Base):
    # Set a table name
    __tablename__ = 'campaigns'

    # Primary key
    id = Column(Integer, primary_key=True)

    # Foreign key
    portal_id = Column(Integer, ForeignKey('portals.id'))

    # Additional columns
    date = Column(String)
    api_type = Column(String)

    # Creating a relation between tables
    portal = relationship('Portal', back_populates='campaign')
    offers = relationship('Offer', back_populates='campaign')


# Create 'portal' database schema
class Portal(Base):
    # Set a table name
    __tablename__ = 'portals'

    # Primary key
    id = Column(Integer, primary_key=True)

    # Additional columns
    name = Column(String)

    # Creating a relation between tables
    campaign = relationship('Campaign', back_populates='portal')


# Create 'offers' database schema
class Offer(Base):
    # Set a table name
    __tablename__ = 'offers'
    'offers'
    # Primary key
    id = Column(Integer, primary_key=True)

    # Foreign key
    campaign_id = Column(Integer, ForeignKey('campaigns.id'))

    # Additional columns
    offer_id = Column(String)
    seller_id = Column(String)
    location = Column(String, nullable='True')
    title = Column(String, nullable='True')
    price = Column(String, nullable='True')
    brand = Column(String, nullable='True')
    model = Column(String, nullable='True')
    production_year = Column(String, nullable='True')
    course = Column(String, nullable='True')
    capacity = Column(String, nullable='True')
    power = Column(String, nullable='True')
    fuel_type = Column(String, nullable='True')
    colour = Column(String, nullable='True')
    damaged = Column(String, nullable='True')
    country = Column(String, nullable='True')
    driving_gear = Column(String, nullable='True')
    number_of_seats = Column(String, nullable='True')

    # Create a relation between tables
    campaign = relationship('Campaign', back_populates='offers')
