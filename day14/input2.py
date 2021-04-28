print("Program started...")

a = input("Enter first number: ")
print("First number:", a, type(a))

b = input("Enter second number: ")
print("Second number:", b, type(b))

result = a + b
'''
Output is 1020 because the input take using input() 
method always comes as a string

In [1]: "10" + "20"
Out[1]: '1020'

In the above example it is doing string concatenation
'''
print("Result:", result, type(result))

'''
If we want integer addition, we should convert string to integer 
before doing the add operation
'''
a_new = int(a) # converting string a to integer a
b_new = int(b) # converting string b to integer b

result_new = a_new + b_new
print("New result:", result_new)