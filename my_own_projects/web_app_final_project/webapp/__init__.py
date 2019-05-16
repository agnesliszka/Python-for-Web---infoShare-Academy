from flask import Flask
from flask_sqlalchemy import SQLAlchemy


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



