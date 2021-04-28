'''
Scope of a variable:
    - a scope of a variables basically means the parts 
    of the code where the variable is accessible
'''

def test():
    '''
    variable a defined here has 'local' scope. it is available only inside test function.
    '''
    a = 10
    print(a)

'''
a is not available outside of test function
'''
print(a) # Error
test()