import random
a=[i for i in range(100)]
c=[]
for i in range(10):
    b=random.sample(a,5)
    c+=b
print(c)