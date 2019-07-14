# -*- coding: utf-8 -*-
# 导入pymysql模块
import hashlib
import pymysql
 
# 连接database
conn = pymysql.connect(
    host="127.0.0.1",
    user="zhd",
    password="123456",
    database="blog",
    port=3306,
    charset="utf8")
 
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
# 得到一个可以执行SQL语句并且将结果作为字典返回的游标
#cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
hash = hashlib.sha1()
hash.update('laowang123'.encode('utf-8'))
# 定义要执行的SQL语句
sql = "INSERT INTO `user`( `name`,`passwd`, `email`) VALUES {};"
op_sql = sql.format(("laowang", hash.hexdigest(),"12213555@qq.com"))
# 执行SQL语句
cursor.execute(op_sql)
conn.commit()
 
# 关闭光标对象
cursor.close()
 
# 关闭数据库连接
conn.close()