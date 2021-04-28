'''
filter_items = lambda a : a[0] == 'b'

fruits = ["apple", "banana", "pear", "orange"]
result = filter(filter_items, fruits)
print(list(result))
'''

'''
Given a list of integers, return the even integers in the list.

input = [11, 4, 5, 8, 9, 2, 12]
output = [4, 8, 2, 12]

input = [3, 5, 7]
output = []
'''

# even_integers = lambda a : a / 2 == 0
even_integers = lambda a : a % 2 == 0

input = [11, 4, 5, 8, 9, 2, 12]
result = filter(even_integers, input)
print(list(result))

input = [3, 5, 7]
result = filter(even_integers, input)
print(list(result))