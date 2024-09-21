for i in range(2,101):
    is_prime_nul=True#标志物以true false为值
    for j in range(2,i):
        if i % j == 0:
            is_prime_nul=False#出现不符合条件的证伪，改变标志位
            break
    if is_prime_nul == True: print(i,'i is prime number')#标志位，最后判断标志是否改变，来决定是否执行


        