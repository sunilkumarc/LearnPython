# Using while loop
fruits = ['Banana', 'Apple', 'Mango']
N = len(fruits)
i = 0
while i < N:
    print(fruits[i])
    i = i + 1

print('----------------------------------------')

# Using For loop
fruits = ['Banana', 'Apple', 'Mango']
N = len(fruits)
for i in range(0, N):
    print(fruits[i])

print('----------------------------------------')

# Using For loop (better syntax):
for anything in fruits:
    print(anything)

print('----------------------------------------')

l = [1, 'Sunil', 0.5, 'Hello World!']
for item in l:
    print(item)