"""
                    批量向数据库加入字典单词，及其词性、释义
"""
import pymysql
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='Zjy20170132',
                     database='dict',
                     charset='utf8')
cur = db.cursor()
with open(r"C:\Users\zhang\code\dict.txt.txt",encoding='utf8') as f:
    try:
        while True:
            line = f.readline()
            if not line:
                print('操作完成')
                break
            content_list = line.rsplit(' ', 2)
            sql_ = ("insert into words (spell,characteristic,meaning)"
                    "values (%s,%s,%s)")
            cur.execute(sql_, [content_list[0], content_list[1], content_list[2]])
            db.commit()
    except Exception as e:
        print(e)
        db.rollback()
cur.close()
db.close()


"""
其中切分单词释义可使用re正则匹配
利用re.findall中有子组就以元组形式返回子组内容（外套列表）直接获取内容
如：re.findall(r'(.+)(num|determiner|adjective|noun|verb|adverb'
                        r'|preposition|conjunction|determiner|conjunction|interjection'
                        r'|tense|demonstrative|definite article|interrogative|acronym)(.+)', line)
这里正则表达式较长，主要由于排列格式有问题，难以切割，为了格式统一，只得将词性一一列举，保证前面的单词（词组）是完整的
当然可以考虑将字符串反转，让后使用空格来匹配，再将除前两项外再拼接在一起，并再次反转，不过如此行为就不如直接使用rsplit来进行切割了
"""
