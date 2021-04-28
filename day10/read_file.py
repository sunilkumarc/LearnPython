'''
f -> file handler object (name can be anything)
open() -> inbuilt python method to open a file
r -> opening the file in read mode which means we can 
only read the contents of this file.
'''

# default path -> current directory
f = open('test_file.txt', 'r')

# using relative path
# f = open('../day9/day9_notes.txt', 'r')

# using absolute path
# f = open('/Users/sunilc/git/codementor/Lalilashka/day9/day9_notes.txt', 'r')

# Read the whole content using file handler f using read() method.
content = f.read()
print(content)

line1 = f.readline()
print(line1)

# f -> points to second line here
line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)

# calling readline() method again will retrn empty string since there are only
# 3 lines in total in the file.
line4 = f.readline()
print(line4)

line5 = f.readline()
print(line5)

# BEST PRACTICE -> close a file using close() method
f.close()
# Generally the last line / last operation after working with files