dic={}
for k in range(10):
    dic.setdefault('k'+str(k),k)
print(dic)