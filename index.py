# OOP review for python
class Employee:

    raise_amt = 1.2
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@company.com'
        
        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_rasie(self):
        self.pay = int(self.pay) * Employee.raise_amt
    
    @classmethod
    def set_raise_amt(cls, amount): # I don't think it is good practice!!
        cls.raise_amt = amount
    
    @classmethod
    def parse_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod # no ops on instance or class
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

import datetime
my_day = datetime.date(2025, 12, 15)
print(Employee.is_workday(my_day))

# emp_1 = Employee('Judy', 'Fox', 300000)
# emp_2 = Employee('San', 'Diego', 250000)

# emp_str_3 = 'Julia-Moore-15000'
# emp_3 = Employee.parse_str(emp_str_3).fullname()
# print(emp_3)

# Employee.set_raise_amt(1.5) # equal to Employee.raise_amount = 1.5
# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

# emp_1.set_raise_amt(1.55) # !! instance impacted class
# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

# print('emp_1 first name', emp_1.first)
# print('emp_2 email', emp_2.email)
# print('number of total employees:', Employee.num_of_employees)
# print('emp_1 full name:', emp_1.fullname())

# print(Employee.__dict__)
# print(emp_1.__dict__)

# print('emp_1 pay before raise', emp_1.pay)
# emp_1.apply_rasie()
# print('emp_1 pay after raise', emp_1.pay)

