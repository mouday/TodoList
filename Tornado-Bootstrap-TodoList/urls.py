# -*- coding: utf-8 -*-

# @File    : urls.py
# @Date    : 2018-08-25
# @Author  : Peng Shiyu

# 路由映射

from handlers import *
from tornado.web import url

handlers = [
    url("/", IndexHandler, name="index"),
    ("/add", AddHandler),
    ("/delete/(?P<uid>\d+)", DeleteHandler),
]
