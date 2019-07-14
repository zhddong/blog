# -*- coding: utf-8 -*-

#导入模板模块
from flask import Flask
import hashlib
from flask import request
from control.markdown2html import article2html#因为markdown2html1模块在control文件夹里，所以control.markdown2html1
from model.blog_user import User

app = Flask(__name__)

@app.route('/blog')
def hello_world():
    return article2html()

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
        return "两次密码输入不一致"
    hash = hashlib.sha1()
    hash.update(password.encode('utf-8'))
    pass_wd = hash.hexdigest() 
    blog_user = User()
    blog_user.insert(pass_wd,nickname,phone)
    blog_user.commit()
    return '{"success":0}'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)