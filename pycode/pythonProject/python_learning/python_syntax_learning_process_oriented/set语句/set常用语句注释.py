# #这里面括号内的所有内容如果没有特殊说明，写代码时不能代入，若可代入会特殊说明，若括号内无内容，则写代码时不能写东西
# #第一部分：创建
# a={item,}#创建集合，但内部至少有一元素
# #第二部分：增
# a.add(item)#增加一个元素
# #第三部分：查
# b in a #查找该元素是否在集合中
# #第四部分：删
# a.pop()#随机删除并返回该值
# a.remove(item)#删除指定元素，若无该元素报错
# a.discard(item)#删除指定元素，若无该元素则什么都不做
# a.clear()#清空集合
# #第五部分：关系运算
# a & b   /   a.intersection(b) #intersection：十字路口，相互作用，此处表示交集
# a | b   /   a.union(b) #并集
# a - b   /   a.difference(b) #差集
# a ^ b   /   a.symmetric_difference(b) #symmetric：对称的，对称差集，即除交集外的并集
# a.issubset(b) #a是否为b的子集
# a.issuperset(b) #a是否为b的父集
# a.update(b) #合并后结果赋予a
# a.intersection/union/difference/symmetric_difference_update(b) #将关系运算的结果赋予a