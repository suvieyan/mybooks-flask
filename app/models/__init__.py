"""
 Created by yan on 2018/9/26 16:24
"""
from flask_sqlalchemy import SQLAlchemy

__author__ = 'yan'


db = SQLAlchemy()

from app.models import user
from app.models import book
from app.models import comments