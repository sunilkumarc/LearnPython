# 1, 2, 10, 15, 3

# Type conversion
# Converting tuple to list in this case
def add_number(*anything):
    # anything = (1, 'Sunil', [10, 20])
    name = anything[1]
    num = anything[2][0]
    print(num)

# anything() -> Function Call
# () -> brackets are used for function calls
# [] -> brackets are used for indexing
add_number(1, "Sunil", [10, 20])