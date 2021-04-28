a = input("Enter first number: ") # '10a'
b = input("Enter second number: ") # '20'

# Definte these two variable here itself so that line number 19 will not 
# throw an error saying variables undefined
a_new = 0
b_new = 0
try:
    # TRY BLOCK
    # Once there is an exception in any line in the TRY BLOCK, the subsequent lines inside
    # the TRY BLOCK will be skipped. The program will start running from EXCEPTION BLOCK

    # We know that these two lines can throw ValueError exception.
    a_new = float(a) # a_new = 10a
    b_new = float(b) # b_new = 20
    
    result_new = a_new + b_new
    print("New result:", result_new)
except ValueError as e:
    # EXCEPTION BLOCK
    print("Invalid inputs")


'''
ValueError: could not convert string to float: 'ab
'''

'''
1.
Take two inputs from the user.
If the inputs are valid, add them and print the result.
If the inputs the invalid, print "Invalid inputs" on the console.
'''

'''
2.
Take two inputs from the user.
If the inputs are valid, add them and print the result.
If the inputs are invalid, then print 0 as the output.
'''