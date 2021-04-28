f = open('create_new_file.txt', 'x')
# 'x' -> create mode
# 'x' will create a file if doesn't exists.
# It returns an error if the file already exists

# close() is not needed in 'x' mode.
# f.close()