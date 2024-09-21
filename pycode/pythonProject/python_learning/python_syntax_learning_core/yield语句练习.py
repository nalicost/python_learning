"""
                yield语句
"""


class GraphicManager:
    def __init__(self):
        self.__shapes_list = []

    def calculate_total_area(self):
        pass

    def add_shape(self, graphic):
        self.__shapes_list.append(graphic)

    def __iter__(self):
        num = 0
        while num < len(self.__shapes_list):
            yield self.__shapes_list[num]
            num += 1


class Graphic:
    pass


object_01 = GraphicManager()
object_01.add_shape(Graphic())
object_01.add_shape(Graphic())
object_01.add_shape(Graphic())
for item in object_01:
    print(item)
