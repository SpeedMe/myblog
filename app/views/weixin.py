# -*- coding: utf-8 -*-

"""
description:
author: HuangLei
date: 2016-06-06 10:48 PM
"""

from flask import request
from app import app
import hashlib
from xml.etree import ElementTree
import sys  # sys.setdefaultencoding is cancelled by site.py



# 博客首页
@app.route('/weixin', methods=['GET'])
def verify_weixin():
    # 获取输入参数
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')
    # 自己的token
    token = "iamhuanglei123"  # 这里改写你在微信公众平台里输入的token
    # 字典序排序
    list = [token, timestamp, nonce]
    list.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, list)
    hashcode = sha1.hexdigest()
    # sha1加密算法

    # 如果是来自微信的请求，则回复echostr
    if hashcode == signature:
        return echostr
    return True


@app.route('/weixin', methods=['POST'])
def weixin_post():
    print(request)
    str_xml = request.data  # 获得post来的数据
    xml = ElementTree.fromstring(str_xml)  # 进行XML解析
    content = xml.find("Content").text  # 获得用户所输入的内容
    msgType = xml.find("MsgType").text
    fromUser = xml.find("FromUserName").text
    toUser = xml.find("ToUserName").text
    print("content:", content, " msg:", msgType, " from_user:", fromUser, " to_user:", toUser)
    return content
