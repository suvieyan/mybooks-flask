"""
 Created by yan on 2018/9/26 16:39
"""
from flask import Blueprint

__author__ = 'yan'

web = Blueprint('web', __name__)


from app.web import user
from app.web import book
from app.web import comments
from app.web import files
