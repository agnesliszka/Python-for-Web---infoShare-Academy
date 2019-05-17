# 3rd party imports
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

# Create 'portal' database schema
class Portal(Base):
    # Set a table name
    __tablename__ = 'portals'

    # Primary key
    id = Column(Integer, primary_key=True)

    # Additional columns
    name = Column(String)

    # Create a relation between tables
    campaign = relationship('Campaign', back_populates='portal')

    def __repr__(self):
        return f'<Portal(name={self.name})>'

# Create 'campaign' database schema
class Campaign(Base):
    # Set a table name
    __tablename__ = 'campaigns'

    # Primary key
    id = Column(Integer, primary_key=True)

    # Foreign key
    portal_id = Column(Integer, ForeignKey('portals.id'), autoincrement='True')

    # Additional columns
    date = Column(Date)
    api_type = Column(String)

    # Create a relation between tables
    portal = relationship('Portal', back_populates='campaign')
    offers = relationship('Offer', back_populates='campaign')

# Create 'offers' database schema
class Offer(Base):
    # Set a table name
    __tablename__ = 'offers'
    
    # Primary key
    id = Column(Integer, primary_key=True)

    # Foreign key
    campaign_id = Column(Integer, ForeignKey('campaigns.id'), autoincrement='True')

    # Additional columns
    offer_id = Column(String)
    seller_id = Column(String)
    location = Column(String, nullable='True')
    title = Column(String, nullable='True')
    price = Column(Float, nullable='True')
    brand = Column(String, nullable='True')
    model = Column(String, nullable='True')
    production_year = Column(String, nullable='True')
    course = Column(Float, nullable='True')
    capacity = Column(Float, nullable='True')
    power = Column(Float, nullable='True')
    fuel_type = Column(String, nullable='True')
    colour = Column(String, nullable='True')
    damaged = Column(String, nullable='True')
    country = Column(String, nullable='True')
    driving_gear = Column(String, nullable='True')
    number_of_seats = Column(Integer, nullable='True')

    # Create a relation between tables
    campaign = relationship('Campaign', back_populates='offers')
