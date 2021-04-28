try:
    # f is defined inside the try block. 
    # So it is available only inside try, except and finally blocks
    f = open("file.txt", "r")
    print("File opened successfully")

    print(a)
    # data = f.read()
    # print(data)
except Exception as e:
    print("Exception: ", e)
finally:
    print("Closing the file")
    f.close()

# NameError: name 'f' is not defined
# f.close()

print("Program exit")

'''
File opened successfully
Exception:  name 'a' is not defined
Closing the file
Program exit
'''