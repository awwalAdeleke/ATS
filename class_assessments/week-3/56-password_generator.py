import string
import random

def password_generator():
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    special_char = string.punctuation
    numbers = string.digits


    joined_str = upper_letters + lower_letters + special_char + numbers
    # print(joined_lists)

    password = random.sample(joined_str, 16)
    password = "".join(password)

    return password

# password_generator()

print(password_generator())