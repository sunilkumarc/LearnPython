# Write a function which takes first_name and last_name as arguments
# and return True if full name is 'Sunil Kumar'
# otherwise return False

def correct_name(first_name, last_name):
    if first_name == 'Sunil' and last_name == 'Kumar':
        return True
    return False

def correct_name_2(first_name, last_name):
    full_name = first_name + ' ' + last_name
    if full_name == 'Sunil Kumar':
        return True
    return False

res = correct_name('Sunil', 'Kumar')
print(res)