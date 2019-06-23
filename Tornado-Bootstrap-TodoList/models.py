# -*- coding: utf-8 -*-

# @File    : model.py
# @Date    : 2018-08-25
# @Author  : Peng Shiyu

# 数据操作

from peewee import *
import os

BASE_DIR = os.path.dirname(__file__)
DB_NAME = "todolist.db"
DB_PATH = os.path.join(BASE_DIR, DB_NAME)

db = SqliteDatabase(DB_PATH)


class TodoListModel(Model):
    event = CharField(default="")
    create_time = DateTimeField(default=None)

    class Meta:
        database = db
        table_name = "todolist"


if not TodoListModel.table_exists():
    TodoListModel.create_table()
