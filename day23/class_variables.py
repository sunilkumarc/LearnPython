class Person:
    species = 'Human'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def func1(self):
        pass
    
    def func2(self):
        pass

p1 = Person("Sunil", 20, "Male")
p2 = Person("Lililashka", 20, "Female")
p3 = Person("Elon Musk", 40, "Male")

'''
Person -> is a class (like a blue print)
Using the blueprint we can create multiple objects of type Person

p1 and p2 -> objects / instances of class Person

The process of creating an object from a class is called 'Instantiation'.
name, age and gender -> are called 'instance variables' / attributes.

Class Variables:
Any property who's value doesn't change for every object created is defined as 
a class variable.

In the above example all the person objects created will always belong to 'Human' species.
So species is defined as a Class Variable.
'''