# -*- coding: utf-8 -*-
import pymysql
class Comment(object):
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
    def comments(self,ct_id,ip,content):
        sql = """INSERT INTO `comment`(`ct_id`, `user_ip`,`content`)
         VALUES (%s,%s,%s)"""
        try:
            self.cursor.execute(sql,(ct_id,ip,content))
            data = self.cursor.fetchall()
            return data

                
        except Exception as e:
            print(sql,e,)
    def commit(self):
        self.conn.commit()