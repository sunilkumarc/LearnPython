# Numbers
#   - Addition
#   - Subtraction
#   - Multiplication
#   - Division (diff between python2 and python 3)
#   - Modulo
#   - Parantheses for precedence
#   - storing in variables and using in calculation
#   - math library
#     - pow
#     - ceil
#     - floor

# Strings
#   - sequence of characters
#   - indexing
#   - slicing
#   - concatenation
#   - searching in strings
#     - if char in string
#   - get first char in string
#   - get last char in string
#   - casting
#     - string to int
#     - int to string

# Lists

s = 'hello world'
search_string = 'hell-'

if search_string in s:
    print(search_string + " is present in " + s)
else:
    print(search_string + " is not present in " + s)

a = [1, 2, 'hello world']
b = [4, 5]
c = a + b
print(c)
if 8 in c:
    print(str(8) + " is present in " + str(c))
else:
    print(str(8) + " is not present in " + str(c))

# Command button + forward slash -> for multi line comments

# string -> int
# int -> string
# int -> float
# float -> int

a = b + c

a = input("Enter a number: ")
print("User entered: ", a)

# Calcutor program
    # - two input from the User
    # - do muliple operaions and store in different variables and print the result
    #     - add
    #     - subtraction
    #     - muliplication
    #     - Division
    #     - modulo
    # - print the results