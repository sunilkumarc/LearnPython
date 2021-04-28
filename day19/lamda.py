'''
Anonymous functions(lambda functions) can be created using the keyword lamda.
On a high level lamda functions (anonymous functions) 

1. Write a function which adds 2 to the given number and returns the result.
'''

# def addTwo(number):
#     result = number + 2
#     return result

# print(addTwo(10))
# print(addTwo(20))
# print(addTwo(30))

# addTwo = lambda number : number + 2
'''
numbers -> argument
number + 2 -> is an expresssion (any valid python statement)
'''

# print(addTwo(10))
# print(addTwo(20))
# print(addTwo(30))

'''
Write a lambda function to multiply two numbers
'''

# multiply = lambda a, b : a * b

# print(multiply(2, 3))
# print(multiply(2, 4))

'''
Write a lambda function to return the sum of all the elements in a list
'''
# list_sum = lambda l : sum(l)
# sum -> is an inbuilt function

# print(list_sum([1,2,3]))

'''
Write a lambda function which take a number and multiplies the number with 3

4 -> 4 * 3 = 12
5 -> 5 * 3 = 12
'''

multiply = lambda a : a * 3
print(multiply(4)) # 12
print(multiply(5)) # 15
print(multiply(6)) # 18