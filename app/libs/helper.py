"""
 Created by yan on 2018/9/26 16:55
"""
import requests
import json

__author__ = 'yan'

def get_openid(appid,secret,code):
    """
    向微信后台发送请求，获取用户的session_key和open_id
    :param appid:开发者的APPID
    :param secret:开发者的AppSecret
    :param code:wx.login 返回的code
    :return:{'session_key': 'kqJhkE9AYV0E6YRm4G0nNQ==', 'openid': 'oTZEu5beSes5Lha9wKhGt5icfCb4'}
    """
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code'.format(appid,secret,code)
    result = requests.get(url).text
    return json.loads(result)

def get_book_info(isbn):
    url = 'https://api.douban.com/v2/book/isbn/' + isbn
    book_info = requests.get(url).text
    book_obj = json.loads(book_info)
    if not book_obj['title']:
        # 书籍不存在
        return
    return book_obj