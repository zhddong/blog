# -*- coding: utf-8 -*-
from flask import Flask  #引入Flask类，Flask类实现了一个WSGI应用
from flask import request,render_template
app =Flask(__name__)  #app是Flask的实例，它接收包或者模块的名字作为参数，但一般都是传递__name__。    

@app.route("/") #使用app.route装饰器会将URL和执行的视图函数的关系保存到app.url_map属性上。
def first(): #处理URL和视图函数的关系的程序就是路由，这里的视图函数就是first。
    return "欢迎来到我的世界"

@app.route("/login",methods=['GET'])   #请求方式为get
def login():
    return render_template('l.html')

@app.route("/login",methods=['POST']) #请求方式为post
def loginin():
    if request.form['username']=='zkx' and request.form['password']=='zkx':
            username =request.form['username']
            return render_template('l.html',username='zkx',moban='moban')
    return render_template('one.html',username='username',moban='shurucuowu')
app.run( host='127.0.0.1', port=666, debug='True')#默认Flask只监听虚拟机的本地127.0.0.1这个地址，端口为666。
