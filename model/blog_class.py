# -*- coding: utf-8 -*-
import pymysql
class Class(object):
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
    #查询
    def query(self):
        sql = "SELECT `id`, `name` FROM `class` WHERE `status`=0"
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            # print("文章详细：",data)
            return data
            
        except Exception as e:
            print(sql,e)
    #添加
    def insert(self,name):
            sql = "INSERT INTO `class`(name) VALUES {}"
            op_sql = sql.format((name))
            print(op_sql)

            try:
                self.cursor.execute(op_sql)
        
            except Exception as e:
                print(op_sql,e)
    #修改
    def modify(self,name,id):
            sql = """UPDATE `class` SET `name`=%s
            WHERE `id`=%s"""
            try:
                self.cursor.execute(sql,(name,id))
            except Exception as e:
                print(sql,e)
    #删除
    def delete(self,delete_id):
            sql = "UPDATE `class` SET `status`=1 WHERE  id=%s"
            try:
                self.cursor.execute(sql,(delete_id))
            except Exception as e:
                print(sql,e)
    def commit(self):
        self.conn.commit()