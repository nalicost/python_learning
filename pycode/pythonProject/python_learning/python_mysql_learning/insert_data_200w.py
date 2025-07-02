import pymysql
import random
import string
db = pymysql.connect(
    host="localhost",
    user="root",
    password="Zjy20170132",
    charset="utf8",
    database="country"
)
cur = db.cursor()
# 单次插入方式
for item in range(2000000):
    name = f"{''.join(random.sample(string.ascii_lowercase, 4))}"
    sql = "insert into students (name) values ('%s')" % (name, )
    try:
        cur.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
"""
多次插入优化
sql = "insert into students (name) values ('%s')"
re_li = []
for item in range(2000000):
    name = f"{''.join(random.sample(string.ascii_lowercase, 4))}"
    re_li.append(name)
try:
    cur.executemany(sql, re_li)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
"""
db.close()
cur.close()
