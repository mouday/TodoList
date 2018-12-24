# -*- coding: utf-8 -*-

# @Date    : 2018-12-23
# @Author  : Peng Shiyu

from datetime import datetime

from flask import request
from flask_restful import Resource
from playhouse.shortcuts import model_to_dict
from .models import TaskModel, StatusModel


class TaskResource(Resource):
    def get(self):
        items = TaskModel.select()
        data = []
        for item in items:
            dct = {}
            for k, v in item.__data__.items():
                if isinstance(v, datetime):
                    dct[k] = v.strftime("%Y-%m-%d %H:%M:%S")
                else:
                    dct[k] = v
            data.append(dct)

        return data

    def post(self):
        title = request.json.get("title")
        create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        TaskModel.create(title=title, create_time=create_time)
        return {"message": "添加成功"}

    def delete(self):
        uid = request.args.get("uid")
        TaskModel.delete().where(TaskModel.id == uid).execute()
        return {"message": "删除成功"}

    def put(self):
        uid = request.json.get("uid")
        status = request.json.get("status")
        TaskModel.update(status=status).where(TaskModel.id == uid).execute()
        return {"message": "更新成功"}


class StatusResource(Resource):
    def get(self):
        items = StatusModel.select()
        data = [model_to_dict(item) for item in items]
        return data
