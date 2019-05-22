from flask_login import UserMixin

from . import db

class Portal(db.Model):

    __tablename__ = 'portals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    campaign = db.relationship('Campaign', back_populates='portal')

class Campaign(db.Model):

    __tablename__ = 'campaigns'

    id = db.Column(db.Integer, primary_key=True)

    portal_id = db.Column(db.Integer, db.ForeignKey('portals.id'), autoincrement='True')
    date = db.Column(db.Date)
    api_type = db.Column(db.String)

    portal = db.relationship('Portal', back_populates='campaign')
    offers = db.relationship('Offer', back_populates='campaign')

class Offer(db.Model):
    __tablename__ = 'offers'

    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'), autoincrement='True')
    offer_id = db.Column(db.String)
    seller_id = db.Column(db.String)
    location = db.Column(db.String)
    title = db.Column(db.String)
    price = db.Column(db.Float)
    brand = db.Column(db.String)
    model = db.Column(db.String)
    production_year = db.Column(db.String)
    course = db.Column(db.Float)
    capacity = db.Column(db.Float)
    power = db.Column(db.Float)
    fuel_type = db.Column(db.String)
    colour = db.Column(db.String)
    damaged = db.Column(db.String)
    country = db.Column(db.String)
    driving_gear = db.Column(db.String)
    number_of_seats = db.Column(db.Integer)
    abnormalities = db.Column(db.String)

    campaign = db.relationship('Campaign', back_populates='offers')

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100))
    password = db.Column(db.String(64))




