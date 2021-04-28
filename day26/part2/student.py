class Student: # student.Student
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Name: {}, Age: {}".format(self.name, self.age))
    
class Classroom: # student.Classroom
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print("Classroom name: {}".format(self.name))
    
def print_all(stu1, cla1): # student.print_all
    stu1.display()
    cla1.display()

SCHOOL_NAME = "Oxford"