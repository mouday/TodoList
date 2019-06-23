# -*- coding: utf-8 -*-

# @Date    : 2018-12-23
# @Author  : Peng Shiyu

from peewee import *
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "todolist.db")

db = SqliteDatabase(DB_PATH)


class BaseModel(Model):
    class Meta:
        database = db


class StatusModel(BaseModel):
    title = CharField(unique=True)


class TaskModel(BaseModel):
    title = CharField()
    status = ForeignKeyField(StatusModel, backref="tasks", default=1)
    create_time = DateTimeField()


db.connection()
tables = [StatusModel, TaskModel]
db.create_tables(tables)
db.close()


if __name__ == '__main__':
    StatusModel.create(title="未开始")
    StatusModel.create(title="进行中")
    StatusModel.create(title="已完成")
