from flask import render_template, redirect
from .forms import OfferForm
from .models import Offer
from . import app
from. import db


@app.route('/oferty', methods=['GET', 'POST'])
def add_client():
    form = OfferForm()

    if form.validate_on_submit():
        validated_data = form.data.copy()
        validated_data.pop('csrf_token')

        offer = Offer(**validated_data)


        return redirect('/')
    else:
        print(form.errors.items())

    return render_template('client_form.html', form=form)

# @app.route('wyszukaj_oferty/')
# def home():
#     clients = Offer.query.all()
#     print(clients)
#     return 'hello'

        # db.session.add(offer)
        # db.session.commit()