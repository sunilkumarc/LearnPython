# While Loop
# For Loop

fruits = ['Banana', 'Apple', 'Mango']
N = len(fruits)

# i -> loop variable
i = 0
while i < N:
    print(fruits[i])
    i = i + 1
    # return fruits[i] return is only used within a function as the last statement.

print('End of program')

# i = 0, 0 < 3 -> fruits[0] => Banana
# i = 1, 1 < 3 -> fruits[1] => Apple
# i = 2, 2 < 3 -> fruits[2] => Mango
# i = 3, 3 < 3 -> false