f = open('new_file.txt', 'w')
# 'w' -> open file in write mode

# Will overwrite any previous content and add below two lines.
# write() method will write a line to the file
f.write('This is some new content we are writing.\n\n\n')
f.write('This is some more content.')
f.close()
'''
Output:

1. Create a new_file.txt
2. Inside the file we will write two lines
'''

# Will overwrite any previous content and add below one line.
f = open('new_file.txt', 'w')
f.write('Third line')
f.close()
'''
Overwrite the whole content with only one line
'''