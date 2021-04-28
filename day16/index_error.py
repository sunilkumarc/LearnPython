'''
There's a list of elements: 10, 20, 30, 40, 50

Take the index input from the user and print the corresponding 
element from the list defined.

For Ex: 2
Output: 30

For Ex: 4
Output: 50
'''

l = [10, 20, 30, 40, 50]
print(l)

a = input("Enter an index: ")

try:
    a_new = int(a) # int('4a') -> ValueError
    print(l[a_new]) # l[5] -> IndexError
except ValueError as e:
    print("Value Error Occurred")
except IndexError as e:
    print("Index Error Occurred")


