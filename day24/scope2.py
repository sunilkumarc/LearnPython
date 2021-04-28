def test():
    '''
    a has local scope within test fucntion
    so a is available insde test2 function as well since test2 is defined inside test function.
    '''
    a = 10 # local variable
    
    def test2():
        print(a)
    
    test2()

# print(a) Error here. a is not available here.
test()