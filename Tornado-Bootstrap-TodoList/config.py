# -*- coding: utf-8 -*-

# @File    : config.py
# @Date    : 2018-08-25
# @Author  : Peng Shiyu

# 配置参数

import os

# 服务器端口
PORT = 8080

# Tornado app配置
settings = {
    'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'cookie_secret': '0Q1AKOKTQHqaa+N80XhYW7KCGskOUE2snCW06UIxXgI=',
    'xsrf_cookies': False,
    'login_url': '/login',
    'debug': True,
}
