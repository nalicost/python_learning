a = int(input('请输入第一个整数：'))
b = int(input('请输入第二个整数：'))
t = True
c, d = a, b
while t:
    t = a % b
    if t != 0:
        a, b = b, t
print(f'{c}与{d}的最大公约数时:{b}, 最小公倍数是:{c * d / b}')
