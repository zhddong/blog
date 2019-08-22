# -*- coding: utf-8 -*-
import pymysql
class Message(object):
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
    def message_add(self,ip,content):
        sql = """INSERT INTO `message`(`ip`,`content`)
         VALUES (%s,%s)"""
        try:
            self.cursor.execute(sql,(ip,content))
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print(sql,e,)
    def message_query(self):
        sql = """SELECT m.updata_time,m.like,m.content
        FROM message as m WHERE 1 order by m.updata_time desc"""
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print(sql,e,) 
    def commit(self):
        self.conn.commit()