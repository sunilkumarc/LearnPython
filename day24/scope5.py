'''
How do we update the value of a global variable inside a function?
'''

a = 10

def test():
    global a # this makes using global a instead of creating a local variable a.
    # update global a = 20
    a = 20

test()
print(a)