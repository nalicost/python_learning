nul_1=[0,5,6,4,8,9,2,3,1,7]
nul_2=[13,14,12,11,20,19,15,16,17,18]
compound=[]
for i in nul_1:
    if 20-i in nul_2:#由于二者满足加法等于20，所以第二个数便可以以第一个取出来的数进行表示，假设有这个数，再检测是否在列表中。
        compound.append(f'({i},{20-i})')
print(compound)