"""
                BMI计算
"""
# 从命令台获取身高体重
weight = float(input('请输入你的体重（公斤）>:'))
height = float(input('请输入你的身高（米）>:'))
bmi = weight / height ** 2
# 将计算结果输出
print('BMI值为：%.1f' % (bmi, ))
