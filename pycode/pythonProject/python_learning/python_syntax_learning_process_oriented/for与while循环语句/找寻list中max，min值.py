nul=[5,7,2,3,9,5,4,10,6,5,4,4,4,0,8,6,5]
# for i in nul:
#     for j in nul:
#         if i > j:
#             break
#     else:
#         print(f'min={i}')
#     for j in nul:
#         if i < j:
#             break
#     else:
#         print(f'max={i}')
#总体思路由于要比大小，要么去两次，如上，较麻烦，要么就取一个出来，然后每个和它比，大了或小了就放进去，再继续比较，即可少取一次
nul_max=nul[0]
nul_min=nul[0]
for i in nul:
    if i > nul_max:
        nul_max=i
    elif i < nul_min:
        nul_min=i
print (f'max={nul_max},min={nul_min}')