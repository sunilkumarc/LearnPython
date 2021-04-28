import os

FOLDER_NAME = 'temp_folder'

if os.path.exists(FOLDER_NAME):
    # os.remove()
    # rmdir() method deletes the given folder only if it is empty
    os.rmdir(FOLDER_NAME) # remove directory
    print("Removed folder successfully")
else:
    print("Folder doesn't exists.")