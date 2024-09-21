"""
    类变量的练习
"""


class Person:
    total_person = 0

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        Person.total_person += 1

    @classmethod
    def get_total_person(cls):
        print(Person.total_person)


per_01 = Person('jack', 'male', 22)
per_02 = Person('sack', 'female', 21)
per_03 = Person('bak', 'male', 12)
Person.get_total_person()
