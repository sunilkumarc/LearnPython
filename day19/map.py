'''
Write a function which takes a list as an input and add 10 to every number in the list.

input -> [1, 2, 3, 4, 5]
output -> [11, 12, 13, 14, 15]
'''

def addTen(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item + 10)
    return output_list

# print(addTen([1, 2, 3, 4, 5]))

# Let's see how we can use map() to simplify the above code

addTen = lambda a : a + 10
result = map(addTen, [1, 2, 3, 4, 5])
'''
first argument -> anonymous function which has the logic to apply for each element
second argument -> input list to map function (addTen)

map function applies the anonymous function to each element in the second argument
'''
# print(list(result))

# map() functions returns an object of type map.
# Generally map type is not human readable. So convert this to list 
# or iterate through a loop to get the elements.
result2 = map(addTen, [100, 200, 300])

# Loop through map and get items one by one
# for item in result2:
#     print(item)

# Convert map object to list and print
print(list(result2))