# Take three numbers as parameters and multiply all 3 of them and 
# return and print the result
# 10, 5, 2 -> 100

# default arguments/parameters in python
def multiplication(a, b, c=4):
    res = a * b * c
    return res

result = multiplication(10, 5, 10)
print(result)