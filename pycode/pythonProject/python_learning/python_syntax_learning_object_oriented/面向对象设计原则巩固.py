"""
                包含封装，继承，多态
"""
# 练习一：定义图形管理器，提供面积计算方法，具体类型包含圆，矩形等，要求满足设计三原则


class ShapeManager:
    def __init__(self):
        self.__shapes_list = []

    def calculate_total_area(self):
        value_total_area = ''
        for item in self.__shapes_list:
            area = item.calculate_area()
            value_total_area += area + '+'
        print(value_total_area[0:len(value_total_area)-1])

    def add_shape(self, shape_object):
        if not isinstance(shape_object, Shape):
            raise TypeError('shape_object type must be ShapeManager')
        self.__shapes_list.append(shape_object)


class Shape:
    shape_manager = ShapeManager()

    def calculate_area(self):
        raise NotImplementedError('calculate_area is not implemented')


class RoundedShape(Shape):
    def __init__(self, radius):
        self.radius = radius
        Shape.shape_manager.add_shape(self)

    def calculate_area(self):
        return f'{self.radius**2}*pi'


class RectangleShape(Shape):
    def __init__(self, width,length ):
        self.width = width
        self.length = length
        Shape.shape_manager.add_shape(self)

    def calculate_area(self):
        return f'{self.width * self.length}'


round_1 = RoundedShape(10)
rectangle_1 = RectangleShape(5, 6)
round_1.shape_manager.calculate_total_area()
