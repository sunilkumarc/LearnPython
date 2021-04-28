'''
Given a list of items return the items as a list which starts with character 'b'.

fruits = ["apple", "banana", "pear", "orange"]
result = ["banana"]

colors = ["black", "red", "orange", "blue", "yello"]
result = ["black", "blue"]
'''

filter_items = lambda a : a[0] == 'b'

fruits = ["apple", "banana", "pear", "orange"]
result = filter(filter_items, fruits)
print(list(result))

colors = ["black", "red", "orange", "blue", "yello"]
result = filter(filter_items, colors)
print(list(result))