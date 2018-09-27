"""
 Created by yan on 2018/9/26 16:31
"""
import datetime
import json

from flask import request, jsonify

from app import secure
from app.libs.helper import get_openid
from app.models.user import User
from . import web
from app.models import db
__author__ = 'yan'


@web.route('/login',methods = ["POST"])
def login():
    """
    login的请求的数据
    :return:
    """
    resp = {'code': 200, 'msg': '', 'data': {}}
    # 如果是json数据，用request.data进行获取，注意获取到的是bytes
    userinfo = str(request.data,encoding='utf-8')
    user = json.loads(userinfo)
    # 根据用户的code 获取用户的openID和session_key
    result = get_openid(secure.APPID,secure.AppSecret,user.get('code'))
    openid = result.get('openid')
    # 查看数据库是否存在该openID
    current_user = User.query.filter_by(openid = openid).first()
    if not current_user:
        session_key = result.get('session_key')
        user['openid'] = openid
        # 不存在，添加到数据库
        now = datetime.datetime.now()
        user_obj = User(openid=openid,session_key=session_key,user_info=json.dumps(user),created_date=now)
        db.session.add(user_obj)
        db.session.commit()
    else:
        # 存在，更新用户的最后一次登录时间
        now = datetime.datetime.now()
        # update方法是一个谬论，不存在
        # ret = User.query.filter_by(openid=openid).first().update({'last_visit_time':now})  # 更新成功返回1，失败返回0
        current_user = User.query.filter_by(openid=openid).first()
        current_user.last_visit_time = now
        db.session.commit()

    resp['data'] = user
    resp['msg'] = '登录成功'
    return jsonify(resp)
