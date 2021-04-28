'''
Shape
    property:
        - area

    method:
        - calculate_area()

- Circle
    - radius

    method:
        calculate_area():
            return (self.radius  * self.radium) * 3.14

- Square
    - side

- Rectangle
    - length
    - breadth
'''

class Shape:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color

    def change_color(self, new_color):
        self.color = new_color

    def calculate_area(self):
        pass
    
class Square(Shape):
    def __init__(self, side, color):
        '''
        super() -> returns base class
        Steps:
        1. first get super class using super() method
        2. then call init method of super class
        '''
        super().__init__(color) # call the parent class init method
        self.side = side
    
    def calculate_area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, length, breadth, color):
        super().__init__(color)
        self.l = length
        self.b = breadth
    
    def calculate_area(self):
        return self.l * self.b

class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * (self.radius ** 2)

sq1 = Square(5, "blue")
print(sq1.get_color())
sq1.change_color("red")
print(sq1.get_color())

rect1 = Rectangle(2, 4, "blue")
rect1.change_color("orange")
print(rect1.get_color())
print(rect1.calculate_area())

'''
If you'r creating a rectangle
    - length
    - breadth
    - color
'''