# -*- coding: utf-8 -*-

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__, static_folder='static', instance_relative_config=True)
app.config.from_pyfile('config.py')
app.config['JSON_AS_ASCII'] = False

db = SQLAlchemy()
db.init_app(app)
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
session._model_changes = {}

from app.views import blog, admin, error, weixin


