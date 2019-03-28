from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///clients_orm.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Create 'campaign' database schema
class Campaign(Base):
    # Set a table name
    __tablename__ = 'campaign'

    # Primary key
    id = Column(Integer, primary_key=True)

    # Foreign key
    portal_id = Column(Integer, ForeignKey('portal.id'))

    # Additional columns
    date = Column(String)
    api_type = Column(String)

    # Creating a relation between tables
    portal = relationship('portal', back_populates='campaign')
    offers = relationship('offers', back_populates='campaign')

# Create 'portal' database schema
class Portal(Base):
    # Set a table name
    __tablename__ = 'portal'

    # Primary key
    id = Column(Integer, primary_key=True)

    # Additional columns
    name = Column(String)

    # Creating a relation between tables
    campaign = relationship('campaign', back_populates='portal')

# Create 'offers' database schema
class Offers(Base):
    # Set a table name
    __tablename__ = 'offers'

    # Primary key
    id = Column(Integer, primary_key=True)

    # Foreign key
    campaign_id = Column(Integer, ForeignKey('campaign.id'))

    # Additional columns
    offer_id = Column(String)
    seller_id = Column(String)
    location = Column(String)
    title = Column(String)
    price = Column(String)
    brand = Column(String)
    design = Column(String)
    title = Column(String)
    production_year = Column(String)
    course = Column(String)
    production_year = Column(String)
    capacity = Column(String)
    power = Column(String)
    fuel_type = Column(String)
    colour = Column(String)
    damaged = Column(String)
    country = Column(String)
    driving_gear = Column(String)
    number_of_seats = Column(String)

    # Create a relation between tables
    campaign = relationship('campaign', back_populates='offers')
