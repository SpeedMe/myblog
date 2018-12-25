# -*- coding: utf-8 -*-

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static', instance_relative_config=True)
app.config.from_pyfile('config.py')
app.config['JSON_AS_ASCII'] = False

db = SQLAlchemy()
db.init_app(app)

from app.views import blog, admin, error, weixin


