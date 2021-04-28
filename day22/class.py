# Blueprint for creating employees
class Employee:
    def __init__(self, name, salary, desk_no, id):
        # attributes are accessing using self keyword inside the class
        self.name = name
        self.salary = salary
        self.desk_no = desk_no
        self.id = id
        self.company = 'Google'

        # result here is just a local variable. it is not a property of Employee class
        # so result cannot be used in other methods of the class like change_salary and change_desk
        result = 10
    
    def change_salary(self, new_salary):
        self.salary = new_salary
    
    def change_desk(self, new_desk):
        self.desk_no = new_desk

'''
class -> keyword (just like def)
Employee -> we're creating employee class here
__init__, change_salary and change_desk are the methods that are available on Employee class

__init__ -> (constructor) is a special method in each class
self.name, self.salary, self.desk_no, self.id -> are attributes(properties) of Employee class
'''

# How do we create an employee using Employee class?
emp1 = Employee("Sunil", 100.0, "1A", 1) # this is how we create an employee

# Lets create another employee
emp2 = Employee("Lililashka", 200.0, "2A", 2)

# In line number 25 and 26 we are creating employee objects using Employee class
# This is called 'instantiating an object'.
# Now emp1 and emp2 are called objects of Employee class
'''
OOP keywords:
- class
- class attributes / class properties
- object
- instantiating an object
'''
print(emp1, type(emp1))
'''
<__main__.Employee object at 0x1016cae48> <class '__main__.Employee'>

A class is a type similar to int, string etc.
'''

'''
self.name = name
self.salary = salary
self.desk_no = desk_no
self.id = id
'''
print(emp1.name)
print(emp1.salary)
print(emp1.desk_no)
print(emp1.id)
# print(emp1.result) this will result in error
'''
error is:

AttributeError: 'Employee' object has no attribute 'result'
'''
print(emp1.company)

# emp2 is another object we have created. Let's print all the attributes of this object
print(emp2.name)
print(emp2.salary)
print(emp2.desk_no)
print(emp2.id)
print(emp2.company)


emp3 = Employee("Bill Gates", 300.0, "3A", 3)
print(emp3.company)

emp1.change_salary(500)
print("emp1 salary: ", emp1.salary)
print("emp2 salary: ", emp2.salary)
print("emp3 salary: ", emp3.salary)
'''
emp1 salary: 500
emp2 salary: 200
emp3 salary: 300
'''

emp3.change_salary(1000)
print("emp1 salary: ", emp1.salary)
print("emp2 salary: ", emp2.salary)
print("emp3 salary: ", emp3.salary)

# Change the emp3's desk to '5B'
emp3.change_desk('5B')
print(emp3.desk_no)