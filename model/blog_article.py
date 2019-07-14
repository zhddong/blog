# -*- coding: utf-8 -*-
import pymysql
class Article(object):
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
	def query(self,id):
		sql = "SELECT `id`, `user_id`, `class_id`, `label_id`, `title`, `content`, `read`, `create_time` FROM `article` WHERE `status`=0 and id=%d" %id
		try:
			self.cursor.execute(sql)
			data = self.cursor.fetchall()
			print("文章详细：",data)
			return data
 			
		except Exception as e:
			print(sql,e)
		