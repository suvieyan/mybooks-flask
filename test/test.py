"""
 Created by yan on 2018/9/21 14:11
"""
import json

__author__ = 'yan'

from flask import Flask, redirect, url_for, request, flash, get_flashed_messages
from urlManager import UrlManager



app = Flask(__name__)
app.secret_key = 'yan'


@app.route('/')
def index():
    login_url = url_for('login')
    return redirect(login_url)
    # return u'这是首页'


@app.route('/login/')
def login():
    url = url_for('hello')  # 通过视图的方法名，找到对应的路由,/api/hello/
    url1 = UrlManager.buildUrl('/api')  # /api
    url2 = UrlManager.buildStaticUrl('/css/bootstrap')  # /css/bootstrap?version=20180925
    return 'Hello World,url:%s,url1:%s, url2:%s'%(url,url1,url2)


@app.route('/api/hello/')
def hello():
    return 'hello'


@app.route('/question/<is_login>/')
def question(is_login):
    print('path',request.method)
    print(request.path)
    print(request.args)
    print('111',request.values.get('is_login'))
    if is_login == '1':
        return u'这是发布问答的页面'
    else:
        print(request.args)
        return redirect(url_for('login'))

@app.route('/error/<is_error>/')
def test_error_page(is_error):
    if is_error == '1':
        return 'Hello World!'
    flash('超时',category='info')  # 给下一个请求传递一个信息
    flash('超时',category='warning')  # 给下一个请求传递一个信息
    return redirect(url_for('error_page'))


@app.route('/error_page/')
def error_page():
    errors = get_flashed_messages(with_categories=False,category_filter=['warning'])  # 取出请求当中的信息，
    # with_categories=True:带类别显示，以元祖形式显示[('info', '超时'), ('warning', '超时')]
    # with_categories=False:不带类别显示，是一个列表['超时', '超时']，
    # category_filter:过滤消息的category
    print(errors)
    return json.dumps(errors)


@app.errorhandler(404)
def page_not_found(error):
    app.logger.info(error)
    app.logger.error(error)  # 输出错误的详细信息
    app.logger.debug(error)  # 输出错误的详细信息
    app.logger.warning(error)  # 输出错误的详细信息
    return 'This page does not exist',404

if __name__ == '__main__':
    app.run(debug=True)