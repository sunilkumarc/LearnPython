class FruitsShop:
    def __init__(self, fruits):
        # fruits is a list here.
        # basically we can keep any data type as class attributes
        self.fruits = fruits
    
    # after self there is nothing. so this method doesn't take any arguments / parameters
    def getFruits(self):
        print(self.fruits)

'''
When we call FruitsShop() method using the class name, that's when __init__ method (constructor) is called.
So __init__ is a special method used to create objects of a class.
'''
f = ['apple', 'banana', 'orange']
shop = FruitsShop(f)
shop.getFruits()