dic={'k0': 0, 'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4, 'k5': 5, 'k6': 6, 'k7': 7, 'k8': 8, 'k9': 9}



# dic_1={}
# for k in range(len(dic)//2):  #由于跳着选所以算出替换次数
#     dic_1.setdefault('k'+str(2*k),-1)   #将对应的key值对应的value修改为指定value
# dic.update(dic_1)
# print(dic)


for k in dic.keys(): #直接取出所有key
    if dic[k] % 2 == 0: #判断key是否符合要求
        dic[k]=-1 #修改
print(dic)