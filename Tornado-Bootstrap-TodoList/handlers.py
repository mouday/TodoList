# -*- coding: utf-8 -*-

# @File    : handlers.py
# @Date    : 2018-08-25
# @Author  : Peng Shiyu

# 请求处理

from datetime import datetime

from models import TodoListModel
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    """
    查询记录
    """

    def get(self):
        rows = TodoListModel.select()
        self.render("todo_list.html", rows=rows)


class AddHandler(RequestHandler):
    """
    新增记录
    """

    def post(self):
        event = self.get_argument("event")
        dct = {
            "event": event,
            "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        TodoListModel.create(**dct)

        self.redirect(self.reverse_url("index"))


class DeleteHandler(RequestHandler):
    """
    删除记录
    """

    def get(self, uid):
        TodoListModel.delete().where(TodoListModel.id == uid).execute()
        self.redirect(self.reverse_url("index"))
