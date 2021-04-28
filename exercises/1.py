'''
Let's build a school program

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name(self):
        return self.name

    def subjects_list(self):
        pass

class Student(Person):
    def __init__(self, name, age, subjects):
        super().__init__(name, age)
        self.subjects = subjects # ["maths", "science"]

    def get_subjects_enrolled_in(self):
        return self.subjects
    
    def enroll_in_subject(self, subject):
        self.subjects.append(subject)
        return subject

    def level(self):
        if self.age <= 12:
            return "elementary level"
        if self.age > 12:
            return "high school level"

s1 = Student("sunil", 10, ["Maths", "Science"])
new_subject = s1.enroll_in_subject("History")

if new_subject == "maths":
    # do some logic
else:
    # do something else

subjects = s1.get_subjects_enrolled_in()

l = s1.level()

if l == 'elementary level':
    print("The student is still in elementary level")
else:
    print("The student is in high school level")

