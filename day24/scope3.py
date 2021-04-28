'''
Global Scope:
    a variable has global scope when it is available throughout the program
'''

# How can we define a global variable?
a = 10 # global variable

def test():
    print(a)

def test2():
    print(a)

print(a)
test()
test2()

'''
Output:
10
10
10

variable a (line number 7) has global scope. it is available through the program
'''