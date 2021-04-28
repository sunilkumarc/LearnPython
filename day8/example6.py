# We can use 'continue' and 'break' statements within FOR loops too

'''
# 2 Ways to go through a list using FOR loop
# 1. Using indexing
# 2. Shortcut to go through list

fruits = ['apple', 'banana', 'mango']
# 1. Using indexing
N = len(fruits)
# if N = 3
# i = 0, 1, 2
for i in range(0, N):
    print(fruits[i])

for f in fruits:
    print(f)
'''

for i in range(10):
    # i -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    if i % 5 == 0:
        continue
    print(i)
'''
1
2
3
4
6
7
8
9
'''
# 2 Mistakes
# 0 is divisibile by 5
# Loop variable stops at 9, not 10.