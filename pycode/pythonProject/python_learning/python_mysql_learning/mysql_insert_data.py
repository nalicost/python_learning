"""
                本demo演示通过pymysql向mysql中读写记录
"""
import pymysql
# 连接上数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     charset='utf8',
                     user='root',
                     password='Zjy20170132',
                     database='stu')
# 获得游标来操作数据库
c = db.cursor()
# 使用try，except结构来防止sql语句错误，使数据库崩溃，try执行数据库操作，except执行出错后的回滚数据库
try:
    name, age, gender, score, time_in_school = (input('name:'), input('age:'), input('gender:'),
                                                input('score:'), input('入学时间:'))
    sql_1 = ("insert into class_1 (name,age,gender,score,入学时间) "
             "values ('%s',%s,'%s',%s,%s);" % (name, age, gender, score, time_in_school))
    # 注意向里面传值时由于传进去的都为字符串，故不会有引号，要自己加上，其次在sql语句中无法用f格式化字符串，用百分号占位符
    c.execute(sql_1)
    # 执行语句
    db.commit()
    # 写操作需要提交
except Exception as e:
    db.rollback()
    print(e)
sql_2 = 'select * from class_1;'
# 执行读操作，不用提交
c.execute(sql_2)
# 获取所有查询结果
result = c.fetchall()
# 元组形式输出结果
print(result)
c.close()
db.close()
