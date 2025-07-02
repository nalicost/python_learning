water_quantity = int(input('请输入年用水量>:'))
if 0 < water_quantity <= 220:
    water_cost = water_quantity * 3.45
elif 220 < water_quantity <= 300:
    water_cost = (water_quantity - 220) * 4.83 + 220 * 3.45
elif 300 < water_quantity:
    water_cost = (water_quantity - 300) * 5.83 + 220 * 3.45 + (300 - 220) * 4.83
else:
    raise ValueError
print(f'总水费为:{water_cost}')
