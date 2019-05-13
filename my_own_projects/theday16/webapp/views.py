from flask import render_template, redirect, request
from .forms import OfferForm
from .models import Offer
from . import app
from. import db


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
    return render_template('offers.html', **data)

@app.route('/brand_search', methods=['GET'])
def brand_search():
    # Create a website to search for the specific brand of the car
    form = OfferForm()
    return render_template("brand_search.html", form = form)

@app.route('/show_searched_brand', methods=['GET', 'POST'])
def show_searched_brand():
    # Get selected brand of the car
    brand = request.args.get('brand')
    # Filter offers of selected brand of the car
    offers_of_selected_brands = Offer.query.filter(Offer.brand == brand)
    print(offers_of_selected_brands)
    # Create data provided to the template
    selected_offers_data = {'offers': offers_of_selected_brands}
    # Show offers of selected brand of the car on the website
    return render_template('show_searched_brand.html', **selected_offers_data)

    # return render_template('show_searched_brand.html', form=searched_offer_model)

# Count number of rows in the table
# number_of_rows = offers.query.filter_by(brand=brand).count()
# return render_template('show_searched_brand.html', form=number_of_rows)

# form = OfferForm()
# searched_offer_model = Offer.query.filter(brand=form.data[brand])



# @app.route('/add', methods=['GET', 'POST'])
# def add_offer():
#     form = OfferForm()
#
#     if form.validate_on_submit():
#         validated_data = form.data.copy()
#         validated_data.pop('csrf_token')
#
#         new_offer = Offer(**validated_data)
#
#         # add new offer to the database
#         db.session.add(new_offer)
#         db.session.commit()
#
#         return redirect('/')
#
#     return render_template('offer_form.html', form=form)



