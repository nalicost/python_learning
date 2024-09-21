arr = ['cat', 'dog', 'tac', 'god', 'act','fgo','fog','fo','of','ogf']
access_dict = {}
output_dict = {}
n=0

#略显麻烦，但是与下方思路一致，区别在于没有使用python自带的对字符的sort函数，而是人为将字母对应数字，通过对数字sort的方式，将同类的value对应同key，解决问题
# for item in arr:
#     feature_list=[]
#     for alpha in item:
#         access_dict.setdefault(alpha,n)#利用setdefault的检查式更新，使多个在不同单词中的相同字母（value)对应同一个（key），以达到数字与字母一一对应的要求
#         n += 1
#         feature_list.append(access_dict[alpha])
#     feature_list.sort()
#     if f'{feature_list}' not in output_dict:
#         output_dict.setdefault(f'{feature_list}', [item, ])
#     else:
#         output_dict[f'{feature_list}'].append(item)
# print(output_dict.values())


#以下简单在于直接使用了python自带的对字符的sort函数，注意虽然现在的python版本不支持int与str一起排序，但可单独排序，str的排序方式依据ascii码。
for item in arr:
    feature=list(item)
    feature.sort()
    feature=tuple(feature)#tuple，即元组的生成方式
    if feature not in output_dict: #类似的此时所有满足同一特征的单词都对应一个key，后将同key的value依次放入dict即可
        output_dict.setdefault(feature,[item,])
    else:
        output_dict[feature].append(item)
print(output_dict.values())