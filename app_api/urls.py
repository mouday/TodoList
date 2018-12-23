# -*- coding: utf-8 -*-

# @Date    : 2018-12-23
# @Author  : Peng Shiyu

from flask import Blueprint
from flask_restful import Api
from . import views

app_api = Blueprint(name="api", import_name=__name__)
restful_api = Api(app_api)

restful_api.add_resource(views.TaskResource, "/item")
restful_api.add_resource(views.StatusResource, "/status")
