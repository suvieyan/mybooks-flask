"""
 Created by yan on 2018/9/27 15:14
"""
import os

import filetype
from flask import request, jsonify

import app
from app.web import web

__author__ = 'yan'

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

@web.route('/upload',methods=['POST'])
def upload():
    resp = {'code': 200, 'msg': '', 'data': {}}
    file_dir = os.path.join(basedir, app.secure.UPLOAD_FOLDER)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(file_dir, filename))  # 保存文件到upload目录
    resp['msg'] = '上传成功'
    return jsonify(resp)
