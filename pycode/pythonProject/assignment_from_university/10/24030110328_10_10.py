

def pi_calculate(k=100):
    if k == 1:
        return 1
    else:
        return (-1) ** (k + 1) / (2 * k - 1) + pi_calculate(k - 1)


print(4 * pi_calculate())
