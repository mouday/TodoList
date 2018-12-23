# -*- coding: utf-8 -*-

# @Date    : 2018-12-23
# @Author  : Peng Shiyu

from flask import send_file


def index():
    return send_file("templates/index.html")
