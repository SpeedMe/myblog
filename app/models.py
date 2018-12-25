# coding: utf-8
from . import db


class Category(db.Model):
    __tablename__ = 'category'

    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(11), nullable=False, server_default='')
    post_num = db.Column(db.Integer, nullable=False, server_default='0')


class Post(db.Model):
    __tablename__ = 'post'

    post_id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, nullable=False, server_default='0')
    title = db.Column(db.String(30), nullable=False, server_default='')
    path_name = db.Column(db.String(100), nullable=False, server_default='')
    page_view = db.Column(db.Integer, nullable=False, server_default='0')
    comment_num = db.Column(db.Integer, nullable=False, server_default='0')
    create_time = db.Column(db.DateTime)
    content = db.Column(db.Text)
