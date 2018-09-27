"""
 Created by yan on 2018/9/26 16:31
"""
import json

from flask import request, jsonify

from app.models import db
from app.models.comments import Comments
from app.models.user import User
from app.web import web

__author__ = 'yan'


@web.route('/commentlist',methods = [ "GET","POST" ])
def comment_list():
    resp = {'code': 200, 'msg': '', 'data': {}}
    book_id = request.values.get('bookid')
    comments = Comments.query.filter_by(bookid=book_id).all()
    comments_list = []
    for item in comments:
        item_dict = item.__dict__
        item_dict.pop('_sa_instance_state')
        openid = item_dict['openid']
        user_info = User.query.filter_by(openid=openid).first().user_info
        user = json.loads(user_info)
        item_dict['title'] = user['nickName']
        item_dict['image'] = user['avatarUrl']
        comments_list.append(item_dict)
    resp['data'] = comments_list
    return jsonify(resp)


@web.route('/addcomment',methods = [ "GET","POST" ])
def add_comment():
    resp = {'code': 200, 'msg': '', 'data': {}}
    book_id = request.values.get('bookid')
    openid = request.values.get('openid')
    comment = request.values.get('comment')
    phone = request.values.get('phone')
    location = request.values.get('location')
    comment = Comments(bookid=book_id,openid=openid,comment=comment,phone=phone,location=location)
    db.session.add(comment)
    db.session.commit()
    resp['msg'] = '添加评论成功'

    return jsonify(resp)


@web.route('/mycomments',methods = [ "GET"])
def my_comments():
    resp = {'code': 200, 'msg': '', 'data': {}}
    openid = request.values.get('openid')
    comments = Comments.query.filter_by(openid=openid).all()
    comments_list = []
    for item in comments:
        item_dict = item.__dict__
        item_dict.pop('_sa_instance_state')
        openid = item_dict['openid']
        user_info = User.query.filter_by(openid=openid).first().user_info
        user = json.loads(user_info)
        item_dict['title'] = user['nickName']
        item_dict['image'] = user['avatarUrl']
        comments_list.append(item_dict)
    resp['data'] = comments_list
    return jsonify(resp)
