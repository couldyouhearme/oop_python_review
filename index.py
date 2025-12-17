# OOP review for python
class Employee:

    raise_amt = 1.2
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = self.first + '.' + self.last + '@company.com' # static at init
        
        Employee.num_of_employees += 1

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last 

    @fullname.deleter
    def fullname(self):
        print('Delete name!!!')
        self.first = None
        self.last = None
    
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    def apply_rasie(self):
        self.pay = int(self.pay) * self.raise_amt # diff: Employee.raise_amt
    
    # special methods
    # refer to class date source code
    def __repr__(self): # conversions to str
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self): # str format
        return '{} - {}'.format(self.fullname, self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname)

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

class Developer(Employee):
    raise_amt = 2.0
    
    def __init__(self, first, last, pay, lang):
        super().__init__(first, last, pay)
        self.lang = lang

# inherit
# print(help(Developer))

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('***', emp.fullname, '***')

# lib
class HTTPException(Exception):
    pass

class BadRequest(HTTPException):
    pass

# setter; deleter
# user_1 = Employee('Tom', 'Cat', 100)
# user_1.fullname = 'Jerry Mounse'
# print(user_1) # Jerry Mounse - Jerry.Mounse@company.com
# del user_1.fullname # Delete name!!!
# print(user_1) # None None - None.None@company.com

# @property
# user_1 = Employee('Tom', 'Cat', 100)
# print(user_1.email()) # TypeError with @property
# print(user_1.email) # Tom.Cat@company.com 
# print(user_1.fullname) # Tom Cat

# __len__ special method
# print(len('test')) # 4
# print('test'.__len__()) # 4
# emp_1 = Employee('Judy', 'Fox', 300000)
# print(len(emp_1)) # 8; space between first and last!

# __add__ special method
# emp_1 = Employee('Judy', 'Fox', 300000)
# emp_2 = Employee('San', 'Diego', 250000)
# print(emp_1 + emp_2) # 550000

# print(1+2) # 3
# print(int.__add__(1, 2)) # 3
# print(str.__add__('a', 'b')) # 'ab'

# __repr__ special method; comment out __str__
# dev_2 = Employee('Soy', 'Milk', 50000)
# print(dev_2) # Employee('Soy', 'Milk', '50000')

#  __repr__; __str__; with both special methods
# print(dev_2) # Soy Milk - Soy.Milk@company.com
# print(dev_2.__repr__()) # Employee('Soy', 'Milk', '50000')
# print(dev_2.__str__()) # Soy Milk - Soy.Milk@company.com
# print(repr(dev_2)) # Employee('Soy', 'Milk', '50000')
# print(str(dev_2)) # Soy Milk - Soy.Milk@company.com



# dev_1 = Developer('Coco', 'Nut', 60000, 'Python')
# dev_2 = Employee('Soy', 'Milk', 50000)
# mgr_1 = Manager('Tofo', 'Soup', 30000, [dev_1])

# print(isinstance(mgr_1, Manager)) 
# print(isinstance(mgr_1, Employee))
# print(isinstance(mgr_1, Developer))

# print(issubclass(Developer, Employee))
# print(issubclass(Developer, Manager))

# print(dev_1.email)
# print(dev_1.lang)

# print(mgr_1.email)
# mgr_1.print_emps()
# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()


# print(dev_1.pay) # 5000
# dev_1.apply_rasie()
# print(dev_1.pay) # 100000.0

# print(dev_2.pay) # 5000
# dev_2.apply_rasie()
# print(dev_2.pay) # 60000.0

# import datetime
# my_day = datetime.date(2025, 12, 15)
# print(Employee.is_workday(my_day))

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

