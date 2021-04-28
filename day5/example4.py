# write a function which takes two parameters a and b
# and returns the remainder and quotient
# 10, 4

# Quotient -> 2
# Remainder -> 1
# 15, 2
# Quotient -> 7
# Remainder -> 1

# Returning multiple values from a function
def divide(a, b):
    remainder = a % b # 1
    quotient = a // b # 7
    return remainder, quotient

result1, result2 = divide(15, 2)
print("Result1:", result1)
print("Result2:", result2)