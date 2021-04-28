# def add(one, two):
#     result = one + two
#     return result

# result = add(1, 2)
# print(result)

'''
Company Application
- Managers

- Employees
    - Name
    - ID
    - Salary
    - Desk No

- Computers
    - Desktop
    - Laptop

- Rooms
    - Meeting Rooms
    - Conference Rooms
'''

'''
Functional Programming -> Everything is done using functions / methods
Requirements:
    - create a employee
    - change an employee's salary
    - give a computer an an employee
'''

def create_employee(name, salary, desk_no, id):
    employee = {
        "id": id,
        "name": name,
        "salary": salary,
        "desk_no": desk_no
    }
    return employee

emp1 = create_employee("Sunil Kumar", 100.0, "1A", 1)
emp2 = create_employee("Lalilashka", 200.0, "2A", 2)

def update_employee_salary(emp, new_salary):
    emp["salary"] = new_salary
    return emp

emp1 = update_employee_salary(emp1, 150.0)

car = {"name": "Mercedes"}
new_car = update_employee_salary(car, 100)
print(new_car)

def create_computer(name, memory, type, color):
    computer = {
        "name": name,
        "memory": memory,
        "type": type,
        "color": color
    }
    return computer

computer1 = create_computer("Macbook", "100 GB", "Laptop", "White")
computer2 = create_computer("LG", "50 GB", "Desktop", "Black")

'''
In [1]: emp = {"name": "sunil"}

In [2]: computer = {"name": "Macbook"}

In [3]: emp
Out[3]: {'name': 'sunil'}

In [4]: computer
Out[4]: {'name': 'Macbook'}

In [5]: emp["comp"] = computer

In [6]: emp
Out[6]: {'comp': {'name': 'Macbook'}, 'name': 'sunil'}

Current: {'id': 1, 'name': 'Sunil Kumar', 'salary': 150.0, 'desk_no': '1A'}

Result: {
    'id': 1, 
    'name': 'Sunil Kumar', 
    'salary': 150.0, 
    'desk_no': '1A',
    'computer': {
        'name': 'Macbook',
        ...
    }
}
'''
def give_laptop_to_employee(employee, computer):
    employee["computer"] = computer
    return employee

emp1 = give_laptop_to_employee(emp1, computer1)
emp2 = give_laptop_to_employee(emp2, computer2)

'''
So far...

We have created functions to
1. create employees
2. update employees with new salary
3. assign a computer to an employee
'''