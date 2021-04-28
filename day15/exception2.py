a = input("Enter first number: ")
b = input("Enter second number: ")

try:
    # everything inside the try and except blocks should be indented
    a_new = float(a) # 10a to float. this raised exception
    b_new = float(b)
    
    # quotient = a / b
    quotient = a_new / b_new
    print("Quotient:", quotient)
except ValueError as e:
    print("Invalid inputs entered!")
except ZeroDivisionError as e2:
    print("Division by 0 is not valid")

print("End of the program")

'''
Enter first number: 10
Enter second number: 0
Division by 0 is not valid
End of the program
'''

'''
Problem Statement:
Take two inputs from the user. 
1. If they are valid, find the quotient and print the result
2. If they are invalid, just output "Invalid input entered!" to the console.

a = 10
b = 5
quotient = 2
'''