"""
        购物车
        开发计划：1、货物数据模型
                    （1）货品数据：（名称，数量，价格，编号）
                2、购买逻辑控制
                    （1）数据：所有货品
                    （2）行为：购买减少货物数量，计算价格，退货增加货物数量，返回金额，金额结算
                3、界面视图
                    （1）行为：选择功能，录入购买编号，录入退货编号，打印商品信息，按要求排序商品并打印商品信息
                注：货品数据单不得在外直接改动，各个数据录入要规定格式
"""


class BuyController:
    """
            购买退货等逻辑判断
    """
    __goods_list = []
    # 存放所有货品
    goods_id = 0
    # 赋予物品id

    def __init__(self):
        # 每次运行创建一次，购买清单
        self.__goods_list_buy = []

    @property
    def goods_list(self):
        """
                返回商品列表（只读）
        :return: 商品列表
        """
        return self.__goods_list

    @property
    def goods_list_buy(self):
        """
                返回购买列表（只读）
        :return: 购买列表
        """
        return self.__goods_list_buy

    @classmethod
    def goods_list_add(cls, value):
        """
                增加货品列表
        :param value: 货品对象
        """
        BuyController.__get_goods_id(value)
        cls.__goods_list.append(value)

    @staticmethod
    def __get_goods_id(value):
        """
                商品编号自动生成
        :param value: 需要赋值编号的商品对象
        """
        BuyController.goods_id += 1
        value.id = BuyController.goods_id

    def goods_list_buy_add(self, goods_id, num):
        """
                增加购买清单
        :param goods_id: 购买的货物id
        :param num: 数量
        :return: bool
        """
        if BuyController.__is_goods_exist(goods_id, num):
            # 保证货品是存在与商品列表的
            BuyController.__goods_list_output(goods_id, num)
            # 调用出货方法
            if self.__is_goods_exist_buy(goods_id):
                # 判断货品是否已存在于购买清单中
                self.__index_goods(goods_id).num += num
                # 存在，直接加数量
            else:
                name = BuyController.__goods_list[goods_id - 1].name
                price = BuyController.__goods_list[goods_id - 1].price
                goods_item = Goods(name, num, price)
                goods_item.id = BuyController.__goods_list[goods_id - 1].id
                self.__goods_list_buy.append(goods_item)
                # 不存在生成
            return True
        return False

    @classmethod
    def __goods_list_output(cls, good_id, num):
        """
                出货方法
        :param good_id: 出货的物品id
        :param num: 出货的数量
        """
        cls.__goods_list[good_id - 1].num -= num

    @classmethod
    def __is_goods_exist(cls, good_id, num=0):
        """
                货品是否存在判断
        :param good_id: 物品id
        :param num: 数量
        :return: bool
        """
        if 0 < good_id <= cls.__goods_list[-1].id:
            return cls.__goods_list[good_id - 1].num - num >= 0
            # 拿出数量后数量大于等于0，说明可以拿的出
        else:
            return False

    def __is_goods_exist_buy(self, goods_id, num=0):
        """
                物品是否存在于购买清单中
        :param goods_id: 货品id
        :param num: 数量
        :return: bool
        """
        item_shopping = self.__index_goods(goods_id)
        if item_shopping:
            return item_shopping.num - num >= 0
        return False

    def __index_goods(self, goods_id):
        """
                找到购买清单中的货品位置
        :param goods_id: 货物id
        :return: 货品对象
        """
        for item_index in range(len(self.__goods_list_buy)):
            # 遍历找
            if self.__goods_list_buy[item_index].name == BuyController.__goods_list[goods_id - 1].name:
                return self.__goods_list_buy[item_index]

    def back_goods(self, goods_id, num):
        """
                退货方法
        :param goods_id: 货品id
        :param num: 数量
        :return: bool
        """
        if BuyController.__is_goods_exist(goods_id) and self.__is_goods_exist_buy(goods_id, num):
            # 判断是否在两个列表中都存在
            self.__index_goods(goods_id).num -= num
            BuyController.__goods_input(goods_id, num)
            # 调用入货函数
            self.__clear_zero_goods()
            # 清理数量归零的货物
            return True
        return False

    def clear_buy(self):
        """
                清空购买清单
        """
        for item_back in range(len(self.__goods_list_buy) - 1, -1, -1):
            # 倒叙，不然跳
            self.back_goods(self.__goods_list_buy[item_back].id, self.__goods_list_buy[item_back].num)
            # 通过调用退货方法，退掉所有数量即可

    @classmethod
    def __goods_input(cls, goods_id, num):
        """
                入货方法
        :param goods_id: 入货id
        :param num: 数量
        """
        cls.__goods_list[goods_id - 1].num += num

    def __clear_zero_goods(self):
        """
                删除数量归零的货物
        """
        for item_clear in range(len(self.__goods_list_buy) - 1, -1, -1):
            # 倒叙删
            if self.__goods_list_buy[item_clear].num == 0:
                del self.__goods_list_buy[item_clear]

    def calculate_total_price(self):
        """
                商品总价计算
        :return: 总价
        """
        total_price = 0
        for item_price in self.__goods_list_buy:
            total_price += item_price.price * item_price.num
        return total_price

    @staticmethod
    def __money_remain(money_calculate, money_input):
        """
                剩余金额计算
        :param money_calculate: 商品总价
        :param money_input: 支付金额
        :return: 剩余金额
        """
        return money_input - money_calculate

    def back_shopping(self, money_input):
        """
                结算购买
        :param money_input: 支付金额
        :return: 剩余金额，以0，1表示bool
        """
        money_calculate = self.calculate_total_price()
        money_remain = BuyController.__money_remain(money_calculate, money_input)
        if money_remain > 0:
            return money_remain, 1
        return 0, 0

    def clear_buy_all(self):
        """
                清空购买清单
        """
        self.__goods_list_buy = []


class Goods:
    """
            货品类
    """
    max_len = 6
    # 所有货品的所有数据成员中字符长度最长的值或default值

    def __init__(self, name, num, price):
        """
                货品数据成员
        :param name: 货品名称，要求为str类型，不能为空
        :param num: 货品存量， 要求为int类型，要求大于等于0
        :param price: 货品价格， 要求为float或int类型， 要求大于0
        """
        self.id = None
        self.name = name
        self.num = num
        self.price = price
        Goods.__max_len_compare(self.name)
        Goods.__max_len_compare(self.price)

    @property
    def name(self):
        """
                货品名字（只读）
        :return: 货品名字
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
                货品名字（只写）
        :param value: 输入的名称
        """
        if isinstance(value, str):
            if value:
                self.__name = value
            else:
                raise ValueError('name must be valuable')
        else:
            raise TypeError('name must be str')

    @property
    def num(self):
        """
                货品数量（只读）
        :return: 货品数量
        """
        return self.__num

    @num.setter
    def num(self, value):
        """
                货品数量（只写）
        :param value: 输入的货品数量
        """
        if isinstance(value, int):
            if value >= 0:
                self.__num = value
            else:
                raise ValueError('num must be natural number')
        else:
            raise TypeError('num must be int')

    @property
    def price(self):
        """
                货品价格（只读）
        :return: 货品价格
        """
        return self.__price

    @price.setter
    def price(self, value):
        """
                货品价格（只写）
        :param value: 输入的货品价格
        """
        if isinstance(value, float) or isinstance(value, int):
            if value > 0:
                self.__price = value
            else:
                raise ValueError('price must be positive number')
        else:
            raise TypeError('price must be digit')

    @classmethod
    def __max_len_compare(cls, item_max):
        """
                最长字符比较，大的就放入max_len
        :param item_max: 需比较的字符串长度
        """
        if len(str(item_max)) > cls.max_len:
            cls.max_len = len(str(item_max))


class ShoppingView:
    """
            界面视图
    """
    def __init__(self):
        # 用来跨类调用方法，只生成一次
        self.__buy_controller = BuyController()

    def main(self):
        """
                主入口
        """
        choice = 1
        while choice != 0:
            # 循环，使购物在不退出情况下，可连续选购
            self.__display_menu()
            choice = input('你选择的功能是:>')
            if choice.isdigit():
                choice = self.__select_function(choice)
                choice = int(choice)
            else:
                print('请输入指定内容')

    @staticmethod
    def __display_menu():
        """
                菜单展示
        """
        print('0)退出程序（购物车有东西时不能退出）')
        print('1)打印商品列表')
        print('2）向购物车增加购买物品')
        print('3）向购物车减少购买物品')
        print('4）清空购物车')
        print('5）查看购物车')
        print('6）打印账单')

    def __select_function(self, choice):
        """
                功能判断
        :param choice: 选择的功能编号
        :return: 选择的功能编号，便于外层循环退出
        """
        if choice == '0':
            choice = self.__exit_print(choice)
        elif choice == '1':
            self.__display_goods_list(self.__buy_controller.goods_list)
        elif choice == '2':
            self.__shopping_goods()
        elif choice == '3':
            self.__cancel_shopping()
        elif choice == '4':
            self.__clear_goods()
        elif choice == '5':
            self.__display_goods_list(self.__buy_controller.goods_list_buy)
        elif choice == '6':
            self.__end_shopping()
        else:
            print('请输入指定内容')
        return choice

    def __end_shopping(self):
        """
                结束购买
        """
        total_price = self.__buy_controller.calculate_total_price()
        print('总价:', total_price)
        money_input = input('请放入钱款:>')
        if money_input.isdigit():
            money_input = float(money_input)
            result_01, result_02 = self.__buy_controller.back_shopping(money_input)
            if result_02:
                self.__display_goods_list(self.__buy_controller.goods_list_buy)
                print('总价：', total_price)
                print('退还金额：', result_01)
                print('支付成功')
                self.__buy_controller.clear_buy_all()
            else:
                print('支付失败')
        else:
            print('支付失败')

    def __clear_goods(self):
        """
                清空购物车
        """
        self.__buy_controller.clear_buy()
        print('清空成功')

    def __cancel_shopping(self):
        """
                取消购买
        """
        item_id = input('你选择退回物品编号是:>')
        item_num = input('你选择退回的数量是:>')
        item_id, item_num, judge = ShoppingView.__digit_transform(item_id, item_num)
        if judge:
            if self.__buy_controller.back_goods(item_id, item_num):
                print('退货成功')
            else:
                print('退货失败')
        else:
            print('退货失败')

    def __shopping_goods(self):
        """
                购买商品
        """
        item_id = input('你选择购买物品编号是:>')
        item_num = input('你选择购买的数量是:>')
        item_id, item_num, judge = ShoppingView.__digit_transform(item_id, item_num)
        if judge:
            result = self.__buy_controller.goods_list_buy_add(item_id, item_num)
            if result:
                print('购买成功')
            else:
                print('购买失败')
        else:
            print('购买失败')

    @staticmethod
    def __display_goods_list(target_list):
        """
                展示货品清单
        :param target_list:  展示列表
        """
        print('货号', ShoppingView.__space_calculate(len('货号')), '货名', ShoppingView.__space_calculate(len('货名')),
              '货价', ShoppingView.__space_calculate(len('货架')), '货量', sep='')
        # 按格式打印
        for item_in_list in target_list:
            id_item = item_in_list.id
            name_item = item_in_list.name
            price_item = item_in_list.price
            print(item_in_list.id, ShoppingView.__space_calculate(id_item), item_in_list.name,
                  ShoppingView.__space_calculate(name_item), item_in_list.price,
                  ShoppingView.__space_calculate(price_item),
                  item_in_list.num)
            # 按格式打印

    def __exit_print(self, choice):
        """
                退出程序
        :param choice: 选择功能
        :return: 以数字形式的bool值，-1表示false
        """
        if not self.__buy_controller.goods_list_buy:
            # 判断购物车是否清空
            print('感谢使用')
            return choice
        else:
            print('购物车未清空')
            return -1

    @staticmethod
    def __space_calculate(item_need=6):
        """
                所需空格计算
        :param item_need: 需要结算空格的
        :return: 返回字符需要的空格
        """
        max_len = 6 if 6 >= Goods.max_len else Goods.max_len if Goods.max_len >= len(str(BuyController.goods_id)) else (
            len(str(BuyController.goods_id)))
        # 调取最长字符长度
        return (max_len - len(str(item_need))) * ' '

    @staticmethod
    def __digit_transform(value_1='1', value_2='1'):
        """
                字符串转数字
        :param value_1: 字符串1
        :param value_2: 字符串2
        :return: 转化后的数字和以数字形式的bool（0， 1）
        """
        if value_1.isdigit() and value_2.isdigit():
            return int(value_1), int(value_2), 1
        return 0, 0, 0


good_list = [[1, 'iphone', 7000], [1, 'ipad', 9000], [30, 'pen', 15], [30, 'book', 20], [30, 'water', 2],
             [60, 'booklet', 4000], [10, 'reminder', 200], [80, 'rock', 5], [10, 'calculator', 200],
             [100, 'battery', 20], [3, 'tv', 3000], [2, 'bike', 700], [130, 'watch', 1500], [400, 'coco cola', 5],
             [80, 'steak', 70], [15, 'blouse', 300], [12, 'football shoes', 400], [180, 'hot dog', 7],
             [1900, 'ice cream', 1], [5, 'sun glasses', 150]]
for item in good_list:
    BuyController.goods_list_add(Goods(item[1], item[0], item[2]))
    # 输入商品列表
view = ShoppingView()
# 生成对象
view.main()
# 进入主界面
