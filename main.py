# -*- coding: utf-8 -*-

#导入模板模块
from flask import Flask
import hashlib
from flask import request
from control.markdown2html import article2html
from model.blog_user import User
from model.blog_article import Article
from flask import make_response
import json
app = Flask(__name__)

@app.route('/blog')
def hello_world():
    return article2html()


def transformation(label_id):
    if label_id == "星座":
        return 0
    elif label_id == "新鲜事":
        return 1
    elif label_id == "科普":
        return 2
    elif label_id == "旅游":
        return 3
    else:
        return 4
def transformation1(label_id1):
    if label_id1 == "国际":
        return 0
    elif label_id1 == "新闻":
        return 1
    elif label_id1 == "八卦":
        return 2
    elif label_id1 == "体育":
        return 3
    else:
        return 4
@app.route('/content', methods=['POST', 'GET'])
def content():
    title = request.form.get("title")
    user_id = request.form.get("author")
    content = request.form.get("content")
    label = request.form.get("label")
    classification = request.form.get("classification")
    user_id = int (user_id)
    blog_article = Article()
    label_id = transformation(label)
    class_id = transformation1(classification)
    print(label_id)
    blog_article.increase(user_id,title,class_id,content,label_id)
    return "kkk"

def make_resdata(code,info):
    res = {}
    res["code"] = code
    res["msg"] = info
    res["data"] ={}
    res = json.dumps(res)
    response = make_response(res)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route('/reg', methods=['POST', 'GET'])
def reg():
    if request.method == "POST":
        phone = request.form.get("cellphone")
        vercode = request.form.get("vercode")
        password = request.form.get("password")
        repass = request.form.get("repass")
        nickname = request.form.get("nickname")
        agreement = request.form.get("agreement")
    else:
        phone = request.args.get("cellphone")
        vercode = request.args.get("vercode")
        password = request.args.get("password")
        repass = request.args.get("repass")
        nickname = request.args.get("nickname")
        agreement = request.args.get("agreement")
    if password != repass:
        return make_resdata(0, "两次密码输入不一致")
    hash = hashlib.sha1()
    hash.update(password.encode('utf-8'))
    pass_wd = hash.hexdigest() 
    blog_user = User()
    blog_user.insert(pass_wd,nickname,phone)
    blog_user.commit()
    return make_resdata(0, "success")
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)