# -*- coding: utf-8 -*-
import pymysql
class User(object):
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
	def insert(self,password,nickname,phone):
		sql = "INSERT INTO `user`( `passwd`, `name`,  `phone`) VALUES {}"
		op_sql = sql.format((password, nickname,phone))


		try:
			self.cursor.execute(op_sql)
 		
		except Exception as e:
			print(sql,e)
	def commit(self):
		self.conn.commit()