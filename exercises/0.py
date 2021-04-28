


# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

i = 1500
result = []
while i <= 2700:
    if (i % 7 == 0) and (i % 5 == 0):
        result.append(i)
    i = i + 1

print(result)

# i = 1500
# i = 1501
# i = 1502
# .
# .
# .
# i = 2700