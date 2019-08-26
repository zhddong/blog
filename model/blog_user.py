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
	def query(self,password,name):
		sql = "SELECT `passwd`, `name` FROM `user` WHERE `passwd` = %s  and `name` = %s"
		try:
			self.cursor.execute(sql,(password,name))
			data = self.cursor.fetchall()
			return data
		except Exception as e:
			print(sql,e)
	def app_index(self,name):
		sql = "SELECT `name` FROM `user` WHERE `name` = %s"
		try:
			self.cursor.execute(sql,(name))
			data = self.cursor.fetchall()
			return data
		except Exception as e:
			print(sql,e)
	def commit(self):
		self.conn.commit()