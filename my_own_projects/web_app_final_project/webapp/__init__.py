from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'afafafafafafdaasdfsdfsdf'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///offers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from . import models
db.create_all()

from . import views
from . import forms

admin = Admin(app, name="Offers search")
admin.add_view(ModelView(models.Offer, db.session))

login_manager = LoginManager(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(models.User).get(user_id)
