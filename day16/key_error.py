d = {} # we create a empty dictionary called d
d['a'] = 10 # add first key value pair: a = 10
d['b'] = 20 # add second key value pair: b = 20

# Let's try to access a key which doesn't exist in the dictionary
'''
1. Program will enter try block
2. It will execute all the lines one by one
3. If there's any exception then only the control will go to except block
4. If none of the statements throw any error inside the TRY block, then
the control will go the first statement after the TRY/EXCEPT block
'''
try:
    val = d['a']
    print(val)
    # KeyError -> is an exception raised when a particular key in not preseint in a dictionary

    # val2 = d['c'] # 'c'
    # The above statement will give:
    # KeyError: 'c' because key 'c' doesn't exists in dictionary d
    print("End of TRY block 1")
    print("End of TRY block 2")
    print("End of TRY block 3")
except KeyError as e:
    print("Key doesn't exist.")

print("End of program")

'''
10
End of TRY block 1
End of TRY block 2
End of TRY block 3
End of program
'''

