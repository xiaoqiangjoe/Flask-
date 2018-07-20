# import shutil
#
# shutil._unpack_zipfile(r'D:/untitled/基础知识/day117/homework/file/s5alipay.zip',r'D:/untitled/基础知识/day117/homework/file')

#################################################
# import datetime
# ctime = datetime.date.today()
# print(ctime)


############################################3

'''制作md5值'''
# import hashlib
# def md5(arg):
#     hash = hashlib.md5(b'jsjyughhhj')
#     hash.update(bytes(arg, encoding='utf-8'))
#     return hash.hexdigest()
# print(md5('1234'))
#################################################
'''测试连接数据库'''

# import pymysql
# from DBUtils.PooledDB import PooledDB
# POOL = PooledDB(
#     creator=pymysql,  # 使用链接数据库的模块
#     maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
#     mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
#     maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
#     maxshared=3,  # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
#     blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
#     maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
#     setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
#     ping=0,
#     # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='123456',
#     database='flaskhome',
#     charset='utf8'
# )
#
#
#
# conn = POOL.connection()
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# cursor.execute('select * from user')
# result = cursor.fetchall()
# conn.close()
# print(result)

#################################################################


#############################################
# lis = [
#     {'id': 1, 'userName': 'xiao', 'a': 1419.0},
#     {'id': 2, 'userName': 'qiang', 'a': 566.0},
#
# ]
#
# l=[]
# for i in lis:
#    l.append([i['userName'],i['a']])
# print(l)
##############################################


# l = [{'line': '1111'},{'line': '10'},{'line': '298'}]
#
# a = []
# for i in l :
#     for j in i.values():
#         print(j)
#         a.append(j)
# print(a)

import datetime
from collections import defaultdict

data= [{'id': 1, 'userName': 'xiao', 'line': '1111', 'datrtime': datetime.date(2018, 4, 30)},
      {'id': 1, 'userName': 'xiao', 'line': '10', 'datrtime': datetime.date(2018, 6, 3)},
      {'id': 1, 'userName': 'xiao', 'line': '298', 'datrtime': datetime.date(2018, 6, 3)}]

'''
new_data=[{
    
    'id':1,
    'userName':'xiao',
    'line':[111,10.198],
    'datrtime':[datetime.date(2018, 4, 30),datetime.date(2018, 6, 3),datetime.date(2018, 6, 3)]
}]
'''




# lst = [{'a': 123}, {'a': 456},{'b': 789}]
#
# dic = {}
# for _ in lst:
#     for k, v in _.items():
#         dic.setdefault(k, []).append(v)
#
# print ([{k:v} for k, v in dic.items()])