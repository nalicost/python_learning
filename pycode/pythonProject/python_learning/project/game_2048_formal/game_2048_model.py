"""
                    2048数据模型层
"""


class DirectionModel:
    """
            方向模型
    """
    Up = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class LocationModel:
    """
            位置模型
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
