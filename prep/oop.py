class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def getDetails(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name
        }

class Student(Person):
    def __init__(self, first_name, last_name, school):
        super().__init__(first_name, last_name)
        self.school = school
    
    def getStudentDetails(self):
        details = super().getDetails()
        details["school"] = self.school
        return details
    
s1 = Student("Sunil", "Kumar", "Lions")
print(s1.getStudentDetails())