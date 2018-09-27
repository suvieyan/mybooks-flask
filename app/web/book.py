"""
 Created by yan on 2018/9/26 16:31
"""
import json

from flask import request, jsonify, flash

from app.models import db
from app.libs.helper import get_book_info
from app.models.book import Book
from app.models.user import User
from app.web import web

__author__ = 'yan'


@web.route('/addbook',methods = ["POST" ])
def add_book():
    resp = {'code': 200, 'msg': '', 'data': {}}
    args = json.loads(str(request.data,encoding='utf-8'))
    isbn = args.get('isbn')
    openid = args.get('openid')
    # isbn 和openID存在
    if isbn and openid:
        # 判断isbn是否存在
        book = Book.query.filter_by(isbn = isbn).first()
        if not book:
            # 书不存在
            book_info = get_book_info(isbn)
            if book_info:
                # 获取图书的字段
                rate = book_info['rating'].get('average')
                title, image, alt, publisher, summary, price = book_info['title'],book_info['image'],book_info['alt'],book_info['publisher'],book_info['summary'],book_info['price']
                tags = ','.join([tag['title'] for tag in book_info['tags']])
                author = ','.join( book_info['author'])
                book = Book(isbn=isbn,rate=rate,title=title,image=image,alt=alt,publisher=publisher,summary=summary,price=price,tags=tags,author=author,openid=openid)
                db.session.add(book)
                db.session.commit()
                book_obj = book.__dict__
                book_obj.pop('_sa_instance_state')
                resp['msg'] = '图书添加成功'
                resp['data'] = book_obj
                return jsonify(resp)
            resp['code'] = -1
            resp['msg'] = '图书不存在'
            return jsonify(resp)
        else:
            book_obj = book.__dict__
            book_obj.pop('_sa_instance_state')
            resp['code'] = -1
            resp['data'] = book_obj
            resp['msg'] = '图书已存在'
            return jsonify(resp)
    flash('openid 或者isbn不存在')
    resp['code'] = -1
    resp['msg'] = 'openid 或者isbn不存在'
    return jsonify(resp)


@web.route('/top',methods = [ "GET","POST" ])
def tops():
    resp = {'code': 200, 'msg': '', 'data': {}}
    books = Book.query.order_by(Book.count.desc())[0:9]
    data = []
    for item in books:
        data.append({
            'id':item.id,
            'title':item.title,
            'image':item.image,
            'count':item.count
        })
    resp['data'] = data
    return jsonify(resp)


@web.route('/booklist',methods = ["GET"])
def book_list():
    resp = {'code': 200, 'msg': '', 'data': {}}
    # if request.values.get('openid'):
    #     openid = request.values.get('openid')
    #     books = Book.query.filter_by(openid=openid).all()
    #
    # else:
    books = Book.query.all()
    data = []
    for item in books:
        # 获取添加人的信息
        user = User.query.filter_by(openid = item.openid).first().user_info
        user_obj = json.loads(user)
        data.append({
            'id':item.id,
            'title':item.title,
            'image':item.image,
            'count':item.count,
            'rate':item.rate,
            'author':item.author,
            'publisher':item.publisher,
            'nickName':user_obj['nickName']
        })
    resp['data'] = data
    resp['msg'] = '获取图书数据成功'
    return jsonify(resp)


@web.route('/bookdetail',methods = ["GET"])
def book_detail():
    resp = {'code': 200, 'msg': '', 'data': {}}
    book_id = request.values.get('id')
    book_detail = Book.query.filter_by(id=book_id).first()
    if book_detail:
        book_obj = book_detail.__dict__
        book_obj.pop('_sa_instance_state')
        user = User.query.filter_by(openid=book_obj['openid']).first()
        user_obj = json.loads(user.user_info)
        book_obj['user_info'] = {
            'name': user_obj['nickName'],
            'image': user_obj['avatarUrl'],
        }
        book_obj['summary'] = book_obj['summary'].split('\n'),
        book_obj['tags'] = book_obj['tags'].split(',')
        resp['data'] = book_obj
        return jsonify(resp)
    resp['msg'] = '图书不存在'
    return jsonify(resp)


@web.route('/mybooks',methods = ["GET"])
def my_books():
    resp = {'code': 200, 'msg': '', 'data': {}}
    openid = request.values.get('openid')
    books = Book.query.filter_by(openid=openid).all()
    data = []
    for item in books:
        # 获取添加人的信息
        user = User.query.filter_by(openid=item.openid).first().user_info
        user_obj = json.loads(user)
        data.append({
            'id': item.id,
            'title': item.title,
            'image': item.image,
            'count': item.count,
            'rate': item.rate,
            'author': item.author,
            'publisher': item.publisher,
            'nickName': user_obj['nickName']
        })
    resp['data'] = data
    resp['msg'] = '获取我的图书数据成功'
    return jsonify(resp)