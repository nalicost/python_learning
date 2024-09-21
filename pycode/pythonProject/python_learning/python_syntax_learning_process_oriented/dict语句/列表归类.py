test_list=[4,6,6,4,2,2,4,8,5,8]
output={}




#较为简单，但是只能处理此类问题，由于只需加入出现数量的数字，并把key命名为该数字，所以直接test_list中直接取，一次性通过count生成，后续相同的覆盖即可
for k in test_list:
    output[k]=[k for i in range(test_list.count(k))]
print(output)






#略显麻烦，但是较为通用，可以每次加入同key，不同value的值
#for k in test_list:
#   if k not in output:#一次循环字典新加
#       output[k]=[k,]
#   else:
#       output[k].append[k]#二次循环列表新加
#print(output)