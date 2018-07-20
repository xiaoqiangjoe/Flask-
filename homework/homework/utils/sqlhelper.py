# from settings import Config
import pymysql

def fetch_one(sql, arg):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='flaskhome', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 字典
    cursor.execute(sql, arg)
    data = cursor.fetchone()
    cursor.close()
    conn.close()
    return data

def fetch_all(sql, arg):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='flaskhome', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 字典
    cursor.execute(sql, arg)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def insert(sql, arg):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='flaskhome', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 字典
    cursor.execute(sql, arg)
    conn.commit()
    cursor.close()
    conn.close()


