'''
sunil = {
    "name": "Sunil",
    "age": 28,
    "country": "India"
}

lili = {
    "name": "Lili",
    "age": 20,
    "country": "Germany"
}

students = [sunil, lili]

Import sunil variable from student.py and print all the attributes.

Hello: {'name': 'Sunil', 'age': 28, 'country': 'India'}
Hello: {'name': 'Sunil', 'age': 28, 'country': 'India'}
'''

# import student

# print(student.sunil)

from student import sunil, students
# print(sunil)

for s in students:
    print(s)