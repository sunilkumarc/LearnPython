total_sum = 0

i = 1
while i <= 10:
    if i == 4:
        break

    total_sum = total_sum + i
    i += 1

print(total_sum)

# i = 1, total_sum = 0 + 1 => 1
# i = 2, total_sum = 1 + 2 => 3
# i = 3, total_sum = 3 + 3 => 6
# i = 4, comes out of the loop