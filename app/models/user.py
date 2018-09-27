"""
 Created by yan on 2018/9/26 16:22
"""
import datetime

from sqlalchemy import Column, Integer, DateTime, String

from app.models import db

__author__ = 'yan'

class User(db.Model):
    """
       一些属性定义重复性比较大，元类可以解决这个问题
    """

    id = Column(Integer, primary_key=True, autoincrement=True)
    openid = Column(String(50), nullable=False,unique=True)  # nullable 不允许为空
    session_key = Column(String(50), nullable=False)  # nullable 不允许为空
    created_date = Column(DateTime, default=datetime.datetime.now())  # 固定的时间
    last_visit_time = Column(DateTime, default=datetime.datetime.now,onupdate=datetime.datetime.now)  # 自动根据当前时间生成时间
    user_info = Column(String(2048),nullable=False)
