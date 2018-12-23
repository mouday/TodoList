# -*- coding: utf-8 -*-

# @Date    : 2018-12-23
# @Author  : Peng Shiyu


from flask import Blueprint
from . import views

app_html = Blueprint(name="app_html", import_name=__name__)

app_html.add_url_rule("/", view_func=views.index)
