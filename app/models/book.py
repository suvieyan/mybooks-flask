"""
 Created by yan on 2018/9/26 16:28
"""
__author__ = 'yan'

from sqlalchemy import Column, Integer, String, Float

from app.models import db

class Book(db.Model):
    """
       一些属性定义重复性比较大，元类可以解决这个问题
    """
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    isbn = Column(String(50), nullable=False,unique=True)  # isbn
    title = Column(String(50), nullable=False)  # nullable 不允许为空
    image = Column(String(100), nullable=False)  # nullable 不允许为空
    alt = Column(String(100), nullable=False)  # nullable 不允许为空
    publisher = Column(String(100), nullable=False)  # nullable 不允许为空
    summary = Column(String(1024), nullable=False)  # nullable 不允许为空
    price = Column(String(100), nullable=False)  # nullable 不允许为空
    rate = Column(Float(), default=None)  # 评分
    tags = Column(String(100), default=None)  # 评分
    author = Column(String(100), default=None)  # 评分
    count = Column(Integer,default=0)
    openid = Column(String(50), nullable=False)  # nullable 不允许为空
