f = open('test_file.txt', 'r')

# 1. f.read()
# 2. f.readline()

# readlines() will read all the lines present in a file 
# as a list and stores into vairable 'lines' in the below line.
lines = f.readlines()
# lines = ['This is the first line.\n', 'This is the second line.\n', 'This is the third line.']
# print(lines)

for line in lines:
    print(line, end="")

'''
for every_item_in_the_list in list_name:
    do something with -> every_item_in_the_list
'''

'''
\n -> is a newline character or baslash n
'''