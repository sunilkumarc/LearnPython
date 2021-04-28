print("Program started...")
a = [10, 20, 30, 40, 50]

try:
    val = a[1]
    print("Value = ", val)
except Exception as e:
    print("Exception!")
finally:
    print("Inside finally")

print("Program exit")

'''
finally -> gets executed in both the cases:
        1. exception occurred
        2. exception didn't occur

Program started...
Exception!
Inside finally
Program exit
'''