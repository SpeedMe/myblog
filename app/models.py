# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, Text, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Category(Base):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True)
    name = Column(String(11), nullable=False, server_default=text("''"))
    post_num = Column(Integer, nullable=False, server_default=text("'0'"))


class Post(Base):
    __tablename__ = 'post'

    post_id = Column(Integer, primary_key=True)
    category_id = Column(Integer, nullable=False, server_default=text("'0'"))
    title = Column(String(30), nullable=False, server_default=text("''"))
    path_name = Column(String(100), nullable=False, server_default=text("''"))
    page_view = Column(Integer, nullable=False, server_default=text("'0'"))
    comment_num = Column(Integer, nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime)
    content = Column(Text)
