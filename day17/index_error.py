'''
There's a list of elements: 10, 20, 30, 40, 50

Take the index input from the user and print the corresponding 
element from the list defined.

For Ex: 2
Output: 30

For Ex: 4
Output: 50
'''

# GENERIC WAY OF HANDLING ALL THE EXCEPTIONS

l = [10, 20, 30, 40, 50]
print(l)

a = input("Enter an index: ")

try:
    a_new = int(a) # int('4a') -> ValueError
    print(l[a_new]) # l[5] -> IndexError

    val = 10/0
except ValueError as e:
    print("Value Error Occurred::Handling value error separately")
# except IndexError as e:
#     print("Index Error Occurred")
# except ZeroDivisionError as e:
#     print("Sunil::Zero division error occurred")
except Exception as e: # Generic way of handling exception
    print("Some exception occurred: ", e)

# 'Exception as e' -> All the exception that can occuer in try block would be handled here.