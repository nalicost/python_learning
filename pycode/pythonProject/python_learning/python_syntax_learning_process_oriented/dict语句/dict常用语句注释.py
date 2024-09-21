# #这里面括号内的所有内容如果没有特殊说明，写代码时不能代入，若可代入会特殊说明，若括号内无内容，则写代码时不能写东西
# #第一部分：创建字典;注：可再嵌套列表或者字典
# a={key_1:value_1,key_2:value_2,.......}
# a=dict(key_1=value_1,key_2=value_2,.......)
# a = {key:value for key in 范围 for value in 范围 if 条件}
# #第二部分：增加
# a[key_n]=value_n#没有重复key的时候新增，有重复key的时候修改value
# a.setdefault(key_n,value_n)#新增单个key与value,没有重复key的时候新增，有重复key的时候输出原先key对应的值
# #第三部分：修改
# a[key_n]=value_new
# a.update(b)#将ab两字典合并，若用同key则value值取b中的
# #第四部分：查
# a.get(key_n)#查找此key值的value值，若无返回None
# a[key_n]#查找此key值的value值，若无报错
# #第五部分：判断
# key_n in a#判断key值是否在a中
# #第六部分：删除
# a.pop(key_n)#拿出key所对应的value，并删除该key
# del a[key_n]#删除该key
# a.popitem()#LIFO(last in first out)删除最后放入字典的一对值
# a.clear()#清空
# #第七部分：打印
# a.keys()#返回所有key值，看起来像列表，其实不是
# a.values()#返回所有value值，看起来像列表，其实不是
# a.items()#返回所有key与value值，以元组形式
# #第八部分：循环
# for k in a.keys()#循环key
# for k in a.values()#循环value
# for k in a.items()#循环key与value一起
# for k,v in dic#循环key,更快推荐
# #第九部分：特殊
# a.fromkeys([],value)#以列表中的每个元素为key，共同赋予相同的value
# #第十部分：
# a.copy()#浅copy
# #第十一部分：
# len(a)#返回字典a长度
