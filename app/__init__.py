"""
 Created by yan on 2018/9/26 16:18
"""
from flask import Flask

from app.models import db

__author__ = 'yan'

def register_web_blueprint(app):
    """
    注册蓝图
    :param app:
    :return:
    """
    from app.web import web
    app.register_blueprint(web)


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')  # 读取配置文件
    db.init_app(app)
    db.create_all(app=app)
    register_web_blueprint(app)

    return app