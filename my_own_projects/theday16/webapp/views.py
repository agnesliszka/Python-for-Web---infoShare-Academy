from flask import render_template, redirect
from .forms import OfferForm
from .models import Offer
from . import app
from. import db


@app.route('/offers')
def get_offers():
    # Get data from offers table
    offers = Offer.query.all()
    print(offers)

    # Create data provided to the template
    data = {'offers': offers}

    # Fulfill the template with the data and send it to the internet browser
    return render_template('offers.html', **data)

@app.route('/')
def home():
    offers = Offer.query.all()
    print(offers)
    return 'hello'

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


# # @app.route('/offers_search')
# # def home():
# #     clients = Offer.query.all()
# #     print(clients)
# #     return 'hello'
#
#         # db.session.add(offer)
#         # db.session.commit()