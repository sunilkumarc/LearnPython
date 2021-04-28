# We have a list of items 1, 2.....10.
# Return the sum of the elements in this list using a while loop

l = [4, 5, 6]
N = len(l)

total_sum = 0
i = 0
while i < N:
    total_sum = total_sum + l[i]
    
    # Incrementing is generally the last statement in a loop
    i = i + 1

print(total_sum)

# i = 0, l[i] => 4, total_sum = total_sum + l[i] => 0 + 4 => 4, total_sum = 4
# i = 1, l[i] => 5, total_sum = total_sum + l[i] => 4 + 5 => 9, total_sum = 9
# i = 2, l[i] => 6, total_sum = total_sum + l[i] => 9 + 6 => 15, total_sum = 15
# i = 3, 3 < 3 => false

# i = 0, N = 3, 0 < 3
    # i = 1, l[i] -> l[1], total_sum = 0 + 5 = 5

# i = 1, N = 3, 1 < 3:
    # i = 2, total_sum = 5 + 6 => 11

# i = 2, 2 < 3:
    # i = 3, total_sum = total_sum + l[3] ==> Gives an error saying index out of range/bounds