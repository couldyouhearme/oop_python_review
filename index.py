# OOP review for python
class Employee:

    raise_amount = 1.2
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
        self.pay = int(self.pay) * Employee.raise_amount
    

emp_1 = Employee('Judy', 'Fox', 300000)
emp_2 = Employee('San', 'Diego', 250000)

# print('emp_1 first name', emp_1.first)
# print('emp_2 email', emp_2.email)
# print('number of total employees:', Employee.num_of_employees)
# print('emp_1 full name:', emp_1.fullname())

# print(Employee.__dict__)
# print(emp_1.__dict__)

# print('emp_1 pay before raise', emp_1.pay)
# emp_1.apply_rasie()
# print('emp_1 pay after raise', emp_1.pay)

