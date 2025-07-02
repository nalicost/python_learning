num_origin = input('请输入四位数明文>:')
num_decryption_list = []
for item in num_origin:
    i = (int(item) + 5) % 10
    num_decryption_list.append(str(i))
num_decryption_list[0], num_decryption_list[2] = num_decryption_list[2], num_decryption_list[0]
num_decryption_list[1], num_decryption_list[3] = num_decryption_list[3], num_decryption_list[1]
print(f"密码>:{''.join(num_decryption_list)}")
