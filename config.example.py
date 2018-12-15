# -*- coding: utf-8 -*-

import os
basedir=os.path.abspath(os.path.dirname(__file__))#get basedir of the project

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-guess'

#for database
# SQLALCHEMY_DATABASE_URI = 'mysql:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = "mysql://username:password@server_ip:port/database_name"

WTF_CSRF_ENABLED = True
SQLALCHEMY_TRACK_MODIFICATIONS = True


LEIHUNAG_ADMIN_KEY = ''