'''
there are 2 variables defined here.
a with local scope
a with global scope
'''
a = 10 # global vairable

def test():
    a = 5
    '''
    Local variable a defined here overrides the global variable a.
    So when we access a, local a is used, not the global a.
    '''
    print(a)

print(a)
test()
'''
10
5
'''