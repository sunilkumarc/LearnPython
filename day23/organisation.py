'''
Let's say we're building an application for a specific company.
Company name remains same for all the employees.

Real World Entities:
Organisation
Employees
'''

class Organisation:
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def add_employee(self, emp):
        self.employees.append(emp)
    
class Employee:
    organisation = 'Google'

    def __init__(self, name, salary, emp_id):
        self.name = name
        self.salary = salary
        self.emp_id = emp_id
    
    def update_salary(self, new_salary):
        self.salary = new_salary

    def display(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)
        print("Emp Id: ", self.emp_id)
        print("Company: ", self.organisation)
        print('------------------')

e1 = Employee("Sunil", 100, 1)
e2 = Employee("Kumar", 200, 2)

org = Organisation("Google")
org.add_employee(e1)
org.add_employee(e2)

e1.display()
e2.display()