"""
                    re模块相关练习演示
"""
import re
# 匹配出How are you?中的所有单词
# 我的解法
print(re.findall('[^ ].[^ ?]', 'How are you?'))
# 通用解法
print(re.findall('[a-zA-Z]*', 'How are you?'))
# 其他解法
print(re.findall('[a-zA-Z][^ ?]*', 'How are you?'))
# 匹配出I'm 18中的数字
# 我的解法，通用解法
print(re.findall('[0-9]*', "I'm 18"))
# 匹配出How are you?中的大写开头的单词
print(re.findall('[A-Z][a-z]*', 'How are you?'))
# 匹配出167 -28 29 -8中的所有数字
print(re.findall('-?[0-9]+', '167 -28 29 -8'))
# 匹配出Port-9 Error #404# %@STD中的每一个部分（空格隔开的）
print(re.findall('[^ ]+', 'Port-9 Error #404# %@STD'))
# 匹配张三：13846524719中的手机号
print(re.findall('[0-9]{11}', '张三：13846524719'))
# 匹配qq：125929699中的qq号
print(re.findall('[1-9][0-9]{6,11}', 'qq：125929699'))
# 匹配12 -36 28 1.34 -3.8中的所有数字
print(re.findall('-?\\d+\\.?\\d+', '12 -36 28 1.34 -3.8'))
# 匹配日薪：$100中的薪资
print(re.findall('\\$\\d+', '日薪：$100'))
# 匹配出[花千骨],[新还珠格格],[楚乔传],[陆贞传奇]中的各作品（带中括号）
print(re.findall(r'\[.+?]', '[花千骨],[新还珠格格],[楚乔传],[陆贞传奇]'))
# 匹配张健赟：zhangjianyun1616@163.com中的邮箱(.com格式)
print(re.findall(r'\b\w+@\w+\.com', '张健赟：zhangjianyun1616@163.com'))
# 匹配密码：1137_a_b33中的密码（8-12位，包含数字，字母，下划线）
print(re.findall(r'\b\w{8,12}\b', '密码：1137_a_b333'))
# 匹配1 -20 1/3 3.5 -3.8 45% 2.3 -1/4中的数字（包含整数，正数，负数，小数，百分数，分数）
print(re.findall(r'-?\d+/?\.?\d*%?', '1 -20 1/3 3.5 -3.8 45% 2.3 -1/4'))
# 匹配I am Jack-suf who is good at iPython.What make me proud of myself is that my mum also is a member of CEO in an
# enterprises.Nice to meet you.中大写字母开头的字母(CEO也算)
print(re.findall(r'\b[A-Z]+\w*-?\w*\b', 'I am Jack-suf who is good at iPython.What make me proud of myself'
                                        ' is that my mum also is a member of CEO in an enterprises.Nice to meet you.'))
# 匹配张三：310105200011035596中的身份证号
print(re.search(r'\b\d{17}(\d|\w)', '张三：31010520001103559x').group())

