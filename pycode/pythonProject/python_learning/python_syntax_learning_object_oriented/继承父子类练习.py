"""
            父类与子类
"""


class Animal:
    def run(self):
        print('run')

    def eat(self):
        print('eat')


class Dog(Animal):
    def guide_people(self):
        print('guide people')


class Bird(Animal):
    def fly(self):
        print('fly')


dg_01 = Dog()
br_01 = Bird()
animal_01 = Animal()
print(isinstance(dg_01, Animal))
print(isinstance(dg_01, Bird))
print(issubclass(Dog, Animal))
print(issubclass(Dog, Bird))


class Car:
    def __init__(self, speed, brand):
        self.speed = speed
        self.brand = brand


class ElectricCar(Car):
    def __init__(self, speed, brand, battery_capacity, charge_efficiency):
        super().__init__(speed, brand)
        self.battery_capacity = battery_capacity
        self.charge_efficiency = charge_efficiency


electric_car_01 = ElectricCar(10, '雪弗莱', 3800, 50000)
print(electric_car_01.brand)
