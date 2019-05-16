from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, StringField, PasswordField
from wtforms.validators import DataRequired


# Create offers form
class OfferForm(FlaskForm):
    id = IntegerField('id', validators=[DataRequired()])
    campaign_id = IntegerField('Campaign id')
    offer_id = StringField('Offer id')
    seller_id = StringField('Seller id')
    location = StringField('Location')
    title = StringField('Title')
    price = FloatField('Price')
    brand = StringField('Brand')
    model = StringField('Model')
    production_year = StringField('Production year')
    course = FloatField('Course')
    capacity = FloatField('Capacity')
    power = FloatField('Power')
    fuel_type = StringField('Fuel type')
    colour = StringField('Colour')
    damaged = StringField('Damaged')
    country = StringField('Country')
    driving_gear = StringField('Driving gear')
    number_of_seats = IntegerField('Number of seats')
    abnormalities = StringField('Abnormalities')

class LoginForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

