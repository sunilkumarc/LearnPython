'''
Write a function to add 10 to the given number and return the result
'''

def addTen(n):
    result = n + 10
    return result

# print(addTen(15))

'''
Write a function to add 20 to the given number and return the result
'''
def addTwenty(n):
    result = n + 20
    return result

# print(addTwenty(10))

def addNumbers(n):
    return lambda a : a + n

'''
lambda a : a + 10
'''
addTen = addNumbers(10)

'''
lambda a : a + 20
'''
addTwenty = addNumbers(20)

print(addTen(100))
print(addTwenty(100))

'''
list = []
while some_condition:
    a = lambda b : b + 10
    list.append(a)
'''