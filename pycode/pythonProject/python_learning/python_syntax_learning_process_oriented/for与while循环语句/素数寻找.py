# for i in range(2,101):#用来取100以内的数字
#     nul=[]#设置标准物，后续进行判断，凭此保证可以将下方循环执行完有共同结果决定是否取值，此位置还可在下方每次循环完后更新nul的值
#     for j in range(2,i):#此处通过选取除数与其相除
#         if i % j == 0:#这段是课后的局部优化代码，当证明不是素数是可直接停止循环，减少运算量
#             nul.append('0')
#             break
#         nul.append(f'{i%j}')#更改标志物
#     if "0" not in nul: print(i)#标志位，判断标志物是否改变，并输出值



#该代码的课后整体优化,标志位直接检查是否更改即可，无需将所有元素放入表格中，只需证伪，将不成立的值放入其中即可，无需放成立的值
# for i in range(2,101):
#     nul=[]
#     for j in range(2,i):
#         if i % j == 0:
#             nul.append('0')
#             break
#     if '0' not in nul: print(i)
#for else 语句方法
for i in range(2,101):
    for j in range(2,i):
        if i % j == 0:
            break
    else:#else放第二格是由于要保证二循环完全完成即可保证是素数，不然不打印
        print(i)



