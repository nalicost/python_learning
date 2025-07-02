"""
                    依赖倒置的强化
"""


class StaffManager:
    def __init__(self):
        self.__staff_list = []

    def add_staff(self, staff_info):
        if not isinstance(staff_info, Staff):
            raise TypeError('staff type must be Staff')
        self.__staff_list.append(staff_info)

    def calculate_total_salary(self):
        total_salary = 0
        for item in self.__staff_list:
            salary = item.calculate_salary()
            total_salary += salary
        print(total_salary)


class Staff:
    staff_manager = StaffManager()

    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_salary(self):
        raise NotImplementedError('calculate_salary must be implemented')


class SalesManager(Staff):
    def __init__(self, base_salary, percentage_from_sale):
        super().__init__(base_salary)
        self.percentage_from_sale = percentage_from_sale
        Staff.staff_manager.add_staff(self)

    def calculate_salary(self):
        return self.base_salary + self.percentage_from_sale


class Encoder(Staff):
    def __init__(self, base_salary, dividend):
        super().__init__(base_salary)
        self.dividend = dividend
        Staff.staff_manager.add_staff(self)

    def calculate_salary(self):
        return self.base_salary + self.dividend


en_01 = Encoder(10000, 5000)
sales_01 = SalesManager(6000, 500)
Staff.staff_manager.calculate_total_salary()
