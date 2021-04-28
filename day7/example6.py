# 'break' statement
# used to break out of a loop

print("Begin of the loop")

i = 1
while i <= 10:
    if i == 5:
        break

    print("i =", i)
    i = i + 1

print("End of the loop")

'''
Begin of the loop
i = 1
i = 2
i = 3
i = 4
End of the loop
'''