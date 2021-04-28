# 1, 2, 10, 15, 3

# Arbiary number of arguments
# anything -> can be any variable name
def add_number(*anything):
    # up to us to use this tuple in any way we want
    # (1, 2, 3, 4, 10)

    # Initialise result to 0
    result = 0
    # --------------------
    # result = 0 + 1 = 1
    # result = 1 + 2 = 3
    # result = 3 + 3 = 6
    # result = 6 + 4 = 10
    # result = 10 + 10 = 20
    for x in anything:
        result = result + x
        print("Result: ", result)
    # --------------------
    return result
    
res = add_number(1, 2, 3, 4, 10)
print("Result: ", res)