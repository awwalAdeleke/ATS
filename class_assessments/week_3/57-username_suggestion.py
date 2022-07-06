import string
import random

def username_suggestion():
    f_name = input("Please enter your first name: ")
    f_name = f_name.lower()
    l_name = input("Please enter your last name: ")
    l_name = l_name.lower()
    numbers = string.digits

    f_name_sample = "".join(random.sample(f_name, 1))
    l_name_sample = l_name
    number_sample = "".join(random.sample(numbers, 2))

    username = f_name_sample + l_name_sample + number_sample

    return username


print(username_suggestion())