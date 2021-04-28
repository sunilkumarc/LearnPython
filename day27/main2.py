# import module1.file1

'''
Approach 1

from module1 import file1, file2

file1.test()
file2.test()
'''

'''
from module1 import file1

file1.test()
file1.test2()
file1.test3()
print(file1.sunil)
'''

from module1.file1 import test
test()

from module1.file2 import test
test()

test()
test()

'''
function inside module1.file1.test()
function inside module1.file2.test()
'''