# -*- coding: utf-8 -*-
import pymysql
class User(object):
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
    def insert(self,password,nickname,phone):
        sql = "INSERT INTO `user`( `passwd`, `name`,  `phone`) VALUES {}"
        op_sql = sql.format((password, nickname,phone))
        try:
            self.cursor.execute(op_sql)
        
        except Exception as e:
            print(sql,e)
    def query(self,password,name):
        sql = "SELECT `passwd`, `name` FROM `user` WHERE `passwd` = %s  and `name` = %s"
        try:
            self.cursor.execute(sql,(password,name))
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print(sql,e)
    def app_index(self):
        sql = "SELECT `name` FROM `user` WHERE `admin`=1"
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print(sql,e)
    def commit(self):
        self.conn.commit()