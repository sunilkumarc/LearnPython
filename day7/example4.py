# 'continue' and 'break' keywords within a loop

i = 0
while i < 10:
    if i == 5:
        i = i + 1
        continue
    
    # skip these statements when i == 5
    print("i =", i)
    i = i + 1

# 'continue' will skip the rest of the statements within a loop.

'''
i = 0
i = 1
i = 2
i = 3
i = 4
i = 6
i = 7
i = 8
i = 9
'''

# i = 4, 4 < 10, 4 == 5, runs print statement, i = 5
# i = 5, 5 < 10, 5 == 5,
# i = 5, 5 < 10, 5 == 5,
# i < 5, 5 < 10, 5 == 5