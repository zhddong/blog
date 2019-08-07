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
app = Flask(__name__)#flask框架的用法

@app.route('/blog')
def hello_world():
    return article2html()

# 实现便签类型的转换
def transformation(label_id):
    if label_id == "星座":
        return 0
    elif label_id == "历史":
        return 1
    elif label_id == "科技":
        return 2
    elif label_id == "旅游":
        return 3
    else:
        return 4
# 实现分类类型的转换
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
def transformation_2(label_id):
    if label_id == 0:
        return "星座"
    elif label_id == 1:
        return "历史"
    elif label_id == 2:
        return "科技"
    elif label_id == 3:
        return "旅游"
    else:
        return "其他"
def status_num(status):
    if status == "on":
        return 1
    else:
        return 0
# 实现文章从数据库的取出
@app.route('/content_list', methods=['POST', 'GET'])
def content_list():
    if request.method == "POST":
        req_id = request.form.get("id")
        req_author = request.form.get("author")
        req_title = request.form.get("title")
        req_label = request.form.get("label")
    else:
        req_id = request.args.get("id")
        req_author = request.args.get("author")
        req_title = request.args.get("title")
        req_label = request.args.get("label")
    # print(req_label)
    # print(fileds,req_id,label_id)
    # req_label = int(req_label)
    blog_article = Article()
    # fileds = (req_id,req_label)
    # if req_id and req_label !=None:
        
    #     data = blog_article.data_display(fileds)
    # else:
    data = blog_article.data_all_display()
    if not data:
        res = {"code": -1,
        "msg": "没有找到",
        "count": 0,
        "data": [] }
        # res = json.dumps(res)
        # response = make_response(res)
        # response.headers["Access-Control-Allow-Origin"] = "*"
        # return response
    

    
    n = list(data)
    a = []
    for i in n:
        id = i[0]#文章id
        name = i[1]#作者
        title = i[2]#文章标题
        label = i[3]#标签
        content = i[4]#文章内容
        create_time = str(i[5])#创建时间
        status = i[6]#文章状态

        if  req_id and int(req_id) != id:
            continue
        if  req_author and req_author != name:
            continue
        if  req_title and req_title not in title:
            continue
        if  req_label and int(req_label) != label:
            continue

        # if req_author in name and req_id=None and req_label=None:
            # data = blog_article.data_name_display(req_author)
        # if req_author not in name:
        #     continue
        # if req_title not in title:
        #     continue
        label_id = transformation_2(label)
        # if status == 0:
        #     status_0 = 0
        # else:
        #     status_0 = 1
        articlecontent = {"id": id,
        "label": label_id,
        "title": title,
        "author": name,
        "content": content,
        "uploadtime": create_time,
        "status": status}
        a.append(articlecontent)
        # print(articlecontent)
    if not a:
        res = {"code": -1,
        "msg": "没有找到",
        "count": 0,
        "data": [] }
    else:
        res = {"code": 0,
        "msg": "",
        "count": len(data),
        "data": a }
    res = json.dumps(res)
    response = make_response(res)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
#实现文章的修改
@app.route('/content_modify', methods=['POST', 'GET'])
def content_modify():
    title = request.form.get("title")
    user_id = request.form.get("author")
    content = request.form.get("content")
    label = request.form.get("label")
    classification = request.form.get("classification")
    status = request.form.get("status")
    status = status_num(status)
    user_id = int (user_id)
    Data_acquired = request.form.get("data.id")
    print(Data_acquired)
    blog_article = Article()
    label_id = transformation(label)
    class_id = transformation1(classification)
    # print(label_id)
    blog_article.increase(user_id,title,class_id,content,label_id,status)
    # return "kkk"
    res = {"code": 0,
        "msg": "",
        "data": [] }
    res = json.dumps(res)
    response = make_response(res)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
# 实现文章的添加
@app.route('/content', methods=['POST', 'GET'])
def content():
    title = request.form.get("title")
    user_id = request.form.get("author")
    content = request.form.get("content")
    label = request.form.get("label")
    classification = request.form.get("classification")
    status = request.form.get("status")
    status = status_num(status)
    user_id = int (user_id)
    blog_article = Article()
    label_id = transformation(label)
    class_id = transformation1(classification)
    # print(label_id)
    blog_article.increase(user_id,title,class_id,content,label_id,status)
    # return "kkk"
    res = {"code": 0,
        "msg": "",
        "data": [] }
    res = json.dumps(res)
    response = make_response(res)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
def make_resdata(code,info):
    res = {}
    res["code"] = code
    res["msg"] = info
    res["data"] ={}
    res = json.dumps(res)
    response = make_response(res)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
# 实现用户的添加
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