'''
Given a list of fruits like "apple", "banana", "pear", "orange" 
return a list of boolean values which represent if the fruits start with character "b"

fruits = ["apple", "banana", "pear", "orange"]
result = [False, True, False, False]
'''

check_fruits = lambda a : int(a[0] == 'b')
# check_fruits = lambda a : int('z' in a)

'''
lambda all_the_variables_come_here : (colon) any_valid_python_statement

lambda a,b,c : a + b + c
'''

fruits = ["apple", "banana", "pear", "orange"]
result = map(check_fruits, fruits)
'''
1. We pass "apple" to the lambda function => returns False
2. We pass "banana" to the lambda function => return True
3. We pass "pear" to the lambda function => return False
4. We pass "orange" to the lambda function => return False
'''
print(list(result))

'''
fruits = ["apple", "banana", "pear", "orange"]
result = [False, False, False, False]
result = [0, 1, 0, 0]
'''