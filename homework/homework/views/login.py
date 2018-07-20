from flask import Blueprint, render_template, Flask, request, redirect, session
from ..utils.md5 import md5
from ..utils import sqlhelper


log = Blueprint('log', __name__)



@log.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('user')
    password = request.form.get('pwd')
    md_pwd = md5(password)
    print('md',md_pwd)

    # conn = pymysql.connect(host='127.0.0.1',user='root',password='123456',database='flaskhome',charset='utf8')
    # # cursor = conn.cursor() # 元祖
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor) # 字典
    # cursor.execute("select id,nickname FROM `user` WHERE userName=%s AND `password`=%s",(username, md_pwd))
    # data = cursor.fetchone()
    # cursor.close()
    # conn.close()

    data = sqlhelper.fetch_one("select id,nickname FROM `user` WHERE userName=%s AND `password`=%s",(username, md_pwd))


    if data is None:
        return render_template('login.html', error='用户名密码错误')
    else:
        session['user_info'] = {'id':data['id'], 'nickname':data['nickname']}

        return redirect('/index')


@log.route('/logout')
def logout():
    if 'user_info' in session:
        del session['user_info']
    return redirect('/login')