'''
1. create employees
2. update employees with new salary
3. assign a computer to an employee
'''

'''
Object Oriented Programming:
============================
- Python is a OOP language

C, C++, Java, JavaScript, Python

OOP: Python, Java, C++
Functional/Procedural: C, Scala
'''

'''
Instead of using functions we will use classes in OOP.

What is a class?
    A class is a blueprint for an actual entity in the real world.

Example: Let's say we have an employee
Employee:
    (properties)
    - name: "Sunil"
    - salary: 100.0
    - desk_no: "1A"
    - id: 1

    (functions to update employee)
    - change employee salary
    - change employee desk

Car:
    - brand: "Mercedes"
    - color: "grey"
    - ground_clearance: 5ft

Instead of representing them as dictionaries we use classes to represent real world entities
'''

# Blueprint for creating employees
class Employee:
    def __init__(self, name, salary, desk_no, id):
        self.name = name
        self.salary = salary
        self.desk_no = desk_no
        self.id = id
    
    def change_salary(self, new_salary):
        self.salary = new_salary
    
    def change_desk(self, new_desk):
        self.desk_no = new_desk
'''
class definition
    a function defition

We combine properties and functions to update those properties inside a single entity class
'''

'''
class Person:
    def __init__(self, name, age, gender):
        pass
    
    def walk(self, steps):
        print("Person walked " + steps + " steps")
    
    def run(self, speed):
        print("Person is running at speed" + speed)
        

self argument shoudl be passed as the first argument for every function that is 
definted within a class in Python.

__init__ -> method is called 'constructor'
constructor is basically a method which is called when an object is created.
basically 'constructor' is just a fancy name for a special method
'''