total_sum = 0

l = [4, 5, 6, 8]
N = len(l)

i = 0
while i < N:
    if l[i] == 8:
        i = i + 1
        continue
    total_sum = total_sum + l[i]
    i = i + 1

print(total_sum)