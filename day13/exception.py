'''
TypeError: unsupported operand type(s) for +: 'int' and 'str'
2. Logical error
    Logical errors are generally called as 'Exception'.

We should always handle logical errors in our code through exception handling.
'''

def add(num1, num2):
    result = num1 + num2
    return result

# print("Program started...")
# add(1, "100")
# print("Program exiting...")
'''
In the above code the program encounters a logical error at line number 14.
So the program stop execution once this error occurs.

Generally in our code we want to handle such cases and do something else.
This is called 'catching an exception'.
'''

num1 = input()
num2 = input()

# print("Program started...")
# Syntax is similar to if - else statements
# try:
#     # try block
    

#     res = add(num1, num2)
#     print(res)
# except: # except is a short form for exception
#     # exception block
#     print("Exception occurred")


# if condition:
#     alksdfjlka
#     aslkdfajsdlkf
# else:
#     alskdfjas
#     askldfjaslkf