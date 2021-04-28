f = open('new_file_2.txt', 'a')
# 'a' is for opening a file in append mode
# Opening a file in append mode will not delete any existing contents in the file.
# It keeps appending new content at the end of the file.

f.write('This is line number 10')
f.close()

'''
Output:

This is my original content in the file.
This is line number 2.
This is line number 2.
This is line number 10
'''