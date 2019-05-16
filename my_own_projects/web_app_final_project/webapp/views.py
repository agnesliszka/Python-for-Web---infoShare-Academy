from flask import render_template, redirect, request
from .forms import OfferForm
from .models import Offer
from . import app


@app.route('/')
def home():
    # Show home page
    html = render_template("home.html")
    return html

@app.route('/offers')
def get_offers():
    # Get data from offers table
    offers = Offer.query.all()
    # Create data provided to the template
    data = {'offers': offers}
    # Fulfill the template with the data and send it to the internet browser
    return render_template('show_offers.html', **data)

@app.route('/brand_search', methods=['GET'])
def brand_search():
    # Create a website to search for the specific brand of the car
    form = OfferForm()
    return render_template("brand_search.html", form = form)

@app.route('/show_searched_brand', methods=['GET', 'POST'])
def show_searched_brand():
    # Get selected brand of the car
    searched_brand = request.args.get('brand')
    # Filter offers of selected brand of the car
    offers_of_selected_brands = Offer.query.filter(Offer.brand == searched_brand).all()
    # Count number of rows in the table
    number_of_rows = Offer.query.filter_by(brand=searched_brand).count()
    # Create data provided to the template
    selected_offers_data = {'offers': offers_of_selected_brands, 'number_of_rows': number_of_rows}
    # Show offers of selected brand of the car on the website
    return render_template('show_searched_brand.html', **selected_offers_data)


