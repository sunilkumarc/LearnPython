# List Comprehension
# A shortcut / way to access or filter elements in a list

'''
Problem:
Given a list l, find all the items within the list which has character 'o' in them
result = ['mango', 'oranges']
'''

l = ['apple', 'banana', 'kiwi', 'mango', 'oranges']
print('Normal way:')
result = []
for i in l:
    if 'o' in i:
        result.append(i)

print(result)

print()

print('List Comprehension way:')
result2 = [i for i in l if 'o' in i]
print(result2)

'''
Syntax of List Comprehension
newlist = [item for item in any_list if condition]
3 Parts:
    - each 'item' which should be added to the newList
    - for loop
    - condition
'''