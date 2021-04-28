'''
Inheritance:

Father -> John
Me -> Sunil

John (1 house, 1m$ of cash)

Whatever belong to my father, belong to their children as well.


Vehicle
    properties:
        - name
        - cost
        - speed
        - ac_enabled

    behaviours:
        - start()
        - apply_brakes()
        - press_accelerator()

Car
Bicycle
.... n number of vehicles
'''
class Vehicle:
    def __init__(self, name, cost, speed):
        self.name = name
        self.cost = cost
        self.speed = speed
    
    def display(self):
        print('--------------------')
        print("Name: ", self.name)
        print("Cost: ", self.cost)
        print("Speed: ", self.speed)
        print('--------------------')
    
    def displaySpeed(self):
        print("Vehicle speed: ", self.speed)

# v1 = Vehicle("Tesla", 100, "100 MPH")
# v1.display()

# Car class is inheriting from Vehicle class
class Car(Vehicle):
    def press_accelerator(self):
        print("Pressed accelerator for car ", self.name)
    
    def displaySpeed(self, test):
        print("Overriding displayspeed method inside car.")


c = Car("Tesla", "100 $", "100 MPH")
c.display()
c.displaySpeed()
c.displaySpeed("asfklsaj")
c.press_accelerator()

'''
Car is inheriting from Vehicle class. This process / concept is called Inheritance -> Car(Vehicle)
Vehicle -> Parent Class
Car -> Child Class

During inheritance all the properties and methods will be inherited to the children class
'''

class BiCycle(Vehicle):
    def press_pedal(self):
        print("Pressing pedal for bicycle ", self.name)

b1 = BiCycle("Hercules", "10$", "10 MPH")
b1.display()
b1.press_pedal()
'''
Parent Class -> Vehicle
Child Class -> BiCycle
'''