

class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def add_item(self, item_):
        if self.free_area >= item.area:
            self.free_area -= item.area
            self.item_list.append(item_.__str__())

    def __str__(self):
        return f"户型：{self.house_type}\n总面积：{self.area}[剩余面积：{self.free_area}]\n家具：{self.item_list}"


class Furniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f"[{self.name}]占地：{self.area}"


if __name__ == "__main__":
    house_1 = House("独门独栋", 400)
    furniture_1 = Furniture("bed", 4.00)
    furniture_2 = Furniture("table", 1.50)
    furniture_3 = Furniture("wardrobe", 2.00)
    for item in (furniture_1, furniture_2, furniture_3):
        house_1.add_item(item)
    print(house_1)
    print(furniture_1)
    print(furniture_2)
    print(furniture_3)
