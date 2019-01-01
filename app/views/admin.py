# -*- coding: utf-8 -*-

"""
description: 管理员路由页面
author: HuangLei
date: 2016-03-04 11:48 AM
"""

from flask import render_template, request
from app import db, app
from app.models import Category, Post
from datetime import *


@app.route('/admin', methods=['GET', 'POST'])
def admin_index():
    if request.method == 'GET':
        user = request.args.get('user')

        if user == app.config['LEIHUNAG_ADMIN_KEY']:
            categories = Category.query.all()
            return render_template('admin/index.html', categories=categories)
        else:
            return render_template('404.html')
    else:
        post = Post()
        post.title = request.values.get("title")
        post.path_name = request.values.get("path")

        post.category_id = request.values.get("category")
        post.author = request.values.get("author")
        category = Category.query.filter_by(category_id=post.category_id).first()
        category.post_num += 1
        post.content = request.values.get("content")

        post.create_time = datetime.now()
        if exist_post(post.title):
            return '已经存在此博客'
        if exist_path_name(post.path_name):
            return '已经存在此路径的博客'

        db.session.add(post)
        db.session.flush()
        db.session.commit()
        return 'ok'


# 判断是否已经存在此博文
def exist_post(title):
    post = Post.query.filter(Post.title == title).first()
    if post:
        return True
    else:
        return False


# 是否已经存在此路径
def exist_path_name(path_name):
    post = Post.query.filter(Post.path_name == path_name).first()
    if post:
        return True
    else:
        return False


# 保存类目
def save_category(category_name):
    category = Category()
    category_old = get_categories_by_name(category_name)
    if category_old:
        category = category_old
        category.post_num += 1
        Category.query.filter(Category.category_id == category.category_id).update(
            {Category.post_num: category.post_num})
        db.session.flush()
        return category.category_id
    else:
        category.name = category_name
        category.post_num = 1
        db.session.add(category)
        db.session.flush()
        return category.category_id


# 根据category_name查找categories
def get_categories_by_name(category_name):
    categories = Category.query.filter(Category.name == category_name).all()
    if len(categories) > 0:
        return categories[0]
    else:
        return None