from flask import render_template, redirect
from .forms import OfferForm, SearchForModelForm
from .models import Offer
from . import app
from. import db


@app.route('/')
def home():
    offers = Offer.query.all()
    print(offers)
    return render_template("home.html")

@app.route('/offers')
def get_offers():
    # Get data from offers table
    offers = Offer.query.all()
    print(offers)

    # Create data provided to the template
    data = {'offers': offers}

    # Fulfill the template with the data and send it to the internet browser
    return render_template('offers.html', **data)

@app.route('/brand_search', methods=['GET'])
def brand_search():
    form = OfferForm()
    return render_template("brand_search.html", form = form)

    # redirect?

# @app.route('/show_searched_brand', methods=['GET', 'POST'])
# def show_searched_brand(form)
#     searched_offer_model = Offer.query.filter(brand=form.data['brand'])
#     /results?show_searched_brand=Audi

#       if form.validate_on_submit():
#         validated_data = form.data.copy()
#         validated_data.pop('csrf_token')
#         return redirect('/offers')
#
#         searched_offer_model = Offer.query.filter(brand=form.data['brand'])
#         return render_template('offers.html', form=searched_offer_model)
#
# # Fulfill the template with the data and send it to the internet browser
#     return render_template('search_for_brand.html', search_for_brand)



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


#

