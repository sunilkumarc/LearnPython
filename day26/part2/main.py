import calculator # We are importing calculator.py as a module here. We skip .py form the filename
import student

result = calculator.add(2, 4)
print(result)

result = calculator.multiply(2, 4)
print(result)

s1 = student.Student("Lily", 20) # package / module name DOT method / class name
# result = add(2, 4) This throws an error. Because add is searched for in the same file
c1 = student.Classroom("Class X")

student.print_all(s1, c1)

print(student.SCHOOL_NAME)
