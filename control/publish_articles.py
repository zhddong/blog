# -*- coding: utf-8 -*-
# 导入pymysql模块
# import hashlib
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
# hash = hashlib.sha1()
# hash.update('laowang123'.encode('utf-8'))
# 定义要执行的SQL语句
sql = "INSERT INTO `article`( `user_id`, `class_id`, `label_id`, `title`, `content`) VALUES {};"
content = '''阿尔法围棋（AlphaGo）是一款围棋人工智能程序。
其主要工作原理是“深度学习”。“深度学习”是指多层的人工神经网络和训练它的方法。
一层神经网络会把大量矩阵数字作为输入，通过非线性激活方法取权重，再产生另一个数据集合作为输出。
这就像生物神经大脑的工作机理一样，通过合适的矩阵数量，多层组织链接一起，形成神经网络“大脑”进行精准复杂的处理，
就像人们识别物体标注图片一样。'''
op_sql = sql.format((3, 1, 1, "阿尔法机器人", content))
# 执行SQL语句
cursor.execute(op_sql)
conn.commit()
 
# 关闭光标对象
cursor.close()
 
# 关闭数据库连接
conn.close()