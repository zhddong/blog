# -*- coding: utf-8 -*-
import pymysql
class About(object):
    """docstring for Article"""
    def __init__(self):
        self.conn = pymysql.connect(
        host="127.0.0.1",
        user="zhd",
        password="123456",
        database="blog",
        port=3306,
        charset="utf8")
        self.cursor = self.conn.cursor()
    def about_query(self):
        sql = """SELECT title,content
        FROM about WHERE 1"""
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print(sql,e,) 
    def commit(self):
        self.conn.commit()