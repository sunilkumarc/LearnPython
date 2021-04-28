# Dictionaries
# Tuples
# Sets
# Booleans

# Dictionaries -> Python [ # HashMap -> Other languages ]
a = {}
a["1"] = "One"
a["2"] = "Two"
a["1"] = "New One"
a["7"] = "Seven"

b = [4, 5, 6, 7]

c = {"1": "One", "2": "Two"}
# print(c)
d = [1, 2, 3, 4, 5, 6]
d.append(7)
print(d)
# print(d)
c["3"] = "Three"
# print(c)

database_connection = {
    "host": "https://host.com/rds",
    "port": "5432",
    "username": "user",
    "pass": "asdfalkjfa"
}
# Hash -> C, C++
# Hash function, hash map.

print(database_connection["host"])

list_of_keys = database_connection.keys()
print("Length of keys: ", len(list_of_keys))

type_of_database_connection = type(database_connection)
print(type_of_database_connection)

a = ()
# print(type(a))
a = a + (1,)
a = a + (2,)
print(a)

# Set is a list of unique values
set_var = set()
set_var.add(1)
set_var.add(1)
set_var.add(2)
print(set_var)

e = [1, 1, 2]
print(e)

f = set(e)
print(f)