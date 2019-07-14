# -*- coding: utf-8 -*-
import pymysql
import types
conn = pymysql.connect(
    host="127.0.0.1",
    user="zhd",
    password="123456",
    database="blog",
    port=3306,
    charset="utf8")
cursor = conn.cursor()
id = 2
sql = "alter table `user`(`status`)  "