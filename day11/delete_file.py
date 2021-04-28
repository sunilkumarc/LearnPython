import os

# os is a inbuilt python library
# os -> operating system
# mac OSx is an operting system
# Windows is an operating system
# Linux is an operting system

# Deletes the given file
FILE_NAME = "testing.txt" 
# os.remove(FILE_NAME) # This lines will throw an error / exception

# print("Exiting program...")

'''
os.path.exists() returns True if the given file/path exists.
Returns False otherwise
'''
if os.path.exists(FILE_NAME):
    os.remove(FILE_NAME) # deletes the file
    print("File deleted successfully")
else:
    print("File doesn't exists")

print("Exiting program...")

'''
1
2

50 (if error in line number 50, then the program will stop here)

...
100
'''