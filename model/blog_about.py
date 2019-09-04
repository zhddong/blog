# -*- coding: utf-8 -*-
import pymysql
class About(object):
    """docstring for Article"""
    def __init__(self,cfg):
        self.conn = pymysql.connect(
        host=cfg["mysql"]["model"]["host"],
        user=cfg["mysql"]["model"]["user"],
        password=cfg["mysql"]["model"]["password"],
        database=cfg["mysql"]["model"]["database"],
        port=cfg["mysql"]["model"]["port"],
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