import os
import shutil
# It is a good practice to import all the package at the beginning of the python file

FOLDER_NAME = 'temp_folder'

if os.path.exists(FOLDER_NAME):
    # The import statements need not be only at the beginning of a python file
    shutil.rmtree(FOLDER_NAME) # remove tree (folder structure)
    # rmtree():
    #   removes every file within a folder and finally deletes the folder as well.

    print("Folder with contents deleted successfully.")
else:
    print("Folder is not found")

'''
os package
    - 100 functions

shutil package
    - improved the functionality present is os package

shutil package is built on top of os package
'''