# -*- coding: utf-8 -*-

# @File    : run.py
# @Date    : 2018-08-25
# @Author  : Peng Shiyu

# 应用启动入口

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application

import config
from urls import handlers

if __name__ == '__main__':
    app = Application(handlers, **config.settings)  # 实例web应用
    # app.listen(8080)             # 绑定服务器端口 二选一

    http_server = HTTPServer(app)  # 实例HTTP服务器
    http_server.listen(config.PORT)

    IOLoop.current().start()  # 启动当前线程的IOLoop
    # http://localhost:8080/
