"""
 Created by yan on 2018/9/26 16:29
"""
__author__ = 'yan'

from sqlalchemy import Column, Integer, String

from app.models import db

class Comments(db.Model):
    """
       一些属性定义重复性比较大，元类可以解决这个问题
    """
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    openid = Column(String(50), nullable=False)  # nullable 不允许为空
    bookid = Column(String(50), nullable=False)  # isbn
    comment = Column(String(200), nullable=False)  # nullable 不允许为空
    phone = Column(String(20), default=None)  # nullable 不允许为空
    location = Column(String(20), default=None)  # nullable 不允许为空
