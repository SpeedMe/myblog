# -*- coding: utf-8 -*-

"""
description: 错误页面
author: HuangLei
date: 2016-03-07 8:55 PM
"""

from app import app
from flask import render_template


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
