'''
Custom Exceptions
'''

print("Program started...")

def test():
    print("test method called")
    a = 10
    print("a:", a)
    try:
        # print(b)
        a = 20
    except Exception as e:
        print("Exception:", e)
        '''
        Why do we raise an exception here?
        Ans: We should raise an exception to let the method caller know
        that there was an exception
        '''
        raise Exception("Some exception has occurred")
    return a

try:
    val = test()
    print("Value of a after test()", val)
except Exception as e:
    print("Some exception occurred when test() method was called")

print("Program exit...")

'''
Program started...
test method called
a: 10
Exception: name 'b' is not defined
Some exception occurred when test() method was called
Program exit...
'''


'''
Program started...
test method called
a: 10
Exception: name 'b' is not defined
Some exception occurred when test() method was called
Program exit...
'''

'''
Program started...
test method called
a: 10
Exception: name 'b' is not defined
'''

# try:
#     val = test()
#     print("val: ", val)
# except Exception as e:
#     print("Line no 22: exception: e")
