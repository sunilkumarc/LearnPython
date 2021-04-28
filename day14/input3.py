'''
Write a python program to take 2 numbers as input from the user,
add them and print the result.

Note: The program should be able to add floating point numbers as well.
Ex:
10 + 20 => 30
10.5 + 20.5 = 31
'''

'''
a = input("Enter first number: ")
b = input("Enter second number: ")

a_new = int(a)
b_new = int(b)

result_new = a_new + b_new
print("New result:", result_new)
'''

a = input("Enter first number: ")
b = input("Enter second number: ")

a_new = float(a)
b_new = float(b)

result_new = a_new + b_new
print("New result:", result_new, type(result_new))


'''
Enter first number: sunil
Enter second number: 20
Traceback (most recent call last):
  File "input3.py", line 25, in <module>
    a_new = float(a)
ValueError: could not convert string to float: 'sunil'

Here ValueError is an exception.
Exceptions are runtime logical errors.
To handle these exceptions we have try - except block
'''

'''
Different ways of taking user input using in Python programs
- input()
- reading from file using open("file_name.txt", 'r')
- APIs (application programming interface)

Client - Server architecture
Client --- Server

Client -> mobile application, website / browser (Ex: facebook mobile app, facebook.com website)
Client is something which users uses to interact with an application

Facebook mobile app -> client
Facebook servers where backend applications are running which take care of 
performing actions based on what user has done on the client

There can be multiple APIs on the server side
Ex:
Send friend request
You should send below data when sending a friend request
- friend name
- friend email
'''