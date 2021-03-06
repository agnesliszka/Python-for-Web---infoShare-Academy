from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, StringField, PasswordField, SelectField
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
    login = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class GraphForm(FlaskForm):
    brand = SelectField('Brand')
    production_year_min = SelectField('Production year min')
    production_year_max = SelectField('Production year max')