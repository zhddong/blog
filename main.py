# -*- coding: utf-8 -*-
#导入模板模块
from flask import Flask
import hashlib
from flask import request
from control.markdown2html import article2html
from model.blog_user import User
from model.blog_article import Article
from model.blog_content_info import Content_info
from model.blog_comment import Comment
from model.blog_class import Class
from flask import make_response
import json
import types
from flask import render_template
app = Flask(__name__,template_folder="./templates",static_folder="./res")#flask框架的用法
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
#显示文章内容以及评论内容
@app.route('/details', methods=['POST','GET'])
def details():
    if request.method == "POST":
        ct_id = request.form.get("id")
        page = request.form.get("page")
        blog_comment = Comment()
        comment = blog_comment.comments_query(ct_id)
        print(ct_id)
        if not comment:
            res = {"code": -1,
            "msg": "还没有评论",
            "count": 0,
            "data": [] }
            res = json.dumps(res)
            response = make_response(res)
            return response
        n = list(comment)
        a = []
        for i in n:
            name = i[0]#用户名
            like= i[1]#点赞量
            content = i[2]#评论内容
            articlecontent = {"name": name,
            "like":like,"content":content[0:200]
            }
            # print(articlecontent)
            a.append(articlecontent)
        page = int(page)
        page = page-1
        b = page*3
        c = a[b:b+3]
        # print(c)
        if not c:
            res = {"code": -1,
            "msg": "没有评论",
            "count": 0,
            "data": [] }
        else:
            res = {"code": 0,
            "msg": "",
            "count": 0,
            "data": c }
        res = json.dumps(res)
        response = make_response(res)
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response
    else:
        ct_id = request.args.get("id")
        blog_article = Article()
        data = blog_article.ct_details(ct_id)
        blog_comment = Comment()
        comment = blog_comment.comments_query(ct_id)
        # print(comment)
        if not data:
            res = "该文章不存在！！！"
            response = make_response(res,404)
            response.headers["Access-Control-Allow-Origin"] = "*"
            return response
        return render_template('details.html',
            ct_title=data[0][0],
            ct_content=data[0][1],
            ct_time=data[0][2],
            ct_read=data[0][5],
            ct_like=data[0][6],
            ct_id=ct_id
            # user_name="happy",
            # comment_like=560,
            # comment_content="这篇文章写得好！！！"
            )

#留言
@app.route('/message', methods=['POST','GET'])
def message():
    if request.method == "POST":
        pass
    else:
        return render_template('html/message.html',
            )
#关于
@app.route('/about', methods=['POST','GET'])
def about():
    if request.method == "POST":
        pass
    else:
        return render_template('html/about.html',
            )
#评论显示
@app.route('/comment', methods=['POST','GET'])
def comment():
    if request.method == "POST":
        pass
    else:
        ct_id = request.args.get("id")
        blog_article = Article()
        data = blog_article.ct_details(ct_id)
        # blog_comment = Comment()
        # comment = blog_comment.comments_query(ct_id)
        print(data)
        return render_template('html/comment.html',
            comment_like=data[0][6],
            comment_time=data[0][2],
            comment_content=data[0][1],
            comment_see=data[0][5],
            comment_title=data[0][0],
            ct_id=ct_id
            )
#评论添加
@app.route('/comment_add', methods=['POST','GET'])
def comment_add():
    if request.method == "POST":
        ct_id = request.form.get("id")
        content = request.form.get("content")
        ct_id = int (ct_id)
        # print(ct_id)
        ip = request.remote_addr
        # print(ip)
        blog_comment = Comment()
        # hash = hashlib.sha1()
        # hash.update(ip.encode('utf-8'))
        # comment_ip = hash.hexdigest()
        # print(ip)
        blog_comment.comments_add(ct_id,ip,content)
        blog_comment.commit()
        res = {"code": 0,
            "msg": "",
            "data": [] }
        res = json.dumps(res)
        response = make_response(res)
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response
    else:
        # ct_id = request.args.get("id")
        # blog_comment = Comment()
        # comment = blog_article.comments_query(ct_id)
        return render_template('html/comment.html',
            comment_like=566,
            comment_time="一天前",
            comment_content="很好",
            comment_see=545,
            comment_title="公司客户",
            ct_id=99
            )
#点赞
@app.route('/index', methods=['POST','GET'])
def fabulous():
    if request.method == "POST":
        ct_id = request.form.get("id")
        ip = request.remote_addr
        # print(ip)
        # print(ct_id)
        # ct_like = request.args.get("like")
        blog_content_info = Content_info()
        hash = hashlib.sha1()
        a = str(ct_id+ip)
        hash.update(a.encode('utf-8'))
        combination = hash.hexdigest()
        data = blog_content_info.ip_address(ct_id,ip,combination)
        print(data)
        state = {"state": data}
        print(state)
        blog_content_info   .commit()
        res = {"code": 0,
            "msg": "",
            "data": state }
        print(res)
        res = json.dumps(res)
        response = make_response(res)
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response
    else:
        return render_template('html/index.html')
#点赞查询
@app.route('/fabulous_query', methods=['POST','GET'])
def fabulous_query():
    if request.method == "POST":
        ct_id = request.form.get("id")
        # print(ip)
        # print(ct_id)
        # ct_like = request.args.get("like")
        blog_content_info = Content_info()
        data = blog_content_info.fabulous_query(ct_id)
        print(data)
        state = {"state": data}
        print(state)
        blog_content_info.commit()
        res = {"code": 0,
            "msg": "",
            "data": state }
        print(res)
        res = json.dumps(res)
        response = make_response(res)
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response
    else:
        return render_template('html/index.html')
#浏览
@app.route('/browse', methods=['GET'])
def browse():
    blog_article = Article()
    data = blog_article.browse(ct_id)
# 闲言文章显示
@app.route('/xianyan_dispaly', methods=['POST', 'GET'])
def xianyan_dispaly():
    if request.method == "POST":
        create_time = request.form.get("create_time")
        title = request.form.get("title")
        content = request.form.get("content")
        page = request.form.get("page")
    else:
        create_time = request.args.get("create_time")
        title = request.args.get("title")
        content = request.args.get("content")
    blog_article = Article()
    data = blog_article.xianyan_display()
    # print(data)
    blog_content_info = Content_info()
    n = list(data)
    a = []
    for i in n:
        title = i[0]#标题
        content= i[1]#文章内容
        create_time = i[2]#创建时间
        content_id = i[4]#文章ID
        is_like = blog_content_info.fabulous_query(content_id)
        if not is_like:
            is_like = 0
        else:
            is_like = 1
        create_time = str(create_time)
        articlecontent = {"create_time": create_time,
        "title":title,"content":content[0:200],
        "id":content_id ,"is_like":is_like
        }
        # print(articlecontent)
        a.append(articlecontent)
    page = int(page)
    page = page-1
    b = page*10
    c = a[b:b+10]
    # print(c)
    if not c:
        res = {"code": -1,
        "msg": "没有找到",
        "count": 0,
        "data": [] }
    else:
        res = {"code": 0,
        "msg": "",
        "count": len(data),
        "data": c }
    res = json.dumps(res)
    response = make_response(res)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
# 分类管理（取出）
@app.route('/classification', methods=['POST', 'GET'])
def classification():
    if request.method == "POST":
        req_id = request.form.get("id")
        name = request.form.get("tags")
    else:
        req_id = request.args.get("id")
        name = request.args.get("tags")
    blog_class = Class()
    data = blog_class.query()
    n = list(data)
    a = []
    for i in n:
        id = i[0]#文章id
        name = i[1]#分类名
        articlecontent = {"id": id,
        "tags":name
        }
        # print(articlecontent)
        a.append(articlecontent)
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
# 分类的添加
@app.route('/classification_name', methods=['POST', 'GET'])
def classification_name():
    if request.method == "POST":
        name = request.form.get("tags")
    else:
        name = request.args.get("tags")
    blog_class = Class()
    print(name)
    blog_class.insert(name)
    res = {"code": 0,
        "msg": "",
        "data": [] }
    res = json.dumps(res)
    response = make_response(res)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
# 实现文章从数据库的取出
@app.route('/content_list', methods=['POST', 'GET'])
def content_list():
    if request.method == "POST":
        req_id = request.form.get("id")
        req_author = request.form.get("author")
        req_title = request.form.get("title")
        req_label = request.form.get("label")
        page = request.form.get("page")
    else:
        req_id = request.args.get("id")
        req_author = request.args.get("author")
        req_title = request.args.get("title")
        req_label = request.args.get("label")
        page = request.args.get("page")
    # print(req_label)
    # print(fileds,req_id,label_id)
    # req_label = int(req_label)
    blog_article = Article()
    # fileds = (req_id,req_label)
    # if req_id and req_label !=None:
    # print(page) 
    #     data = blog_article.data_display(fileds)
    # else:
    data = blog_article.data_all_display()
    # print(data)
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
        # if status == 0:
        #     status_0 = 0
        # else:
        #     status_0 = 1
        label_id = transformation_2(label)
        articlecontent = {"id": id,
        "label": label_id,
        "title": title,
        "author": name,
        "content": content,
        "uploadtime": create_time,
        "status": status}
        a.append(articlecontent)
        # print(articlecontent)
    page = int(page)
    page = page-1
    b = page*10
    # print(b)
    if not a:
        res = {"code": -1,
        "msg": "没有找到",
        "count": 0,
        "data": [] }
    else:
        res = {"code": 0,
        "msg": "",
        "count": len(data),
        "data": a[b:b+10] }
    res = json.dumps(res)
    response = make_response(res)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
# 文章的删除
@app.route('/delete_articles', methods=['POST', 'GET'])
def delete_articles():
    delete_id = request.form.get("id")
    print(delete_id)
    blog_article = Article()
    blog_article.delete(delete_id)  
    res = {"code": 0,
        "msg": "",
        "data": [] }
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
    # print(user_id)
    user_id = int (user_id)
    article_id = request.form.get("id")
    # print(Data_acquired)
    blog_article = Article()
    label_id = transformation(label)
    class_id = transformation1(classification)
    # print(label_id)
    print(user_id,title,class_id,content,label_id,status,article_id)
    blog_article.modify(user_id,title,class_id,content,label_id,status,article_id)
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