
# Arbitary keyword arguments => arbitary arguments + keyword arguments
def print_user_details(**user_details):
    # user_details -> is a dictionary
    # user_details = {
    #     "last_name": "Kumar",
    #     "first_name": "Sunil",
    #     "age": 25,
    #     "place": "India"
    # }
    print(user_details)

# Whenever passing keyword arguments we need to use double * in function definition -> comes as a dictionary
print_user_details(last_name="Kumar", first_name="Sunil", age=25, place="India")

# Whenever passing without keyword arguments we need to use single * in function 
# definition -> comes as a tuple
# print_user_details("Kumar", "Sunil", 25, "India")
