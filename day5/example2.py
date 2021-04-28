# Create a function which takes first name and last name
# and joins them and returns the full name
# Eg: Sunil, Kumar -> Sunil Kumar

def join_names(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name

result = join_names("Sunil", "Kumar")
print(result)