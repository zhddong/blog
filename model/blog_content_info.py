# -*- coding: utf-8 -*-
import pymysql
class Content_info(object):
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
    def ip_address(self,ct_id,ip,combination):
        sql = """INSERT INTO `content_info`(`ct_id`, `ip_address`,`md5`)
         VALUES (%s,%s,%s)"""
        try:
            self.cursor.execute(sql,(ct_id,ip,combination))
            data = self.cursor.fetchall()
            return data

                
        except Exception as e:
            print(sql,e,)
            return 1
    def fabulous_query(self,content_id):
        sql = """SELECT `ct_id`
        FROM  `content_info` WHERE `ct_id`=%s"""
        try:
            self.cursor.execute(sql,(content_id))
            data = self.cursor.fetchall()
            return data

                
        except Exception as e:
            print(sql,e,)
    
    def commit(self):
        self.conn.commit()