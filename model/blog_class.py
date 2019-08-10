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
	def query(self):
		sql = "SELECT `id`, `name` FROM `class` WHERE 1"
		try:
			self.cursor.execute(sql)
			data = self.cursor.fetchall()
			# print("文章详细：",data)
			return data
 			
		except Exception as e:
			print(sql,e)
	def insert(self,name):
			sql = "INSERT INTO `class`(name) VALUES {}"
			op_sql = sql.format((name))
			print(op_sql)

			try:
				self.cursor.execute(op_sql)
 		
			except Exception as e:
				print(op_sql,e)