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
        sql = "SELECT `id`, `user_id`, `class_id`, `label_id`, `title`, `content`, `read`, `create_time` FROM `article` WHERE `status`=1 and id=%d" %id
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            # print("文章详细：",data)
            return data
            
        except Exception as e:
            print(sql,e)
    def increase(self,user_id,title,class_id,content,label_id,status):
            sql = "INSERT INTO `article`( `user_id`, `title`, `class_id`,`content`, `label_id`, `status`) VALUES {}"
            op_sql = sql.format((user_id,title,class_id,content,label_id,status))
            print(op_sql)

            try:
                self.cursor.execute(op_sql)
        
            except Exception as e:
                print(op_sql,e)
    def modify(self,user_id,title,class_id,content,label_id,status,article_id):
            sql = """UPDATE `article` SET `user_id`=%d,`title`="%s",`class_id`=%d,
            `content`="%s",`label_id`=%d,`status`=%d
            WHERE `id`=%s"""%(user_id,title,class_id,content,label_id,status,article_id)
            # op_sql = sql.format((user_id,title,class_id,content,label_id,status,id))
            # print(sql)
            # print(user_id,title,class_id,content,label_id,status,article_id)#检测收到的数据

            try:
                self.cursor.execute(sql)
        
            except Exception as e:
                print(sql,e)
    def delete(self,delete_id):
            sql = "UPDATE `article` SET `status`=2 WHERE  id=%s"%delete_id
            try:
                self.cursor.execute(sql)
            except Exception as e:
                print(sql,e)
    def data_all_display(self):
        # %(id,"%",author,"%","%",title,"%",label)
        sql = """SELECT a.id,user.name,a.title,a.label_id, 
        a.content,a.create_time,  a.status,user.status,user.id 
        FROM article as a,user WHERE user.status=0  and a.user_id=user.id """
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data

            
        except Exception as e:
            print(sql,e)
    def xianyan_display(self):
        # %(id,"%",author,"%","%",title,"%",label)
        sql = """SELECT a.title,
        a.content,a.create_time,user.id ,a.id 
        FROM article as a,user WHERE user.status=0  and a.user_id=user.id  order by a.create_time desc"""
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data

            
        except Exception as e:
            print(sql,e)
    def ct_details(self,id):
        sql = """SELECT a.title,
        a.content,a.create_time,user.id ,a.id,a.read ,a.like
        FROM article as a,user WHERE user.status=0  and a.user_id=user.id  and a.id=%s"""
        try:
            self.cursor.execute(sql,(id))
            data = self.cursor.fetchall()
            return data

                
        except Exception as e:
            print(sql,e)
    # def data_display(self,fileds):
    #   # %(id,"%",author,"%","%",title,"%",label)
    #   sql = """SELECT a.id,user.name,a.title,a.label_id, 
    #   a.content,a.create_time,  a.status,user.status,user.id 
    #   FROM article as a,user WHERE user.status=0  and a.user_id=user.id and a.id=%s  and  a.label_id=%s"""
    #   try:
    #       self.cursor.execute(sql,fileds)
    #       data = self.cursor.fetchall()
    #       return data

            
    #   except Exception as e:
    #       print(sql,e)
    # def data_name_display(self,name):
    #   # %(id,"%",author,"%","%",title,"%",label)
    #   sql = """SELECT a.id,user.name,a.title,a.label_id, 
    #   a.content,a.create_time,  a.status,user.status,user.id 
    #   FROM article as a,user WHERE user.status=0 and a.user_id=user.id user.name=name"""
    #   try:
    #       self.cursor.execute(sql)
    #       data = self.cursor.fetchall()
    #       return data

            
    #   except Exception as e:
    #       print(sql,e)
        
if __name__ == '__main__':
    a = Article()
    # b = a.data_display(2,"o","结巴",1)
    # print(b)
    c = a.xianyan_display()
    print(c)
    import time
    time.sleep(100) 