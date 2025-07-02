

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def get_info(self):
        return "商品名称:{},价格:{}元,库存:{}件".format(self.name,self.price,self.stock)

    def update_stock(self, amount):
        self.stock += amount
        return "更新库存后：{}件".format(self.stock)
# 请在此处添加DiscountedProduct类的代码


class DiscountedProduct(Product):
    def __init__(self, name, price, stock, discount_rate):
        super().__init__(name, price, stock)
        self.discount_rate = discount_rate

    def get_info(self):
        return "商品名称:{},价格:{}元,库存:{}件,折扣:{}%".format(self.name, self.price, self.stock, self.discount_rate)

    def get_discounted_price(self):
        return self.price * self.discount_rate / 100


# 示例代码
if __name__ == "__main__":
    # 创建商品实例
    product1 = Product("普通商品A", 100, 50)
    discounted_product1 = DiscountedProduct("特价商品B", 200, 30, 15)

    # 展示商品信息
    print(product1.get_info())
    print(discounted_product1.get_info())
    print("特价商品折扣后价格:{}元".format(discounted_product1.get_discounted_price()))

    # 更新库存
    product1.update_stock(-10)
    discounted_product1.update_stock(5)