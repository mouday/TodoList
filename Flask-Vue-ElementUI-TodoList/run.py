# -*- coding: utf-8 -*-

# @Date    : 2018-12-22
# @Author  : Peng Shiyu

from flask import Flask
from app_api.urls import app_api
from app_html.urls import app_html

app = Flask(__name__)

app.register_blueprint(blueprint=app_html, url_prefix="/")
app.register_blueprint(blueprint=app_api, url_prefix="/api")


if __name__ == '__main__':
    app.run(debug=True)
