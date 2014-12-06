import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api, Resource

#ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
#print os.path.dirname(os.path.abspath(__file__))
#print ASSETS_DIR

#app = Flask(__name__,template_folder=ASSETS_DIR,static_url_path= ASSETS_DIR)
app = Flask(__name__)
app.config.from_object('config')
api = Api(app)

db = SQLAlchemy(app)
#api_manager = APIManager(app,flask_sqlalchemy_db = db)

from app import PL_view,DL_models,PL_fields,SL_models

# To create and delete all the tables
#db.drop_all()
#db.create_all()