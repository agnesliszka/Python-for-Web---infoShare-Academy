from flask import render_template, redirect, request
from flask.views import View

from .forms import OfferForm
from .models import Offer
from . import app


@app.route('/')
def home():
    # Show home page
    html = render_template("home.html")
    return html

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

# @app.route('/offers')
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

    def dispatch_request(self):
        return self.render_template(self.get_context())

class OfferListView(ListView):
    template_name = 'show_offers.html'

    def get_objects(self):
        return Offer.query.all()

app.add_url_rule('/show_offers', view_func=OfferListView.as_view('get_offers'))


