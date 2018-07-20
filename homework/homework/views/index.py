from flask import Blueprint, render_template, Flask, request, redirect, session, jsonify
# import pymysql
from ..utils import sqlhelper
import os, json, shutil, uuid, datetime

# import shutil
# import uuid
# import datetime
ind = Blueprint('ind', __name__)


@ind.before_request
def process_request():
    if not session.get("user_info"):
        return redirect("/login")

    return None


@ind.route('/index')
def index():
    # conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='flaskhome', charset='utf8')
    # # cursor = conn.cursor() # 元祖
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 字典
    # cursor.execute("SELECT id,userName from User;")
    # data = cursor.fetchall()
    # print('data1',data)
    # cursor.close()
    # return render_template('index.html', data=data)
    # data = sqlhelper.fetch_all("SELECT id,userName from User;",[])
    # print(data,type(data))

    data = sqlhelper.fetch_all(
        "select user.id,user.userName,sum(coderecord.line) from `user` LEFT JOIN coderecord ON coderecord.user_id = `user`.id group by user.id;",
        [])

    list = []
    for data_list in data:
        list.append([data_list['userName'], data_list['sum(coderecord.line)']])

    return render_template('index.html', data=data, list=json.dumps(list))


@ind.route('/showdetail/<string:userid>', methods=['GET', 'POST'])
def showdetail(userid):
    # conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='flaskhome', charset='utf8')
    ## cursor = conn.cursor() # 元祖
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 字典
    # cursor.execute("SELECT id,line,datrtime from Coderecord where user_id =%s",(userid,))
    # data = cursor.fetchall()
    # print('data2', data)
    # cursor.close()
    # data = sqlhelper.fetch_all("SELECT id,line,datrtime from Coderecord where user_id =%s",(userid,))
    # print('data',data)

    data = sqlhelper.fetch_all(
        "SELECT user.id,user.userName , coderecord.line, coderecord.datrtime FROM user  LEFT JOIN coderecord ON coderecord.user_id = `user`.id  where user.id=%s group by coderecord.id",
        (userid,))
    print('data',data)

    lines = []
    for line in data:
        if 'line' in line:
            lines.append(int(line['line']))

    names = []
    for name in data:
        if 'userName' in name:
            names.append(name['userName'])

    ctimes = []
    for ctime in data:
        if 'datrtime' in ctime:
            ctimes.append(ctime['datrtime'])

    time_str_list = []
    for time_str in ctimes:

        time_str_list.append(time_str.strftime('%Y-%m-%d'))




    new_data = [{'name': list(set(names)), 'data': lines}]

    return render_template('showdetail.html', data=data, new_data=json.dumps(new_data), time_str_list=time_str_list)


@ind.route('/uplode', methods=['GET', 'POST'])
def uplode():
    if request.method == 'GET':
        return render_template('uplode.html')

    file_obj = request.files.get('code')
    # print(type(file_obj))
    # print(file_obj.filename)
    # print(file_obj.stream)

    # 1 上传压缩文件
    new_tuple_name = file_obj.filename.rsplit('.', maxsplit=1)
    # print('new_tuple_name', new_tuple_name) ['新建文本文档', 'txt']

    if len(new_tuple_name) != 2:
        return '请上传zip文件'
    if new_tuple_name[1] != 'zip':
        return '请上传zip文件'

    '''
    # 2 接收并处理
    # 获取路径并保存在本地服务器
    file_path = os.path.join('file', file_obj.filename)
    file_obj.save(file_path)
    # 3 解压zip文件
    shutil._unpack_zipfile(file_path, r'D:/untitled/基础知识/day117/homework/file')
    '''
    # 2 读取压缩文件的内容file_obj.stream，并解压上传

    unpack_path = os.path.join('file', str(uuid.uuid4()))
    shutil._unpack_zipfile(file_obj.stream, unpack_path)

    # 3 遍历文件夹的内容

    # ('file\\165ce7b0-e830-4dec-b419-e3ab80800c00', ['s5alipay', '__MACOSX'], [])
    total_num = 0
    for base_path, file_folder_list, file_list in os.walk(unpack_path):
        for file_name in file_list:
            file_path = os.path.join(base_path, file_name)  # 单个文件名的具体路径
            file_ext = file_path.rsplit('.', maxsplit=1)
            if len(file_ext) != 2:
                continue
            if file_ext[1] != 'py':
                continue
            file_num = 0
            with open(file_path, 'rb') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    if line.startswith(b'#'):
                        continue
                    file_num += 1
            total_num += file_num

    # 4 写入数据库

    ctime = datetime.date.today()
    print(total_num, ctime, session['user_info']['id'])
    '''
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='flaskhome', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id from Coderecord where datrtime=%s and user_id=%s",(ctime,session['user_info']['id']))
    data = cursor.fetchone()
    cursor.close()
    conn.close()
    '''
    data = sqlhelper.fetch_one("select id from Coderecord where datrtime=%s and user_id=%s",
                               (ctime, session['user_info']['id']))

    if data:
        return "今天已经上传"

    # conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='flaskhome', charset='utf8')
    # # cursor = conn.cursor() # 元祖
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 字典
    # cursor.execute("INSERT INTO Coderecord(line,datrtime,user_id) VALUE (%s,%s,%s) ",(total_num, ctime, session['user_info']['id']))
    # conn.commit()
    # cursor.close()
    # conn.close()
    sqlhelper.insert("INSERT INTO Coderecord(line,datrtime,user_id) VALUE (%s,%s,%s) ",
                     (total_num, ctime, session['user_info']['id']))

    return render_template('uplode.html')
