"""
            多态与继承的练习
"""
# 任务一：手雷炸了，伤害玩家/敌人/房屋......


class Bomb:
    def explode(self, things):
        if not isinstance(things, Object):
            raise TypeError('things must be an instance of Object')
        print('炸了')
        things.get_hurt()


class Object:
    def get_hurt(self):
        raise NotImplementedError('get_hurt is not implemented')


class Player(Object):
    def get_hurt(self):
        print('玩家受伤')


class Enemy(Object):
    def get_hurt(self):
        print('敌人受伤')


class Buildings(Object):
    def get_hurt(self):
        print('房屋受损')


bomb_01 = Bomb()
p_01 = Player()
b_01 = Buildings()
bomb_01.explode(p_01)
bomb_01.explode(b_01)