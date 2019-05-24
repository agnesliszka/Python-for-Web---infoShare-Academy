import os
import time
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from flask import render_template, redirect, request, url_for, flash
from flask.views import View
from flask_login import current_user, login_user, logout_user, login_required

from .forms import OfferForm, LoginForm, GraphForm
from .models import Offer, Campaign, Portal, User
from . import app, db
from . import size

@app.route('/')
def home():
    # Show home page
    html = render_template("home.html")
    return html

@app.route('/brand_search', methods=['GET'])
@login_required
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

# @app.route('/offers')
# @login_required
# @login_required
# def get_offers():
#     # Get data from offers table
#     offers = Offer.query.all()
#     # Create data provided to the template
#     data = {'offers': offers}
#     # Fulfill the template with the data and send it to the internet browser
#     return render_template('show_offers.html', **data)

class ListView(View):
    template_name = 'objects_list.html'

    def get_objects(self):
        raise NotImplementedError()

    def get_context(self):
        return {'objects': self.get_objects()}

    def render_template(self, context):
        return render_template(self.__class__.template_name, **context)

    @login_required
    def dispatch_request(self):
        return self.render_template(self.get_context())

class OfferListView(ListView):
    template_name = 'show_offers.html'

    def get_objects(self):
        return Offer.query.all()

    def get_context(self):
        return {'offers': self.get_objects()}

app.add_url_rule('/show_offers', view_func=OfferListView.as_view('get_offers'))

class Statistics(ListView):
    decorators = [login_required]

    template_name = 'statistics.html'

    def get_objects(self):
        number_of_campaigns = Campaign.query.count()
        number_of_offers = Offer.query.count()
        number_of_portals = Portal.query.count()

        the_oldest_car = db.session.query(db.func.min(Offer.production_year)).one()[0]
        the_youngest_car = db.session.query(db.func.max(Offer.production_year)).one()[0]
        the_cheapest_car = db.session.query(db.func.min(Offer.price)).one()[0]
        the_most_expensive_car = db.session.query(db.func.max(Offer.price)).one()[0]
        the_lowest_course = db.session.query(db.func.min(Offer.course)).one()[0]
        the_highest_course = db.session.query(db.func.max(Offer.course)).one()[0]


        context = {'Number of campaigns': number_of_campaigns, 'Number of offers': number_of_offers, 'Number of portals': number_of_portals}
        context.update({'The oldest car': the_oldest_car})
        context.update({'The youngest car': the_youngest_car})
        context.update({'The cheapest car': the_cheapest_car})
        context.update({'The most expensive car': the_most_expensive_car})
        context.update({'The lowest course': the_lowest_course})
        context.update({'The highest course': the_highest_course})
        return context

app.add_url_rule('/statistics', view_func=Statistics.as_view('statistics'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in')
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data,
                                    password=form.password.data).first()

        if user is None:
            flash('Incorrect login/password')
            return redirect(url_for('home'))

        login_user(user)
        flash('You have successfully logged in')
        return redirect(url_for('home'))

    return render_template('login_form.html', form=form)

@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('You have successfully logged out')

    return redirect(url_for('home'))

@app.route('/graph', methods=['GET', 'POST'])
@login_required
def graph():

    offers_df = pd.read_sql_table('offers', str(app.config['PANDAS_DATABASE_URI']), index_col='id')
    brand_list = list(set(offers_df.brand))
    production_year_list = list(sorted(set(offers_df.production_year)))

    form = GraphForm()
    choices = list()
    choices.append(['All', 'All'])
    choices.extend([(brand, brand) for brand in brand_list])
    form.brand.choices = choices
    form.brand.default = choices[0][0]
    form.production_year_min.choices = [(production_year, production_year) for production_year in production_year_list]
    form.production_year_max.choices = [(production_year, production_year) for production_year in production_year_list]
    form.production_year_min.default = "2000"
    form.production_year_max.default = "2019"

    if form.is_submitted():
        if form.data['brand'] == 'All':
            brands = brand_list
        else:
            brands = [form.data['brand'], ]

        production_year_start = int(form.data['production_year_min'])
        production_year_stop = int(form.data['production_year_max'])

        fig, ax = plt.subplots(figsize=size)
        fig.suptitle('Brand - course')

        ax.set_ylabel('Course in km')
        ax.set_xlabel('Production year')

        for brand in brands:
            ofx = offers_df[
                (offers_df.brand == brand) &
                (offers_df.course > 10000)
                ].groupby('production_year')

            ax.plot(ofx.course.mean(), label=brand)

        ax.legend(loc=2)

        folder_name = os.path.join(app.root_path, 'static', 'img')
        file_name = '%s.png' % time.time()
        fig.savefig(os.path.join(folder_name, file_name))

        return render_template('graph.html', filename='img/%s' % file_name,
                               form=form, brand=brand, year_range=(production_year_start, production_year_stop))
    else:
        form.process()
        return render_template('graph_form.html', form=form)


