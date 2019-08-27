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
    def comments_add(self,ct_id,ip,content):
        sql = """INSERT INTO `comment`(`ct_id`, `user_ip`,`content`)
         VALUES (%s,%s,%s)"""
        try:
            self.cursor.execute(sql,(ct_id,ip,content))
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print(sql,e,)
    def comments_query(self,ct_id):
        sql = """SELECT b.name,c.like,c.content
        FROM article as a,user as b,comment as c WHERE b.status=0  and a.user_id=b.id and c.ct_id=a.id and c.ct_id=%s"""
        try:
            self.cursor.execute(sql,(ct_id))
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print(sql,e,) 
    def comment_management(self):
        sql = """SELECT id,user_ip,content,create_time
        FROM comment WHERE 1"""
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print(sql,e,)
    def commit(self):
        self.conn.commit()