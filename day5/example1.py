# add_two_numbers -> function name
# a, b -> paramters
# returning the result stored in variable res
# empty space before any python statement is called indentation

# def multiply_three_numbers(a, b, c):
#     res = a * b * c
#     return res

# this is how we define a fucntion
def add_two_numbers(a, b):
    res = a + b
    print("Printing res inside function:",res)
    return res

# this is how we call a function
result = add_two_numbers(10, 20)
print("Print result outside function:",result)