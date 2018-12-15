# -*- coding: utf-8 -*-from flask import url_for, render_templatefrom app import app, sessionfrom app.models import Post, Categoryfrom flask import Markupfrom sqlalchemy.orm import defer, load_onlyimport misaka as m# 博客首页@app.route('/', methods=['GET'])def hello_world():    posts = session.query(Post).order_by(Post.create_time.desc()) \        .options(load_only("path_name", "title", "create_time")).all()    session.commit()    return render_template('blog/index.html', posts=posts)# 博文页面@app.route('/<path>.html', methods=['GET'])def get_post(path):    post = session.query(Post).filter(Post.path_name == path).one()    pre_post = session.query(Post).filter(Post.create_time < post.create_time).order_by(        Post.create_time.desc()).options(load_only("path_name", "title")).first()    next_post = session.query(Post).filter(Post.create_time > post.create_time).order_by(        Post.create_time.asc()).options(load_only("path_name", "title")).first()    # 访问量加1    post.page_view += 1    session.commit()    # 如果存在此博客    if post:        post_html = m.html(post.content,                           extensions=m.EXT_NO_INTRA_EMPHASIS | m.EXT_FENCED_CODE | m.EXT_AUTOLINK)        return render_template('blog/post.html', post=post, pre_post=pre_post, next_post=next_post,                               content=Markup(post_html))    else:        return render_template('404.html')# 个人介绍@app.route('/about', methods=['GET'])def about():    return render_template('about.html')# 简历@app.route('/resume')def resume():    return render_template('resume/index.html')# google网站验证@app.route('/google17605fc6a4735d88.html', methods=['GET'])def google_site_manager():    return render_template('seo/google17605fc6a4735d88.html')# 百度网站验证@app.route('/baidu_verify_IQvNCxILKP.html', methods=['GET'])def baidu_site_manager():    return render_template('seo/baidu_verify_IQvNCxILKP.html')