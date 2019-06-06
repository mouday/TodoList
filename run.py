# -*- coding: utf-8 -*-

# @Date    : 2019-06-06
# @Author  : Peng Shiyu

from __future__ import unicode_literals, print_function

import datetime

from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine, text

from tinydb import TinyDB, Query

tiny_db = TinyDB('db.json')

app = Flask(__name__)
engine = create_engine("mysql://root:123456@127.0.0.1:3306/demo?charset=utf8")
con = engine.connect()


def get_table_config():
    show_table = tiny_db.table("showTable")
    saved_tables = set(show_table.all())

    sql = "show tables"
    cursor = con.execute(sql)
    items = []
    for row in cursor.fetchall():
        table = row[0]
        if table in saved_tables:
            show = True
        else:
            show = False

        item = {
            "table": table,
            "show": show
        }
        items.append(item)
    return items


@app.route("/")
def index():
    sql = "show tables"
    cursor = con.execute(sql)
    tables = []
    for row in cursor.fetchall():
        table = row[0]
        tables.append(table)

    return render_template("index.html", tables=tables)


@app.route("/getTableData")
def table_detail():
    table = request.args.get("table")

    sql = "select * from {table} ORDER by id desc limit 20".format(table=table)
    cursor = con.execute(sql)
    titles = cursor.keys()
    print(titles)
    items = []
    for row in cursor:
        item = {}
        for key in titles:
            value = row[key]
            if isinstance(value, datetime.datetime):
                value = value.strftime("%Y-%m-%d %H:%M:%S")
            if isinstance(value, datetime.date):
                value = value.strftime("%Y-%m-%d")
            item[key] = value
        items.append(item)

    data = {
        "items": items,
        "titles": titles,
        "message": "数据已加载"
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
