# addTwo = lambda a : a + 2
# addThree = lambda a : a + 3
# addFour = lambda a : a + 4

# addTwo(10) # 12
# addTwo(12) # 14 

# Replace above 3 anonymous functions with just one function

def add_function(n):
    # anonymous_func = lambda a : a + n
    # return anonymous_func
    return lambda a : a + n

add_two = add_function(2)
'''
add_two = lambda a : a + 2
'''
print(add_two(10)) # 12

add_five = add_function(5)
'''
add_five = lambda a : a + 5
'''
print(add_five(10))
print(add_five(20))

add_ten = add_function(10)
print(add_ten(10)) # 20
print(add_ten(100)) # 110

add_hundred = add_function(100)
print(add_hundred(10))
print(add_hundred(100))

